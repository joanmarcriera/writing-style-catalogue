---
title: Master Style Transformer
template_type: Meta / Style Conversion
use_case: Transform any existing content into a different writing style, register, or format without losing factual accuracy.
audience: Any reader of the transformed output — defined by the chosen target style
output_format: Varies by target style (e.g. bulleted brief, structured email, narrative memo)
---

# Master Style Transformer

## Purpose

Use this template when you have existing content that needs rewriting for a different audience, medium, or communication style — without changing its factual substance. It is the most flexible template in this catalogue: you supply the raw material and the target style, and the LLM restructures, reframes, and rewords accordingly. Reach for it when a colleague hands you a draft that is too long, too dense, too informal, or simply written for the wrong audience. It is also useful for translating internal jargon-heavy analysis into board-ready language, or vice versa, when the same information must serve multiple stakeholders.

## Copy-paste prompt

```
You are an expert writing coach and editor. Your task is to transform the content provided into the target style, preserving all factual meaning while adapting structure, tone, and length to suit the new format and audience.

AUDIENCE: [AUDIENCE]

PURPOSE: [PURPOSE]

CONTEXT: [CONTEXT]

INPUT (content to transform):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME]

TARGET STYLE: [e.g. Smart Brevity / BLUF / Minto Pyramid / Plain English / Consulting Memo / Board Paper / Executive Briefing — specify one]

TONE: [TONE]

LENGTH: [LENGTH]

FORMAT: [FORMAT]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Rewrite the input in the target style, adapting structure and language accordingly.
2. Preserve all material factual claims, numbers, dates, decisions, obligations, risks, and named entities from the original. Do not invent, alter, or silently drop facts that affect meaning.
3. Clearly distinguish between facts (things stated in the input), assumptions (things inferred or implied), and recommendations (suggested actions) — label them if the target style permits.
4. Write in British English throughout (spellings: organisation, recognise, colour, behaviour, programme, practise as verb, licence as noun, etc.).
5. Avoid over-polished corporate language: no "leveraging synergies", "going forward", "best-in-class", or similar filler. Be direct.
6. Where uncertainty exists in the source material, carry it through honestly — use phrases such as "this assumes…", "based on available data…", or "further validation is needed before…".
7. Match tone and formality to the target audience: [TONE].
8. Target length: [LENGTH]. Do not pad to meet length; cut ruthlessly to stay within it.
9. Format the output as: [FORMAT].
10. Apply these constraints: [CONSTRAINTS].
11. If critical information is missing and the output would be misleading without it, output only: "Critical question: [one focused question]". Otherwise proceed using the supplied information and label assumptions clearly.
12. Before finalising, check the output against these review criteria: audience fit, target style fidelity, factual preservation, clear separation of facts and assumptions, British English, no invented details, no filler.
13. Output only the transformed document. No preamble, no commentary, no "Here is your rewritten text:".
```

## Variables to customise

- `[AUDIENCE]` — who will read the transformed output. Examples: "CFO and Finance Director", "engineering team leads", "non-technical board members", "a prospective client's procurement team".
- `[PURPOSE]` — what the document needs to achieve. Examples: "secure budget approval", "update the board on programme status", "explain a technical architecture to senior leadership".
- `[CONTEXT]` — background information that helps the LLM make good choices. Examples: "this is a lengthy internal technical report being converted into an executive briefing for a board meeting on 20 June", "the original was written by an engineer for engineers; it needs to work for a CISO with no cloud background".
- `[INPUT]` — paste the full raw content here. Any format is acceptable: bullet points, prose, a transcript, raw notes, a previous draft.
- `[DESIRED_OUTCOME]` — what the finished document should accomplish. Examples: "the reader approves the budget", "the reader understands the risk and what action is needed", "the reader can follow the argument without needing to ask follow-up questions".
- `[TONE]` — the register to write in. Examples: "formal and authoritative", "professional but direct", "conversational and approachable", "neutral and analytical".
- `[LENGTH]` — target length or word count. Examples: "one page maximum", "under 400 words", "1,500–2,000 words".
- `[FORMAT]` — how the output should be structured. Examples: "three-section memo with bullet points", "slide-by-slide outline", "prose with H2 section headings", "BLUF email with a bulleted fact list".
- `[CONSTRAINTS]` — any restrictions. Examples: "no jargon or acronyms without first defining them", "cite the source of every statistic", "no bullet points — continuous prose only", "must fit on one A4 page".

