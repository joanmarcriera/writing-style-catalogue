---
title: Job Application Prompts
template_type: Job Application / Cover Letter / CV Summary
use_case: Write a compelling, specific cover letter or professional summary that connects the applicant's experience to the role, avoids generic phrasing, and gives a hiring manager a clear reason to interview.
audience: Hiring managers, talent acquisition teams, and recruitment panels
output_format: Structured one-page cover letter or professional summary with personalised opening, specific evidence, role alignment, and a clear call to action
---

# Job Application Prompts

## Purpose

A cover letter fails when it is generic — when it could have been written for any job at any company. It succeeds when it makes a specific argument: here is why this role at this organisation, at this point in my career, is exactly where I should be. Use this template when you need to write a cover letter or professional summary that goes beyond restating CV content, connects experience to the employer's actual needs, and reflects genuine interest in the role. The output should sound like a confident professional who has done their research — not a template filler.

## Copy-paste prompt — Cover letter

```
You are an experienced career coach with deep knowledge of what makes a cover letter stand out to a hiring manager. Write a compelling, specific, one-page cover letter.

AUDIENCE: [AUDIENCE — the hiring manager, their role and organisation]

PURPOSE: [PURPOSE — the role being applied for]

CONTEXT: [CONTEXT — any relevant background: how you found the role, any connection to the organisation, what stage the application is at]

INPUT (the applicant's relevant experience, achievements, and career background; the job description or key requirements of the role; why this role and this organisation appeal):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. the hiring manager invites the applicant to interview]

TONE: [TONE]

LENGTH: [LENGTH — recommended: one page, 350–450 words]

FORMAT: [FORMAT — recommended: personalised opening / two to three paragraphs of specific evidence and alignment / closing with a clear ask]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Open with a specific, personalised hook — not "I am writing to apply for..." Reference something specific about the organisation, the role, or a relevant professional connection that shows this application is not generic.
3. In the body, focus on two or three specific achievements or experiences that are directly relevant to the role. Use concrete evidence: numbers, outcomes, named projects, or specific skills demonstrated. Do not simply restate the CV — add a layer of interpretation ("what I took from this was..." or "this taught me that...").
4. Explicitly connect the applicant's experience to the employer's needs as stated in the job description or input. Show you have read the role carefully.
5. Include a sentence or two about why this organisation specifically — not just the role. What is it about this employer that makes this the right next step?
6. Close with a confident, direct ask for an interview. Do not use "I hope to hear from you" or "please do not hesitate to contact me". Be direct: "I would welcome the opportunity to discuss this further" or "I am available for an interview at your convenience."
7. Preserve all specific details from the input — do not invent experience, achievements, or qualifications.
8. Distinguish between confirmed experience (stated in the input) and inferred strengths (qualities implied by the experience). Do not overstate.
9. Avoid generic phrases: "I am a team player", "I am passionate about...", "I am a self-starter", "going forward". Be specific.
10. Tone: [TONE — recommended: confident, professional, direct — not sycophantic or over-formal].
11. Length: [LENGTH].
12. Apply these constraints: [CONSTRAINTS].
13. Output only the cover letter. No preamble.
```

## Copy-paste prompt — Professional summary (for CV or LinkedIn)

```
You are a professional CV writer. Write a concise professional summary that captures the applicant's value proposition in three to five sentences.

AUDIENCE: [AUDIENCE — hiring managers and recruiters in the target sector]

PURPOSE: [PURPOSE — the type of role being targeted]

CONTEXT: [CONTEXT]

INPUT (career background, key achievements, specialist skills, and target role type):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TONE: [TONE — recommended: confident, direct, professional]

LENGTH: [LENGTH — recommended: 60–100 words]

FORMAT: Three to five sentences: who you are / what you are known for / what you bring / what you are looking for next

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Write in British English throughout.
2. Do not open with "I am a..." — start with a strong statement of professional identity or specialism.
3. Include at least one specific achievement or quantified outcome.
4. State the type of role or direction being sought in the final sentence.
5. Avoid generic descriptors: "results-driven", "passionate", "dynamic", "innovative leader". Be specific.
6. Do not repeat the job title in the first sentence if it is already in the CV header.
7. Output only the professional summary. No preamble.
```

## Variables to customise

- `[AUDIENCE]` — the hiring manager or recruitment team. Examples: "the Head of Technology at Meridian Financial Services", "a talent acquisition team at a Big Four professional services firm", "a founder-led technology start-up hiring their first Head of Engineering".
- `[PURPOSE]` — the role being applied for. Examples: "Head of IT Infrastructure and Cloud Operations", "Senior Tax Adviser — Financial Services", "Director of Identity and Access Management".
- `[CONTEXT]` — background for the LLM. Examples: "the applicant was referred by a mutual contact at the organisation", "this is a career transition from in-house tax to advisory; the cover letter needs to address this directly", "the applicant is currently at a Big Four firm and this is a move to industry".
- `[INPUT]` — the raw material: the applicant's relevant experience and achievements, the job description or key requirements, and the reasons the role and organisation appeal.
- `[DESIRED_OUTCOME]` — what success looks like. Examples: "an interview invitation within two weeks", "the cover letter stands out from a competitive shortlist by being specific and evidence-based".
- `[TONE]` — "confident, professional, direct" for most professional roles. "Warmer and more conversational" for creative or culture-driven organisations.
- `[LENGTH]` — one page, 350–450 words for a cover letter. 60–100 words for a professional summary.
- `[FORMAT]` — use the recommended structure. Adjust the number of body paragraphs based on how many key experience points need to be covered.
- `[CONSTRAINTS]` — examples: "the applicant is making a career change — address this directly rather than avoiding it", "the applicant has a gap year that needs to be acknowledged", "do not reference the previous employer by name — describe it by type (e.g. 'a FTSE 100 financial services firm')".

