---
title: LinkedIn Post — Professional Prompt Bundles
category: Example
description: A real public-project bundle showing how verified repository facts become an understated launch post.
bundle_id: linkedin-catalogue-launch
artefact: Professional LinkedIn launch post
audience: Senior technology, writing, knowledge-management, and AI practitioners
scenario: verified-public-project
style_path: styles/social-media-style.md
pattern_path: patterns/what-so-what-now-what.md
prompt_path: prompt-templates/linkedin-prompts.md
rubric_path: rubrics/linkedin-post-rubric.md
---

# LinkedIn Post — Professional Prompt Bundles

## Professional context

The author is announcing a public professional-writing catalogue. The post should lead with the working principle learned from building it, then give readers evidence they can inspect themselves.

## Source packet

```text
SCENARIO: Verified public project; facts must be rechecked against the live release before publication.
AUTHOR VIEW: The most useful part of a writing prompt is often the review checklist attached to it.
LIVE URL: https://p.riera.co.uk/
SOURCE URL: https://github.com/joanmarcriera/writing-style-catalogue
VERIFIED RELEASE CLAIM: The catalogue publishes 12 interactive worked bundles.
BUNDLE STAGES: professional context and source packet; completed copy-paste prompt; output excerpt; rubric scorecard and human-review requirements.
ARTEFACT EXAMPLES: board paper, decision record, operational runbook, executive report, LinkedIn post.
OBSERVED FAILURE MODES: missing facts, invented claims, flattened nuance, and register that does not fit the audience.
AUTHOR RULE: A draft is not complete when the model stops; it is complete when the relevant rubric passes and a human accepts the remaining checks.
TONE: Understated, evidence-first, direct; no emojis or engagement claims.
CALL TO CONVERSATION: Ask practitioners what is on their own pre-release checklist.
```

## Completed prompt

```text
You are editing a LinkedIn launch post for a senior AI and cloud architect. Write for technology leaders, professional writers, knowledge-management practitioners, and people who use LLMs for consequential documents.

Use only the SOURCE PACKET. Do not invent adoption, traffic, user feedback, performance, catalogue counts, professional endorsements, or claims about all LLMs. If the live URL, source URL, bundle count, bundle stages, or author rule has not been verified against the deployed release, return MISSING INFORMATION and do not write the post.

Preserve this hook: “The most useful part of a writing prompt is not the prompt. It’s the review checklist attached to it.” Explain the catalogue through three bullets: artefact structure; facts-only prompt placeholders; review rubric. State the observed failure modes as lessons from building the catalogue, not universal research findings. Use short mobile-readable paragraphs, British English, no emojis, no hype, and 260–360 words. End with the supplied specific question, then the two URLs and no more than five relevant hashtags. Output only plain post text.

Before finalising, apply the LinkedIn Post Rubric. Evidence, insight, voice, mobile readability, links, and publication integrity are critical gates. Preserve nuance even if a sharper claim would sound more viral.

SOURCE PACKET:
[Paste the verified source packet above here.]
```

## Output excerpt

```text
The most useful part of a writing prompt is not the prompt. It’s the review checklist attached to it.

I keep a public catalogue of professional writing workflows at p.riera.co.uk: board papers, decision records, runbooks, reports, and LinkedIn posts. The worked examples show the whole bundle, because the bundle is the point:

• A style definition and structure pattern, so you start from the artefact you need rather than a blank chat window.
• A copy-paste prompt with explicit placeholders for the facts only you have.
• A review rubric that gates the draft before it goes anywhere.

My rule: the draft is not done when the model stops. It is done when the rubric passes—and when a human accepts the checks the model cannot perform.
```

## Review scorecard

| Criterion | Score | Evidence | Gate |
|---|---:|---|---|
| Hook | 5 | The first two lines state a precise counter-intuitive principle. | Pass |
| Evidence | 5 | Catalogue features and links map to the verified release packet. | Human check |
| Professional insight | 5 | The post gives readers a transferable release rule. | Pass |
| Voice | 5 | Direct, understated, and free of invented success claims. | Pass |
| Publication integrity | 4 | Counts and URLs require one final live check before scheduling. | Human check |

## Human review before use

- Recheck the live bundle count, labels, links, and social preview after deployment.
- Read the final post aloud for personal voice and confirm every public claim.
- The author, not the model, decides when and where to schedule it.

## Reuse this bundle

- [Social Media Style](../styles/social-media-style.md)
- [What / So What / Now What Pattern](../patterns/what-so-what-now-what.md)
- [LinkedIn Prompts](../prompt-templates/linkedin-prompts.md)
- [LinkedIn Post Rubric](../rubrics/linkedin-post-rubric.md)
