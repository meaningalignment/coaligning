# A New Toolkit: Explicit Norm & Value Representations

The advantage with preference relations or text strings, is they can represent anything. No assumptions get baked in about what values are, when they apply, or about the nature of the good (what kinds of attractor states values tend towards).

But this is also a great weakness: it means an alignment target specified in either of these ways can be pushed in any direction, arbitrarily. It can be polluted by considerations we wouldn't, on reflection, want to call values -- considerations which don't point to or converge towards anything anyone would call good.

This is one root cause of the problems with SIDT and the naive textual approaches catalogued in Section 2: it is why addictive or manipulated behaviours can masquerade as bona-fide "values", why zero-sum brinkmanship in negotiation is mistaken for "optimal cooperation", why ideological signals like 'Defund the Police' or 'Family Values' get treated as fundamental values rather than tribal affiliations, and why vague aspirational statements like 'AI should always do the right thing' offer minimal practical guidance while creating an illusion of normative constraint.

To overcome these limitations, we need a framework that takes a substantive stance on what values and norms actually are, rather than treating all preference relations or text strings as equally valid candidates.

## The Central Proposal: Full-Stack Alignment via Explicit Representations

This section introduces the central proposal of the paper—Full‑Stack Alignment via *explicit, structured representations* of norms and values. Rather than leaving normative content to be inferred ad hoc by models or users, we advocate for **explicit**, **accountable**, and **structured** representations of what matters.

What distinguishes our approach is the commitment to modeling values and norms with discernible structure that can be inspected, verified, and deliberated over. This epistemological stance is necessary for addressing high-stakes socio-technical alignment challenges precisely because it overcomes the key limitations of both preference-based and text-based paradigms: neither of those paradigms takes a substantive stance on what norms and values are meant to point towards. Utility functions can represent any consistent set of choices, constructive or destructive; text strings can encode any instructions, cooperative or uncooperative.

Our central thesis is that genuine values and norms have inherent structure that can be represented explicitly. This structure manifests in two key ways, each corresponding to a complementary implementation strategy:

## 1. Identifying Convergent Value Patterns

The first approach identifies specific patterns that consistently emerge when analyzing values and norms across different scenarios. Rather than treating all possible preferences as equally valid, this approach recognizes that certain values reliably appear and stabilize across diverse contexts.

Recent research on self-other generalization demonstrates this approach by focusing on considerations that remain consistent when viewed from multiple perspectives. For example, a value like "honesty" tends to be recognized across different agents, contexts, and time periods. This is not coincidental - as Velleman argues in his philosophical works (1989, 2009), genuine values emerge through a natural filtering process: considerations that remain beneficial across multiple perspectives and contexts become recognized as values, while merely instrumental concerns or temporary preferences don't achieve this stability.

Similarly, when modeling cooperation, we can move beyond standard game theory approaches like Nash equilibria by using frameworks such as *Kantian equilibria* (Roemer, 2010) or *dependency equilibria* (Spohn, 2003; Treutlein, 2023). These frameworks identify cooperation patterns where agents consider "what if everyone like me acted this way?" rather than just maximizing personal outcomes. This approach reveals how certain cooperative norms naturally emerge as stable patterns in social interactions, even without external enforcement.

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

Each approach 'takes a stance' on what norms and values are, rather than leaving everything to be inferred ad hoc from preferences or prompts. This commitment to explicit structure directly addresses the three key failures identified in Section 2: it provides transparency where there was opacity, normative structure where there was a-normativity, and contextual grounding where there was context-blindness. In the following section, we demonstrate how these techniques apply in practice through five case studies spanning diverse domains, showing how explicit norm and value representations can overcome the limitations of both preference-based and naive textual approaches.