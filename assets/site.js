const DATA = window.CATALOGUE_DATA || { sections: [], items: [], bundles: [] };
const bundles = DATA.bundles || [];

const kindLabels = {
  style: "St",
  pattern: "Pt",
  template: "Pr",
  "meta-prompt": "Mp",
  skill: "Sk",
  workflow: "Wf",
  example: "Ex",
  checklist: "Ch",
  rubric: "Rb",
  reference: "Rf",
};

const stageDefinitions = [
  { id: "brief", label: "Brief" },
  { id: "prompt", label: "Prompt" },
  { id: "output", label: "Output" },
  { id: "review", label: "Review" },
];

let selectedBundle = bundles[0] || null;
let selectedStage = "brief";
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

function stripMarkdown(value) {
  return String(value ?? "")
    .replace(/^#{1,6}\s+/gm, "")
    .replace(/^[-*]\s+/gm, "• ")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .trim();
}

function basename(path) {
  return String(path || "").split("/").pop().replace(/\.md$/, "");
}

function scrollToPanel(selector) {
  const panel = $(selector);
  if (!panel) return;
  window.requestAnimationFrame(() => panel.scrollIntoView({ behavior: "auto", block: "start" }));
}

function scrollPreviewWhenStacked() {
  if (window.matchMedia("(max-width: 1180px)").matches) {
    scrollToPanel(".preview");
  }
}

function setActiveNav(kind) {
  document.querySelectorAll("[data-section-link]").forEach(link => {
    link.classList.toggle("active", link.dataset.sectionLink === kind);
  });
}

function showCatalogueKind(kind, options = {}) {
  activeKind = kind;
  activeQuery = "";
  $("#site-search").value = "";
  renderSections();
  renderResults();
  setActiveNav(kind);
  if (options.scroll) scrollToPanel("#catalogue");
}

function renderSections() {
  const allButton = sectionButton({ label: "All files", count: DATA.items.length, kind: "all" });
  $("#section-list").replaceChildren(allButton, ...DATA.sections.map(sectionButton));
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
  button.addEventListener("click", () => showCatalogueKind(section.kind, { scroll: true }));
  return button;
}

function renderBundles() {
  const cards = bundles.map((bundle, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `workflow-card ${selectedBundle?.id === bundle.id ? "active" : ""}`;
    button.setAttribute("aria-pressed", String(selectedBundle?.id === bundle.id));
    button.innerHTML = `
      <span class="workflow-number">${escapeHtml(String(index + 1).padStart(2, "0"))}</span>
      <span>
        <h3>${escapeHtml(bundle.artefact)}</h3>
        <p>${escapeHtml(bundle.description)} · ${escapeHtml(bundle.audience)}</p>
      </span>
      <span class="workflow-time">4 stages</span>
    `;
    button.addEventListener("click", () => {
      selectedBundle = bundle;
      selectedStage = "brief";
      renderBundles();
      renderPreview();
      scrollPreviewWhenStacked();
    });
    return button;
  });
  $("#bundle-list").replaceChildren(...cards);
}

function renderTabs() {
  const tabs = stageDefinitions.map(stage => {
    const button = document.createElement("button");
    const selected = selectedStage === stage.id;
    button.type = "button";
    button.className = `bundle-tab ${selected ? "active" : ""}`;
    button.id = `tab-${stage.id}`;
    button.dataset.stage = stage.id;
    button.setAttribute("role", "tab");
    button.setAttribute("aria-selected", String(selected));
    button.setAttribute("aria-controls", "bundle-stage");
    button.tabIndex = selected ? 0 : -1;
    button.textContent = stage.label;
    button.addEventListener("click", () => selectStage(stage.id, true));
    button.addEventListener("keydown", handleTabKeydown);
    return button;
  });
  $("#bundle-tabs").replaceChildren(...tabs);
}

function handleTabKeydown(event) {
  if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
  event.preventDefault();
  const current = stageDefinitions.findIndex(stage => stage.id === selectedStage);
  let next = current;
  if (event.key === "ArrowRight") next = (current + 1) % stageDefinitions.length;
  if (event.key === "ArrowLeft") next = (current - 1 + stageDefinitions.length) % stageDefinitions.length;
  if (event.key === "Home") next = 0;
  if (event.key === "End") next = stageDefinitions.length - 1;
  selectStage(stageDefinitions[next].id, true);
}

function selectStage(stage, focusTab = false) {
  selectedStage = stage;
  renderTabs();
  renderStage();
  if (focusTab) $(`#tab-${stage}`)?.focus();
}

function renderScorecard(bundle) {
  const rows = bundle.scorecard.map(row => `
    <tr>
      <th scope="row">${escapeHtml(row.criterion)}</th>
      <td><span class="score">${escapeHtml(row.score)}/5</span></td>
      <td>${escapeHtml(row.evidence)}</td>
      <td><span class="gate gate-${escapeHtml(row.gate.toLowerCase().replaceAll(" ", "-"))}">${escapeHtml(row.gate)}</span></td>
    </tr>
  `).join("");
  return `
    <div class="review-summary">
      <table class="scorecard">
        <thead><tr><th>Criterion</th><th>Score</th><th>Evidence</th><th>Gate</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <h3>Human review before use</h3>
      <pre class="stage-copy stage-copy-short">${escapeHtml(stripMarkdown(bundle.humanReview))}</pre>
    </div>
  `;
}

function renderStage() {
  if (!selectedBundle) return;
  const panel = $("#bundle-stage");
  panel.setAttribute("aria-labelledby", `tab-${selectedStage}`);
  if (selectedStage === "brief") {
    panel.innerHTML = `
      <p class="stage-label">Professional context</p>
      <div class="stage-context">${escapeHtml(stripMarkdown(selectedBundle.context))}</div>
      <p class="stage-label">Source packet</p>
      <pre class="stage-copy">${escapeHtml(selectedBundle.sourcePacket)}</pre>
    `;
  } else if (selectedStage === "prompt") {
    panel.innerHTML = `<pre class="stage-copy">${escapeHtml(selectedBundle.prompt)}</pre>`;
  } else if (selectedStage === "output") {
    panel.innerHTML = `<pre class="stage-copy">${escapeHtml(selectedBundle.output)}</pre>`;
  } else {
    panel.innerHTML = renderScorecard(selectedBundle);
  }
}

function renderPreview() {
  if (!selectedBundle) {
    $("#preview-title").textContent = "Bundle data unavailable";
    return;
  }
  $("#preview-title").textContent = selectedBundle.artefact;
  $("#preview-description").textContent = selectedBundle.description;
  $("#preview-audience").textContent = `For ${selectedBundle.audience}`;
  $("#open-source").href = selectedBundle.sourcePath;
  const links = selectedBundle.links.map(link => {
    const anchor = document.createElement("a");
    anchor.className = `tag tag-${link.kind}`;
    anchor.href = link.path;
    anchor.title = link.path;
    anchor.textContent = `${link.label} · ${basename(link.path)}`;
    return anchor;
  });
  $("#bundle-chain").replaceChildren(...links);
  renderTabs();
  renderStage();
}

function filteredItems() {
  const terms = activeQuery.trim().toLowerCase().split(/\s+/).filter(Boolean);
  return DATA.items.filter(item => {
    const kindMatch = activeKind === "all" || item.kind === activeKind;
    const haystack = `${item.title} ${item.description} ${item.section} ${item.category} ${item.path}`.toLowerCase();
    return kindMatch && (!terms.length || terms.every(term => haystack.includes(term)));
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
    empty.innerHTML = "<h3>No matches</h3><p>Try board, tax, slide, runbook, ADR, briefing, SEO, website, or prompt.</p>";
    $("#result-grid").replaceChildren(empty);
    return;
  }

  const cards = items.slice(0, 24).map(item => {
    const card = document.createElement("a");
    card.className = "result-card";
    card.href = item.path;
    card.innerHTML = `
      <div class="result-meta">
        <span class="tag tag-${escapeHtml(item.kind)}">${escapeHtml(item.kind)}</span>
        <span class="tag">${escapeHtml(item.path)}</span>
      </div>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.description)}</p>
    `;
    const bundle = bundles.find(candidate => candidate.sourcePath === item.path);
    if (bundle) {
      card.addEventListener("click", event => {
        event.preventDefault();
        selectedBundle = bundle;
        selectedStage = "brief";
        renderBundles();
        renderPreview();
        scrollPreviewWhenStacked();
      });
    }
    return card;
  });
  $("#result-grid").replaceChildren(...cards);
}

function bindSearch() {
  const input = $("#site-search");
  input.addEventListener("input", () => {
    activeQuery = input.value;
    activeKind = "all";
    renderSections();
    renderResults();
    setActiveNav("all");
  });
  document.addEventListener("keydown", event => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      input.focus();
    }
  });
}

