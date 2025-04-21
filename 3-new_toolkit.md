# A New Toolkit: Explicit Norm & Value Representations

Having seen why existing approaches break down, this section introduces the central proposal of the paper—Full‑Stack Alignment via *explicit, structured representations* of norms and values. We first outline two complementary design strategies (value‑attractors and structural tightening) and then preview how these tools integrate with familiar methods in economics and machine learning.

The limitations of both preference-based and text-based paradigms point to a common inadequacy: neither takes a substantive stance on what norms and values are. Utility functions can represent any consistent set of choices, constructive or destructive; text strings can encode any instructions, cooperative or uncooperative.

We will argue that socio-technical alignment becomes tractable when we adopt **explicit, structured representations of norms and values**—representations that can be inspected, verified, and deliberated over.

What distinguishes our approach is the commitment to **explicit**, **accountable**, and **structured** representations of what matters, rather than leaving normative content to be inferred ad hoc by models or users. This epistemological stance—that values and norms have discernible structure that must be explicitly modeled—is, we argue, necessary for addressing high-stakes socio-technical alignment challenges.

Here are two fundamental ways to implement this approach:

## 1. Value Convergence: Identifying Stable Normative Reference Points

The first approach identifies well-defined attractor points in training or deliberation space toward which values or norms naturally trend. This approach posits that certain normative structures emerge reliably when we examine patterns of convergence across agents, contexts, or time frames.

Recent work on self-other generalization exemplifies this approach, conceptualizing values as considerations that exhibit stability across different agents' standpoints and/or across contexts and time frames for a single agent. This echoes philosophical work by Velleman on values as enabling compact, self-understandings and self/other understandings. In *Practical Reflection* (1989) and *How We Get Along* (2009), Velleman argues that values emerge through a compression process: considerations that are good across multiple agents, time frames, and contexts are more likely to represent genuine values rather than instrumental concerns or contingent preferences.

Similarly, instead of analyzing stable strategic outcomes in terms of Nash equilibria or correlated equilibria, we could model certain forms of decentralized cooperation as *Kantian equilibria* (Roemer, 2010) or *dependency equilibria* (Spohn, 2003; Treutlein, 2023), where agents *universalize their policies* to relevantly similar agents when deciding what to do. This makes norms a stable attractor in policy space, given a social set-up.

## 2. Tightening the Structure of Norms and Values

The second approach characterizes the structure of norms or values more precisely, so as to exclude some coherent preference-relations or text strings that would not qualify as genuine values or norms.

Instead of representing the value(s) associated with a choice in terms of one or more utility functions, we can represent values as sets of *constitutive attentional policies* (Klingefjord, Lowe, & Edelman, 2024)—criteria that one intrinsically attends to when making decisions guided by a particular value. Such a specification language:

- Distinguishes constitutive from instrumental considerations
- Excludes tribal affiliations and ideological markers
- Represents the phenomenology of value-guided attention
- Enables verification of reasoning chains

Similarly, a norm could be structured as a constraint system, or as a filter for altering a plan of action so as to comply with the norm. Such schemas for values or norms protect alignment targets from pollution by arbitrary external goals or social pressures that cannot be properly characterized as norms or values.

These structured representations enable more robust forms of normative reasoning about potential actions. Rather than axiomatizing rational choice via completeness and independence, we can adopt *thicker accounts of normative justification*, where choices are reasonable insofar as they can be justified according to contextually-relevant criteria (e.g., Does the choice promote one's values? Does it uphold the standards of one's social role? Is it reasonably rejectable by others affected by the choice?).

## Integration with Existing Methods

These two approaches to structured normative representation need not take us too far afield from current methods in game theory, microeconomics, and RL training:

- The major results of rational choice, game theory, and microeconomics assume the existence of utility functions that represent preference orderings which comply with certain axioms of rationality. To capture richer sets of values and norms, this basic mathematical structure can be preserved, but the space of objects over which utility functions are defined can be enriched significantly—"utility" would no longer reflect the individual preferability of some option, but something thicker, such as an all-things-considered value judgment.

- For instance, an enriched model of rational choice can account for how agents trade off norm compliance with their individual desires or objectives when taking actions, resulting in norm-augmented utility functions (Oldenburg & Zhi-Xuan, 2024). This factoring would be useful for determining new norms that better promote each individual's interests, or for designing welfare functions that account for intrinsically-valued norms while factoring out oppressive norms.

- Similarly, one can model how individuals make decisions based on values that are constitutive of their conception of a good life, weighted against considerations that are merely instrumental to some further value or goal (Edelman, 2022). These trade-offs can be captured by a utility function, but an institution or algorithm might prioritize constitutive values over instrumental ones.

- RL-based training methods which condition on reasoning traces can still be used, but instead of having a human annotator or an unprincipled expert model evaluate the reasoning, it can be evaluated more systematically via formal models of values-based reasoning.

Each approach 'takes a stance' on what norms and values are, rather than leaving everything to be inferred ad hoc from preferences or prompts. This commitment to explicit structure is essential for addressing the socio-technical alignment challenges that define our time. In the following section, we demonstrate how these techniques apply in practice through five case studies spanning diverse domains.
