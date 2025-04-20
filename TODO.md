# Here's what o3 thinks

“Co‑aligning AI and Institutions” is an ambitious, concept–driven position paper that argues the alignment community must move beyond (a) utility / preference–maximisation inherited from economics and (b) today’s largely text‑based “prompt or constitution” techniques, and instead build AI systems and social institutions around explicit, structured representations of norms and values.  The authors call the resulting research programme Full‑Stack Alignment (FSA) and sketch two complementary technical avenues (value‑attractors & tighter structural definitions) plus five motivating case studies.

What works well

• Timely scope‑expansion The paper squarely addresses the mounting realisation that “single‑agent alignment” is inadequate once AI systems are embedded in markets, firms, nations,
  etc.
• Clear diagnosis of limitations The critique of revealed‑preference economics (instability, manipulability, blindness to higher goods, etc.) and of pure natural‑language constitutions (specification fragility, unverifiability, ideological drift) is persuasive and crisply articulated.
• Constructive alternative By insisting on inspectable, formal-ish value / norm objects, the paper offers a concrete pivot rather than a purely negative critique.  The two proposed families—(1) attractor‑based convergence criteria and (2) constitutive‑attentional‑policy style schemas—come with pointers to relevant literature (Kantian equilibria, value graphs, resource‑rational contractualism).
• Rich illustrative domain list The five case studies (value‑stewarding agents, norm‑competent agents, value‑revealing negotiators, meaning‑preserving economy, AI‑speed regulation) showcase the breadth of the programme and help non‑specialists see why the tooling matters.
• Road‑map orientation Section 5 gives readers a sense of “what to work on Monday morning”, which many alignment manifestos lack.

Where it still feels thin

    1. Formal precision
        • Key constructs (“constitutive attentional policies”, “moral graph”, “integrity”) are described narratively; no formal definitions, data‑structures, or algorithms are provided.
        • Without sample representations or toy experiments it is hard to assess tractability or compute cost.
    2. Empirical grounding
        • The case studies are thought‑experiments.  Even a miniature proof‑of‑concept (e.g. an RL environment where agents with explicit norm objects outperform utility‑maximisers) would dramatically strengthen the argument.
    3. Over‑general critique of SIDT
        • Modern mechanism‑design already contains richer models (stochastic preferences, menu‑dependent choice, participatory budgeting, etc.).  A more nuanced comparison would acknowledge this progress and clarify the delta FSA adds.
    4. Governance & pluralism
        • Saying that structured value graphs yield “democratic legitimacy” does not by itself address plural, in‑commensurable values or power asymmetries in who authors the schemas.  The paper could engage with political‑philosophy work on legitimacy, contestability, and value disagreement.
    5. Adoption pathway
        • The roadmap outlines research stages but is lighter on incentive design or institutional realpolitik: Who funds, standardises, and enforces these structured value objects?  How do we migrate existing organisations?

Suggestions for a revision

• Add a worked example—e.g. represent the classic Trolley Problem in a constitutive‑attentional‑policy language and show how an LLM conditioned on that representation passes a new
  moral generalisation test.
• Provide a minimal API / type‑signature for “value card”, “norm schema”, and “moral graph”; contrast with RLHF reward models.
• Compare FSA to adjacent proposals (Cooperative AI foundation models, Stuart Russell’s “assistance games”, Anthropic’s Constitutional AI) in a dedicated related‑work section.
• Address pluralism explicitly: how are conflicting value graphs merged, and who arbitrates when universalisation fails?
• Sketch an incremental deployment plan (start inside safety‑critical verticals → open standard → regulatory endorsement).

Bottom line

The paper is intellectually stimulating and pushes the conversation in a vital direction; however, to persuade a technically minded audience it needs a tighter bridge from concept to implementation and clearer engagement with existing advanced work in economics, mechanism design, and cooperative AI.  With one or two concrete prototypes and a more fine‑grained literature comparison, it could become a cornerstone reference for socio‑technical alignment research.

# Furthermore

Here are “easy‑wins” that would materially strengthen the manuscript yet require only light editorial work (a few hours each, not new experiments).

1. Add a one‑page Glossary / Definitions Box (after the Abstract)
    • Define: constitutive attentional policy, moral graph, integrity, value attractor, Kantian equilibrium, resource‑rational contractualism…
    • Benefit: readers never lose the thread; reviewers get crisp handles for critique.
2. Insert a worked micro‑example sidebar (½–1 page, Section 3)
    • Encode a familiar dilemma (e.g., Trolley) with two value cards + a norm card.
    • Show—in plain English, no code—how the “universalise” rule selects an action.
    • Benefit: instantly makes the abstract framework concrete; no new data needed.
3. Nuance the SIDT critique (expand §2.1 intro paragraph + footnotes)
    • Acknowledge modern extensions (incomplete preferences, participatory budgeting, menu‑dependent choice).
    • Cite 2‑3 representative papers and specify *what is still missing* for FSA.
    • Benefit: pre‑empts “straw‑man” push‑back with minimal text changes.
4. Add a Related‑Work comparison table (end of Section 3 or Appendix)
    Columns: FSA construct | Mechanism‑design analogue | Cooperative‑AI analogue | Key delta
    • 10–12 rows, ½ page.
    • Benefit: situates contribution; reviewers love tables.
5. Provide a citation‑style cleanup pass
    • Normalise to one format (APA or numeric) and ensure every in‑text citation appears in refs.
    • Benefit: polish; prevents desk‑reject for style sloppiness.
6. Supply an Appendix snippet of the proposed JSON schema for a Value Card
    • 20 lines of annotated JSON or YAML.
    • Benefit: gives technically minded readers a tangible artefact without committing to full implementation.
7. Tighten Section headings & forward pointers
    • Add one‑sentence “road signs” at the start of Sections 2, 3, 4 (“In this section we …”).
    • Benefit: improves flow; costs minutes.
8. Clarify governance & pluralism caveat (2–3 sentences in §5)
    • Acknowledge value conflict and outline how moral graphs remain contestable.
    • Benefit: closes an obvious hole; avoids needing a full new subsection.