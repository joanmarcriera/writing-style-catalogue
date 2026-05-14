---
title: Learning Notes Prompts
template_type: Learning Notes / Study Summary
use_case: Convert raw study material, course notes, a book summary, or professional experience into structured, memorable learning notes that aid retention and practical application.
audience: The learner themselves — and optionally colleagues or teammates with whom notes are shared
output_format: Structured learning notes with key concepts explained in plain language, examples, application prompts, open questions, and a personal summary
---

# Learning Notes Prompts

## Purpose

Learning notes are not transcriptions — they are a processed version of knowledge, filtered through your own understanding and connected to what you already know. Use this template when you want to convert raw material (a course, a book, an article, a training session, or an experience) into structured notes that you will actually return to and use. The output should explain concepts in your own words, connect ideas to practical application, and surface the questions you still have. Well-structured learning notes also make it easier to share knowledge with colleagues — for example, summarising a conference session or distilling a professional development book into a team brief.

## Copy-paste prompt

```
You are a learning design specialist. Convert the raw material provided into structured, practical learning notes that aid understanding, retention, and application.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (the raw material to convert: course notes, a book or article summary, transcript, or description of an experience):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: 400–800 words; notes should be concise and scannable]

FORMAT: [FORMAT — recommended: Topic and Source / Key Concepts (explained in plain language, not copied verbatim) / Concrete Examples / Practical Applications / Open Questions / Summary in One Paragraph]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Explain key concepts in plain, accessible language — not copied verbatim from the source. A concept is understood when it can be explained simply. If a concept cannot be explained simply, flag it as "still unclear" rather than restating jargon.
3. For each key concept, include at least one concrete example. The example should make the concept tangible — either drawn from the input material or logically consistent with it. Do not invent examples that contradict the source.
4. Practical applications section: describe specifically how these ideas could be used in a real professional context. Examples: "this applies directly to our IAM governance review next month", "this framework could be used to structure the next post-incident debrief". If the input does not suggest a clear application, prompt the learner with a question ("where in your current work could this apply?").
5. Open questions: list two to four genuine questions raised by the material — things not fully answered, tensions between concepts, or things the learner wants to explore further. These are valuable; they signal where deeper learning is needed.
6. Summary paragraph: write a single paragraph capturing the most important insight from the material in the learner's own words. This should be the paragraph you would read six months later to remind yourself what you learned.
7. Distinguish between: concepts that are clearly explained in the source (confirmed), concepts where the source is ambiguous (flagged), and the learner's own interpretations or applications (labelled "My interpretation:" or "Application:").
8. Do not pad. Every sentence should add value. Shorter notes that are actually read and used beat longer notes that are not.
9. Tone: [TONE — recommended: clear, personal, direct — notes should sound like a real person thinking, not a textbook].
10. Length: [LENGTH].
11. Apply these constraints: [CONSTRAINTS].
12. Output only the learning notes. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who the notes are for. Examples: "the learner only (personal reference)", "the wider IT team (these notes will be shared after a conference)", "a new team member being onboarded to the IAM governance model".
- `[PURPOSE]` — what the notes cover. Examples: "summarise the key concepts from a one-day Entra ID Governance training course", "distil lessons from a conference presentation on blameless postmortem culture", "convert rough notes from reading 'Thinking in Systems' into usable reference material".
- `[CONTEXT]` — background for the LLM. Examples: "the learner is a cloud operations engineer who is new to identity governance", "the notes will be used to brief a team that did not attend the training", "this is professional development learning outside of the learner's current specialism".
- `[INPUT]` — the raw material: course notes, a transcript, a book summary, rough bullet points from a session, or a description of an experience.
- `[DESIRED_OUTCOME]` — what the notes should enable. Examples: "the learner can explain the key concepts to a colleague without re-reading the source material", "the team has a concise reference for the access review process introduced in the training", "the learner has identified two practical applications they will implement in the next 30 days".
- `[TONE]` — "clear, personal, direct". Learning notes should sound like the learner's own voice — not a textbook or a corporate summary.
- `[LENGTH]` — 400–800 words. Concise and scannable. If a session covered a large amount of material, prioritise the most important concepts rather than trying to capture everything.
- `[FORMAT]` — use the recommended structure. Add a "Share-with-team summary" section (100 words maximum) if the notes will be distributed to colleagues.
- `[CONSTRAINTS]` — examples: "focus only on the IAM-specific content from the course — skip the general cloud architecture modules", "the notes will be shared publicly on the team wiki — avoid referencing the specific client names mentioned in the training case studies", "limit to five key concepts — the course was broad; choose the most applicable".

## Example input

```
AUDIENCE: The learner (a cloud operations engineer at Meridian Financial Services) and their team (to be shared on the team wiki after review)
PURPOSE: Summarise key learning from a half-day internal training session on blameless postmortem culture and incident management
CONTEXT: The training was delivered by the Head of Site Reliability Engineering as part of a wider initiative to improve incident response at Meridian. The learner attended along with five colleagues. The training was based on the Google SRE Book (postmortem culture chapter) and the team's own incident history.
INPUT:
  Rough notes from the session:
  - Definition: a postmortem is a written record of an incident — its impact, causes, and actions to prevent recurrence. The goal is learning, not blame.
  - Key principle: blameless — humans are not the root cause; they are operating in systems that allowed errors to occur. The question is "what made this error possible?" not "who made the mistake?"
  - 5 Whys: ask "why" five times to get from the proximate cause (what happened) to the root cause (why the system allowed it). Example from the session: a deployment failure → deployment wasn't tested in staging → no staging environment available → staging env was decommissioned 3 months ago as a "cost saving" → cost saving was approved without considering the deployment risk.
  - Good postmortems: written within 72 hours; reviewed by the team; focus on systemic improvements, not individual blame; published internally so others can learn.
  - Our current problem at Meridian: we write postmortems but they don't result in action. Actions are assigned but not tracked. The SRE lead suggested we need a way to track action items from postmortems in a system that has visibility at leadership level.
  - Tension identified: blameless culture is harder in regulated environments (FCA requirements mean someone has to be accountable for control failures). The training didn't fully resolve this — the SRE lead said "accountability for outcomes and blameless root cause analysis can coexist, but you have to be deliberate about it."
