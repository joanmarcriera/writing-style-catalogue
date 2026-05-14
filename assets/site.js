const DATA = window.CATALOGUE_DATA || { sections: [], items: [] };

const workflows = [
  {
    id: "board-paper",
    title: "Board paper",
    audience: "Board, committee, non-executive directors",
    time: "2-4 hrs",
    description: "Full governance paper on a major decision, with options, risk, financials, recommendation, and resolution wording.",
    source: "prompt-templates/board-paper-prompts.md",
    chain: [
      ["style", "Board Paper"],
      ["pattern", "Context / Analysis / Options / Recommendation"],
      ["template", "board-paper-prompts"],
      ["skill", "create-board-pack"],
      ["rubric", "board-paper-rubric"],
    ],
    prompt: "You are preparing a board paper for [BOARD]. The decision is [DECISION]. Context: [CONTEXT]. Use Context / Analysis / Options / Recommendation. Include financials, risks, assumptions, proposed resolution, and British English. Review against the board-paper rubric.",
  },
  {
    id: "tax-note",
    title: "Tax technical note",
    audience: "Tax team, finance director, adviser review",
    time: "3-6 hrs",
    description: "Structured tax analysis that separates facts, assumptions, law, conclusion, confidence, caveats, and next steps.",
    source: "prompt-templates/tax-note-prompts.md",
    chain: [
      ["style", "Tax Advisory"],
      ["pattern", "Question / Facts / Analysis / Conclusion"],
      ["template", "tax-note-prompts"],
      ["skill", "create-tax-technical-note"],
      ["rubric", "tax-note-rubric"],
    ],
    prompt: "You are drafting a UK tax technical note. Question: [QUESTION]. Facts: [FACTS]. Applicable law supplied for verification: [LAW]. Separate confirmed facts from assumptions. Do not invent references. State confidence level, caveats, next steps, and qualified adviser review requirement. Use British English.",
  },
  {
    id: "slide-deck",
    title: "Slide deck",
    audience: "Board, ExCo, client, internal leadership",
    time: "60-120 min",
    description: "Slide-by-slide outline with message titles, visual direction, speaker notes, and a clear final ask.",
    source: "prompt-templates/presentation-prompts.md",
    chain: [
      ["style", "Consulting Style"],
      ["pattern", "Problem / Evidence / Recommendation / Action"],
      ["template", "presentation-prompts"],
      ["skill", "create-slide-deck"],
      ["rubric", "slide-deck-rubric"],
    ],
    prompt: "Create a slide deck outline for [AUDIENCE] on [TOPIC]. Purpose: [DECISION OR ACTION]. Use one idea per slide, message titles, 2-4 bullets, visual suggestion, and substantive speaker notes. End with a clear call to action, not just Q&A. Use British English.",
  },
  {
    id: "pdf-report",
    title: "PDF-ready report",
    audience: "Client, regulator, board, internal stakeholders",
    time: "90-180 min",
    description: "Markdown-first formal document with title page, table of contents, executive summary, sections, appendices, and export guidance.",
    source: "prompt-templates/pdf-document-prompts.md",
    chain: [
      ["style", "Executive Briefing"],
      ["pattern", "Context / Analysis / Recommendation"],
      ["template", "pdf-document-prompts"],
      ["skill", "create-pdf"],
      ["rubric", "executive-communication-rubric"],
    ],
    prompt: "Write a PDF-ready Markdown document for [AUDIENCE]. Purpose: [PURPOSE]. Include title page elements, table of contents, executive summary, numbered sections, tables where useful, appendices, and page-break hints. Separate facts and assumptions. Use British English.",
  },
  {
    id: "runbook",
    title: "Operational runbook",
    audience: "On-call engineer, service owner, support lead",
    time: "45-90 min",
    description: "Incident response procedure with detection, triage, commands, escalation, verification, and post-incident actions.",
    source: "skills/create-runbook.md",
    chain: [
      ["style", "Technical Documentation"],
      ["pattern", "Objective / Scope / Procedure / Exceptions"],
      ["template", "technical-documentation-prompts"],
      ["skill", "create-runbook"],
      ["rubric", "technical-documentation-rubric"],
    ],
    prompt: "Write a runbook for [INCIDENT TYPE]. Audience: [ON-CALL ROLE]. Include detection triggers, first-five-minute triage, response steps, exact commands where supplied, escalation triggers, resolution verification, and post-incident actions. Use British English.",
  },
  {
    id: "adr",
    title: "Architecture decision record",
    audience: "Engineers, architects, future maintainers",
    time: "30-60 min",
    description: "Permanent record of a technical decision, the alternatives considered, rationale, consequences, and status.",
    source: "skills/create-adr.md",
    chain: [
      ["style", "ADR"],
      ["pattern", "Decision / Rationale / Consequences"],
      ["template", "decision-record-prompts"],
      ["skill", "create-adr"],
      ["rubric", "technical-documentation-rubric"],
    ],
    prompt: "Write an ADR for [DECISION]. Context: [CONTEXT]. Alternatives: [OPTIONS]. State status, decision, rationale, consequences, trade-offs, and related decisions. Keep it concise, factual, and in British English.",
  },
];

