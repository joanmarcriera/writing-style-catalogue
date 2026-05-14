---
title: Translation & Localisation Prompts
template_type: Translation / Localisation
use_case: Translate and adapt content for a target language and market, preserving meaning and brand voice while adjusting for cultural context, local conventions, and idiomatic appropriateness.
audience: The intended readers in the target language and market — customers, partners, employees, or regulators
output_format: Localised content that reads naturally in the target language, with cultural adaptations noted and any translation uncertainties flagged
---

# Translation & Localisation Prompts

## Purpose

Translation converts words; localisation converts meaning. A word-for-word translation of marketing copy, a legal notice, or a product interface will often produce text that is grammatically correct but culturally off — it sounds like a translation, not like content written for that market. Use these prompts when you need to adapt content for a specific language and market, whether that is a client communication in French, a product onboarding email in Spanish, or a legal disclosure in German. The prompt framework applies whether you are using an LLM for a first draft (to be reviewed by a native speaker) or for a quick internal communication where professional translation is not required. Always have legally binding, marketing-critical, or regulatory content reviewed by a qualified human translator.

**Important:** For legal documents, regulatory submissions, financial disclosures, or high-stakes marketing content, LLM translation should be treated as a first draft only. A qualified human translator should review the output before publication or distribution.

## Copy-paste prompt — Localisation

```
You are a professional localisation specialist with fluency in the target language and deep knowledge of the target market. Translate and adapt the content provided, preserving the original meaning while ensuring the result reads naturally and appropriately for the target audience and market.

AUDIENCE: [AUDIENCE — who will read the localised content, in the target market]

PURPOSE: [PURPOSE — what the content needs to achieve in the target market]

CONTEXT: [CONTEXT — where this content will appear (email, website, app, legal document); what the original content is; the relationship between sender and recipient in the target market]

INPUT (the source content to translate and localise):
[INPUT]

DESIRED_OUTCOME: [DESIRED_OUTCOME — e.g. content that reads as though written by a native speaker for this market; a first draft for professional review]

TONE: [TONE — and how tone conventions may differ in the target market]

LENGTH: [LENGTH — note if the translated content must fit within a character or word limit, e.g. for UI strings]

FORMAT: [FORMAT — reproduce the original format unless instructed otherwise; note any formatting conventions specific to the target market]

CONSTRAINTS: [CONSTRAINTS]

INSTRUCTIONS:
1. Translate accurately, prioritising meaning over literal word-for-word equivalence. Where the source uses an idiom, cultural reference, or phrase that does not translate directly, adapt it to achieve the same communicative effect in the target language.
2. Preserve the factual meaning of all content — do not add, remove, or alter factual claims, legal obligations, or data during translation.
3. Preserve the tone and register of the original in the target language. If the source is formal, the translation should be formal in the target language's conventions for formality — which may differ from English conventions.
4. Adapt cultural references, examples, and conventions for the target market:
   - Dates: use the local format (e.g. DD/MM/YYYY in most of Europe; YYYY-MM-DD in some Asian markets)
   - Numbers: use local decimal and thousands separators (e.g. 1.234,56 in German vs. 1,234.56 in English)
   - Currency: convert or retain as instructed; note if conversion rates apply
   - Units: convert to local standards if relevant
   - Names and titles: use local conventions for addressing people formally or informally
5. Flag the following explicitly as notes below the translation:
   a. Any phrase or idiom in the source that has no direct equivalent in the target language, with the adaptation chosen and a brief explanation
   b. Any cultural reference or example that may not resonate in the target market, with the adaptation made
   c. Any section where the source content is ambiguous or unclear, which may affect translation accuracy
   d. Any section where you recommend professional review before publication (e.g. legal language, regulatory terminology)
6. Do not translate brand names, product names, or proprietary terms unless specifically instructed. Keep trade marks in their original form.
7. Distinguish between: accurate translation (the meaning is clear and the translation is confident), adaptive translation (the meaning required cultural adaptation — flagged), and uncertain translation (the source is ambiguous or the target language equivalent is contested — flagged for review).
8. Tone: [TONE].
9. Length: [LENGTH — if there is a character or word limit, aim to meet it; note any significant expansion or compression in the translation notes].
10. Apply these constraints: [CONSTRAINTS].
11. Output the translated content first, then the translation notes as a separate section.
```

