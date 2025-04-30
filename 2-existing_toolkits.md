# 2 Why Existing Toolkits Fail

## 2.1 Inadequacy of Utility Function and Preference-Based Approaches

To address the challenge of socio‑technical alignment we must rethink how institutions are designed and evaluated. The formal apparatus that still dominates this work—microeconomics, game theory, mechanism design, welfare economics, and social‑choice theory—was forged in, and for, the 20th century. We bundle these strands under the label *Standard Institution Design Toolkit (SIDT)*.

The SIDT idealises agents as *utility / preference maximisers*: each individual comes equipped with a complete, context‑independent ordering over outcomes. Over the last three decades researchers have proposed a wealth of refinements—menu‑dependent and **incomplete** preferences (Gul & Pesendorfer 2001; Bewley 2002), models of **social** or **other‑regarding** preferences (Fehr & Schmidt 1999), **behavioural** relaxations of expected‑utility axioms (Tversky & Kahneman 1992), and participatory-budgeting or quadratic-voting mechanisms that elicit richer information (Goel et al. 2019). These advances fix important *technical* bugs, yet they leave four *philosophical* limitations untouched:

### 2.1.1 Epistemic Limitations

The SIDT suffers from fundamental **opacity**: preferences remain private data with no shared representation that lets others audit, deliberate over, or contest them[^1]. Without an inspectable model of what people value and why, we cannot verify that AI systems have properly understood human intentions.

Preference-based approaches also cannot account for how human values actually function. People's preferences are often **incomplete**, **inconsistent**, and **unstable** over time. Utility theory lacks mechanisms to model agents who change, reshape, and discover preferences—much less agents that *reason* about which preferences or values are more sensible or justified to hold.

When scaled to collective contexts, this opacity creates accountability gaps. Representative agents cannot explain their reasoning about values, and there's no way to validate or challenge an AI's interpretation of what a community considers worth preserving or pursuing.

### 2.1.2 Autonomy Problems

The SIDT exhibits **a-normativity**: it stays neutral about *which* preferences are worth having and cannot distinguish authentic desires from manipulated ones[^2]. As established in welfare economics debates associated with Amartya Sen, revealed preference proves fundamentally limited as a measure of benefit.

Businesses, governments, and other entities have learned to exploit individuals under the guise of serving preferences, particularly through AI systems[^3]. As AI systems grow more sophisticated and pervasive, this manipulation intensifies. Current AI models actively engage in reward hacking[^4], and humans similarly "hack" themselves through behaviors that satisfy proximate preferences while undermining deeper values.

This creates a significant challenge: SIDT provides no principled way to distinguish authentic from manipulated preferences, considering humans to be "fulfilling their preferences" even when engaged in maladaptive behaviors like compulsive scrolling or AI-mediated addiction. A preference-maximizing model happily optimizes users into digital dependence because the revealed data say "they like it," creating inherent vulnerabilities in any system designed on these foundations.

### 2.1.3 Sociality Deficiencies

The SIDT exhibits **context-blindness**: utility is attached to solitary outcomes, not to the mesh of roles, narratives, and shared norms in which human action is embedded. This ignores how our values are fundamentally shaped by social context.

Game-theoretic approaches to cooperation—a cornerstone of the SIDT—fail to capture how humans actually cooperate. In classical solution concepts like Nash equilibria, agents maximize payoffs assuming independent and uncorrelated actions. This view of "rational" multi-agent interaction provides no framework for understanding genuine shared social norms.

Standard game theory has been repeatedly criticized for failing to predict cooperation in settings like the one-shot Prisoner's Dilemma, where humans frequently cooperate, and for its inability to explain humans' ability to make and maintain promises without external enforcement. The strategic rationality endorsed by conventional game theory is essentially Machiavellian—a rationality where deceptive promises are considered reasonable and coercive tactics are fair play.

This inadequacy extends to democratic institutions. Preference/utility frameworks in social choice theory fail to support sophisticated democratic processes where:

- Impacted individuals typically lack time to express detailed preferences about every possible outcome
- Representative agents cannot provide accountable reasoning
- Preference frameworks assume static preferences rather than capturing how preferences evolve through deliberation

The standard version of social choice misses the most powerful lever in democratic deliberation: inspiration. Effective democratic mechanisms should not merely aggregate existing preferences but facilitate the formation of new ones.

### 2.1.4 Aspirational Blindness

Perhaps most fundamentally, the SIDT assumes agents have fixed preferences disconnected from broader notions of the good. This prevents individuals, societies, and AI systems from aspiring to ideals beyond preference satisfaction.

Our social embeddedness—whether understood through shared values, norms, or beliefs—suggests forms of goodness beyond preference satisfaction: moral progress, enhanced cooperation across scales, and the discovery of deeper truths[^9]. As long as individual preferences remain the sole measure of good, these dimensions cannot be acknowledged.

While preference satisfaction metrics might show economic growth, other social goods appear to be declining: our capacity for collective knowledge production has deteriorated through misinformation; shared moral frameworks have weakened; and cooperation mechanisms have eroded across various domains. Preference-based metrics cannot detect these declines, nor would AI systems designed to maximize preference satisfaction address them.

### 2.1.5 The Fundamental Misalignment

These four limitations point to a deeper problem: a fundamental misalignment between SIDT's model of human agency and how humans actually relate to values and norms. The ultimate test of any framework for human agency is how well the systems it informs *fit* human nature. Current mechanism design implies agents who optimize, calculate, strategize, and reduce values to numbers. These activities aren't foreign to human nature, but they don't capture its fullness.