const kindLabels = {
  "style": "St",
  "pattern": "Pt",
  "template": "Pr",
  "meta-prompt": "Mp",
  "skill": "Sk",
  "workflow": "Wf",
  "example": "Ex",
  "checklist": "Ch",
  "rubric": "Rb",
  "reference": "Rf",
};

let selectedWorkflow = workflows[0];
let activeKind = "all";
let activeQuery = "";

const $ = (selector) => document.querySelector(selector);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderSections() {
  const container = $("#section-list");
  const allButton = sectionButton({ label: "All files", count: DATA.items.length, kind: "all" });
  container.replaceChildren(allButton, ...DATA.sections.map(sectionButton));
}

function sectionButton(section) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = `section-row ${section.kind === activeKind ? "active" : ""}`;
  button.dataset.kind = section.kind;
  button.innerHTML = `
    <span class="section-icon">${escapeHtml(kindLabels[section.kind] || "-")}</span>
    <span>${escapeHtml(section.folder || section.label)}</span>
    <span class="section-count">${escapeHtml(section.count)}</span>
  `;
  button.addEventListener("click", () => {
    activeKind = section.kind;
    activeQuery = "";
    $("#site-search").value = "";
    renderSections();
    renderResults();
  });
  return button;
}

function renderWorkflows() {
  const container = $("#workflow-list");
  container.replaceChildren(...workflows.map((workflow, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `workflow-card ${workflow.id === selectedWorkflow.id ? "active" : ""}`;
    button.innerHTML = `
      <span class="workflow-number">${escapeHtml(String(index + 1).padStart(2, "0"))}</span>
      <span>
        <h3>${escapeHtml(workflow.title)}</h3>
        <p>${escapeHtml(workflow.description)} &middot; ${escapeHtml(workflow.audience)}</p>
      </span>
      <span class="workflow-time">${escapeHtml(workflow.time)}</span>
    `;
    button.addEventListener("click", () => {
      selectedWorkflow = workflow;
      renderWorkflows();
      renderPreview();
    });
    return button;
  }));
}

function renderPreview(item = selectedWorkflow) {
  $("#preview-title").textContent = item.title;
  $("#preview-description").textContent = item.description || item.audience || "";
  $("#prompt-preview").textContent = item.prompt || `${item.title}\n\n${item.description || ""}`;
  $("#open-source").href = item.source || item.path || "START-HERE.md";

  const chain = item.chain || [[item.kind || "reference", item.section || "Catalogue"]];
  $("#bundle-chain").replaceChildren(...chain.map(([kind, label]) => {
    const tag = document.createElement("span");
    tag.className = `tag tag-${kind}`;
    tag.textContent = `${kind} · ${label}`;
    return tag;
  }));
}