## Variables to customise

- `[AUDIENCE]` — the intended readers in the target market. Examples: "French-speaking financial services professionals in France (not Canada)", "Spanish-speaking SME business owners in Spain", "German corporate clients — formal register expected".
- `[PURPOSE]` — what the content needs to achieve. Examples: "inform a French-speaking client of a change to their service terms", "market a cloud advisory service to German mid-market CIOs", "translate a user onboarding email for a Spanish-language market launch".
- `[CONTEXT]` — background for the LLM. Examples: "this is a client-facing service update email from a UK financial services firm; the recipient is a French corporate client; the relationship is formal", "this is UI copy for a SaaS platform being launched in Germany; character limits apply to button labels and error messages".
- `[INPUT]` — the source content to translate. Include the full text, formatted clearly.
- `[DESIRED_OUTCOME]` — what success looks like. Examples: "content that a native French speaker would read as having been written in French, not translated", "a first draft for review by the German-language marketing team", "a quick internal translation for a team briefing — professional quality not required".
- `[TONE]` — register in the source language and any known conventions in the target language. Examples: "formal in English; French equivalent — 'vous' not 'tu'", "professional but warm in English; German equivalent — formal 'Sie' with no small talk", "conversational in English; Spanish equivalent — maintain warmth; use 'usted' in Spain for B2B".
- `[LENGTH]` — note character limits for UI strings. For document translation, length will expand or contract depending on the target language.
- `[FORMAT]` — reproduce the original formatting in the translated output. Flag any format conventions specific to the target market.
- `[CONSTRAINTS]` — examples: "do not translate the product name 'Meridian CloudBridge Connector'", "the legal disclaimer must be reviewed by a qualified legal translator before distribution", "this is a first draft only — flag any section with less than 90% confidence for human review".

## Example input

```
AUDIENCE: German-speaking corporate clients (IT leadership and procurement contacts) at mid-market financial services firms in Germany; formal B2B context
PURPOSE: Translate a sales outreach email for use by Meridian's German-speaking business development team
CONTEXT: Meridian Advisory is expanding into the German market. This outreach email has been written in English by the UK marketing team. It will be localised for the German market and sent by a native German-speaking business development manager. The German B2B register is more formal than typical UK professional email.
INPUT:
  Subject: Cloud security and IAM — a challenge you may be facing

  Hi [Name],

  I came across your profile and noticed you're leading IT security at [Company]. I work with financial services firms navigating the challenges of cloud migration — particularly around identity and access management (IAM) and regulatory compliance.

  One pattern we see frequently: firms get the cloud infrastructure right, but the governance and access control model doesn't keep pace. The result is audit findings, FCA pressure, and a lot of manual remediation.

  We've recently helped a UK asset manager achieve full IAM compliance ahead of a regulatory inspection — reducing their provisioning time by 80% in the process.

  Would you be open to a 20-minute call to discuss whether there's a fit? I can share a brief overview of what we've done for similar firms.

  Best regards,
  [Name]
  Meridian Advisory
DESIRED_OUTCOME: A first draft that reads naturally in German for a formal B2B context; flagged for review by a native German speaker before sending.
TONE: Formal (Sie-form); professional; direct but not pushy. German B2B emails are typically more formal and less conversational than UK equivalents; avoid informal phrases.
LENGTH: Approximately the same length as the original; no strict limit
CONSTRAINTS: Do not translate "IAM" — use the acronym with the German expansion on first use (Identitäts- und Zugriffsmanagement). Do not translate "Meridian Advisory". Flag any phrases that are UK-specific and may not resonate in the German market (e.g. FCA reference).
```

## Example output

---

**TRANSLATED CONTENT:**

**Betreff:** Cloud-Sicherheit und Identitätsmanagement – eine Herausforderung, die Sie möglicherweise kennen