DESIRED_OUTCOME: The learner can explain blameless postmortem principles to a colleague and has identified at least one practical change they will make to Meridian's current incident management process.
TONE: Clear, personal, direct — written as if explaining to a smart colleague who wasn't there
LENGTH: 500–650 words
CONSTRAINTS: Include the "5 Whys" example from the session verbatim — it was particularly good. Flag the regulatory accountability tension as an open question. Add a 100-word team share summary at the end.
```

## Example output

---

## Learning Notes: Blameless Postmortem Culture

**Source:** Internal training — Head of SRE, Meridian Financial Services, May 2026
**For:** Personal reference + team wiki

---

### Key Concepts

**1. What a postmortem actually is**
A postmortem is a written record of an incident — what happened, its impact, its causes, and the actions being taken to prevent recurrence. That definition sounds simple, but the word "blameless" is doing a lot of work. It means the purpose is learning, not fault-finding. An incident report that concludes with "engineer X made an error" has failed — because it hasn't told you what made that error possible, or how to prevent the next one.

**2. Blameless root cause analysis**
The core principle: humans are not the root cause of incidents. They are operating in systems that allowed — or even encouraged — errors to occur. The right question is always "what made this error possible?" not "who made the mistake?"

This changes what you look for. Instead of "the engineer didn't test the deployment," you ask why testing was skipped, why there was no gate that required it, why the system allowed an untested deployment to go to production.

**3. The 5 Whys in practice**
This technique works. Here's the example from the session:
- A deployment failed in production
- Why? It wasn't tested in staging
- Why? No staging environment was available
- Why? The staging environment was decommissioned three months ago
- Why? It was identified as a cost saving
- Why was that cost saving approved? Because the decision-makers didn't understand the deployment risk it introduced

The root cause isn't "the engineer didn't test." It's a governance decision that removed a safety control without understanding the consequence. That's fixable. Blaming the engineer isn't.

**4. What makes a postmortem good (vs. just documented)**
Written within 72 hours; reviewed with the team, not by one person; focused on systemic improvements; published internally so others can learn from it. The discipline is the timeline — a postmortem written two weeks later is working from memory, not data.

---

### Practical Applications

Our current gap at Meridian: we write postmortems, but the actions don't get tracked. They get assigned and then lose visibility. *Application:* propose that postmortem actions are logged in the same tracking system as programme risks — with a monthly review by the Head of IT Operations. This gives them the leadership visibility they currently lack.

The 5 Whys technique should replace our current "root cause: human error" conclusion pattern. I'll suggest this as a standard for the next incident debrief — even as a 10-minute exercise.

---

### Open Questions

1. **The regulatory accountability tension.** In a regulated environment (FCA), someone is accountable for control failures. How do you run a blameless RCA while also satisfying the regulator's expectation of named accountability? The training acknowledged this but didn't resolve it. I want to think about this more before the next postmortem.

2. **Postmortem action tracking.** What's the right cadence for reviewing open postmortem actions? Monthly feels right, but the SRE lead didn't specify.

3. **When is a 5 Whys analysis too shallow?** The technique assumes linear causality. What about incidents with multiple simultaneous contributing causes?

---

### Summary

Blameless postmortem culture is about treating incidents as learning opportunities, not blame opportunities. The key shift is asking "what made this error possible?" rather than "who made the error?" — because that question points to systemic fixes rather than individual performance management. Our current postmortem process at Meridian produces documents; it doesn't reliably produce improvement. The practical fix is tracking postmortem actions as formally as we track project risks.

---

### Team share summary (100 words)

Half-day training on blameless postmortem culture — key takeaway: humans aren't root causes; the systems they operate in are. We should stop writing "human error" as a root cause and ask what made that error possible. The 5 Whys technique is a practical way to get there (example: a deployment failure traced back to a cost-saving decision that removed a staging environment). Our current gap: postmortem actions aren't tracked formally, so they don't get done. Proposal to follow: add postmortem actions to our risk tracking system.

---

## Review checklist

- [ ] Key concepts are explained in plain language — not copied verbatim from the source
- [ ] Each concept has at least one concrete example
- [ ] Practical applications are specific — not just "this could be useful"
- [ ] Open questions reflect genuine gaps or tensions in the material
- [ ] Summary paragraph captures the single most important insight
- [ ] The learner's interpretations and applications are distinguishable from source content
- [ ] Nothing is padded — every sentence earns its place
- [ ] British English used throughout
- [ ] Length is within the 400–800 word target (plus any team share summary)

---

Use for studying, professional development, conference debriefs, or skill-building.
