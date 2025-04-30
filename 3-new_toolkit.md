# A New Toolkit: Explicit Norm & Value Representations

The advantage with preference relations or free-form text strings, is they can represent anything. Utility functions can represent any consistent set of choices, constructive or destructive; text strings can encode any instructions, cooperative or uncooperative. No assumptions get baked in about what values are, when they apply, or about the nature of the good (what kinds of attractor states values tend towards).

Yet that's also their chief drawback: an alignment target expressed this way can be pulled in any direction. It risks being polluted by considerations we would not, on reflection, recognise as values at all—signals we would not identify with any notion of the good.

This is one root cause of the problems with SIDT and the naive textual approaches catalogued in Section 2: it explains why addictive or manipulated behaviours can masquerade as bona-fide *values*, why zero-sum brinkmanship is mistaken for "optimal cooperation," why slogans like "Defund the Police" are read as deep commitments rather than tribal badges, and why vague aspirations such as "AI should always do the right thing" create an illusion of constraint while offering little guidance.

## The Central Proposal: Full-Stack Alignment

To overcome these limitations, we need a framework that takes a stance on what values and norms are, or are about, rather than treating all preference relations or text strings as equally valid candidates.

In other words, we must say more about **normativity itself**.  There are two places to start: (a) We can try to constrain the **content** of normativity – what values or norms are *for*, what they're supposed to *point at*, how we'd *recognize a good one*; or (b) we can constrain the **form** of the normative, finding *explicit, structured representations* of norms and values that resist drift in arbitrary directions.

## Approach 1: Attractors in Value Space

The first approach addresses the **content** question by taking a substantive stance on normativity itself. If values are for something—if what's good is not arbitrary but advances in an identifiable direction—then we can distinguish authentic normative considerations from mere preferences, tribal markers, or passing fads based on their content.

This approach identifies 'attractors in value space'—organizing principles that help us understand what values are ultimately about, and provide criteria for recognizing which considerations might reliably re-emerge and stabilize regardless of cultural or historical contingencies, and which should be considered as noise.

We can identify various types of attractors in value space, with current research offering strong support for at least two:

1. **Values-as-compression-across-contexts**: Values that efficiently encode 'goodness' across diverse scenarios. Recent research on self-other generalization exemplifies this attractor by identifying considerations that remain consistent when viewed from multiple perspectives. For example, a value like "honesty" tends to be recognized across different agents, contexts, and time periods. As Velleman argues (1989, 2009), genuine values emerge through a natural filtering process—considerations that remain beneficial across multiple perspectives become recognized as values, while merely instrumental concerns or temporary preferences don't achieve this stability.

2. **Coordination-equilibria**: Values that emerge as optimal solutions to recurring social cooperation problems. This is demonstrated in frameworks such as *Kantian equilibria* (Roemer, 2010) or *dependency equilibria* (Spohn, 2003; Treutlein, 2023), which move beyond standard game-theory approaches like Nash equilibria. These frameworks identify cooperation attractors where agents ask "what if everyone like me acted this way?" rather than merely maximizing personal outcomes. Certain cooperative norms thus appear as attractors in value space that stabilize in social interactions even without external enforcement.

Beyond these established patterns, promising directions for further exploration include **autocatalysis-of-flourishing** (where value-aligned actions create positive feedback loops that further enhance flourishing) and **capability-expansion-networks** (where values systematically increase what agents can accomplish together beyond their individual limitations).

Taken together, these empirical filters help *identify* which candidate values deserve explicit status. However, determining what values are ultimately about is only half the challenge. Even once we've identified genuine value attractors, we need safeguards to ensure those values remain stable under the pressure of optimization processes and don't drift toward arbitrary targets.

## Approach 2: The Form of Values and Good Normative Reasoning

This second approach tackles the complementary **form** question by establishing formal constraints on how values and norms are represented and reasoned about. While the first approach helps us distinguish authentic values from mere preferences based on content, this approach provides structured frameworks for encoding those values so they resist misinterpretation and manipulation.

Research in this area has developed several distinct formal frameworks:

1. **Constitutive attentional policies**: Instead of representing values associated with choices as utility functions, we can encode them as sets of criteria that agents intrinsically attend to when making decisions guided by that value (Klingefjord, Lowe, & Edelman, 2024). This specification language:

   - Distinguishes constitutive from instrumental considerations
   - Excludes tribal affiliations and ideological markers
   - Represents the phenomenology of value-guided attention
   - Enables verification of reasoning chains

2. **Normative constraint systems**: Norms can be structured as formal constraint systems or filters that modify plans of action to ensure compliance. These systems specify boundary conditions that acceptable actions must satisfy, creating a clear demarcation between norm-compliant and norm-violating behavior. Such schemas protect alignment targets from pollution by arbitrary external goals or social pressures that cannot be properly characterized as legitimate norms.

3. **Thick justificatory frameworks**: Rather than axiomatizing rational choice via completeness and independence, these frameworks adopt more substantive accounts of normative justification. Choices are deemed reasonable insofar as they can be justified according to contextually-relevant criteria, such as:
   
   - Whether the choice promotes one's constitutive values
   - Whether it upholds the standards of one's social role
   - Whether it could be reasonably rejected by others affected by the choice

These structured representations provide guardrails that keep normative reasoning on track, preventing it from being hijacked by optimization processes or strategic manipulation.

## Integration with Existing Methods

These two approaches to structured normative representation need not take us too far afield from current methods in game theory, microeconomics, and RL training:

- The major results of rational choice, game theory, and micro-economics assume utility functions that represent stable preference orderings. To capture richer values and norms, we can keep that mathematical scaffolding but enlarge the domain—"utility" would no longer reflect mere preferability, but an all-things-considered value judgment.

- For instance, an enriched model of rational choice can account for how agents trade off norm compliance with their individual desires or objectives when taking actions, resulting in norm-augmented utility functions (Oldenburg & Zhi-Xuan, 2024). This factoring would be useful for determining new norms that better promote each individual's interests, or for designing welfare functions that account for intrinsically-valued norms while factoring out oppressive norms.

- Similarly, one can model how individuals make decisions based on values that are constitutive of their conception of a good life, weighted against considerations that are merely instrumental to some further value or goal (Edelman, 2022). These trade-offs can be captured by a utility function, but an institution or algorithm might prioritize constitutive values over instrumental ones.

- RL-based training methods which condition on reasoning traces can still be used, but instead of having a human annotator or an unprincipled expert model evaluate the reasoning, it can be evaluated more systematically via formal models of values-based reasoning.

Each approach 'takes a stance' on what norms and values are, rather than leaving everything to be inferred ad hoc from preferences or prompts. In the following section, we demonstrate how these techniques apply in practice through five case studies spanning diverse domains.