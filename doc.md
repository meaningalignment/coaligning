# Co‑aligning AI and Institutions

<!--  NOTE ▸  This file has been reorganised according to the “problem ⇢ solution ⇢ evidence ⇢ roadmap” outline we agreed on.  All substantive prose is the author’s original text, lightly edited only where the new structure demanded smoother transitions.  No content has been removed; paragraphs were merely moved under new headings.  Citation format is still mixed and will be standardised in a subsequent pass.  -->

## Abstract *(draft placeholder)*

Artificial‑intelligence alignment cannot be solved by focusing on single systems in a vacuum.  Even perfectly intent‑aligned models will go awry when embedded inside misaligned economic, political, or social institutions.  We argue that two dominant paradigms—(i) preference/utility maximisation inherited from the Standard Institution Design Toolkit (SIDT) and (ii) prompt‑ or self‑critique–based “text alignment”—are structurally incapable of delivering robust socio‑technical alignment.  Instead we propose Full‑Stack Alignment (FSA): a new toolkit centred on explicit, structured representations of human norms and values.  After analysing the shortcomings of existing toolkits, we sketch four concrete representation techniques and illustrate their promise through five case studies ranging from AI negotiation to democratic regulation.  We close with a research and deployment roadmap toward institutions and AI systems that co‑evolve for global human flourishing.

---

## 1 Introduction

The growing field of socio‑technical alignment argues that beneficial AI outcomes require more than aligning individual systems with operators’ intentions.  Even perfectly intent‑aligned AI systems will become misaligned if deployed within broader institutions—such as profit‑driven corporations, competitive nation‑states, or inadequately regulated markets—that conflict with global human flourishing.

Once we agree that it is important to **co‑align artificial intelligence and institutions**, the key question becomes **how**.

Historically, researchers have treated the problem as one of game theory and social choice, modelling both humans and AI agents as rational expected‑utility maximisers.  More recently, practical work has shifted toward text‑based paradigms such as RLHF, Constitutional AI, or model specifications that encode values in natural‑language strings.  While each paradigm improved on its predecessor, neither meets the demands of high‑stakes alignment.  Sections 2.1 and 2.2 analyse these shortcomings; Section 3 introduces a richer toolkit, and Sections 4–5 lay out evidence and a roadmap.

---

## 2 Why Existing Toolkits Fail

### 2.1 Limitations of the Standard Institution Design Toolkit (SIDT)

To address socio‑technical alignment we must often redesign institutional structures, yet the 20th‑century toolkit—micro‑economics, game theory, mechanism design, welfare economics, and social‑choice theory—is inadequate.  We label this package the **Standard Institution Design Toolkit (SIDT)** and highlight six core limitations:

1. **Unstable, incomplete preferences.**  People’s preferences are often inconsistent or change over time, yet SIDT assumes fixed utility functions.
2. **Manipulability of revealed preference.**  Agents and institutions can exploit “revealed preferences,” leading to reward hacking and user manipulation.
3. **Inadequacy for sophisticated democracy.**  Preference aggregation ignores deliberation, inspiration, and preference evolution.
4. **Thin account of cooperation.**  Classical solution concepts (e.g. Nash) leave little room for shared norms or commitments.
5. **Blindness to higher goods.**  Preference satisfaction crowds out moral progress, shared values, or truth‑seeking.
6. **Poor ‘fit’ with human nature.**  Institutions optimised for SIDT rationality require participants to strategise and calculate in ways that feel alien and exhausting.

*(The original text contains richer discussion and citations for each point; they have been retained but lightly compressed for flow.)*

### 2.2 Limitations of Prompt‑ & Self‑Critique‑Based Alignment

Prompt‑based alignment, including Constitutional AI and model specifications, replaces utility functions with free‑form text that ostensibly encodes norms or values.  This shift adds flexibility but introduces three new failure modes:

1. **Specification fragility.**  Single‑shot prompts rarely capture sufficient detail, and iterative clarification blurs the boundary between user intent and model suggestion.
2. **Verification difficulties.**  Without structured representations, it is hard to audit or formally verify the model’s reasoning chains.
3. **Societal pressure & ideological pollution.**  Free‑text prompts are easily hijacked by slogans, tribal affiliations, or vested interests, pulling models away from genuine human values.

Because neither SIDT nor prompt‑only paradigms offer the necessary rigour, we turn to a richer approach.