Sehr geehrte/r [Name],

ich bin auf Ihr Profil aufmerksam geworden und habe gesehen, dass Sie die IT-Sicherheit bei [Unternehmen] verantworten. Ich arbeite mit Finanzdienstleistern zusammen, die die Herausforderungen der Cloud-Migration bewältigen – insbesondere im Bereich Identitäts- und Zugriffsmanagement (IAM) und regulatorische Compliance.

Ein Muster, das wir regelmäßig beobachten: Unternehmen optimieren ihre Cloud-Infrastruktur erfolgreich, aber das Governance-Modell und die Zugriffskontrolle halten nicht Schritt. Die Folgen sind Audit-Befunde, regulatorischer Druck und aufwändige manuelle Nachbearbeitung.

Wir haben kürzlich einem britischen Vermögensverwalter geholfen, die vollständige IAM-Compliance vor einer behördlichen Prüfung zu erreichen – und dabei die Bereitstellungszeiten um 80 Prozent zu reduzieren.

Wären Sie für ein 20-minütiges Gespräch offen, um zu erörtern, ob ein gemeinsamer Ansatz sinnvoll wäre? Ich kann Ihnen gern einen kurzen Überblick über unsere Erfahrungen mit vergleichbaren Unternehmen zukommen lassen.

Mit freundlichen Grüßen
[Name]
Meridian Advisory

---

**TRANSLATION NOTES:**

**Adaptation — FCA reference removed:**
The original English email refers to "FCA pressure" (the UK Financial Conduct Authority). This is a UK-specific regulator and will not resonate in the German market, where the relevant regulators are BaFin (Bundesanstalt für Finanzdienstleistungsaufsicht) and, for some institutions, the ECB/SSM. The phrase has been replaced with "regulatorischer Druck" (regulatory pressure) — a neutral formulation applicable to the German regulatory environment. *If the email is specifically targeting firms under BaFin supervision, consider replacing with "BaFin-Anforderungen" for greater specificity. Recommend review by a German-speaking business development manager before sending.*

**Register — formality:**
The English original uses "Hi [Name]" (informal) and "Best regards" (semi-formal). German B2B email convention requires "Sehr geehrte/r [Name]" (formal salutation) and "Mit freundlichen Grüßen" (formal close). These have been applied throughout. The body copy has been made slightly more formal in register — shorter sentences and the removal of conversational phrasing ("I work with..." becomes a more formal construction in German).

**IAM — acronym handling:**
Per constraint, "IAM" is retained as an acronym with the German expansion "Identitäts- und Zugriffsmanagement" on first use.

**"80% reduction in provisioning time" — retained:**
This figure is presented as an outcome from a specific engagement. It has been translated accurately and retained. *Note: if this figure is used in a regulated communications context (e.g. as a performance claim), it should be reviewed against applicable German advertising and financial communications rules before distribution.*

**Confidence level:**
This translation is provided at approximately 90% confidence as a first draft for native-speaker review. The legal/regulatory implications of the phrase "regulatorische Compliance" in the specific context of German financial services regulation have not been independently verified.

---

## Review checklist

- [ ] Factual meaning is preserved — no claims added, removed, or altered in translation
- [ ] Tone and register are appropriate for the target language and market conventions
- [ ] Cultural references, idioms, and examples have been adapted — not translated literally
- [ ] Local conventions applied: date formats, number formats, currency, titles
- [ ] Brand names and proprietary terms are retained in their original form (unless instructed)
- [ ] Translation notes flag: adaptations made, cultural adjustments, and sections for professional review
- [ ] Uncertain or ambiguous sections are explicitly flagged — not guessed at
- [ ] Important caveat included: professional review recommended for legal, regulatory, or high-stakes marketing content
- [ ] British English used in the meta-text (notes, headings) surrounding the translated content
- [ ] Character or word limits respected (if applicable)

---

Note: Professional translation recommended for legal, marketing, or critical content. LLM output should be treated as a first draft for human review in those cases.