async function copyText(text) {
  if (navigator.clipboard?.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      // Fall through for browsers or origins that deny the async clipboard API.
    }
  }
  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  document.body.append(textarea);
  textarea.select();
  const copied = document.execCommand("copy");
  textarea.remove();
  return copied;
}

function bindControls() {
  $("#theme-toggle").addEventListener("click", event => {
    const root = document.documentElement;
    const dark = root.dataset.theme !== "dark";
    root.dataset.theme = dark ? "dark" : "light";
    event.currentTarget.textContent = dark ? "Light" : "Dark";
    event.currentTarget.setAttribute("aria-pressed", String(dark));
  });
  $("#density-toggle").addEventListener("click", event => {
    const root = document.documentElement;
    const regular = root.dataset.density !== "regular";
    root.dataset.density = regular ? "regular" : "compact";
    event.currentTarget.textContent = regular ? "Compact" : "Regular";
  });
  $("#copy-prompt").addEventListener("click", async event => {
    if (!selectedBundle) return;
    const original = event.currentTarget.textContent;
    try {
      const copied = await copyText(selectedBundle.prompt);
      if (!copied) throw new Error("Clipboard copy was rejected");
      event.currentTarget.textContent = "Copied full prompt";
    } catch {
      selectedStage = "prompt";
      renderTabs();
      renderStage();
      $("#bundle-stage").focus();
      event.currentTarget.textContent = "Select prompt text";
    }
    window.setTimeout(() => { event.currentTarget.textContent = original; }, 1600);
  });
}

function bindNav() {
  document.querySelectorAll("[data-section-link]").forEach(link => {
    link.addEventListener("click", event => {
      event.preventDefault();
      const target = link.dataset.sectionLink;
      setActiveNav(target);
      if (target === "bundles") scrollToPanel("#bundles");
      else showCatalogueKind(target, { scroll: true });
    });
  });
}

renderSections();
renderBundles();
renderPreview();
renderResults();
bindSearch();
bindControls();
bindNav();