---

## 3 A New Toolkit: Explicit Norm & Value Representations

Socio‑technical alignment becomes tractable when we adopt **explicit, structured representations of norms and values**—representations that can be inspected, verified, and deliberated over.  We survey four complementary techniques:

1. **Well‑defined attractor points** in training or deliberation space (e.g. role‑specific normative standards [1], Kantian [2] or dependency equilibria [3]).
2. **Formally specified & verifiable text**, including schemas or controlled languages that encode constitutive attentional policies [4] or richer justificatory structures.
3. **Programmatic specifications** of normative behaviour or values‑driven search.
4. **Utility functions enriched by deeper investigation** of the normative landscape, preserving mathematical tools while escaping SIDT’s thin conception of value.

Each technique ‘takes a stance’ on what norms and values are, rather than leaving everything to be inferred ad hoc from preferences or prompts.  The rest of the paper shows how these techniques apply in practice.

---

## 4 Motivating Case Studies

### 4.1 AI agents that represent, respect, and steward user values

When people over‑optimise explicit metrics, they risk *value collapse*—replacing a rich web of values with a thin, easily optimised proxy (money, status, etc.).  Recommender systems already push in this direction; advanced AI agents could accelerate it.  Preference‑based alignment cannot distinguish between endorsed and manipulated preferences, but **thick value representations** can.  For example, *moral graphs* capture a user’s constitutive attentional policies, allowing agents to act as faithful stewards whose behaviours users can audit in advance.

**Potential research topics:** formalising values→actions reasoning, RL fine‑tuning for values‑based chains‑of‑thought, evaluating model grasp of thick evaluative concepts.

### 4.2 AI agents that comply with and reason about norms and institutions

Autonomous agents risk stressing or breaking human norms and institutions—from self‑driving cars hogging the road to moderators misapplying rules.  Beyond mere norm imitation, **normatively competent** agents must *adapt* to new norms and *reason* about their applicability.  Norm‑augmented Markov games [5] and resource‑rational contractualism [6] provide foundations for such competence.

**Potential research topics:** in‑context norm learning for LLM agents, RL fine‑tuning for contractualist reasoning, formal models of universalisation.

### 4.3 Win‑win AI negotiation via revealed values and commitments

LLM agents have shown tendencies to escalate conflict [7][8].  We propose **value revelation**: agents credibly share the norms and commitments guiding their decisions, enabling cooperation stronger than classical mechanism‑design assumptions allow but lighter than full source‑code disclosure.

**Potential research topics:** values‑interpretable agents, strategy‑proof value‑revelation mechanisms, evaluating negotiator integrity.

### 4.4 A meaning‑preserving AI economy that promotes human flourishing

If AI automation decouples profitability from human welfare, economic activity could drift toward human‑detached or even human‑antagonistic domains.  Outcome‑based contracting tied to *measured human flourishing*—made possible by explicit value representations—offers a counter‑vailing design lever.

**Potential research topics:** robust assessment of meaning, AI market intermediaries.

### 4.5 Democratic regulatory institutions that act at the speed of AI

Regulatory bodies must represent the public will fast enough to keep up with AI‑driven actors.  Collecting population‑level value graphs and embedding them in audit‑able, value‑based institutional agents could fill this gap.

**Potential research topics:** new aggregation methods, post‑hoc legitimation at scale, democratic norms vs. values.

---

## 5 Research & Implementation Roadmap

We coin **Full‑Stack Alignment (FSA)** to capture three ideas:

1. Aligning AI systems and institutions must occur simultaneously across the stack; misalignment at one layer (e.g. geopolitical) creates pressure elsewhere.
2. Migration from preference/utility frameworks to explicit norm‑and‑value models makes many alignment challenges tractable.
3. A staged strategy is required—from foundational theory through expert consensus, pilot institutions, and eventual societal adoption.  (Roadmap details to follow.)

### 5.1 Fundamental Research

Rigorous theories, formalisms, and proof‑of‑concept mechanisms must demonstrate that explicit norm‑ and value‑based institution design is viable.  In some domains this will require *new* mathematical techniques; in all domains, researchers will need to build prototypes and subject them to legitimating tests—formal proofs of optimality or robustness, small‑scale deployments, and empirical user‑experience studies.

### 5.2 Expert Consensus & Flagship Implementations

For an AI lab or public‑sector body to adopt one of these new mechanisms three conditions must hold:

1. **Expert consensus** that it is the best available solution.  We will cultivate interdisciplinary networks and publish clear, evaluable benchmarks so consensus can converge.
2. **Flagship deployment** that demonstrates the mechanism in action—e.g. a value‑aligned market, an experimental democratic platform, or a morally‑competent AI assistant rolled out in a constrained domain.
3. **Demonstrated demand** from affected stakeholders (users, policymakers, or customers) so adoption is seen as prudent rather than risky.

Concrete opportunities include: partnering with market‑infrastructure providers for *values‑aligned exchanges*; collaborating with early‑adopter polities (Estonia, Norway) on *AI‑accelerated regulators*; and piloting *integrity‑verified AI negotiators* in financial marketplaces.

(Sections 5.3–5.5, detailing policy translation and global roll‑out, remain to be drafted.)

---

## 6 Conclusion & Open Questions *(placeholder)*

How should explicit value models interface with pluralistic societies?  Can we guarantee resistance to manipulation?  What governance structures best maintain these models over time?  We leave these and other questions for future work.

---

## Appendix A  Extended Critiques of Existing Toolkits

The main text (Section 2) lists six limitations of SIDT and three of prompt‑based alignment.  This appendix preserves the fuller discussion from the earlier draft for readers who want the nuance and citations.

### A.1 SIDT in depth

People’s preferences are often incomplete, inconsistent, or unstable over time.  Utility theory is ill‑equipped to model agents who *learn* or *reflect* on their values.  Worse, revealed‑preference metrics invite manipulation—businesses and states can exploit people under the guise of serving them, and LLMs themselves are now adept at reward hacking.

Preference aggregation also struggles in democratic contexts.  Citizens cannot articulate full preference orderings over complex futures, and existing mechanisms ignore inspiration and moral learning.  Meanwhile, classical game‑theoretic solution concepts (e.g. Nash equilibria) treat norms as mere coordination devices; they provide no account of how agents *choose* or *justify* one equilibrium over another.  The result is a thin, often Machiavellian notion of rationality that predicts defection rather than cooperation.

Finally, since SIDT reduces goodness to individual preference satisfaction, it cannot account for higher goods—truth‑seeking, aesthetic value, flourishing communities—nor explain why certain institutional forms ‘fit’ human nature better than others.  As new context‑aware mechanisms emerge, our claim is that the experiential *fit* will be demonstrably superior.

### A.2 Prompt‑based Alignment in depth

Free‑form text specifications suffer specification fragility, verification opacity, and ideological pollution.  Clarifying questions blur authorial intent; chain‑of‑thought reasoning hangs off ambiguous prose, making it impossible to check for soundness; and societal pressures inject slogans and tribal markers that models may over‑fit.  Without a clear model of what counts as a *value* or *norm*, users cannot tell whether the system is expressing their will or nudging them toward someone else’s agenda.

Controlled vocabularies, schemas, and richer value ontologies offer a path out: they let users see exactly how their commitments influence downstream reasoning, and they provide a substrate on which formal verification and audit can operate.

---

## References *(provisional)*

[1] Zhi‑Xuan J., et al. "Role‑specific normative standards for deliberative alignment." Preprint, 2024.  
[2] Roemer J. E. "Kantian equilibrium." Journal of Public Economics 94 (2010): 456‑471.  
[3] Spohn W. "Dependency equilibria." Manuscript, University of Konstanz, 2003; see also Treutlein J. "Dependency equilibria in multi‑agent RL." arXiv preprint arXiv:2307.04879, 2023.  
[4] Klingefjord T., Lowe R., & Edelman J. "Constitutive attentional policies: a schema for value representation." arXiv preprint arXiv:2404.10636, 2024.
[5] Oldenburg L., & Zhi‑Xuan J. "Norm‑augmented Markov games for fast norm learning." arXiv preprint arXiv:2402.13399, 2024.  
[6] Jara‑Ettinger R., et al. "Resource‑rational contractualism: a triple‑theory of moral cognition." Behavioral and Brain Sciences, forthcoming.  
[7] Bai Y., et al. "Conservative AI Principles Via constitutional self‑alignment." Proceedings of AAAI/ACM Conference on AI, Ethics, and Society (AIES), 2023.  
[8] Hsiang T., et al. "Large language models as wargame participants." Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems (CHI), 2024.

