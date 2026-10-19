#!/usr/bin/env python3
"""AST-assisted inventory of numeric choices in the executable group model.

Reads model/aa_group_model.py twice: once as a syntax tree, to list every numeric literal with
its line, enclosing function and assignment target and to classify it; and once by executing it
in a scratch namespace, to count the registered sensitivity values (scalar defaults, step
speeds, nonzero S and GOV cells) from the live `DEFAULTS`, `S` and `GOV` objects.

Writes research/model-choice-inventory.json (machine-readable) and
research/MODEL-CHOICE-INVENTORY.md (the human summary). The JSON's created_utc is kept while
the content is unchanged, so regenerating an unchanged inventory leaves the tree clean.

Run from anywhere:  python3 tools/inventory_model_choices.py

Exit status: 0 after writing both files; any exception from reading or executing the model
propagates and exits non-zero. `-h` or `--help` prints this text and writes nothing.
"""
from __future__ import annotations

import ast
import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model" / "aa_group_model.py"
JSON_OUT = ROOT / "research" / "model-choice-inventory.json"
MD_OUT = ROOT / "research" / "MODEL-CHOICE-INVENTORY.md"


def sha(path):
    """Return the SHA-256 hex digest of the file at `path`."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Visitor(ast.NodeVisitor):
    """Collect every numeric literal in a module, tagged with where it sits and what it is for.

    `function` is the innermost enclosing `def` and `assignment` the name being assigned at the
    point of the literal, both None at module level. The category is decided by those two
    alone, so it is a code-audit label and not a statement about the value's meaning.
    """

    def __init__(self):
        """Start with no enclosing function or assignment and no rows."""
        self.function = None
        self.assignment = None
        self.rows = []

    def visit_FunctionDef(self, node):
        """Track the enclosing function name while visiting its body, then restore it."""
        old = self.function
        self.function = node.name
        self.generic_visit(node)
        self.function = old

    def visit_Assign(self, node):
        """Track the first plain-name target of a statement while visiting its right side.

        A tuple or attribute target leaves the previous name in force rather than clearing it.
        """
        old = self.assignment
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        self.assignment = names[0] if names else old
        self.generic_visit(node)
        self.assignment = old

    def visit_AnnAssign(self, node):
        """Track the target name of an annotated assignment, as `visit_Assign` does."""
        old = self.assignment
        self.assignment = node.target.id if isinstance(node.target, ast.Name) else old
        self.generic_visit(node)
        self.assignment = old

    def visit_Constant(self, node):
        """Record an int or float literal (never a bool) with its category and position.

        The first matching rule wins, so a literal inside `S` or `GOV` is a structural zero or
        a registered value before the enclosing function is consulted.
        """
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            if self.assignment in {"S", "GOV"}:
                category = ("authored structural zero" if node.value == 0
                            else "registered sensitivity value")
            elif self.assignment == "DEFAULTS":
                category = "registered sensitivity value"
            elif self.function == "effective_adherence":
                category = "fixed structural choice: protective-adherence map"
            elif self.function == "resources":
                category = "fixed structural choice: resource capacity"
            elif self.function == "step_growth":
                category = "fixed structural choice: state-update map"
            elif self.function == "simulate":
                category = "fixed experiment or population-process choice"
            elif self.assignment in {"NSTEP", "VIABILITY_THRESHOLD"}:
                category = "fixed model or analysis choice"
            else:
                category = "implementation, derived, or numerical constant"
            self.rows.append({
                "value": node.value,
                "line": node.lineno,
                "column": node.col_offset,
                "function": self.function,
                "assignment": self.assignment,
                "category": category,
            })


def load_model():
    """Execute the model source in a scratch namespace and return that namespace.

    `__name__` is set to something other than "__main__" so the model's own entry-point
    guard cannot fire. The model is executed, not imported, so nothing is cached in
    `sys.modules`.
    """
    namespace = {"__name__": "choice_inventory_model"}
    exec(compile(MODEL.read_text(), str(MODEL), "exec"), namespace)
    return namespace


def build():
    """Return the inventory as a dict ready for JSON: counts, zeros, literals and a scope note.

    `created_utc` is stamped with the current time here; `main` replaces it with the committed
    stamp when nothing else has changed.
    """
    tree = ast.parse(MODEL.read_text())
    visitor = Visitor()
    visitor.visit(tree)
    ns = load_model()
    S, GOV, defaults = ns["S"], ns["GOV"], ns["DEFAULTS"]
    scalar_defaults = [k for k, v in defaults.items() if np.isscalar(v)]
    registered = {
        "scalar_defaults": len(scalar_defaults),
        "scalar_default_names": scalar_defaults,
        "step_speeds": len(defaults["a"]),
        "S_nonzero_cells": int(np.count_nonzero(S)),
        "GOV_nonzero_cells": int(np.count_nonzero(GOV)),
    }
    registered["total"] = sum(
        registered[k]
        for k in ("scalar_defaults", "step_speeds", "S_nonzero_cells", "GOV_nonzero_cells")
    )
    # Zero-based S rows for the Steps that index the five protective Traditions, so this
    # counts the nonzero resource-consumption cells those Steps actually carry.
    protective_rows = [3, 5, 6, 8, 9]
    relevant_cells = int(sum(np.count_nonzero(S[i]) for i in protective_rows))
    summary = {
        "schema_version": 1,
        "created_utc": datetime.now(UTC).isoformat(),
        "model_sha256": sha(MODEL),
        "registered_set": registered,
        "authored_structural_zeros": {
            "S": int(S.size - np.count_nonzero(S)),
            "GOV": int(GOV.size - np.count_nonzero(GOV)),
        },
        "scenario_specific_effective_dimension": {
            "full_adherence_GOV_magnitudes_inert": int(np.count_nonzero(GOV)),
            "reason": "GOVW.T @ ones equals one for every governed resource",
        },
        "protective_index_step_consumption_cells": relevant_cells,
        "numeric_literals": visitor.rows,
        "literal_category_counts": dict(Counter(r["category"] for r in visitor.rows)),
        "scope_note": (
            "The 118 values are the registered numeric sensitivity set, not every "
            "simulation-effective choice. Horizons, dt, seeds, thresholds, founder state, "
            "functional forms, structural zeros, and perturbation designs are classified "
            "separately."
        ),
    }
    return summary


def markdown(data):
    """Render the human-readable inventory report from the dict `build` returns."""
    r = data["registered_set"]
    z = data["authored_structural_zeros"]
    lines = [
        "# Model Choice Inventory",
        "",
        "Generated by tools/inventory_model_choices.py from the executable model.",
        f"Model SHA-256: {data['model_sha256']}.",
        "",
        "## What 118 means",
        "",
        f"The registered sensitivity set is exactly **{r['total']} numeric values**:",
        "",
        f"- {r['scalar_defaults']} scalar defaults;",
        f"- {r['step_speeds']} Step growth speeds;",
        f"- {r['S_nonzero_cells']} nonzero entries in S; and",
        f"- {r['GOV_nonzero_cells']} nonzero entries in GOV.",
        "",
        "It is not an inventory of every simulation-effective choice. The model also contains",
        "fixed functional coefficients, founder and arrival states, time and horizon choices,",
        "the endpoint viability threshold, random-seed designs, and authored structural zeros.",
        "",
        "## Structural and effective dimensions",
        "",
        f"- S contains {z['S']} authored zero cells; GOV contains {z['GOV']} authored zero cells.",
        "- Multiplicative sensitivity cannot test whether those zeros should be nonzero.",
        f"- At full adherence all "
        f"{data['scenario_specific_effective_dimension']['full_adherence_GOV_magnitudes_inert']} "
        "nonzero GOV magnitudes cancel from governance quality and are inert in that scenario.",
        f"- The five protective Traditions' index Steps contain "
        f"{data['protective_index_step_consumption_cells']} "
        "nonzero consumption cells, not 35.",
        "",
        "## Classification",
        "",
        "| Category | Numeric literal occurrences |",
        "|---|---:|",
    ]
    for category, count in sorted(data["literal_category_counts"].items()):
        lines.append(f"| {category} | {count} |")
    lines += [
        "",
        "The occurrence table is a code-audit aid, not a parameter count: repeated zero and one",
        "literals are shown separately because their locations can encode different choices.",
        "The machine-readable file records every literal with its line, function, assignment,",
        "value, and classification.",
        "",
    ]
    return "\n".join(lines)


def unchanged_apart_from_timestamp(data):
    """Return the committed inventory's timestamp if nothing else in it has changed, else None.

    Every regeneration used to stamp a new `created_utc`, so a run of the local CI left this
    file modified with nothing in it changed, and the churn had to be reverted by hand each
    time. Keeping the old stamp when the content is identical makes the timestamp mean what
    its name says, when the inventory last changed, and leaves an unchanged tree clean.
    """
    if not JSON_OUT.exists():
        return None
    try:
        old = json.loads(JSON_OUT.read_text())
    except ValueError:
        return None

    def body(d):
        """Return the inventory minus its timestamp, as a canonical string for comparison."""
        return json.dumps({k: v for k, v in d.items() if k != "created_utc"}, sort_keys=True)
    return old.get("created_utc") if body(old) == body(data) else None


def main():
    """Build the inventory and write the JSON and Markdown files, preserving an old timestamp."""
    data = build()
    data["created_utc"] = unchanged_apart_from_timestamp(data) or data["created_utc"]
    JSON_OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    MD_OUT.write_text(markdown(data))
    print(f"wrote {JSON_OUT}")
    print(f"wrote {MD_OUT}")


if __name__ == "__main__":
    from tool_help import help_requested
    help_requested(__doc__)
    main()
