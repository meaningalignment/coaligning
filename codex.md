# Codex Orientation File

This markdown file is **for the agents (and authors) working on this repository over multiple sessions.**  
It captures the project’s current state, style rules, and the outstanding work so that each future Codex / ChatGPT session can pick up the thread without having to re-read everything.

> *Do **not** include this file in the final manuscript; it is internal documentation only.*


## 1 ▪ One-paragraph thesis

“Co-aligning AI and Institutions” argues that classical single-agent AI-alignment is insufficient because an aligned model embedded in mis-aligned institutions will still produce harm.  It critiques two prevailing paradigms—(i) the **Standard Institution Design Toolkit (SIDT)** with its thin preference/utility formalism, and (ii) **naive text-based value specifications** (prompts, constitutions)—and proposes **Full-Stack Alignment (FSA)**: co-align both AI and the institutions around it using **explicit, structured representations of norms and values** (“thick models of choice”).  Two design strategies (value-attractors & structural tightening) and five application domains illustrate the programme, followed by a research & adoption roadmap.


## 2 ▪ Repo layout (2025-04-28)

```
0-abstract.md            – 75-word hook + high-level abstract
1-introduction.md        – Motivation & problem framing
2-existing_toolkits.md   – Detailed critique of SIDT + naive text specs
3-new_toolkit.md         – FSA proposal (value attractors, structured norms)
4-case_studies.md        – 5 illustrative domains
5-roadmap.md             – Research & implementation plan
6-conclusion.md          – Wrap-up + open questions
7-footnotes.md           – Footnotes / side citations
8-related_work.md        – Comparison table to neighbouring work
index.md                 – Table of contents for pandoc build
TODO.md                  – Reviewer-style feedback & task list
codex.md                 – ← *you are here* (internal orientation)
```

Build/compile scripts are **not yet** included; the paper is currently edited as standalone Markdown chapters.


## 3 ▪ House style

1. Language – Use crisp, formal yet readable academic prose.  British or American English is fine; stay consistent **within a file**.
2. Citations – Inline parenthetical with author & year **or** numeric, but we must migrate to a single style before submission (see TODO #5).
3. Headings – Title Case for `#` & `##`; sentence case for deeper levels.
4. Line length – < 120 chars soft-wrap; no hard line breaks unless markdown renderer misbehaves.
5. Markdown – Fenced code blocks for examples; tables use `|` syntax; footnotes with `[^n]` defined in 7-footnotes.md.
6. Terminology – Always bold the first appearance of core FSA terms (Value Card, Moral Graph, etc.) in a file.


## 4 ▪ Open tasks snapshot

This condenses the longer TODO.md into quick “what to do next” breadcrumbs.  Update after each substantial PR.

🔹 **Easy-wins (editorial)**
   1. Glossary box after Abstract (1 page) – *not started*
   2. Worked micro-example sidebar in §3 – *placeholder present, needs prose & maybe pseudo-code*
   3. Nuance SIDT critique (§2.1 intro + footnotes 1-3) – *partial*
   4. Related-work comparison table – *draft exists in 8-related_work.md; refine & integrate where cited*
   5. Citation-style standardisation – *open*
   6. JSON schema snippet for a Value Card (appendix) – *none yet*
   7. Section “road-sign” sentences – *some done; check all top-level sections*
   8. Pluralism/legitimacy caveat in §5 – *needs 2–3 sentences*

🔹 **Substantive (may require new experiments)**
   • Formal definitions / algorithms for constitutive attentional policy, moral graph, integrity.
   • Toy environment or experiment that showcases FSA beating SIDT baseline.
   • Adoption-pathway / incentive analysis.


## 5 ▪ Typical workflow for future sessions

1. Start with `git status` / `ls -R` to refresh context.  
2. Open the relevant markdown file with `cat` or an editor tool.  
3. Apply targeted edits via `apply_patch`; keep commits small & focused.  
4. Cross-reference TODO items above and tick them off or update status notes here.  
5. Run a markdown linter / pandoc build if added later (currently none configured).  
6. Verify that footnote numbers remain sequential; update 7-footnotes.md as needed.  
7. Update this codex.md “Open tasks snapshot” section if scope changes.  


## 6 ▪ Memory joggers for the agent

• The key novelty is **structured value & norm representations**; almost every section should tie back to that.  
• Avoid straw-manning SIDT; acknowledge existing advances while insisting on what’s still missing.  
• When adding examples, prefer domains already referenced in §4 to maintain narrative cohesion.  
• Keep references minimal until we decide on a citation manager (BibTeX vs. manual list).  
• Don’t expose this codex.md in external drafts.


–––  End of file  –––