Consequently, participating in institutions designed on these principles requires constant effortful adaptation. People must translate their rich value landscape into the narrow language of preferences and utilities, abandoning much of what gives those values meaning in the first place.

The SIDT achieved prominence because it offered mathematical expressiveness and parsimony. These theories were "good enough" for the institution design challenges of their era. However, contemporary AI alignment challenges require novel governance forms that the SIDT cannot adequately conceptualize or analyze. We need approaches that better reflect how humans actually relate to values, norms, and social coordination.

## 2.2 Inadequacy of Naive Value-Representations

While the SIDT relies on mathematics at the expense of normative understanding, natural language approaches swing to the opposite extreme. From AI constitutions to alignment prompts, these approaches encode values as free-form text—simple to author but destined to break under institutional pressure. The core problem is not that these specifications use natural language, but that they lack any principled structure to constrain interpretation or guide reasoning.

These naive approaches turn alignment into a glorified game of "guess what I mean," where AI systems must extract coherent principles from ambiguous instructions and apply them consistently across novel contexts. This methodology might work for low-stakes applications, but it fundamentally cannot scale to the institutional challenges of socio-technical alignment. Three critical vulnerabilities illustrate why:

### 2.2.1 Specification Challenges

Naive text-based alignment begins with an impossible task: distilling complex human values into unambiguous instructions. Even with iterative refinement, text specifications inevitably suffer from both under- and over-specification—simultaneously too vague in critical areas and too specific in others. These problems compound exponentially as AI systems take on more complex responsibilities, where chains of reasoning create distance between stated intentions and resultant behaviors.

Having agents request clarification through follow-up questions merely postpones the fundamental problem. Without structured representations of values or norms, it becomes difficult to determine when sufficient information has been gathered to guide decision-making appropriately. The model lacks clear criteria for understanding what constitutes an adequate representation of a user's values or the norms appropriate to a context.

This specification problem manifests in several ways:

1. **Elicitation Confusion**: In extended dialogues between users and AI systems, it becomes increasingly difficult to distinguish genuine user preferences from model-suggested options that users simply accept. User satisfaction may reflect successful preference elicitation or subtle manipulation, with no clear way to tell the difference.

2. **Aspirational Vagueness**: In social contexts where multiple stakeholders are involved, natural language representations tend toward abstract principles that sound appealing but provide minimal concrete guidance. Constitutional approaches often produce statements like "The AI should always do the right thing" or "The AI should be fun"—principles that are impossible to operationalize consistently across contexts and stakeholders.

As documented in our analysis of Constitutional AI approaches[^10]:

> "These constitutional approaches are not fine-grained: principles are generally vague and can be interpreted in many ways. Many different principles might apply for a given output and there is no way of reconciling which principle should be prioritized in a given context. This makes them less auditable, as it's difficult to determine which principles were used to produce a particular output.
>
> For example, these comments were surfaced as shared 'values' by CCAI:
> - The AI should always do the right thing
> - The AI should not give advice
> - The AI should be fun
> - The AI should actively address and rectify historical injustices and systemic biases
> - The AI should remain unbiased and state only proven facts
> - The AI should promote self-motivation and positive reinforcement
>
> Are these all values? Some seem more like policies, some like vague aspirational statements, some like goals. If a person upvotes one of these comments, can we assume they have a particular value? The same one that others who upvoted that comment have?"

3. **Ideological Pollution**: Value elicitation methods that rely on free-form text often become contaminated with polarized ideological markers rather than authentic personal values. Statements like "Defund the Police" or "Family Values" typically reflect tribal affiliations rather than the actual values that guide individuals' meaningful choices.

### 2.2.2 Reasoning Verification Problems

Even if we could obtain adequate natural language specifications, verifying that an AI system correctly reasons about these specifications remains problematic. Without structured representations, an AI's reasoning processes can connect to text in arbitrary ways that resist systematic verification.

While formal models exist for reasoning about values and norms—models that can validate whether normative reasoning is sound—they require structured inputs rather than arbitrary text. Free-form language allows too many interpretive pathways, making it impossible to guarantee consistent application of principles across different contexts and time periods.

### 2.2.3 Vulnerability to Social Pressure

Finally, the use of free-form text for alignment targets makes them vulnerable to various forms of social pressure. When anything can be added to prompts or constitutional principles, alignment targets become susceptible to tribal affiliations and ideological signaling that may redirect AI behavior away from what affected populations would consider wise and toward adherence to prevailing rhetorical positions.

The prevalence of ideological markers in value elicitation is not accidental but reflects intense social pressures that influence how people articulate their values and norms. The challenge lies in developing methods that can bypass these pressures to access genuine personal and shared values.

A promising approach involves developing clear, structured models of values and norms that end-users can understand and apply. Such models would specify what counts as a value or norm rather than relying solely on free-form text. With these structured representations, users can better distinguish their authentic values from imposed ideological positions.

Previous research demonstrates the efficacy of this approach[^11]:

> "If someone claims to have a value like 'Defund the Police' or 'Abortion is Murder,' they are then asked about meaningful choices they themselves have made, and what they paid attention to during the choice. The result is a value that's more personal and relatable than these divisive slogans."

This approach to eliciting structured value representations can mitigate the influence of ideological rhetoric, enabling more authentic representation of both individual and collective values in AI systems.
