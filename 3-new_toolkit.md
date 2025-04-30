# A New Toolkit: Explicit Norm & Value Representations

The advantage with preference relations or free-form text strings, is they can represent anything. Utility functions can represent any consistent set of choices, constructive or destructive; text strings can encode any instructions, cooperative or uncooperative. No assumptions get baked in about what values are, when they apply, or about the nature of the good (what kinds of attractor states values tend towards).

Yet that's also their chief drawback: an alignment target expressed this way can be pulled in any direction. It risks being polluted by considerations we would not, on reflection, recognise as values at all—signals we would not identify with any notion of the good.

This is one root cause of the problems with SIDT and the naive textual approaches catalogued in Section 2: it explains why addictive or manipulated behaviours can masquerade as bona-fide *values*, why zero-sum brinkmanship is mistaken for “optimal cooperation,” why slogans like “Defund the Police” are read as deep commitments rather than tribal badges, and why vague aspirations such as “AI should always do the right thing” create an illusion of constraint while offering little guidance.

## The Central Proposal: Full-Stack Alignment

To overcome these limitations, we need a framework that takes a stance on what values and norms are, or are about, rather than treating all preference relations or text strings as equally valid candidates.

In other words, we must say more about **normativity itself**.  There are two places to start: (a) We can try to constrain the **content** of normativity – what values or norms are *for*, what they're supposed to *point at*, how we'd *recognize a good one*; or (b) we can constrain the **form** of the normative, finding *explicit, structured representations* of norms and values that resist drift in arbitrary directions.

## Approach 1: Attractors in Value Space

 The first approach identifies specific patterns that consistently emerge when analyzing values and norms across different scenarios. Rather than treating all possible preferences as equally valid, this approach recognizes that certain values reliably appear and stabilize across diverse contexts.

This approach tackles the **content** question by proposing that values are fundamentally oriented toward certain structural patterns or 'attractors in value space.' These attractors represent organizing principles that help us understand what values are ultimately 'about,' offering criteria for distinguishing authentic normative considerations from mere preferences, tribal markers, or passing desires. Rather than treating all possible preferences as equally valid candidates for values, this framework takes a substantive stance on the nature of normativity itself.

It *identifies* **attractors in value space**—functional patterns that help distinguish genuine values from mere preferences. Rather than treating every preference as equally valid, it identifies the values that reliably re-emerge and stabilise.

We can identify at least four types of attractors in value space: (1) Values-as-compression-across-contexts, which efficiently encode 'goodness' across diverse scenarios; (2) Coordination-equilibria, which emerge as optimal solutions to recurring social cooperation problems; (3) Autocatalysis-of-flourishing, where value-aligned actions create conditions that further enhance flourishing; and (4) Capability-expansion-networks, which systematically increase what agents can accomplish together beyond individual limitations.

Recent research on self-other generalization demonstrates this approach by focusing on considerations that remain consistent when viewed from multiple perspectives. For example, a value like "honesty" tends to be recognized across different agents, contexts, and time periods. This is not coincidental - as Velleman argues in his philosophical works (1989, 2009), genuine values emerge through a natural filtering process: considerations that remain beneficial across multiple perspectives and contexts become recognized as values, while merely instrumental concerns or temporary preferences don't achieve this stability.

Similarly, when modelling cooperation, we can move beyond standard game-theory approaches like Nash equilibria by using frameworks such as *Kantian equilibria* (Roemer, 2010) or *dependency equilibria* (Spohn, 2003; Treutlein, 2023). These frameworks uncover cooperation attractors in which agents ask “what if everyone like me acted this way?” rather than merely maximising personal outcomes. In this light, certain cooperative norms appear as attractors in value space that stabilize in social interactions even without external enforcement.

Taken together, these empirical filters help *identify* which candidate values deserve explicit status.  The next approach tackles the complementary problem of **how to represent** such values so they remain stable under optimisation pressure.

## Approach 2: The Form of Values and Good Normative Reasoning

This approach addresses the **form** question by establishing formal constraints on the representation of values and norms, or on reasoning about them. It *specifies* how to encode the previously identified values, tightening the representational language so that not every coherent preference or slogan qualifies as a norm.

Instead of representing the value(s) associated with a choice in terms of one or more utility functions, we can represent values as sets of *constitutive attentional policies* (Klingefjord, Lowe, & Edelman, 2024)—criteria that one intrinsically attends to when making decisions guided by a particular value. Such a specification language:

- Distinguishes constitutive from instrumental considerations
- Excludes tribal affiliations and ideological markers
- Represents the phenomenology of value-guided attention
- Enables verification of reasoning chains

Similarly, a norm could be structured as a constraint system, or as a filter for altering a plan of action so as to comply with the norm. Such schemas for values or norms protect alignment targets from pollution by arbitrary external goals or social pressures that cannot be properly characterized as norms or values.

These structured representations enable more robust forms of normative reasoning about potential actions. Rather than axiomatizing rational choice via completeness and independence, we can adopt *thicker accounts of normative justification*, where choices are reasonable insofar as they can be justified according to contextually-relevant criteria (e.g., Does the choice promote one's values? Does it uphold the standards of one's social role? Is it reasonably rejectable by others affected by the choice?).

## Integration with Existing Methods

These two approaches to structured normative representation need not take us too far afield from current methods in game theory, microeconomics, and RL training:

- The major results of rational choice, game theory, and micro-economics assume utility functions that represent stable preference orderings. To capture richer values and norms, we can keep that mathematical scaffolding but enlarge the domain—"utility" would no longer reflect mere preferability, but an all-things-considered value judgment.

- For instance, an enriched model of rational choice can account for how agents trade off norm compliance with their individual desires or objectives when taking actions, resulting in norm-augmented utility functions (Oldenburg & Zhi-Xuan, 2024). This factoring would be useful for determining new norms that better promote each individual's interests, or for designing welfare functions that account for intrinsically-valued norms while factoring out oppressive norms.

- Similarly, one can model how individuals make decisions based on values that are constitutive of their conception of a good life, weighted against considerations that are merely instrumental to some further value or goal (Edelman, 2022). These trade-offs can be captured by a utility function, but an institution or algorithm might prioritize constitutive values over instrumental ones.

- RL-based training methods which condition on reasoning traces can still be used, but instead of having a human annotator or an unprincipled expert model evaluate the reasoning, it can be evaluated more systematically via formal models of values-based reasoning.

Each approach 'takes a stance' on what norms and values are, rather than leaving everything to be inferred ad hoc from preferences or prompts. In the following section, we demonstrate how these techniques apply in practice through five case studies spanning diverse domains.