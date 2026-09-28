# The invitation, ready to send

Drafted 22 September 2026. This is the missing piece between `2-recruiting-note.pdf`, which holds
two blurbs, and an actual message: subject lines, the logistics, answers to the questions people
ask, a nudge, and a thank-you. Markdown rather than LaTeX because it exists to be pasted into an
email client.

**Nothing here describes the argument, and nothing here says how many rows the book leaves empty
or which they are.** A respondent who knows that is no longer independent. Keep it that way when
you reply to them, too: the most likely way to spoil the round is a friendly answer to a follow-up
question.

**Before you send anything**, check the attachment list. Send `1-respondent-form.pdf`, and
`3-response-template.pdf` if they would rather return a clean sheet than a marked-up form. Never
send `4-collator-notes.pdf` or a link to the repository.

---

## Subject line

Pick one:

- A half-hour favour that needs your judgement, not your time
- Would you fill in a grid for me, before I explain it?
- A question about AA's Traditions I am not allowed to answer myself

---

## The email

> Dear [Name],
>
> I have a favour to ask that comes with an odd condition: please say yes or no before I explain
> what it is for.
>
> For [the last two years / some time now] I have been writing a long piece of research about how
> groups that decide by discussion stay reliable, with AA as the case. One part of it rests on a
> table I filled in myself: twelve Traditions down the side, eight things a group supplies to its
> members across the top, and a mark in each cell where I judged that the Tradition governs the
> supply of that thing. Everything else in the project has been checked half to death. This table
> cannot be checked that way, because every check I can run varies the numbers in it and takes its
> shape as given. The only test is whether somebody else fills in the same grid, from the same
> definitions, without having seen mine.
>
> That is the favour. Twenty to forty minutes with the attached form, which contains everything
> you need: the eight things, the twelve Traditions in short form, the grid, and three questions
> afterwards that matter as much as the grid does.
>
> Three things worth saying plainly. There are no right answers and I am not testing you: a
> disagreement with my version is worth more to me than agreement, because agreement I already
> have. Nothing you write will be published under your name. And you do not need to tell me
> anything about your own membership or your own recovery; the form does not ask and neither do I.
>
> The condition is that you fill it in before I tell you anything more about the project, and
> before reading any of it. If you have already read the part it belongs to, that does not
> disqualify you, but say so when you return it so I can record it. If you happen to know who else
> I have asked, please do not compare notes until everyone's form is back.
>
> If you can, [date]. If that is tight, tell me and I will wait, because a considered form late is
> worth more than a quick one on time.
>
> Thank you either way.
>
> [your name]

---

## The short version, for a message rather than an email

> Can I ask you a half-hour favour? I have been writing something about AA's Traditions, and one
> part of it rests on a table I filled in myself. I cannot test it by thinking about it harder;
> the only test is whether somebody else fills in the same grid the same way without seeing mine.
> Twelve Traditions down the side, eight things a group gives its members across the top, mark
> which affects which. No right answers, and disagreement helps me more than agreement. One
> catch: you have to do it before I tell you anything else about the project. Interested?

---

## The longer version, if they ask what they are contributing to

Use this only after they have agreed, and still without describing the argument.

> The project argues that some of AA's Traditions do a particular structural job, and it tries to
> be honest about which of its claims are earned and which are asserted. The model is frozen, every
> number in the text is reproducible from a cached run, and there are checkers that fail the build
> if a figure in a chapter does not match the data behind it.
>
> None of that reaches this table. Every check varies the values in it and prices the consequences;
> none can test the pattern, because the pattern is the input. One person's judgement is
> load-bearing and there is no computational way around it.
>
> So I am asking two or three people to fill in the same grid independently. If you and the others
> mark it as I did, that part of the argument has independent support for the first time. If you do
> not, one of my chapters is wrong, and I would rather learn that from you than from a reviewer.
> The comparison was written and tested before any form came back, so I cannot choose the
> flattering analysis afterwards.

---

## Answers to the questions people actually ask

Keep these short when you use them. Every extra sentence about the project costs independence.

**Do I have to be in AA?** No. What helps is knowing AA well enough to have opinions about what the
Traditions do in practice. If you have never encountered them, the short form on the grid is
probably not enough to work from.

**Will I be named?** No. The record keeps who filled in each form, what they were told, and whether
they had read the relevant part, because the analysis has to report that. Nothing is published
under your name.

**What if I think the whole framing is wrong?** Then say so on question two, which asks exactly
that. An objection to the list of eight things is a more serious objection to the book than any
individual cell, and it is the answer I would least like and most need.

**What if I cannot decide on a cell?** Mark the one you would defend rather than splitting the
difference. The presence or absence of a mark matters far more than its size. If you want to record
strength, the form lets you, but do the marks first.

**How long, really?** Twenty to forty minutes. It is longer if you argue with yourself about the
definitions, which is a good sign rather than a bad one.

**Can I do it on paper?** Yes. Print it, mark it, photograph it. Or use the response sheet, or just
send me the twelve rows in an email.

**What happens to my answers?** They are compared with mine on three things: which rows come out
empty, how the grids agree cell by cell, and what happens to the conclusions when the analysis is
rerun on yours instead of mine. The form says the same thing.

**Can I see the chapter first?** Not before you return the form. Afterwards, yes, and I will send
you what your form did to it.

---

## The nudge, after a week or so

> No pressure at all, and no need to apologise if it has not happened. If you would rather not, say
> so and I will stop asking; if you still want to, the form is attached again. It is still twenty
> to forty minutes and it is still the only part of this I cannot do myself.

---

## The thank-you, once the form is back

Send this after you have saved their form as
`research/governance-elicitation-<initials>.md` and run `python3 model/elicitation_compare.py`.

> Thank you. That is now recorded, and it is the only part of the project that came from someone
> other than me.
>
> Here is what your version did to it: [what the comparison reported, in one or two sentences,
> whichever way it went]. [If the forms disagree with the book: you have found a real problem, and
> the chapter will say so.]
>
> If you would like to read the part it belongs to now, say the word and I will send it.

---

## After the round, for the record

The steps that follow are in `0-start-here.pdf`: save each form, run the comparison, record in
`research/SOURCES.md` who filled each one in and what they were told, and propagate the result
through the layers in `CLAUDE.md` exactly as any other change to a public claim. Do not edit
`model/elicitation_compare.py` once forms start arriving; if it has to change, make the change,
record it in `research/progress-log.md`, and report both analyses.
