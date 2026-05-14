---
title: Technical Documentation
category: Specialist
aliases: [Technical Writing, Engineering Docs]
---

# Technical Documentation

## What This Style Is

Precise, comprehensive technical writing. Explains systems, processes, or code in detail. Includes background, explanation, examples, and reference material.

**Core principle**: Explain exactly how something works with enough detail to implement or troubleshoot.

## When to Use It

- System architecture documentation
- API documentation
- Engineering runbooks
- Technical specifications
- Installation or setup guides
- Troubleshooting guides
- Infrastructure or deployment documentation

## When NOT to Use It

- Executive updates (use Smart Brevity)
- Teaching beginners (use Socratic or Tutorial)
- Policy or compliance (use Legal Professional)
- Quick decisions (use BLUF)

## Core Structure

```
[OVERVIEW]
What this document covers and who should read it.

[PREREQUISITES]
Assumed knowledge or required setup.

[CORE EXPLANATION]
How the system or process works.

[EXAMPLES]
Real code snippets or scenarios.

[COMMON ISSUES AND TROUBLESHOOTING]
Known problems and solutions.

[REFERENCE]
APIs, commands, or detailed specifications.

[GLOSSARY]
Terms and definitions specific to this domain.
```

## Copy-Paste Prompt Template

```
You are a technical documentation expert. Write technical documentation for:

TOPIC:
[What system, process, or API you're documenting]

AUDIENCE:
[Who will read this: engineers, DevOps, architects?]

CORE CONCEPTS:
[What does the reader need to understand?]

HOW IT WORKS:
[Step-by-step or architectural explanation]

COMMON USE CASES:
[How is this typically used?]

TROUBLESHOOTING:
[What breaks? How to fix it?]

INSTRUCTIONS:
1. Write for the stated audience (assume their expertise level)
2. Start with overview; build to detail
3. Include code examples where relevant
4. Provide real troubleshooting scenarios
5. Use headings to break sections
6. Include reference material (APIs, commands)
7. Avoid jargon without explanation

Output only the technical documentation. No preamble.
```

## Short Example

**Kubernetes Pod Lifecycle Documentation**

**Overview**
This document explains how Kubernetes manages pod lifecycle—from creation through termination. It covers init containers, readiness/liveness probes, and graceful shutdown.

**Prerequisites**
You should understand Kubernetes basics: nodes, containers, and ReplicaSets.

**Pod Lifecycle Stages**

*1. Pod Pending*
• Kubernetes has accepted the pod but it's not running yet
• Reasons: Waiting for node resources, pulling image, or running init containers

*2. Pod Running*
• At least one container has started
• Readiness probes determine if traffic should be sent

*3. Pod Succeeded or Failed*
• All containers have terminated
• Reason depends on exit codes and restart policy

**Readiness and Liveness Probes**

Readiness probes tell Kubernetes if the pod can handle traffic. Liveness probes check if the pod should be restarted.

Example readiness probe (HTTP):
```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

**Common Issues**

*CrashLoopBackOff*
Pod restarts repeatedly. Check:
1. Application logs: `kubectl logs <pod>`
2. Application exits too quickly without crashing
3. Configuration mismatches

*Pod Stuck in Pending*
Node cannot accommodate pod. Check:
1. Resource requests: `kubectl describe pod <pod>`
2. Node capacity: `kubectl top nodes`
3. Taints and tolerations matching

**Reference**
[Kubernetes Pod Spec Reference: verify online before relying on availability]

## Quality Checklist

- [ ] Overview explains what the document covers
- [ ] Prerequisites are explicit
- [ ] Explanation includes diagrams or visual structure
- [ ] Examples are realistic and copy-paste ready
- [ ] Troubleshooting covers common issues
- [ ] Technical accuracy is verified
- [ ] No unexplained jargon
- [ ] Links or references are current

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|----------------|-----|
| Assumes too much knowledge | Readers get lost | State prerequisites clearly |
| Missing examples | Theory without practice | Include real code or scenarios |
| No troubleshooting | Readers stuck when something breaks | Add common issues and fixes |
| Outdated references | Readers follow incorrect guidance | Verify all links and code are current |
| Poor organisation | Hard to find information | Use clear headings and structure |

---

See [prompt-templates/technical-documentation-prompts.md](../prompt-templates/technical-documentation-prompts.md) for more templates.

See [examples/technical-runbook.md](../examples/technical-runbook.md) for a complete example.
