---
title: Presentation Prompts
template_type: Presentation / Slide Deck Outline
use_case: Create a structured, narrative-driven slide deck outline with speaker notes that enables a confident, persuasive presentation to a defined audience.
audience: Varies — board members, leadership teams, conference audiences, clients, or internal teams
output_format: Slide-by-slide outline with slide title, two to four bullet points per slide, visual suggestion, and speaker notes
---

# Presentation Prompts

## Purpose

A presentation is not a document read aloud — it is a visual aid that supports a spoken argument. Use this template to create a slide deck outline that tells a coherent story, guides the audience from problem to solution to call to action, and gives the presenter everything they need in speaker notes. The template is most useful when you have the substance of what you want to say but need help structuring it into a narrative arc that works for a specific audience and time slot. The output is an outline — not finished slide copy — but it should be detailed enough to hand off to a designer or import directly into PowerPoint or Google Slides.

## Copy-paste prompt

```
You are a senior presentation designer and communications strategist. Create a detailed slide deck outline with speaker notes for a persuasive, narrative-driven presentation.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (all substance: key messages, data, facts, examples, and any existing draft content):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE]

LENGTH: [LENGTH — recommended: specify the target number of slides or presentation duration, e.g. "12–15 slides for a 20-minute presentation"]

FORMAT: [FORMAT — recommended: slide-by-slide outline with title / bullet points (2–4 per slide) / visual suggestion / speaker notes]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Structure the deck as a narrative, not a document. The audience should be taken on a journey: from "here is the problem or situation" → "here is why it matters" → "here is the solution or recommendation" → "here is what we are asking you to do".
3. Apply the "one idea per slide" rule. Each slide should communicate one clear point. The title should be a statement of that point (e.g. "Cloud migration will save £1.8M per year" not "Financial benefits").
4. For each slide, provide:
   - Slide title (a statement, not a topic label)
   - Two to four bullet points (slide copy — what appears on the slide; keep each bullet to one line)
   - Visual suggestion (what type of chart, image, icon, or diagram would reinforce the message)
   - Speaker notes (what the presenter says when this slide is on screen — two to five sentences; these carry the depth and nuance, not the slide itself)
5. Speaker notes must be substantive — they should give the presenter the words to say, not just "talk about X". Include the key insight, any caveat, and the transition to the next slide.
6. Preserve all facts and figures from the input — do not invent data points. If a fact is an estimate or assumption, flag it in the speaker notes.
7. Do not put every fact on the slides — reserve the detail for speaker notes. The slide is for the audience to glance at; the presenter carries the substance.
8. Distinguish between confirmed facts and assumptions — use speaker notes to flag where data is an estimate or projection.
9. Avoid bullet-point soup. If you are tempted to put more than four bullets on a slide, split it into two slides.
10. Include a strong opening slide that earns attention in the first 30 seconds, and a closing main slide with a clear call to action — not "Questions?" or "Thank you" as the final message. Put Q&A, contact details, and backup data in appendix slides if needed.
11. Tone: [TONE].
12. Length: [LENGTH].
13. Apply these constraints: [CONSTRAINTS].
14. Output only the slide deck outline. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — who will be in the room. Examples: "Group Board of Directors (non-technical; 20-minute slot)", "IT Leadership Team (technical; 45-minute working session)", "prospective client (head of procurement and CTO; first meeting; 30 minutes)".
- `[PURPOSE]` — what the presentation is trying to achieve. Examples: "secure board approval for the cloud migration programme", "align the IT Leadership Team on the IAM strategy recommendation", "win a vendor shortlisting decision from the procurement team".
- `[CONTEXT]` — background for the LLM. Examples: "this follows a written board paper that has been pre-circulated; the presentation is the 'headline' version for the meeting", "the audience has seen a demo already; this is the business case presentation".
- `[INPUT]` — all the substance: key messages, data, facts, stories, examples, and any existing content.
- `[DESIRED_OUTCOME]` — what should happen when the presenter finishes. Examples: "the board votes to approve the programme", "the leadership team agrees to proceed with Option A", "the client asks for a proposal".
- `[TONE]` — register for the presentation. Examples: "confident and authoritative", "collaborative and consultative", "energetic and persuasive".
- `[LENGTH]` — number of slides or duration. Examples: "10–12 slides for a 15-minute presentation", "20 slides for a 40-minute session with Q&A".
- `[FORMAT]` — use the slide-by-slide outline format. Add a "Deck summary" section at the top if the requester needs a one-page overview of the narrative arc.
- `[CONSTRAINTS]` — examples: "no more than 3 words per bullet point on slide — all detail in speaker notes", "must include an ROI calculation", "follow the organisation's brand guidelines (primary colour: dark blue; sans-serif font only)", "do not include vendor names on the slides — refer to 'preferred partner'".

## Example input

```
AUDIENCE: Group Board of Directors at Meridian Financial Services — 9 members; mix of executive and non-executive; non-technical; 15-minute slot at the June 2026 board meeting
PURPOSE: Present the case for the cloud migration programme and secure formal board approval
CONTEXT: A full board paper has been pre-circulated. This presentation is the spoken version for the board meeting — it should be persuasive and concise, not a repeat of the paper. The board has been broadly supportive in prior discussions.
INPUT:
  Key messages:
  1. The current infrastructure is a growing risk — the data centre lease expires December 2027, hardware is ageing beyond support
  2. 76% of workloads are ready to migrate now; the technical groundwork is done
  3. Financial case: £3.2M investment; £1.8M annual savings from Year 3; 26-month payback; 5-year NPV £4.1M
  4. Risk is manageable: phased migration, rollback capability, FCA compliance maintained throughout
  5. Q1 is already on track: Phase 1 pilot complete; audit passed; on budget
  6. Ask: approve Option A (full cloud migration) and authorise £3.2M capex