function filteredItems() {
  const q = activeQuery.trim().toLowerCase();
  return DATA.items.filter(item => {
    const kindMatch = activeKind === "all" || item.kind === activeKind;
    const haystack = `${item.title} ${item.description} ${item.section} ${item.category} ${item.path}`.toLowerCase();
    return kindMatch && (!q || haystack.includes(q));
  });
}

function renderResults() {
  const items = filteredItems();
  const title = activeKind === "all"
    ? "All files"
    : (DATA.sections.find(section => section.kind === activeKind)?.label || "Catalogue");
  $("#catalogue-title").textContent = title;
  $("#catalogue-summary").textContent = `${items.length} result${items.length === 1 ? "" : "s"}${activeQuery ? ` for “${activeQuery}”` : ""}.`;

  if (!items.length) {
    const empty = document.createElement("div");
    empty.className = "result-card empty";
    empty.innerHTML = `
      <h3>No matches</h3>
      <p>Try a broader term such as board, tax, slide, runbook, ADR, briefing, or prompt.</p>
    `;
    $("#result-grid").replaceChildren(empty);
    return;
  }

  $("#result-grid").replaceChildren(...items.slice(0, 24).map(item => {
    const card = document.createElement("button");
    card.type = "button";
    card.className = "result-card";
    card.innerHTML = `
      <div class="result-meta">
        <span class="tag tag-${escapeHtml(item.kind)}">${escapeHtml(item.kind)}</span>
        <span class="tag">${escapeHtml(item.path)}</span>
      </div>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.description)}</p>
    `;
    card.addEventListener("click", () => {
      renderPreview({
        title: item.title,
        description: item.description,
        source: item.path,
        path: item.path,
        kind: item.kind,
        section: item.section,
        prompt: `${item.title}\n\n${item.description}\n\nSource: ${item.path}`,
      });
    });
    return card;
  }));
}

function bindSearch() {
  const input = $("#site-search");
  input.addEventListener("input", () => {
    activeQuery = input.value;
    activeKind = "all";
    renderSections();
    renderResults();
  });

  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      input.focus();
    }
  });
}

function bindToggles() {
  $("#theme-toggle").addEventListener("click", (event) => {
    const root = document.documentElement;
    const dark = root.dataset.theme !== "dark";
    root.dataset.theme = dark ? "dark" : "light";
    event.currentTarget.textContent = dark ? "Light" : "Dark";
    event.currentTarget.setAttribute("aria-pressed", String(dark));
  });

  $("#density-toggle").addEventListener("click", (event) => {
    const root = document.documentElement;
    const compact = root.dataset.density !== "regular";
    root.dataset.density = compact ? "regular" : "compact";
    event.currentTarget.textContent = compact ? "Regular" : "Compact";
  });

  $("#copy-prompt").addEventListener("click", async (event) => {
    const text = $("#prompt-preview").textContent;
    const original = event.currentTarget.textContent;
    try {
      await navigator.clipboard.writeText(text);
      event.currentTarget.textContent = "Copied";
    } catch {
      event.currentTarget.textContent = "Select text";
      $("#prompt-preview").focus();
    }
    setTimeout(() => {
      event.currentTarget.textContent = original;
    }, 1200);
  });
}

function bindNav() {
  document.querySelectorAll("[data-section-link]").forEach(link => {
    link.addEventListener("click", () => {
      document.querySelectorAll("[data-section-link]").forEach(item => item.classList.remove("active"));
      link.classList.add("active");
      const target = link.dataset.sectionLink;
      if (target !== "workflows") {
        activeKind = target;
        renderSections();
        renderResults();
      }
    });
  });
}

renderSections();
renderWorkflows();
renderPreview();
renderResults();
bindSearch();
bindToggles();
bindNav();
