---
title: Create Training Material
skill_type: Document generation
output: Structured training content with clear learning objectives, module-by-module explanations, worked examples, practice exercises, and an assessment — suitable for self-paced or facilitated delivery
tools_needed: LLM (Claude/ChatGPT/Gemini), Word or Google Docs, Learning Management System (optional)
difficulty: Medium
---

# Skill: Create Training Material

## What this skill does

Produces structured, learner-focused training content that guides a participant from zero (or baseline) knowledge to a defined level of competence. Good training material is not an information dump — it is a designed learning experience that breaks content into digestible modules, uses worked examples to anchor abstract concepts, provides practice opportunities before assessment, and gives the learner a way to check their own understanding. This skill works best when you have a clear target audience, a specific learning objective, and real-world examples from the relevant domain.

## When to use it

- Creating onboarding material for a new team member who must learn a system, process, or domain (IAM concepts, tax compliance, cloud infrastructure)
- Developing a one-day or half-day workshop on a technical or professional topic (e.g. Microsoft Entra ID for non-technical managers, GDPR awareness for staff)
- Building a self-paced eLearning module that runs without a facilitator
- Producing reference material that doubles as a training resource (e.g. a new SOP with explanatory context)
- Updating existing training after a system change, policy update, or regulatory change

## Inputs required

- The topic — stated precisely (not "cloud security" but "Microsoft Entra ID fundamentals for service desk staff")
- The target audience: their role, existing knowledge level, and any misconceptions to address
- The learning objectives — what must the learner be able to do at the end (not know, but do)
- The key content: concepts, processes, or skills to cover
- Real-world examples or scenarios from the learner's actual work context
- Delivery format: self-paced reading, facilitated workshop, video script, or blended
- Assessment method: quiz, scenario exercise, practical task, or line manager sign-off

## Copy-paste prompt

```
You are an instructional designer and subject matter expert. Create training material for the topic and audience described below.

AUDIENCE: [Who will receive this training — role, existing knowledge level, any learning barriers]
PURPOSE: [Why this training exists — what problem it solves; what risk it mitigates; what capability it builds]
CONTEXT: [Organisational context; any related systems, policies, or processes the learner must already understand]
INPUT: [Key concepts, processes, or skills to cover; any worked examples or scenarios to include; any existing documentation to draw from]
DESIRED_OUTCOME: [Specific, measurable learning objectives — use "After this training, the learner will be able to [verb] [task]" format]
TONE: Clear, instructional, and encouraging. Training material should feel like a knowledgeable colleague explaining, not a policy document lecturing.
LENGTH: Structured by module. Each module: 400–600 words of explanation + 1 worked example + 1 practice exercise. Total: as many modules as the learning objectives require.
FORMAT: H2 for module titles; H3 for sub-sections. Worked examples in a callout box ("Example: ..."). Practice exercises as numbered tasks. Assessment as a set of 5–8 scenario-based questions at the end.
CONSTRAINTS: Use British English. Use active voice. Every concept must be illustrated with a worked example from the learner's actual work context. Do not include knowledge for its own sake — every piece of content must connect to a learning objective. Output only the training material; no preamble.

STRUCTURE:
# Training: [Topic]
**Audience**: [Role]
**Duration**: [Estimated time to complete]
**Prerequisites**: [What the learner must know before starting]

## Learning objectives
After completing this training, you will be able to:
1. [Objective 1]
2. [Objective 2]

## Module 1: [Topic]
[Explanation — 400–600 words]
> **Example**: [Worked example from the learner's context]
**Practice**: [1–2 tasks for the learner to complete]

## Assessment
[5–8 scenario-based questions with answer key]
```

## Suggested output structure

- **Header** — topic, audience, estimated duration, prerequisites
- **Learning objectives** — 3–5 specific, measurable objectives using active verbs (identify, configure, draft, classify, escalate)
- **Module 1–N** — one module per major concept or skill; each with explanation, worked example, and practice exercise
- **Summary** — one-page recap of key points from all modules
- **Assessment** — 5–8 scenario-based questions (not factual recall questions — "what would you do if..." not "what is the definition of...")
- **Further reading** — 3–5 references for learners who want to go deeper

## Quality controls

- [ ] Every learning objective uses a measurable active verb (not "understand" — use "identify", "configure", "draft", "classify")
- [ ] Every concept has a worked example from the learner's actual work context — not a generic textbook example
- [ ] Practice exercises give the learner something to do, not just something to read
- [ ] Assessment questions are scenario-based, not simple recall
- [ ] The estimated duration is realistic — 400 words of training material takes approximately 15–20 minutes to work through
- [ ] A learner with no prior knowledge of the topic can complete the material without asking for help
- [ ] British English throughout; technical terms defined at first use

## Common failure modes

- **Objectives written as "understand X"**: "Understand" is not measurable — replace with a verb that produces an observable output: "configure MFA for a new user account", "classify a data asset as Restricted, Internal, or Public"
- **No examples**: Abstract concepts without examples are forgotten within 48 hours — every concept needs a grounding example from the learner's actual job
- **Assessment tests memory not competence**: A quiz that asks "What does MFA stand for?" tests recall; "A user calls to say they cannot log in after you enabled MFA on their account — what are the first three steps you take?" tests competence — use the latter
- **Too long per module**: Modules over 800 words lose learner attention; split long modules into two
- **Ignores existing knowledge**: Training that explains concepts the audience already knows wastes their time and loses credibility — calibrate content to the stated knowledge level

## Example request

"Create a half-day training programme on Microsoft Entra ID (Azure AD) fundamentals for IT service desk staff who currently manage on-premise Active Directory. They are comfortable with AD concepts (users, groups, OUs, GPOs) but have no Azure experience. Learning objectives: identify the key differences between on-premise AD and Entra ID; create and manage user accounts in Entra ID admin centre; assign and manage group memberships; enable and troubleshoot MFA for end users; escalate complex Entra ID issues correctly. Include scenario-based assessment questions. British English."