## Example input

```
AUDIENCE: Non-technical board members (no cloud or IT background)
PURPOSE: Secure board approval to proceed with cloud migration programme
CONTEXT: A detailed 40-page technical feasibility report was produced by the infrastructure team. The board meeting is on 20 June. Board members need a 10-minute read, not a technical deep-dive.
INPUT:
  The infrastructure team has completed a comprehensive technical feasibility assessment
  of migrating the organisation's on-premises data centre workloads to a public cloud
  environment (Azure). The assessment covered 147 workloads across four business units.
  Of these, 112 (76%) are assessed as directly cloud-compatible with minimal rework;
  23 (16%) require moderate refactoring; and 12 (8%) are legacy systems that will need
  decommissioning or replacement prior to migration. Total migration cost is estimated
  at £3.2M over 24 months, with annual operating savings of £1.8M beginning in Year 3
  (post-migration). Risk is assessed as medium overall, primarily around data migration
  continuity and staff capability uplift. The programme requires a dedicated programme
  manager, external SI partner support, and internal resourcing commitment of approximately
  4 FTE across the programme lifecycle.
DESIRED_OUTCOME: The board votes to approve the migration programme and allocates the £3.2M budget.
TARGET STYLE: Executive Briefing (Minto Pyramid — recommendation first, then supporting argument)
TONE: Professional, confident, non-technical
LENGTH: One page (approximately 350 words)
FORMAT: Short headline, executive summary paragraph, three supporting bullet sections, clear recommendation and ask
CONSTRAINTS: No technical acronyms without explanation; all financial figures must be included; note any assumptions
```

## Example output

---

**Cloud Migration Programme — Board Approval Requested**

**Recommendation**
The board is asked to approve a £3.2M cloud migration programme, to be delivered over 24 months, which will reduce annual operating costs by £1.8M from Year 3 onwards.

**Summary**
The infrastructure team has assessed all 147 of the organisation's current IT workloads and confirmed that the majority are straightforwardly compatible with a move to Microsoft Azure (a major public cloud platform). The programme is financially sound — costs are recouped within 27 months — and the risk profile is manageable with appropriate resourcing.

**Key findings**
- 76% of workloads (112 of 147) can migrate with little or no rework; 16% need moderate technical updates; 8% are legacy systems that must be replaced before migration can proceed.
- Total programme cost: £3.2M over 24 months, comprising external partner fees, internal staff time, and tooling.
- Annual savings from Year 3: £1.8M (primarily through elimination of data centre lease, hardware maintenance, and licensing costs). This figure assumes current cost levels hold; it has not been stress-tested against a significant change in cloud provider pricing.

**Resource requirements**
The programme requires a dedicated programme manager (to be appointed), an external systems integration partner (procurement to begin if approved), and approximately four internal staff committed part-time across the programme.

**Risks and mitigations**
The primary risks are data continuity during migration and the need to upskill internal IT staff on cloud operations. Both are well understood and have established mitigations: phased migration with rollback capability, and a structured training programme commencing in Month 3.

**Board recommendation**
Approve the cloud migration programme and authorise expenditure of £3.2M over financial years 2026–27 and 2027–28. A programme initiation document will be presented at the September board meeting.

---

## Review checklist

- [ ] All factual figures from the original source are preserved accurately
- [ ] Facts, assumptions, and recommendations are clearly distinguishable
- [ ] The target style has been faithfully applied (structure, length, tone)
- [ ] No corporate filler language or vague qualifiers remain
- [ ] British English spellings used throughout
- [ ] Any uncertainties in the source material are flagged honestly in the output
- [ ] The document works as a standalone read — no prior context needed
- [ ] The output length matches the specified target

---

See [STYLE-SELECTION-GUIDE.md](../STYLE-SELECTION-GUIDE.md) to choose the right target style.