DESIRED_OUTCOME: The board votes to approve the resolution as written in the board paper.
TONE: Confident, clear, non-technical — the board should feel informed and assured, not sold to
LENGTH: 8–10 slides for a 15-minute slot (2 minutes per slide maximum; allow 3 minutes for Q&A)
CONSTRAINTS: No more than 4 bullets per slide. All detail in speaker notes. No technical jargon. Include a clear call-to-action slide at the end. Do not include individual staff names.
```

## Example output

---

## Slide Deck Outline: Cloud Migration Programme — Board Approval

**Deck summary:** 9 slides / 15 minutes / Audience: Group Board / Ask: Approve £3.2M cloud migration

---

### Slide 1 — Title slide
**Title:** Securing Meridian's Infrastructure for the Next Decade

**Bullets:** (none — title slide only)

**Visual:** Clean title card with Meridian branding; subtitle "Cloud Migration Programme — Board Approval, June 2026"

**Speaker notes:** "Good morning. This presentation covers the cloud migration programme — why we need to act now, what we're proposing, and the decision we're asking the board to make today. You've seen the full paper; this is the 10-minute version of the argument."

---

### Slide 2 — The problem is real and time-limited
**Title:** Our data centre lease expires in December 2027 — and the hardware is already beyond its planned life

**Bullets:**
- Primary data centre lease: expires December 2027
- Hardware estate: beyond planned replacement cycle
- Renewal cost (do nothing): £5.8M over 5 years — with no modernisation benefit
- Three 2025 security incidents linked to ageing infrastructure

**Visual:** Timeline graphic showing lease expiry and hardware end-of-life dates converging in 2027

**Speaker notes:** "The status quo is not a neutral choice. If we do nothing, we face a £5.8M spend over five years, no improvement in capability, and increasing risk as hardware ages further. The lease expiry in December 2027 is a hard deadline — we need a plan in place well before then. The three security incidents last year were a signal; we shouldn't wait for a more serious one."

---

### Slide 3 — The technical groundwork is done
**Title:** 76% of workloads are ready to migrate — the hard assessment work is complete

**Bullets:**
- 147 workloads assessed by the infrastructure team
- 112 (76%) ready to migrate with minimal work
- 23 (16%) need moderate updating; 12 (8%) to be decommissioned
- Platform selected: Microsoft Azure (existing Microsoft licensing; FCA compliance posture)

**Visual:** Donut chart showing 76% / 16% / 8% workload breakdown

**Speaker notes:** "We've done the technical homework. 147 workloads have been individually assessed. The vast majority — three quarters — are straightforwardly cloud-ready. The assessment took four months and was validated by external advisers. We know what we're moving, and we know how. The platform choice is Azure, which aligns with our existing Microsoft licensing and has the compliance posture needed for a regulated environment like ours."

---

### Slide 4 — The financial case is robust
**Title:** £3.2M investment; £1.8M saved every year from Year 3

**Bullets:**
- Total investment: £3.2M over 24 months
- Annual savings from Year 3: £1.8M (data centre, hardware, licensing)
- Payback period: 26 months
- 5-year NPV: £4.1M positive; IRR: 28%

**Visual:** Waterfall chart showing cumulative cost/savings over 5 years, with breakeven point highlighted at Month 26

**Speaker notes:** "The financial case is straightforward. We invest £3.2M over two years, and from Year 3 we save £1.8M per year — primarily through exiting the data centre leases and eliminating hardware maintenance. The payback period is 26 months. Over five years, the net present value is £4.1M positive. These figures are based on current contracted costs; the assumption is that cloud pricing remains broadly stable. A 20% increase in cloud costs would reduce annual savings to approximately £1.4M — the programme would still be NPV-positive."

---

### Slide 5 — Risk is manageable
**Title:** Four risks identified; each has a tested mitigation

**Bullets:**
- Data continuity: phased migration with rollback at each stage
- Staff capability: structured training programme + managed service retained post-migration
- Regulatory compliance: FCA pre-notified; external compliance review in Q3
- Vendor dependency: architecture designed for portability

**Visual:** 2x2 risk matrix (likelihood vs. impact) showing four risks in amber/green quadrant

**Speaker notes:** "The risk profile is medium overall — manageable, not negligible. The most significant risk is data continuity during migration, which is why we're taking a phased approach: we won't move to the next batch of workloads until the previous batch has been validated. We can roll back at any stage. On regulatory compliance, we've already pre-notified the FCA and commissioned an independent compliance review."

---

### Slide 6 — Q1 is already on track
**Title:** The programme has already proven itself — Phase 1 complete, on budget, audit passed

**Bullets:**
- Phase 1 pilot (38 workloads): complete and signed off
- Azure security baseline: passed independent audit — zero critical findings
- Q1 spend: £610k against £600k budget (within contingency)
- Phase 2 now under way

**Visual:** Programme timeline with Phase 1 ticked off and Phase 2 in progress

**Speaker notes:** "This isn't a theoretical proposal — we've already started. Phase 1, our pilot of 38 workloads, has been completed and signed off. The Azure security configuration passed an independent audit with no critical findings. We're £10k over budget in Q1, which is within our contingency. The programme team has demonstrated it can execute. Phase 2 is already mobilised."

---

### Slide 7 — One issue requires your decision today
**Title:** One risk needs board action: a second delivery partner is needed for Phase 2

**Bullets:**
- Primary partner (Nexus Solutions) at capacity from July
- Without a second partner: Phase 2 slips 6–8 weeks (go-live February 2027)
- CloudBridge Ltd assessed and available; cost £180k within contingency
- Decision needed today to protect the October 2026 go-live

**Visual:** Timeline comparison — October 2026 vs. February 2027 go-live scenarios

**Speaker notes:** "There is one issue I need to flag directly. Our primary delivery partner won't be able to resource Phase 2 from July at the required pace. We've identified and assessed a second accredited partner — CloudBridge. Their cost of £180k falls within the programme contingency. If we approve their engagement today, we protect the October go-live and the associated Year 3 savings. If we defer, Phase 2 slips to February 2027 and we lose one quarter of savings."

---

### Slide 8 — The board's decision
**Title:** We are asking the board to approve Option A and authorise £3.2M

**Bullets:**
- Option A: full cloud migration (recommended)
- Option B: hybrid — does not resolve the 2027 lease risk; costs more over 5 years
- Option C: do nothing — £5.8M spend, no modernisation, FCA compliance risk
- Proposed resolution: as set out in the board paper

**Visual:** Simple three-column comparison table (Option A / B / C) with cost and key outcome for each

**Speaker notes:** "The board paper sets out three options in full. In brief: Option A is the only one that resolves the infrastructure risk, meets the FCA requirements, and does so within a commercially sound business case. Options B and C either defer the problem or cost more. The proposed board resolution is on page 8 of the paper. We're asking you to pass it today."

---

### Slide 9 — What happens next
**Title:** If approved today, the programme proceeds to full deployment

**Bullets:**
- June: CloudBridge contract signed; Phase 2 accelerates
- July–September: main migration (74 workloads)
- October 2026: Phase 2 go-live
- Q4 2026 Board: programme completion report

**Visual:** Clean four-step timeline arrow

**Speaker notes:** "If the resolution is passed today, we can sign the CloudBridge contract this week. The Phase 2 migration runs through to October. We'll bring a completion report to the Q4 board meeting. The next steering group update goes to the CIO fortnightly. Are there any questions before we move to the resolution?"

---

## Review checklist

- [ ] Each slide communicates one clear idea — the title is a statement, not a topic label
- [ ] No more than four bullets per slide — detail is in speaker notes
- [ ] Speaker notes give the presenter actual words to say, not just prompts
- [ ] Facts and figures from the input are preserved accurately
- [ ] Estimates and assumptions are flagged in speaker notes
- [ ] The narrative arc is clear: problem → evidence → solution → ask
- [ ] The final slide has a specific call to action — not "Thank you" or "Questions?"
- [ ] No technical jargon that a non-specialist audience would not understand
- [ ] British English used throughout
- [ ] Slide count is within the specified target

---

Keep slides concise; details go in speaker notes.
