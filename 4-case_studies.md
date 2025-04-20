# Early Evidence Deeper Reps Have Promise to Co-align AI and Institutions

To make our case concretely, we'll pick five representative problems which serve as motivation for new theoretical approaches. These challenges represent domains where preference/utility frameworks demonstrably fall short.

## 4.1 AI agents that represent, respect, and steward user values

**AI that drives us towards value collapse** 🔥

When people over-index on explicit metrics or singular objectives as their goals in life, they are at risk of phenomenon called *value collapse* [[X](https://royalinstitutephilosophy.org/event/value-collapse/)] — losing touch with the rich complex of values that they originally cared about, and replacing it with a thin conception of what matters (e.g. money, status, etc.) Many social forces already encourage such collapse, and as AI plays an increasing role in our individual and social lives (as assistants, delegates, confidantes...) we risk losing autonomy to AI systems that homogenize and flatten our values into easy-to-optimize objectives. In the worst case, such objectives might be entirely uncorrelated with what we truly valued to start with.

This form of AI misalignment is much subtler than simply optimizing for the "wrong" goal or utility function. Indeed, a large part of the risk is that AI systems will interpret or reshape our values into more pliable or easily-satisfiable forms — all in the guise of "being helpful" or "providing assistance". Many recommender systems already suffer from this property [?], and advanced AI agents are even more likely to skillfully manipulate and capture our values, even if they seem to be aligned at the surface-level.

How can we avoid such AI-driven value collapse — at the individual level, but also in society writ large? Part of this will involve counteracting economic incentives towards collapse (see section 4.4), but we will also need AI that is genuinely capable of actualizing and helping us actualize our values — AI that can serve as faithful trustees, acting upon our values by reasoning about which values to apply, prioritize, or refine in new situations; and AI that can serve as skilled advisors, helping us reflect upon what really matters while still respecting our autonomy in deciding our own values.

To avoid value collapse, we'd want an agent to have clear values that the user recognizes as their own, and that the user trusts to be a faithful steward of those values. That collection of the values should be testable — so the user can be satisfied that it generalizes to novel situations, even before sending the agent out to work. Those values should also go deeper than surface-level or contingent preferences: preferences due to misinformation, lack of foresight, or social norms that don't have inherent value for the user should be interrogated for what really matters; preferences due to strategic situations which the user would rather be rid of than comply with should be abstracted.

In short, the values of the agent should be those most likely to be retroactively endorsed by the user, and to hold throughout a variety of situational changes.[*]

For the reasons we highlighted earlier, preference-based alignment can't distinguish between preferences that would or would not be retroactively endorsed. But new models of agency with thick representations of values can. Recent advances in the thick representation of values can be used to align user and agent behavior in a human-legible way and to define non-manipulation. For instance, in our moral graphs paper[3], we define values in terms of user legible values cards:

> Our approach to representing values comes from the literature of sequential choice-making—the theories of sequential search (Simon, 1956; Kahan et al., 1967), information pickup (Gibson, 1966), and option set formation (Smaldino and Richerson, 2012; Morris et al., 2021). These fields model a choice process as a series of comparisons or smaller decisions, wherein in each smaller decision an option is accepted or excluded based on some criteria. There is therefore a relationship between the path of attention a person follows when considering options, and the criteria they use for choosing.
>
>
> Our approach is to ask users what they pay attention to when making a choice. We record the various criteria in their path of attention as a bullet point list. We call the items on these lists "attentional policies" (APs).
>
> We then filter this list of attentional policies, to carry through from section 3 the idea that values are not all criteria used in choice, but the ones which are not merely instrumental – that connect the choice to something the user wants to uphold, honor, or cherish, or something they find beautiful, good, or true.
>

In our [model integrity post](https://meaningalignment.substack.com/p/model-integrity), we propose how the applicability of a set of values could be tested and trusted by users, before they deploy their agent.

> Finally, an LLM agent has **values-trust** if its legible values make it clear to humans *where* it can be trusted. Roughly speaking: given a model's values, can a human easily predict a domain where it will make decisions they'll approve of?
>

And again in the moral graphs paper, we talk about how values can be collected so as to exclude social norms, ideological commitment, strategic concerns ,etc, getting closer to the heart of what the user really cares about.

> This definition of values has many advantages. It allows us to neatly avoid ideological scissor
statements. We define ideology and ideological statements as follows:
>
>
> Definition 4.4 (Ideological statement). A belief or statement can be called ideological if it aims at justifying one social order or political arrangement over another (Eagleton, 1991; Joseph, 2004; Macionis, 2009).
>
> If someone claims to have a value like "Defund the Police" or "Abortion is Murder", they are then asked about meaningful choices they themselves have made, and what they paid attention to during the choice. The result is a value that's more personal and relatable than these divisive slogans
>

All of these things would be impossible in a preference-based framework, but possible when agents use richer models of human values, such as the moral graph:

> Conceptually, a moral graph can be thought of as a map of moral learning, depicting the values we live and have have lived by as we go through life, and the transitions we've made from lesser to "wiser" (section 3) values, as we gain more clarity about what's important to us. In MGE, we extends this concept to participants of a deliberative process – edges represent broad agreement amongst participants that one value is wiser than another, for a particular context. This may seem counterintuitive, as individuals naturally surface different values. Yet, we found that participants overwhelmingly converge on the directionality of these transitions, and are able to endorse and evaluate moral reasoning without having lived through it themselves
>

Such an agent can be guided by fine-grained, contextually appropriate values rather than opaque preference aggregations, or vague principles. When a user gives an instruction, the agent can identify the relevant moral context, retrieve the appropriate values from the graph, and use these values to determine whether and how to fulfill the instruction.

**Potential Research Topics**

- Formalization of values→actions reasoning (e.g., Ruth Chang's choice theory)
- RL fine-tune methods for values-based reasoning models
- Evaluating model understanding of thick evaluative concepts

## 4.2 AI agents that comply with and reason about norms and institutions

**AI-mediated disintegration of norms and institutions** 🔥

As autonomous agents take up roles in our society previously filled by humans, we face an increasing risk that such agents will stress and ultimately break the norms and institutions that humans maintain. Whether as self-driving cars on the road, remote AI workers executing tasks on the Internet, or moderators and enforcers of organizational rules and policies, such agents may fail to comply with implicit norms that distribute shared resources (e.g. norms against hogging the road or a website's limited bandwidth), or fail to understand the purpose behind an institutional rule (e.g. a AI moderator that bans users as "discriminatory" for using reclaimed slurs). Sophisticated AI agents may even exploit existing rules or their loopholes in their favor, strategically enforcing or complying with rules in a way that leads to institutional dysfunction.

To guard against AI that leads to the breakdown of human norms and institutions, we believe that it is important to build AI agents that are not just norm-aware, but *normatively competent*. Existing LLM-based systems provide a starting point here. By being trained on human text, they already contain knowledge about extant and historical human norms. Furthermore, as approaches like Anthropic's Constitutional AI [CITE] and OpenAI's model specification [CITE], LLM chatbots can be prompted with lists of normative principle in natural language, which they can interpret and comply with to a good degree.

Yet, awareness and compliance with norms in the training data or model constitution is not enough for full normative competence. For AI agents in dynamic environments interacting with a large and potentially changing mix of other agents, it is also important to *adapt* to new norms and institutional practices online, and to *reason* about how and whether particular norms or rules should apply in an ever-evolving context. Imitation learning of how humans comply with norms does not provide this, since it assumes norms are fixed. And traditional game-theoretic reasoning is often worse — it encourages agents to reason about whether to obey a norm, but according a logic that rewards defecting from such norms as long it would benefit the defector.

What alternative approaches might enable normative competence? Models of online learning of social norms and institutions — formulated as norm-augmented Markov games [[X](https://arxiv.org/abs/2402.13399)] — provide a framework for how agents can rapidly learn the norms practiced by a population of agents from limited demonstrations, and how they can be incentivized to comply with them. This could be turned into training paradigms for norm-adaptive AI agents, where agents are rewarded for complying with norms that are good predictors of other agents' group behavior (and where such behavior cannot be explained by individual desires.)

What about normative reasoning? While many avenues are open, here we highlight computational models of contractualist reasoning — and in particular, resource-rational contractualism [[X](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/resourcerational-contractualism-a-triple-theory-of-moral-cognition/5A567D41A472DBC0D965460966580C74)]. In resource-rational contractualism, norms are modeled as approximations to the social arrangements that would be agreed upon if people could negotiate towards fair and mutually-beneficial outcomes. Since actual negotiation is costly, people follow existing norms by default, but if the cognitive costs are worth it, people might *simulate* what norms others would agree to for a particular context (virtual bargaining) and the outcomes if everyone were to practice the new set of norms (universalization). These mechanisms provide a rich toolkit for generalizing norms to new scenarios, or selecting between multiple possible norms or conventions — a toolkit which could be embedded in AI agents either by training or design.

**Potential Research Topics**

- In-context norm learning for LLM agents via multi-agent training
- RL finetuning for contractualist chain-of-thought reasoning
- Extensions of norm-augmented games to capture richer institutional structure
- Formal models of universalization reasoning and virtual bargaining

## 4.3 Win-Win AI negotiation via revealed values and commitments

**Machiavellian AI negotiation leads to lose-lose equilibria**

In a world filled with AI agents and perhaps even AI corporations, AI systems may replace humans in negotiating both private and public contracts, or engaging in diplomacy and international relations. The costs of failing to cooperate or coordinate in these domains can be very high, ranging from failure to realize the gains of cooperation to outright conflict and war. And while humans do not always succeed in negotiating mutually valuable outcomes, it is a real possibility that AI agents will lack human-like cooperative intuitions, and do even worse. Indeed, existing LLM agents have already been shown to escalate conflict in wargames more often than humans [[X](https://ojs.aaai.org/index.php/AIES/article/view/31681), [X](https://dl.acm.org/doi/abs/10.1145/3630106.3658942)].

If standard game-theoretic models cannot reliably ensure mutually-beneficial negotiation without the risk of defection or the accumulation of credible threats, what options are available instead? Our suggestion is to design agents that can credibly reveal the values and normative commitments that guide their decision-making procedures — and to be able to model other agents as credible revelators (instead of ruthless strategizers). This property is an instance of what we call [integrity](https://meaningalignment.substack.com/p/model-integrity) — the capacity for an agent to make legible and reliably follow through on its values and commitments.

Value revelation draws upon existing ideas in game theory, but fruitfully combines them to avoid their pitfalls. In [(partial) revelation games](https://www.cs.toronto.edu/~cebly/Papers/HyafilBoutilier_ijcai07.pdf), agents share information about their utility functions with other agents, enabling better outcomes. However, all agents are still assumed to be utility maximizers — agents cannot reveal other facts about how they make decisions. In [open-source game theory](https://arxiv.org/abs/2208.07006), agents share the full source code of how they make decisions. Such source code can deviate from utility maximization in arbitrary ways, and hence enable strong cooperation. But this ability is unrealistic for LLMs or other sufficiently complex agents.

Since values carry thick information about not just the outcomes that matter to an agent, but also about the norms they are committed to when making decisions, value revelation provides a sweet spot between open-sourcing and utility revelation. By revealing values (e.g. belief in reciprocal justice, or the sanctity of friendship), agents shares partial information about their underlying decision procedures ("source code"), providing reasons for cooperation that can be far stronger than merely revealing their preferences.

We note that value revelation is not a complete solution. Work still needs to be done to ensure truthful revelation of values (e.g. through institutional vetting of the integrity of AI negotiators), and to guard against ruthless agents who nonetheless claim to be honest or justice-seeking (e.g. by developing strategy-proof value revelation mechanisms). Other ways of enabling more cooperative outcomes, such as [Kantian optimization](https://www.jstor.org/stable/40587794) and [dependency equilibria](https://kops.uni-konstanz.de/handle/123456789/3505), are also complementary to value revelation. Finally, it may turn out that there are other tractable ways to sharing "partial source code" besides via value revelation (e.g. formal certificates). Nonetheless, insofar as human values can serve as an efficient "compression" of how suitably human-like LLM agents make decisions, we believe this is a promising avenue for improving AI negotiation.

**Potential Research Topics**

- Values-interpretable LLM agents
- Strategy-proof value revelation mechanisms
- Evaluating the integrity of AI negotiators
- Formal models of value revelation (e.g. partial-source game theory?)

## 4.4 A meaning-preserving AI economy that promotes human flourishing

The AI-run economy obviates human flourishing

Already in our current economy,  some economic activity seems more closely connected with the wellbeing of human beings than others. We can broadly call some economic activity human-detached (such as zero-sum or negative-sum financial speculation) and other economic activity could be called human-antagonistic (such as addictive products, some social media, etc).

There's clear evidence that the volume of human-detached economic activity has grown by several orders of magnitude in recent decades[*], and there's less conclusive evidence that the volume of human-antagonistic activity has grown too[*]. In both cases, ML has been a driving factor, via, e.g., algorithmic trading and social media recommenders.

A brake on these trends has been the continued importance of human beings to companies (as workers and customers) and to countries (as a tax base). Human lives can't get that bad or irrelevant, because they will stop being productive or being an income source.

Supposing the future is one where many profitable companies consist mainly of AI workers, and where, correspondingly, national tax bases shift from income tax to forms of corporate taxation, there will be significantly less pressure to keep human lives viable and good. And at the same time, significantly more capacity to extend the economy in human-detached and human-antagonistic directions.

Tying the economy to human flourishing can be thought of a problem of tying the payment flows in contracts to human flourishing, and doing this on such a broad basis that lower, more infrastructural and speculative parts of the economy are also remain accountable to human flourishing.

This can be thought of as a problem in dynamic and outcome-based contracting.

- **Dynamic contracting** is a subfield in economics which involve the use of AI to make contracts that balance risk and reward, or achieve other complex goals for pricing and provision.
- **Outcome-based contracting** refers to aligning payouts of contracts to the ultimate benefit being sought. For instance, in the airline industry, tying repair contracts to the readiness of the aircraft for flight when its needed.

In general, outcome-based contracts are easiest to implement in domains where the desired outcomes can be crisply specified, quantified, and assessed in a fraud-resistant way. Until recently, human flourishing was not something to be crisply specified, quantified, or assessed in a fraud-resistant way.

But the same techniques to collect human values in the section above, can also be used to collect information about what parts of users' lives are most meaningful to them, and how their lives are going on that basis. Instead of a festival selling tickets, payment could be tied to relationship formation, or other important aspects of community. Instead of a gym membership, the gym could be funded by how fit members get and stay, etc.

Although there's much work to be done to show that outcome-based contracts can be tied directly to the goals of human flourishing, this serves as another example about how models that are explicit about values can make yet another sociotechnical alignment challenge tractable.

**Potential Research Topics**

- Robust Assessment of Meaning
- AI Market Intermediaries

## 4.5 Democratic regulatory institutions that act at the speed of AI

Democratically ungovernable AI futures

Regulation has multiple purposes. One purpose is to create, in public domains like markets, the conditions for positive-sum collaboration[*]. In the future we describe, this aspect of regulation make be taken up by other means, such as the norms-based reasoning hinted at in section 4.2.

But another purpose of regulation is to consult and express the will of the people against private actors and trends. If regulators continue to work as they presently do, they'll be unable to fulfill this function: AI actors will operate much faster than regulators can, and across jurisdictions for which no capable regulatory body exists.

Imagine an AI agent representing a corporation (or even a mission-driven NGO) that plans to redirect a river running across national boundaries. The plan, while technically legal, would ideally be subject to regulatory oversight representing the people who's lives will be impacted. What we might want in such a situation, would be for the relevant agent to negotiate with another agent which represents the will of the relevant people, and which manages and legitimates the expression of that will in an auditable, responsible, and retroactively-scrutinized-and-approved way.

Finally, we have the challenge of creating new institutions charged with representing the values of, and possibly protecting the norms of, a large, mixed population, and which can act to represent those populations at the speed of AI.

In section 4.1, we presented an approach for collecting values from individual users. This can also be used to collect and update a population's values. Those values can be collected into an inspectable, auditable data structure, such as the one we call a moral graph.

> A set of values cards alone does not provide an alignment target, as there is no way to tell which value to prioritize when, or how to resolve conflicting values. As discussed in file 3-new_toolkit.md, existing alternatives such as majority voting or bridging-based ranking fail to meet our desiderata. Instead, we propose an alignment target we call a moral graph. This structure is inspired by the theory of how values can be reconciled described in file 3-new_toolkit.md, and as we'll show in file 5-roadmap.md, does well on our criteria for scalability, auditability and legitimacy.
>

This can use to train, guide, or assess the operations of new institutions, which operate at the speed of AI agents but represent the public will.

In future work, we may use models of value- and norms-based reasoning to get this regulatory infrastructure to produce checkable justifications for actions, in terms of the values and norms of a population, and to unsure that these justifications are non-manipulative in the same sense as discussed in section 4.1.

We believe there will be a explosion of democratic mechanism designs based on explicit representations of values and norms, and auditable values- and norms-based thinking, and that these new democratic mechanisms will fill in the gaps and failures we see in current democracies.

**Potential Research Topics**

- New, robust aggregation methods
- Post-hoc legitimation by large populations
- Philosophical work on democratic norms vs values

Recently, mechanisms by Conitzer[7] and Klingefjord et al[8] leave the SIDT behind. The success of these mechanism shows a field of opportunity for mechanism designers, but for now, to go there, they'd need to leave behind the formalisms dear to them (maximin, strategy-proof, Condorcet, Kaldor-Hicks, proportionality, etc). This makes new mechanisms harder to design and justify.
