---
title: Master Style Transformer
category: Meta
---

# Master Style Transformer

Transform any content into any writing style.

## Purpose

Convert existing text into a specific writing style. Use when you have content but it's in the wrong style for your audience.

## Copy-Paste Prompt

```
You are an expert writing coach. Transform the following text from its current style into the target style.

CURRENT TEXT:
[Paste your existing text here]

TARGET STYLE:
[e.g., Smart Brevity, BLUF, Minto Pyramid, Plain English, etc.]

TARGET AUDIENCE:
[Who will read this]

KEY POINTS TO PRESERVE:
[What must remain in the output]

INSTRUCTIONS:
1. Rewrite in the target style
2. Preserve all key facts and points
3. Adjust tone and structure to match style
4. Remove unnecessary elaboration
5. Ensure output is optimised for target audience

Output only the transformed text in the target style. No preamble.
```

## Variables to Customise

- `[CURRENT TEXT]` → Your existing content (any format)
- `[TARGET STYLE]` → Choose from styles/ folder
- `[TARGET AUDIENCE]` → Who will read this
- `[KEY POINTS TO PRESERVE]` → Critical information that must stay

## Example Input

```
Our engineering team has been working on optimising our database queries. 
We've conducted extensive analysis and found that by implementing better 
indexing strategies and query optimisation, we can significantly reduce 
database load. The projected improvements are approximately 30-40% faster 
response times. Implementation will take approximately 2-3 months, with 
phased deployment to minimise risk.
```

## Example Output (Smart Brevity)

**Database Performance Optimisation – 30–40% Speed Improvement Expected**

• Analysis shows indexing and query optimisation can significantly improve response times
• Phased implementation over 2–3 months minimises risk to production systems
• Expected impact: 30–40% faster queries; reduced database load

**Context**
Current database bottleneck is limiting application performance. Optimisation strategy focuses on indexing (70% impact) and query rewrites (30% impact). Risk is low; phased approach allows validation at each stage.

**Next Steps**
Engineering begins Phase 1 (indexing) next week. We'll report results by 15 June.

## Review Checklist

- [ ] Style matches chosen framework
- [ ] All key facts are preserved
- [ ] Tone is appropriate for audience
- [ ] Length is optimised for style
- [ ] Structure follows style guide
- [ ] Edited for clarity and concision

---

See [STYLE-SELECTION-GUIDE.md](../STYLE-SELECTION-GUIDE.md) to choose the right target style.