## Example input — Cover letter

```
AUDIENCE: Head of Infrastructure and Cloud, Meridian Financial Services
PURPOSE: Head of Cloud Operations — a senior role leading a team of 12 engineers managing Meridian's Azure estate following its cloud migration
CONTEXT: The applicant (James Okafor) found the role through LinkedIn. No prior personal connection. The applicant is currently Cloud Platform Lead at Nexus Solutions, a cloud delivery partner that worked on Meridian's cloud migration programme — so there is relevant prior engagement (though not in a leadership capacity at client level).
INPUT:
  About the applicant:
  - Cloud Platform Lead at Nexus Solutions for 4 years; led technical delivery on 6 Azure migration programmes for financial services clients, including the Meridian programme
  - Before Nexus: 3 years as a Senior Azure Infrastructure Engineer at Barclays; responsible for the Azure landing zone design for Barclays' cloud-first programme
  - Azure certifications: Solutions Architect Expert, Security Engineer Associate
  - Specific achievement: on the Meridian programme, led the Azure security baseline design — zero critical findings in the independent audit
  - Team leadership: at Nexus, line-managed a team of 4 engineers; mentored two engineers to promotion
  - Why this role: wants to move from consulting (delivery for multiple clients) to operational leadership (owning an estate); Meridian's ambition to be cloud-first for 5 years resonates; the opportunity to lead the team he helped build is unusual and compelling
  - Why Meridian: already knows the estate intimately from the programme; believes the migration is just the start — there is significant optimisation and governance work ahead
DESIRED_OUTCOME: James is invited to a first-stage interview.
TONE: Confident, professional, direct — not sycophantic; the letter should read as from someone who knows their value
LENGTH: One page, 380–420 words
CONSTRAINTS: Do not reference Meridian by name in the opening sentence. Mention the Azure security audit result. Do not use the word "passionate".
```

## Example output

---

James Okafor
[Address] | [Email] | [Phone]

[Date]

Head of Infrastructure and Cloud
Meridian Financial Services

**Re: Head of Cloud Operations**

Having spent the last year helping to design and deliver the Azure migration programme at Meridian — including the security baseline that passed your independent audit without a single critical finding — I know your cloud estate better than almost anyone outside the organisation. That is a strong start for a Head of Cloud Operations. It is also, I think, an unusual opportunity: the chance to transition from the team that built the foundation to the team that runs and develops it.

For the past four years at Nexus Solutions, I have led technical delivery on Azure migration programmes for six financial services clients, managing the full complexity of regulated environments: data residency, FCA operational resilience requirements, privileged access design, and multi-stakeholder governance. Before that, I spent three years as a Senior Azure Infrastructure Engineer at Barclays, where I designed the Azure landing zone for their cloud-first programme. I hold the Azure Solutions Architect Expert and Security Engineer Associate certifications.

What I want next is operational ownership — responsibility for an estate, a team, and a direction of travel — rather than project-to-project delivery for multiple clients. The Meridian role offers exactly that. I have managed a team of four engineers at Nexus and mentored two to promotion; leading a team of twelve is a stretch I am ready for and actively seeking. The migration programme I contributed to is complete, but the optimisation, governance, and capability development work ahead is where the real value will be built — and that is the work I find most compelling.

I am also genuinely drawn to Meridian's five-year cloud-first ambition. The foundation is strong. The opportunity to contribute to what comes next — not just what has been completed — is what makes this the right move.

I would welcome the opportunity to discuss this further. I am available for a first-stage conversation at your convenience.

James Okafor

---

## Review checklist

- [ ] Opening is personalised and specific — not "I am writing to apply for..."
- [ ] At least two specific achievements with concrete evidence are included
- [ ] The applicant's experience is connected to the employer's stated needs
- [ ] A sentence or two explains why this organisation specifically, not just the role type
- [ ] Closing is a direct ask — not a passive "I hope to hear from you"
- [ ] No generic phrases: "team player", "passionate", "results-driven", "self-starter"
- [ ] All experience claims match the input — nothing invented
- [ ] Tone is confident and professional — not sycophantic or over-formal
- [ ] British English used throughout
- [ ] Length is within one page (350–450 words)

---

See [styles/job-application-style.md](../styles/job-application-style.md) for job application style.
