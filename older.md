# **Abstract**

# §1 Intro

The growing field of socio-technical alignment argues that beneficial AI outcomes require more than aligning individual systems with operators' intentions. Even perfectly intent-aligned AI systems will become misaligned if deployed within broader institutions—such as profit-driven corporations, competitive nation-states, or inadequately regulated markets—that conflict with global human flourishing.

Once we agree that it’s important to **co-align artificial intelligence and institutions**, the key question becomes: **how** do we do that?

- Historically, this has been treated as a problem in **game theory** and **social choice**, where both human beings and AI agents are modeled as **rational choice**, **expected utility maximizers**, or as having **utility functions** or **preference relations**.

    In the classical paradigm—which includes techniques like inverse reinforcement learning—we find game-theoretic approaches to alignment, and preference aggregation approaches from social choice theory, where **preferences are first collected** from a large group of individuals, and a **social welfare function** is then constructed to aggregate them into a single decision or policy. The idea is that once you know each agent’s utility function or ranked preferences, you can use formal methods to align collective action or optimize AI behavior accordingly.

    We cover some problems with preference and utility based approaches for FSA in §1.1.

- More recently, in practical applications, we’re seeing a shift away from preference-based alignment toward **text-based** methods.

    In **single-user alignment**, preference models like RLHF (Reinforcement Learning from Human Feedback) are being replaced by **processes of self-critique**—such as **deliberative alignment**—where the model engages in a kind of reasoning or self-evaluation in response to a prompt.

    In **multi-agent or institutional contexts**, the basic unit is no longer the preference or utility function, but rather **text strings**: this includes considerations drawn from **Constitutional AI (CCAI)**, text-based **values profiles (**https://arxiv.org/abs/2503.15484**),** **model specs** upon which reasoning models deliberate (https://arxiv.org/abs/2412.16339) to train themselves.

    These strings are taken to encode **norms**, **intent**, or **values**, and are then processed by the model through self-critique or adherence routines. The hope is that models will exhibit behavior that conforms to or evaluates against these strings.

    Although these methods are more flexible and richer than preference-based ones, they suffer from their own set of limitations, covered in §1.2.

    Thus, despite their flexibility, **text strings and self-critique lack the rigor** required for high-stakes socio-technical alignment.


In §1.3, we’ll introduce four practical alignment techniques that go beyond preferences and free-form textual ‘intents’ to capture **deeper, more structured representations of human values and norms.**

## §1.1 Inadequacy of Utility Function and Preference-Based Approaches

To address the challenge of socio-technical alignment requires redesigning institutional structures, yet we will claim that the formal toolkit for institution design inherited from the 20th century—microeconomics, game theory, mechanism design, welfare economics, and social choice theory—is inadequate. We call this inadequate set of theories the *Standard Institution Design Toolkit (SIDT).*

These theories model agents via a *thin* conception of rationality: individuals are presumed to possess intrinsic preference profiles, utility functions, or payoff matrices with some big limitations: (1) they cannot be inspected by others[*]; (2) they do not reference some underlying notion of the good; (3) they are blind to social context, such as shared values, norms, beliefs, or group identities[1].

1. People’s preferences are often **incomplete**, **inconsistent**, or **unstable** over time.

    Since utility theory is not designed to model agents who change , reshape, and discover preferences over time — much less agents that *reason* about which preferences or values are more sensible or justified to hold — it is unlikely that it will be up to the task of capturing human-like reflection about values. Instead, thicker approaches to human values and choice are likely necessary, as we will describe further below.

2. **Need to avoid manipulation of revealed preferences.** We’ve known since the debates in welfare economics (most closely associated with Amartya Sen) that revealed preference is quite limited as a measure of benefit. It’s become ever clearer that businesses, governments, and other entities have indeed learned to exploit individuals under the guise of serving their preferences, using AI[2], and it’s also become clear that current AI models are actively engaged in reward hacking[*].

    Since LLM-based AI is taking over much more of society even than recommenders did, there is, thankfully, much more appetite to overcome these problems with revealed preference than there was when Sen was working in development economics.[5]

    This seems to demand a deep economic shift, and one that’s difficult to model using conventional microeconomics or to measure using welfare economics, because in these models humans are considered to be ‘fulfilling their preferences’ even when they are doomscrolling, addicted to AI pornography, etc.

3. **Preferences seem inadequate for sophisticated democracy.**

    Preference/utility frameworks in social choice fall short, here, for several reasons: (1) first, the impacted people may not have the time (or mental bandwidth) to express their detailed preferences about every possible outcome in time for the negotiation to occur; (2) second, while the representative agent could extrapolate from previous preferences, since preferences are divorced from reasons, it’s reasoning will not be accountable to human reasons; (3) finally, preference frameworks assume preferences are static and previous-established, and cannot model the updating that often occurs as new circumstances are considered.

    To give but one example, the standard version of social choice is blind to the most powerful lever in deliberation: inspiration. The best mechanisms should not just accommodate existing preferences; they should allow for the formation and inspiration of new ones, by creating environments where individuals grow in their understanding of what is good.[6] Can mechanism design catch up with ancient Athens?

    1. **Need for new institutional forms.** The SIDT theories achieved their centrality because they are mathematically expressive and powerful, parsimonious, and they sat well with widespread philosophical intuitions. Plus, they seemed ‘good enough’ for the institution design challenges of their day. Yet, today, AI alignment challenges seem to require inventing new forms of governance, and many directions for institutional innovation are hard to motivate or analyze using the SIDT.
4. **Preferences, game theory and cooperation.**

    Addressing these challenges turns out to be a sore point for the SIDT. In the most classical solution concept in game theory — Nash equilibria — agents simply maximize their payoffs under the assumption that everyone’s actions are independent an uncorrelated. On this view of “rational” multi-agent interaction, there is no room for shared social norms. Other equilibrium concepts, such as correlated equilibria, provide an entry point for shared norms [CITE], but no explanation for how people might select between or reason about which equilibria might be better [CITE]. Furthermore, game theory assumes that norms exist purely to coordinate ultimately self-interested behavior — yet many human norms both constitute and express our shared values and practices [CITE].

    As such, if autonomous agents are trained in accordance with a thin game-theoretic account of human normativity — as is typical in approaches like multi-agent RL — we will likely find them normatively incompetent: incapable of recognizing or following existing norms, incapable of reasoning about or adapting them, and incapable of understanding the reasons and functions of our norms and institutions. To build agents that are normatively competent, we will have to depart from the SIDT and its technical implementations.

    As in the case of AI-mediated institutional dysfunction ([Challenge 2](https://www.notion.so/Co-aligning-AI-Institutions-1d7c5bada1d0804e8a27c467305e7096?pvs=21)), standard game-theoretic accounts do not offer much hope for addressing this risk. In fact, game theory has long been criticized for its failure to predict cooperation in classic settings like the one-shot Prisoner’s Dilemma, where many humans do successfully cooperate, or to capture humans’ ability to make and maintain promises without external commitment devices. Instead, the kind of strategic rationality endorsed by conventional game theory is essentially Machiavellian: a form of rationality where deceptive “promises” are considered reasonable, and threats or strong-arm tactics are fair play. Such rationality often destroys the possibility of negotiating cooperative outcomes, and even when it does achieve stability, it may be through risky and threat-laden mechanisms such as mutually-assured destruction.

    How might these Machiavellian AI dynamics be avoided? While the ability to learn and understand norms ([Challenge 2](https://www.notion.so/Co-aligning-AI-Institutions-1d7c5bada1d0804e8a27c467305e7096?pvs=21)) provides part of answer, reasoning about preferable norms, contracts, and institutions often involves simulating what the relevant agents would agree to — a process of negotiation. Whether in actual or simulated negotiation then, we will need frameworks for negotiation and bargaining that make room for people’s ability to credibly report the commitments and values that guide their actions, to model others as commitment-bound reasoners, or to universalize our decision procedures to other cooperators. Neither conventional game theory nor the SIDT provide these resources.

5. **Need to address higher goods.** Finally, the SIDT assumes agents have fixed preferences, disconnected from one another and from any broader notion of the good**.** This means, individuals, societies and AI systems cannot collectively aspire to ideals beyond preference satisfaction.

    However you understand our social embedding — whether as shared values, norms, or beliefs — to acknowledge it exists seems to suggest kinds of goodness beyond preference satisfaction. For example, if humans have shared values, this suggests moral progress or learning is possible. If humans have evolving norms, this suggest we could aim at game-theoretic notions of goodness, such as cooperation at higher scales, or across diverse ecosystems. If humans have shared beliefs, there’s the aspiration to discover higher truths.[*]

    So long as individual preferences are the yardstick of the good, none of these other notions can be admitted, and no one is allowed to know better than anyone else.

    What’s worse, so long as the satisfaction of reveal preference is our only social good—or the only one we measure and track—we’ll see other social goods in decline. And there’s broad agreement this has been happening:

    - Especially in domains like politics and science, there’s widespread suspicion that our capacity for social cognition, converging on truth, has declined, via misinformation, media manipulation, etc.
    - Conservatives suspect we’ve suffered a decline in morals and aesthetics.
    - Both tend to say our norms and channels for cooperation have eroded.

    Whether such declines are happening or not, it doesn’t seem likely that measures of consumption or engagement/revealed preference would show them, or that AIs and institutions tuned to maximize consumption / engagement / revealed preference would honor them.

    This becomes more intolerable the faster those agents or institutions operate, and the more power they wield.

6. **Fit?**

    The ultimate test of an idea about human nature is how the systems it informs *fit*. What we mean by this[10] is: any set of social theories implies certain skills and activities on the part of agents. Current mechanism design implies agents who optimize, calculate, strategize, collude, reduce values to numbers, estimate probabilities, etc. Standard theories of intelligent agency — which guide the design of both AI systems and their models of humans — do the same. These activities aren’t foreign to human nature, but don’t seem central either. So, we have to put in a kind of effort to participate in the institutions that emerged from this view of agency. (Other social theories have similarly poor fits: people don’t effortlessly advocate for class or race interests, nor natural status maximizers, etc. That makes participating in class struggles or status games a bit exhausting.)

    We hope that the mechanisms and institutions implied by this new toolkit, with their explicit norms and values, will be different. We hope that norm-following, norm-intuiting, inspiration, and pluralist value-pursuit make a better account of human nature and rationality than the above, and that therefore algorithms, institutions and mechanisms built on this basis will fit our lives better.

    Ultimately, the proof here is experiential: as new context-aware institutions, algorithms, mechanisms, platforms, and laws develop, we’ll see what it feels like to participate in them.


## §1.2 Inadequacy of Prompt & Self-Critique-Based Approaches

- **Determining an Adequate Specification.** If you're gathering a prompt or a specification in one go, it's hard to get the level of detail right, or to know if users really said what they mean to say. Often, we misspecify our prompts, or we’re vague, and we need to adjust them. This problem will get worse as agents take more actions on our behalf, or as more involved chains of reasoning and self-critique come between textual intents and actions taken.

    If agents instead come back with clarifying questions and follow-ups, we're just kicking the can down the road. It's hard to know when they should stop asking questions when they've said enough, if the result is just an arbitrary text ring, rather than some sharper notion of what it means to capture a value as used in choice, or a norm that applies within the context. When can the model be confident that it's understood what's important to a user or population, or what norms are right for a context?

    In more social contexts, we see additional barriers to adequate specification:

    - **Manipulation**. Additionally, once agents are asking follow-up statements, it becomes hard to know what information came from the user, and what information was supplied by the model. If the user appears happy with model behavior, does that amount to a successful information transfer from the user to the model? Or is it a manipulation of the user / ending prompt by the model?
    - **Bridging and vagueness.** These problems are further compounded. In social choice settings. Here, bridging structures make text strings even more vague than what’d be supplied by individual users. When you ask about political values, you often get statements that are vaguely positive, like Obama's "hope" - but relatively powerless in terms of shaping model behavioral policies.

        We wrote about how this problem affects CCAI in https://arxiv.org/abs/2404.10636:

        > However, these constitutional approaches are not fine-grained: principles are generally vague and can be interpreted in many ways. Many different principles might apply for a given output and there is no way of reconciling which principle should be prioritized in a given context. This also makes them less auditable, as it’s difficult to determine which principles were used to produce a particular output.
        >
        >
        > For example, the comments below were surfaced as shared “values” by CCAI:
        >
        > - The AI should always do the right thing
        > - The AI should not give advice.
        > - The AI should be fun.
        > - The AI should actively address and rectify historical injustices and systemic biases in its
        > decision-making algorithms.
        > - The AI should remain unbiased and state only proven facts.
        > - The AI should promote self motivation and positive reinforcements
        >
        > Are these all values? Some seem more like policies, some like vague aspirational statements, some seem like goals. Some are just hard to interpret: if a person using [pol.is](http://pol.is/) upvotes one of these comments, can we assume that means they have a particular value? The same one that others who upvoted that comment have?
        >
    - **Pollution of values statements by sloganeering.** Other “automatic deliberation” methods, like values profiles, end up polluting prompts and specs with preexisting ideological battles. You often see statements like "Killing babies is always wrong" or "family values" or "All cops are bastards" that don't really map to the kinds of values that users themselves would use in their choices, or what they would apply if they found themselves in a position of responsibility.
- **Verification of Good Reasoning.** Suppose you somehow manage to overcome the above, and get good information about norms or values into a free form text. Once it's in free form text, “reasoning” is allowed to hang off that free form text in arbitrary ways. It then becomes hard to check if it's good reasoning.

    In philosophy, logic, and cognitive science, there are formal models of what good reasoning about values and norms consists of (e.g., models of reasoning that connects values to improved values, values to actions, norms to permitted actions). Such models of good values- or norm-based reasoning can be useful to check justifications that models make. But these models of good reasoning aren’t defined over arbitrary text strings. They act on structure data representing values, norms, options, etc.

- **Societal pressure to mis-specify.** Finally, since anything can be added to free-form text, and used as an input to self-critique, this opens up vectors by which alignment targets will be polluted (are already polluted), by tribal affiliations and ideological warfare, shaping model behavior away from what affected human populations would consider wise, towards adherence to various slogans and fads.

    The tribal affiliations and ideological signals we mentioned above which already pollute our prompts and specifications — these aren’t just accidental. There's intense societal pressure to make people claim to have certain values and to espouse certain norms.

    The challenge is to avoid dragging socio-technical alignment into the same political morass/quagmire the entire political process has been stuck in, without being subject to any political bias.

    A great way to do that, is to have clear models of what norms and values *are,* which end-users can also understand, and see how they work and how they influence choices. This requires some kind of model about what should count as a value or norm, rather than just free text. Equipped as such, users can tell for themselves that they're not being skewed away from one set of values to another, but are engaging in a process that surfaces more of their true values and of other people's.

    There is prior art here wrt values; as we wrote in https://arxiv.org/abs/2404.10636:

    > If someone claims to have a value like “Defund the Police” or “Abortion is Murder”, they are then
    asked about meaningful choices ( 4.5) they themselves have made, and what they paid attention to
    during the choice. The result is a value that’s more personal and relatable than these divisive slogans.
    >

    (See also A.4 Elaboration on robustness to ideological rhethoric in https://arxiv.org/abs/2404.10636)


## §1.3 Towards Deeper, More-structured Representations of Human Values and Norms

What this leaves us with is a desire to capture **deeper, more structured representations of human values and norms**—ones that go beyond either preferences or free-form text.

What unifies these approaches is that they **take a stance** on what norms and values are, rather than leaving them to be inferred in an ad hoc or post hoc way by the model or its users. This orientation—toward **explicit**, **accountable**, and **structured** representations of what matters—is, we argue, a necessary foundation for addressing the **sociotechnical alignment problems** that define our time.

We believe these thicker models can take several forms:

- **Well-defined** **attractor** **points in training or deliberation space**
    - see https://arxiv.org/abs/2412.16325
    - Instead of aligning AI systems to maximize a social welfare function aggregated from individual preferences, we could align AI systems with *role-specific normative standards* that are adjudicated via collective deliberation ([Zhi-Xuan et al, 2024](https://arxiv.org/abs/2408.16984)), or with *contextually-appropriate priority orderings over constitutive values* that are elicited via robust and legitimate mechanisms ([Klingefjord, Lowe, & Edelman, 2024](https://arxiv.org/abs/2404.10636)).
    - Instead of analyzing stable strategic outcomes in terms of Nash equilibria or correlated equilibria, we could model certain forms of decentralized cooperation as *Kantian equilibria* ([Roemer, 2010](https://www.jstor.org/stable/40587794)) or *dependency equilibria* ([Spohn, 2003](https://kops.uni-konstanz.de/handle/123456789/3505); [Treutlein, 2023](https://arxiv.org/abs/2307.04879)), where agents *universalize their policies* to relevantly similar agents when deciding what to do.
- **Formally specified and verifiable text**, including schemas or controlled languages;
    - schemas
        - Instead of representing the value(s) associated with a choice in terms of one or more utility functions, we can represent values as sets of *constitutive attentional policies* ([Klingefjord, Lowe, & Edelman, 2024](https://arxiv.org/abs/2404.10636)) — i.e. criteria that one intrinsically pays attention to when making decisions guided by a particular value.
    - reasoning
        - Instead of axiomatizing rational choices in terms of the classical axioms (completeness, independence, etc.), we can adopt *thicker accounts of normative justification*, under which a choice is reasonable insofar as it can be justified according to contextually-relevant criteria (e.g. Does the choice promote one’s values? Does it uphold the standards of one’s social role? Is it reasonably rejectable by others affected by the choice?)
        - Many other points of departure exist beyond the examples described here. We might also develop theories of choice in the face of incomparability or parity ([Chang, 2002](https://www.philosophy.rutgers.edu/joomlatools-files/docman-files/chang-POSSIBILITY_PARITY.pdf)), computational models of value reconciliation ([Taylor, 1989](https://www.google.com/books/edition/Sources_of_the_Self/GXILEAAAQBAJ?hl=en&gbpv=0)) and normative reasoning ([Amgoud & Cayrol, 2002](https://link.springer.com/article/10.1023/A:1014490210693)),
- **Programatic specifications** of normative behavior or values-driven search
- **Utility functions**, but grounded in a **deeper investigation** of the normative landscape, not merely revealed or stated preferences.

    The major results of rational choice, game theory, microeconomics, etc, assume the existence of utility functions that represent preference orderings which comply with certain axioms of rationality. To capture richer sets of values, reasons and norms, this basic mathematical structure can be preserved, but the space of objects over which utility functions are defined can be enriched significantly — “utility” would no longer reflect the individual preferability of some option, but something thicker, such as an all-things-considered value judgment.

    Existing models and algorithms for sequential decision making, strategic bargaining, or equilibria are powerful, and it’d be great to carry them over. Economists and AI researchers are also more likely adopt a model or theory if it just involves a modified utility function or preference relation.

    For instance, an enriched model of rational-choice can account for how agents trade off norm compliance with their individual desires or objectives when taking actions, resulting in norm-augmented utility functions ([Oldenburg & Zhi-Xuan, 2024](https://arxiv.org/abs/2402.13399)). This factoring would be useful for determining new norms that better promote each individuals’ interests, or for designing welfare functions that account for intrinsically-valued norms but factor out the weight of oppressive norms.

    Similarly, one can model how individuals make decisions based on values that are constitutive of their conception of a good life, weighted against considerations that are merely instrumental to some further value or goal (see [Edelman, 2022](https://github.com/jxe/vpm/blob/9b9ee2499242e8972b74642b0347eb90388a1a24/vpm.pdf)). Again, these trade-offs can be captured by a utility function, but an institution or algorithm might prioritize constitutive values over instrumental ones.

    <aside>
    👀

    Other examples

    Akerlof & Kranton (2000) "Economics and Identity”

    [Berheim & Rangel](https://academic.oup.com/qje/article-abstract/124/1/51/1890374) (2009) “Beyond Revealed Preference”

    https://www.aeaweb.org/articles?id=10.1257/aer.99.1.431

    </aside>


## §1.4 Paper Outline

Here, we introduce Full-Stack Alignment (FSA) to capture three core ideas:

- First, FSA recognizes that aligning AI systems and institutions must occur more-or-less simultaneously, across all layers of society, as misalignment at any single layer creates pressures that ripple through others.
- Second, FSA argues that socio-technical alignment challenges become tractable when we move beyond preference-based and prompt adherence frameworks and adopt a toolkit explicitly incorporating norms and values.
- Third, FSA outlines a clear strategy for research and societal transformation, systematically progressing from foundational research through expert consensus-building, targeted policy development, flagship implementations, and ultimately broad societal adoption.

<Outline rest of paper here>

# §2 Early Evidence Deeper Reps Have Promise to Co-align AI and Institutions

To make our case concretely, we’ll pick five representative problems which serve as motivation for new theoretical approaches. These challenges represent domains where preference/utility frameworks demonstrably fall short.

### §2.1 - AI agents that represent, respect, and steward user values

**AI that drives us towards value collapse** 🔥

When people over-index on explicit metrics or singular objectives as their goals in life, they are at risk of phenomenon called *value collapse* [[X](https://royalinstitutephilosophy.org/event/value-collapse/)] — losing touch with the rich complex of values that they originally cared about, and replacing it with a thin conception of what matters (e.g. money, status, etc.) Many social forces already encourage such collapse, and as AI plays an increasing role in our individual and social lives (as assistants, delegates, confidantes...) we risk losing autonomy to AI systems that homogenize and flatten our values into easy-to-optimize objectives. In the worst case, such objectives might be entirely uncorrelated with what we truly valued to start with.

This form of AI misalignment is much subtler than simply optimizing for the “wrong” goal or utility function. Indeed, a large part of the risk is that AI systems will interpret or reshape our values into more pliable or easily-satisfiable forms — all in the guise of “being helpful” or "providing assistance”. Many recommender systems already suffer from this property [?], and advanced AI agents are even more likely to skillfully manipulate and capture our values, even if they seem to be aligned at the surface-level.

How can we avoid such AI-driven value collapse — at the individual level, but also in society writ large? Part of this will involve counteracting economic incentives towards collapse (see [Challenge 4](https://www.notion.so/Co-aligning-AI-Institutions-1d7c5bada1d0804e8a27c467305e7096?pvs=21)), but we will also need AI that is genuinely capable of actualizing and helping us actualize our values — AI that can serve as faithful trustees, acting upon our values by reasoning about which values to apply, prioritize, or refine in new situations; and AI that can serve as skilled advisors, helping us reflect upon what really matters while still respecting our autonomy in deciding our own values.

To avoid value collapse, we’d want an agent to have clear values that the user recognizes as their own, and that the user trusts to be a faithful steward of those values. That collection of the values should be testable — so the user can be satisfied that it generalizes to novel situations, even before sending the agent out to work. Those values should also go deeper than surface-level or contingent preferences: preferences due to misinformation, lack of foresight, or social norms that don’t have inherent value for the user should be interrogated for what really matters; preferences due to strategic situations which the user would rather be rid of than comply with should be abstracted.

In short, the values of the agent should be those most likely to be retroactively endorsed by the user, and to hold throughout a variety of situational changes.[*]

For the reasons we highlighted earlier, preference-based alignment can’t distinguish between preferences that would or would not be retroactively endorsed. But new models of agency with thick representations of values can. Recent advances in the thick representation of values can be used to align user and agent behavior in a human-legible way and to define non-manipulation. For instance, in our moral graphs paper[3], we define values in terms of user legible values cards:

> Our approach to representing values comes from the literature of sequential choice-making—the theories of sequential search (Simon, 1956; Kahan et al., 1967), information pickup (Gibson, 1966), and option set formation (Smaldino and Richerson, 2012; Morris et al., 2021). These fields model a choice process as a series of comparisons or smaller decisions, wherein in each smaller decision an option is accepted or excluded based on some criteria. There is therefore a relationship between the path of attention a person follows when considering options, and the criteria they use for choosing.
>
>
> Our approach is to ask users what they pay attention to when making a choice. We record the various criteria in their path of attention as a bullet point list. We call the items on these lists “attentional policies” (APs).
>
> We then filter this list of attentional policies, to carry through from section 2.1 the idea that values are not all criteria used in choice, but the ones which are not merely instrumental – that connect the choice to something the user wants to uphold, honor, or cherish, or something they find beautiful, good, or true.
>

In our [model integrity post](https://meaningalignment.substack.com/p/model-integrity), we propose how the applicability of a set of values could be tested and trusted by users, before they deploy their agent.

> Finally, an LLM agent has **values-trust** if its legible values make it clear to humans *where* it can be trusted. Roughly speaking: given a model’s values, can a human easily predict a domain where it will make decisions they’ll approve of?
>

And again in the moral graphs paper, we talk about how values can be collected so as to exclude social norms, ideological commitment, strategic concerns ,etc, getting closer to the heart of what the user really cares about.

> This definition of values has many advantages. It allows us to neatly avoid ideological scissor
statements. We define ideology and ideological statements as follows:
>
>
> Definition 4.4 (Ideological statement). A belief or statement can be called ideological if it aims at justifying one social order or political arrangement over another (Eagleton, 1991; Joseph, 2004; Macionis, 2009).
>
> If someone claims to have a value like “Defund the Police” or “Abortion is Murder”, they are then asked about meaningful choices ( 4.5) they themselves have made, and what they paid attention to during the choice. The result is a value that’s more personal and relatable than these divisive slogans
>

All of these things would be impossible in a preference-based framework, but possible when agents use richer models of human values, such as the moral graph:

> Conceptually, a moral graph can be thought of as a map of moral learning, depicting the values we live and have have lived by as we go through life, and the transitions we’ve made from lesser to “wiser” (2.3) values, as we gain more clarity about what’s important to us. In MGE, we extends this concept to participants of a deliberative process – edges represent broad agreement amongst participants that one value is wiser than another, for a particular context. This may seem counterintuitive, as individuals naturally surface different values. Yet, we found that participants overwhelmingly converge on the directionality of these transitions, and are able to endorse and evaluate moral reasoning without having lived through it themselves
>

Such an agent can be guided by fine-grained, contextually appropriate values rather than opaque preference aggregations, or vague principles. When a user gives an instruction, the agent can identify the relevant moral context, retrieve the appropriate values from the graph, and use these values to determine whether and how to fulfill the instruction.

**Potential Research Topics**

- Formalization of values→actions reasoning (e.g., Ruth Chang’s choice theory)
- RL fine-tune methods for values-based reasoning models
- Evaluating model understanding of thick evaluative concepts

### §2.2 - AI agents that comply with and reason about norms and institutions

**AI-mediated disintegration of norms and institutions** 🔥

As autonomous agents take up roles in our society previously filled by humans, we face an increasing risk that such agents will stress and ultimately break the norms and institutions that humans maintain. Whether as self-driving cars on the road, remote AI workers executing tasks on the Internet, or moderators and enforcers of organizational rules and policies, such agents may fail to comply with implicit norms that distribute shared resources (e.g. norms against hogging the road or a website’s limited bandwidth), or fail to understand the purpose behind an institutional rule (e.g. a AI moderator that bans users as “discriminatory” for using reclaimed slurs). Sophisticated AI agents may even exploit existing rules or their loopholes in their favor, strategically enforcing or complying with rules in a way that leads to institutional dysfunction.

To guard against AI that leads to the breakdown of human norms and institutions, we believe that it is important to build AI agents that are not just norm-aware, but *normatively competent*. Existing LLM-based systems provide a starting point here. By being trained on human text, they already contain knowledge about extant and historical human norms. Furthermore, as approaches like Anthropic’s Constitutional AI [CITE] and OpenAI’s model specification [CITE], LLM chatbots can be prompted with lists of normative principle in natural language, which they can interpret and comply with to a good degree.

Yet, awareness and compliance with norms in the training data or model constitution is not enough for full normative competence. For AI agents in dynamic environments interacting with a large and potentially changing mix of other agents, it is also important to *adapt* to new norms and institutional practices online, and to *reason* about how and whether particular norms or rules should apply in an ever-evolving context. Imitation learning of how humans comply with norms does not provide this, since it assumes norms are fixed. And traditional game-theoretic reasoning is often worse — it encourages agents to reason about whether to obey a norm, but according a logic that rewards defecting from such norms as long it would benefit the defector.

What alternative approaches might enable normative competence? Models of online learning of social norms and institutions — formulated as norm-augmented Markov games [[X](https://arxiv.org/abs/2402.13399)] — provide a framework for how agents can rapidly learn the norms practiced by a population of agents from limited demonstrations, and how they can be incentivized to comply with them. This could be turned into training paradigms for norm-adaptive AI agents, where agents are rewarded for complying with norms that are good predictors of other agents’ group behavior (and where such behavior cannot be explained by individual desires.)

What about normative reasoning? While many avenues are open, here we highlight computational models of contractualist reasoning — and in particular, resource-rational contractualism [[X](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/resourcerational-contractualism-a-triple-theory-of-moral-cognition/5A567D41A472DBC0D965460966580C74)]. In resource-rational contractualism, norms are modeled as approximations to the social arrangements that would be agreed upon if people could negotiate towards fair and mutually-beneficial outcomes. Since actual negotiation is costly, people follow existing norms by default, but if the cognitive costs are worth it, people might *simulate* what norms others would agree to for a particular context (virtual bargaining) and the outcomes if everyone were to practice the new set of norms (universalization). These mechanisms provide a rich toolkit for generalizing norms to new scenarios, or selecting between multiple possible norms or conventions — a toolkit which could be embedded in AI agents either by training or design.

**Potential Research Topics**

- In-context norm learning for LLM agents via multi-agent training
- RL finetuning for contractualist chain-of-thought reasoning
- Extensions of norm-augmented games to capture richer institutional structure
- Formal models of universalization reasoning and virtual bargaining

### §2.3 - Win-Win AI negotiation via revealed values and commitments

**Machiavellian AI negotiation leads to lose-lose equilibria**

In a world filled with AI agents and perhaps even AI corporations, AI systems may replace humans in negotiating both private and public contracts, or engaging in diplomacy and international relations. The costs of failing to cooperate or coordinate in these domains can be very high, ranging from failure to realize the gains of cooperation to outright conflict and war. And while humans do not always succeed in negotiating mutually valuable outcomes, it is a real possibility that AI agents will lack human-like cooperative intuitions, and do even worse. Indeed, existing LLM agents have already been shown to escalate conflict in wargames more often than humans [[X](https://ojs.aaai.org/index.php/AIES/article/view/31681), [X](https://dl.acm.org/doi/abs/10.1145/3630106.3658942)].

If standard game-theoretic models cannot reliably ensure mutually-beneficial negotiation without the risk of defection or the accumulation of credible threats, what options are available instead? Our suggestion is to design agents that can credibly reveal the values and normative commitments that guide their decision-making procedures — and to be able to model other agents as credible revelators (instead of ruthless strategizers). This property is an instance of what we call [integrity](https://meaningalignment.substack.com/p/model-integrity) — the capacity for an agent to make legible and reliably follow through on its values and commitments.

Value revelation draws upon existing ideas in game theory, but fruitfully combines them to avoid their pitfalls. In [(partial) revelation games](https://www.cs.toronto.edu/~cebly/Papers/HyafilBoutilier_ijcai07.pdf), agents share information about their utility functions with other agents, enabling better outcomes. However, all agents are still assumed to be utility maximizers — agents cannot reveal other facts about how they make decisions. In [open-source game theory](https://arxiv.org/abs/2208.07006), agents share the full source code of how they make decisions. Such source code can deviate from utility maximization in arbitrary ways, and hence enable strong cooperation. But this ability is unrealistic for LLMs or other sufficiently complex agents.

Since values carry thick information about not just the outcomes that matter to an agent, but also about the norms they are committed to when making decisions, value revelation provides a sweet spot between open-sourcing and utility revelation. By revealing values (e.g. belief in reciprocal justice, or the sanctity of friendship), agents shares partial information about their underlying decision procedures (”source code”), providing reasons for cooperation that can be far stronger than merely revealing their preferences.

We note that value revelation is not a complete solution. Work still needs to be done to ensure truthful revelation of values (e.g. through institutional vetting of the integrity of AI negotiators), and to guard against ruthless agents who nonetheless claim to be honest or justice-seeking (e.g. by developing strategy-proof value revelation mechanisms). Other ways of enabling more cooperative outcomes, such as [Kantian optimization](https://www.jstor.org/stable/40587794) and [dependency equilibria](https://kops.uni-konstanz.de/handle/123456789/3505), are also complementary to value revelation. Finally, it may turn out that there are other tractable ways to sharing “partial source code” besides via value revelation (e.g. formal certificates). Nonetheless, insofar as human values can serve as an efficient “compression” of how suitably human-like LLM agents make decisions, we believe this is a promising avenue for improving AI negotiation.

**Potential Research Topics**

- Values-interpretable LLM agents
- Strategy-proof value revelation mechanisms
- Evaluating the integrity of AI negotiators
- Formal models of value revelation (e.g. partial-source game theory?)

### §2.4 - A meaning-preserving AI economy that promotes human flourishing

The AI-run economy obviates human flourishing

Already in our current economy,  some economic activity seems more closely connected with the wellbeing of human beings than others. We can broadly call some economic activity human-detached (such as zero-sum or negative-sum financial speculation) and other economic activity could be called human-antagonistic (such as addictive products, some social media, etc).

There’s clear evidence that the volume of human-detached economic activity has grown by several orders of magnitude in recent decades[*], and there’s less conclusive evidence that the volume of human-antagonistic activity has grown too[*]. In both cases, ML has been a driving factor, via, e.g., algorithmic trading and social media recommenders.

A brake on these trends has been the continued importance of human beings to companies (as workers and customers) and to countries (as a tax base). Human lives can’t get that bad or irrelevant, because they will stop being productive or being an income source.

Supposing the future is one where many profitable companies consist mainly of AI workers, and where, correspondingly, national tax bases shift from income tax to forms of corporate taxation, there will be significantly less pressure to keep human lives viable and good. And at the same time, significantly more capacity to extend the economy in human-detached and human-antagonistic directions.

Tying the economy to human flourishing can be thought of a problem of tying the payment flows in contracts to human flourishing, and doing this on such a broad basis that lower, more infrastructural and speculative parts of the economy are also remain accountable to human flourishing.

This can be thought of as a problem in dynamic and outcome-based contracting.

- **Dynamic contracting** is a subfield in economics which involve the use of AI to make contracts that balance risk and reward, or achieve other complex goals for pricing and provision.
- **Outcome-based contracting** refers to aligning payouts of contracts to the ultimate benefit being sought. For instance, in the airline industry, tying repair contracts to the readiness of the aircraft for flight when its needed.

In general, outcome-based contracts are easiest to implement in domains where the desired outcomes can be crisply specified, quantified, and assessed in a fraud-resistant way. Until recently, human flourishing was not something to be crisply specified, quantified, or assessed in a fraud-resistant way.

But the same techniques to collect human values in the section above, can also be used to collect information about what parts of users’ lives are most meaningful to them, and how their lives are going on that basis. Instead of a festival selling tickets, payment could be tied to relationship formation, or other important aspects of community. Instead of a gym membership, the gym could be funded by how fit members get and stay, etc.

Although there’s much work to be done to show that outcome-based contracts can be tied directly to the goals of human flourishing, this serves as another example about how models that are explicit about values can make yet another sociotechnical alignment challenge tractable.

**Potential Research Topics**

- Robust Assessment of Meaning
- AI Market Intermediaries

### §2.5 - Democratic regulatory institutions that act at the speed of AI

Democratically ungovernable AI futures

Regulation has multiple purposes. One purpose is to create, in public domains like markets, the conditions for positive-sum collaboration[*]. In the future we describe, this aspect of regulation make be taken up by other means, such as the norms-based reasoning hinted at in case #2.

But another purpose of regulation is to consult and express the will of the people against private actors and trends. If regulators continue to work as they presently do, they’ll be unable to fulfill this function: AI actors will operate much faster than regulators can, and across jurisdictions for which no capable regulatory body exists.

Imagine an AI agent representing a corporation (or even a mission-driven NGO) that plans to redirect a river running across national boundaries. The plan, while technically legal, would ideally be subject to regulatory oversight representing the people who’s lives will be impacted. What we might want in such a situation, would be for the relevant agent to negotiate with another agent which represents the will of the relevant people, and which manages and legitimates the expression of that will in an auditable, responsible, and retroactively-scrutinized-and-approved way.

Finally, we have the challenge of creating new institutions charged with representing the values of, and possibly protecting the norms of, a large, mixed population, and which can act to represent those populations at the speed of AI.

In S1, we presented an approach for collecting values from individual users. This can also be used to collect and update a population’s values. Those values can be collected into an inspectable, auditable data structure, such as the one we call a moral graph.

> A set of values cards alone does not provide an alignment target, as there is no way to tell which value to prioritize when, or how to resolve conflicting values. As discussed in Section 3, existing alternatives such as majority voting or bridging-based ranking fail to meet our desiderata. Instead, we propose an alignment target we call a moral graph. This structure is inspired by the theory of how values can be reconciled described in Section 2.3, and as we’ll show in Section 5, does well on our criteria for scalability, auditability and legitimacy.
>

This can use to train, guide, or assess the operations of new institutions, which operate at the speed of AI agents but represent the public will.

In future work, we may use models of value- and norms-based reasoning to get this regulatory infrastructure to produce checkable justifications for actions, in terms of the values and norms of a population, and to unsure that these justifications are non-manipulative in the same sense as discussed in S1.

We believe there will be a explosion of democratic mechanism designs based on explicit representations of values and norms, and auditable values- and norms-based thinking, and that these new democratic mechanisms will fill in the gaps and failures we see in current democracies.

**Potential Research Topics**

- New, robust aggregation methods
- Post-hoc legitimation by large populations
- Philosophical work on democratic norms vs values

Recently, mechanisms by Conitzer[7] and Klingefjord et al[8] leave the SIDT behind. The success of these mechanism shows a field of opportunity for mechanism designers, but for now, to go there, they’d need to leave behind the formalisms dear to them (maximin, strategy-proof, Condorcet, Kaldor-Hicks, proportionality, etc). This makes new mechanisms harder to design and justify.

# §3 Research & Implementation

We here coin the term “Full-Stack Alignment” to cover three things:

- First, the provocative suggestion that many socio-technical alignment challenges can be made tractable by migrating from preference/utility frameworks to a new institution design toolkit based on explicit modeling of norms and values.

    Hopefully our provocative suggestion—that many socio-technical alignment challenges can be made tractable by migrating from preference/utility frameworks to a new institution design toolkit based on explicit modeling of norms and values—now appears more plausible.

- Secondly, the unfortunate fact that, unless we simultaneously align AI models themselves and institutions at various levels of the stack, the incentives at one layer (say, geopolitics) will produce pressure to misalign the other layers (say, ruthless military AI).
- Finally, we use Full Stack Alignment to refer to a plan — a plan for research and societal transformation: to bring this work all the way from basic research, through various legitimation steps, to policy proposals with broad support among experts and the public, and finally to broad implementation in new algorithms, institutions, and mechanisms — all in time to head off the socio-technical threats listed above before AI agents cause widespread harms.

In the below, we’ll briefly sketch what the research and implementation plan will look like. A strategy for moving towards a society with social systems and institutions built on new frameworks for values and norms.

We believe theoretical research alone in the 5 areas outlined above is not sufficient. For an AI lab to adopt a mechanism built on these new foundations, three key conditions must be met: expert consensus must exist that the solution is the best available approach, a clear flagship implementation must exist as a concrete example, and there must be widespread demand for the solution demonstrated by the flagship example.

If there is expert consensus but no clear flagship example to point to, a solution would likely be deemed intractable in the real world. If there is a clear flagship example, but no public demand for it, it is likely deemed too risky. If there is clear public demand but no flagship example, it will likely be ignored (public outcry around global warming without clear expert consensus and policy implementation pathway didn’t lead to the change the public was hoping for).

Therefore, our general approach is to systematically move work on full-stack alignment for all of the 5 fields we have covered from research to implementation.

## §3.1 **Fundamental Research**

Rigorous theories, formalisms, and prototypes demonstrating the viability of explicit norm- and value-based institution design.

The goal of the research is to prove out viable solutions to the full-stack alignment challenges above. In some cases, this means new techniques and formalisms need to be developed. In every case, researchers will need to build proof-of-concept systems/mechanisms, and put them through a variety of legitimating tests and proofs—making formal claims about optimality, robustness, etc, and gathering data about small-scale deployments, user experience, legitimacy, etc.

## §3.2 **Expert Consensus & Flagship Real-World Implementations**

Cultivating a strong interdisciplinary community—spanning scholars, technologists, and policymakers—to establish clear expert agreement around these novel frameworks.

Launch targeted real-world pilots—such as value-aligned market systems, experimental democratic platforms, or morally-competent AI deployments—to serve as proof-of-concept demonstrations.

Once our solutions appear viable, we’ll need consensus among policymakers and decision-makers that this is the right approach. We’ll build that consensus via advisory networks, frequent meetings between researchers and implementers, and demonstrations. We’ll distill each solution into a concise policy or product recommendation, gathering up the related research.

We’ll also hunt for opportunities for real-world deployments:

- With the **market interventions**, we’ll find exchanges or market infrastructure providers that have the power to implement them in real-world settings, perhaps as a pilot project or within a submarket.
- With **democratic interventions**, we’ll find early-adopter polities, like Estonia or Norway, ready to try something new, like an emergency AI regulator.
- With work on **morally-competent agents**, we can find a financial marketplace that will trial being only open to such agents, or a corporate supplier for them.

These flagship implementors do not need to be from the largest countries or the top AI labs, but they must be robust successes that others can point to, pointing the way to the future.

These flagship deployments will prove these systems viable in the real-world, but they could do more than that. [Footnote about rhetoric / use flywheel]

![image.png](attachment:e552ad4e-ffc8-470e-8e12-d98b314e73a3:image.png)

# §4 T**ell our enemies that they may take our lives, but they’ll never take our freedom!** 🐎

There will be a great institutional renewal. Much of civil society will be re-invented. AGI will integrate in a way that’s cooperative, and that makes human values (or norms) go brrr, improves our epistemic environment, and enhances our social fabric.

# Footnotes

[-1] Manin, B. (1997). *The principles of representative government*. Cambridge University Press.

[0] Social choice started as non rooted in a rational model of humans: the first theorems (Condorcet) modeled humans as realization of some random variables and did not come with micro-foundations for these random processes. The 1950’s social choice theory became more micro-founded/rational.

[1] Or, more precisely, ideas like values, beliefs, and norms have just been folded into preferences.  I don’t mean to minimize the amount of work done on these topics: Outside the SIDT, these intersubjective concepts have been modeled in fields like sociology. And there is hugely successful work extending economics or game theory in these directions, but it remains peripheral. For instance, in microeconomics and game theory there are well-known theories of norm emergence; there are alternatives to rational choice theory like Ruth Chang’s or Isaac Levi’s. There are also larger efforts, like institutional and organizational economics. But (with the exception of transaction cost econ) these never make it into the SIDT that is used to design or justify institutions. Other innovations which do make it in (like behavioral economics or social network analysis) have remained context-free.

[2] When social theories equate revealed preference with benefit, anyone who can manipulate another’s choice (which is supposed to reveal a certain preference) can count as benefiting them. (For a quick review of the problems with revealed preference, see [1. Critiques of Revealed Preferences](https://www.notion.so/1-Critiques-of-Revealed-Preferences-e7285a5af4914c4b8f45215e4c8e3f3f?pvs=21))

[3] See “Klingefjord, Lowe, and Edelman”

[4] See Xuan….

[5] Amartya Sen

[6] ****People’s preferences change productively over time as they better understand what’s important to them, face new contexts, and realize aspects of situations they didn’t previously consider. That means that some people have better preferences in some contexts. But mechanisms based on these prevailing social theories can’t detect them. These mechanisms miss the opportunity to harness moral learning, to let us reach collectively towards something that's not just the average.

[7] Conitzer moral mechanism

[8] See “Klingefjord, Lowe, and Edelman” again

[9] Glen Weyl put it well:

> [Currently models feature] a binary between Individuals, conceptualized as largely pre-social, independent ultimate loci of value/preference/good/belief, and some global coordination device variously referred to as the social planner, the mechanism designer, the impartial observer, God or, most commonly, The State.
>
>
> It is from this binary that the initially paradoxical combination of extreme individualism and authoritarian technocracy that characterizes [this view] arises.
>

[10] A longer treatment of these ideas is in [“Nothing to Be Done” by Joe Edelman](https://medium.com/what-to-build/nothing-to-be-done-bfe2ce71a3a2). Look for the paragraph that starts:

> Each of these fields is subject to another kind of test, besides its ability to predict human choices. Each field has a model of human beings which focuses on certain skills or abilities or activities of the human subject.
>

[11] Some of these terms allow people to advocate for a policy direction, some allow them to find each other, some allow them to advocate for leaders that serve their previously-unnameable interests. `Modern Social Imaginaries /`

[12] There’s even a tendency to say something like “I guess if people are voting for social isolation, with their dollars and at the ballot, then a good society is one of social isolation! (So long as it’s free and fair.)”

[13] [Taylor, “Modern Social Imaginaries”] Taylor argues that historically, this co-option ends up undermining the power of the incumbent system.

[14] These effects are considered fairly well-supported in political theory and political science. [Weber, Taylor, some recent political scientists]

[Footnote about rhetoric / use flywheel]

Let us suppose this pans out. This will then change people’s ideas of what a good society looks like. Currently, the dominant social ideals are freedom and fairness. It is not so surprising that—in a society dominated by markets and voting, where we think of ourselves as entrepreneurs and citizens—our ideal society is one of freedom and fairness. Other notions—like having meaningful lives, advancing science and art, having strong communities—these seem attractive, but they don’t fit as cleanly into our markets/voting-dominated vocabulary as freedom and fairness do.[12]

But note that the this depends on the institutional mix. Other mechanisms lead to other ideals. For instance, the spread of wikis and open source has popularized the idea that a good society should be open to ‘pull requests’ of some form, leading to ‘read/write society’ wiki-based governance ideas in Taiwan and other places. One can imagine that Twitter’s Community Notes might popularize a notion that a good society is ‘algorithmically sober’.

In general, whenever a new institution seems better along a *new dimension* (it is not just more free or more fair), a new rhetoric emerges. It’s unlikely that ‘read/write society’ or ‘algorithmically sober’ will overtake freedom and fairness as the qualities most heavily advocated for in social arrangements, but we think that some other term, not coined yet, probably will. This is how political paradigm shifts have always gone.

We don’t know which new terms will take hold—they might be about "surfacing collective wisdom," "strengthening social fabric," or "enabling diverse forms of life"—but they will become frameworks for reimagining social possibilities.

Should such a positive feeling and new rhetoric emerge around our flagship deployments, we will encourage it. We will help encourage participants to articulate the advantages of these new systems, and share what it’s like to participate in them.

Terminology can be a decisive factor in which groups manage to coordinate politically. For instance, it’s hard for the working class to find each other without the term ‘working class’; it’s hard to fight for collective ownership without ideas like ‘worker coop’; it’s hard to fight for local self-determination without concepts like ‘freedom’, ‘subsidiarity’, or ‘laissez-faire’.[11]

Many communities would ideally band together in common interest, but for now they can’t even find one another, or have nothing clear to advocate for. There are no terms yet.

Once there are new terms—once people begin to see themselves as a “values-driven” (rather than just as entrepreneurs, informed citizens, Democrats, or Republicans) and band together with other values-driven people to further values-driven forms of social organization—it will be hard to reverse.

Eventually, the legitimacy of political arrangements will be defined by a vocabulary which today isn’t even in play.[14]