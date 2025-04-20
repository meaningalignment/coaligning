# Related Work Comparison

The literature on alignment, mechanism design, ethics, and multi‑agent learning is vast.  This appendix situates *Full‑Stack Alignment (FSA)* concepts alongside the closest ideas in adjacent fields and highlights the delta each contribution adds.  The table is meant as a navigational aide rather than an exhaustive survey.

| FSA concept | Closest idea in economics / mechanism design | Closest idea in AI / cooperative AI | Key delta introduced by FSA |
|-------------|----------------------------------------------|-------------------------------------|------------------------------|
| **Constitutive attentional policy** (value *card*) | Preference refinement / lexicographic utilities | RLHF preference model; Chain‑of‑Thought rationales | Explicitly distinguishes *constitutive* from *instrumental* considerations and is designed for auditability & endorsement, not just optimisation. |
| **Moral graph** (value graph at population scale) | Welfare function with interpersonal comparisons; Social welfare ordering | Value aggregation via voting models, e.g. quadratic voting; democratic RL | Captures *relationships* (refines, conflicts, supersedes) among values  +  supports contestability; not a single scalar objective. |
| **Value attractor / self‑other generalisation** | Kantian equilibrium (Roemer 2010), dependency equilibria | Cooperative MARL regularisers (e.g. LOLA, Opponent Shaping) | Treats convergence criteria as *normative* fixed points rather than merely strategic equilibria. |
| **Integrity & value revelation** | Costly signalling; cheap‑talk equilibria with credence | Open‑source game theory; model watermarking | Middle ground: share structured value commitments (partial source code) that are verifiable but keep strategic internals private. |
| **Norm‑augmented Markov games** | Social & moral preferences in repeated games | Normative RL, Social Influence bonus | Formal separation between individual pay‑offs and population norms enables rapid norm learning & adaptation. |
| **Resource‑rational contractualism** | Rawlsian contractarianism, bargaining solutions | Virtual bargaining (Jara‑Ettinger et al.) | Implements *bounded* universalisation that scales to LLM reasoning budgets. |
| **Outcome‑based contracting for meaning** | Dynamic principal–agent contracts | Alignment via reward models of human satisfaction | Pay‑outs keyed to *measured flourishing* using structured value schema; resists preference manipulation. |
| **Democratic regulator at AI speed** | Delegative / liquid democracy; participatory budgeting | Alignment assemblies; LLM policy bots | Builds legitimacy on population‑level moral graph and provides verifiable reasoning traces in real time. |
| **Values‑interpretable architectures** | Mechanism transparency (auditability) | Interpretable self‑explaining neural networks | Ties explanations to *formal value objects* rather than post‑hoc saliency maps. |
| **Thick evaluative concept competence** | Sen’s capability approach | Expression of moral concepts in LLMs (Anthropic, DeepMind studies) | Requires models to map concepts to structured attentional policies, enabling verification and refinement. |

*Citations (representative):* Gul & Pesendorfer 2001; Bewley 2002; Fehr & Schmidt 1999; Tversky & Kahneman 1992; Roemer 2010; Oesterheld 2022; Jara‑Ettinger 2023; Goel et al. 2019; Anthropic 2022.
