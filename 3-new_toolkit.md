# Towards Deeper, More-structured Representations of Human Values and Norms

What this leaves us with is a desire to capture **deeper, more structured representations of human values and norms**—ones that go beyond either preferences or free-form text.

What unifies these approaches is that they **take a stance** on what norms and values are, rather than leaving them to be inferred in an ad hoc or post hoc way by the model or its users. This orientation—toward **explicit**, **accountable**, and **structured** representations of what matters—is, we argue, a necessary foundation for addressing the **sociotechnical alignment problems** that define our time.

Neither preference/utility nor text strings take a stand as to what values norms are, or should be. A utility function can represent any consistent set of choices, constructive or destructive. A text string can represent any instructions, cooperative or uncooperative.

Here are two ways to drop this constraint:

**#1 - One can define an equilibria or gradient along which values or norms trend towards.**

An example is recent work on self-other generalization (https://arxiv.org/abs/2412.16325). One way to understand this work, is that it takes values to be things that are good from many agents' standpoints, and/or for one agent across contexts and time frames. This echoes work by Philosopher David Velleman's on values as enabling compact, self-understandings and self/other understandings. In [Practical Reflection](https://press.uchicago.edu/ucp/books/book/distributed/P/bo5473177.html) and [How We Get Along](https://www.cambridge.org/core/books/how-we-get-along/92875A2B5F77047AB8D4231BBBAF3191), David Velleman talks about values as resulting from a kind of compression. If something is good for you and also good for me, that means it's more likely to be just… good. If something is good for me now, and also going to be good for me in 20 years, that also means it's more likely to be a kind of universally good thing. If something is good in a wide variety of situations, that means it's more likely to be an insight into what's generally good.

As another example, instead of analyzing stable strategic outcomes in terms of Nash equilibria or correlated equilibria, we could model certain forms of decentralized cooperation as *Kantian equilibria* ([Roemer, 2010](https://www.jstor.org/stable/40587794)) or *dependency equilibria* ([Spohn, 2003](https://kops.uni-konstanz.de/handle/123456789/3505); [Treutlein, 2023](https://arxiv.org/abs/2307.04879)), where agents *universalize their policies* to relevantly similar agents when deciding what to do. This makes norms a stable attractor in policy space, given a social set-up.

**#2 - One can characterize the structure of norms or values more tightly, so as to exclude some coherent preference-relations or text strings.**

- Instead of representing the value(s) associated with a choice in terms of one or more utility functions, we can represent values as sets of *constitutive attentional policies* ([Klingefjord, Lowe, & Edelman, 2024](https://arxiv.org/abs/2404.10636)) — i.e. criteria that one intrinsically pays attention to when making decisions guided by a particular value. Such a language of specification can be used to exclude instrumental concerns or strategic aims from value space, as well as considerations like tribal affiliations.
- Similarly, a norm could be structured as a kind of constraint system, or as a filter for altering a plan of action so as to comply with the norm.

Such schemas for values or norms can be used protect against the pollution of alignment targets with arbitrary external goals or social pressures which can't be well-characterized as norms and values.

They also can form the basis for more robust forms of values- or norms-based reasoning about potential action. Across philosophy, logic, and cognitive science, there's been a great deal of work on how reasoning connects our values and norms to choice, and on when this should count as good reasoning. This work can be used to train AI models to think well about their choices, or even to provably or auditably making such good choices, according to these theories. But in general, these theories don't act on text strings or preference relations but on deeper, more structured notions of what norms and values are.

This includes structured reasoning for justifying both the choices of individual agents and for justifying and legitmating social choices:

- Instead of axiomatizing rational choices in terms of the classical axioms (completeness, independence, etc.), we can adopt *thicker accounts of normative justification*, under which a choice is reasonable insofar as it can be justified according to contextually-relevant criteria (e.g. Does the choice promote one's values? Does it uphold the standards of one's social role? Is it reasonably rejectable by others affected by the choice?)
- Many other points of departure exist beyond the examples described here. We might also develop theories of choice in the face of incomparability or parity ([Chang, 2002](https://www.philosophy.rutgers.edu/joomlatools-files/docman-files/chang-POSSIBILITY_PARITY.pdf)), computational models of value reconciliation ([Taylor, 1989](https://www.google.com/books/edition/Sources_of_the_Self/GXILEAAAQBAJ?hl=en&gbpv=0)) and normative reasoning ([Amgoud & Cayrol, 2002](https://link.springer.com/article/10.1023/A:1014490210693)),
- Instead of aligning AI systems to maximize a social welfare function aggregated from individual preferences, we could align AI systems with *role-specific normative standards* that are adjudicated via collective deliberation ([Zhi-Xuan et al, 2024](https://arxiv.org/abs/2408.16984)), or with *contextually-appropriate priority orderings over constitutive values* that are elicited via robust and legitimate mechanisms ([Klingefjord, Lowe, & Edelman, 2024](https://arxiv.org/abs/2404.10636)).

🍁

We believe that deeper, more-structured representations of values and norms are necessary for socio-technical alignment, for reasons we will go into below. But this need not take us too far afield from current methods in game theory, microeconomics, and RL training.

- The major results of rational choice, game theory, microeconomics, etc, assume the existence of utility functions that represent preference orderings which comply with certain axioms of rationality. To capture richer sets of values, reasons and norms, this basic mathematical structure can be preserved, but the space of objects over which utility functions are defined can be enriched significantly — "utility" would no longer reflect the individual preferability of some option, but something thicker, such as an all-things-considered value judgment.

    For instance, an enriched model of rational-choice can account for how agents trade off norm compliance with their individual desires or objectives when taking actions, resulting in norm-augmented utility functions ([Oldenburg & Zhi-Xuan, 2024](https://arxiv.org/abs/2402.13399)). This factoring would be useful for determining new norms that better promote each individuals' interests, or for designing welfare functions that account for intrinsically-valued norms but factor out the weight of oppressive norms.

    Similarly, one can model how individuals make decisions based on values that are constitutive of their conception of a good life, weighted against considerations that are merely instrumental to some further value or goal (see [Edelman, 2022](https://github.com/jxe/vpm/blob/9b9ee2499242e8972b74642b0347eb90388a1a24/vpm.pdf)). Again, these trade-offs can be captured by a utility function, but an institution or algorithm might prioritize constitutive values over instrumental ones.

    <aside>
    👀

    Other examples

    Akerlof & Kranton (2000) "Economics and Identity"

    [Berheim & Rangel](https://academic.oup.com/qje/article-abstract/124/1/51/1890374) (2009) "Beyond Revealed Preference"

    https://www.aeaweb.org/articles?id=10.1257/aer.99.1.431

    </aside>

- Similarly, RL-based training methods which condition on reasoning traces (https://arxiv.org/abs/2412.16339) can still be used, but instead of having a human annotator or an unprincipled expert model evaluate the reasoning, it can be evaluated more systematically via the formal models of values- or norms-based reasoning above.

    Or similar human data approaches (https://arxiv.org/abs/2503.15484) can be used, but with a filter which collects only data which is judged to be of the type (normative, values-based) required.
