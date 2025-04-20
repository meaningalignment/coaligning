# Inadequacy of Utility Function and Preference-Based Approaches

To address the challenge of socio-technical alignment requires redesigning institutional structures, yet we will claim that the formal toolkit for institution design inherited from the 20th century—microeconomics, game theory, mechanism design, welfare economics, and social choice theory—is inadequate. We call this inadequate set of theories the *Standard Institution Design Toolkit (SIDT).*

These theories model agents via a *thin* conception of rationality: individuals are presumed to possess intrinsic preference profiles, utility functions, or payoff matrices with some big limitations: (1) they cannot be inspected by others[*]; (2) they do not reference some underlying notion of the good; (3) they are blind to social context, such as shared values, norms, beliefs, or group identities[1].

1. People's preferences are often **incomplete**, **inconsistent**, or **unstable** over time.

    Since utility theory is not designed to model agents who change , reshape, and discover preferences over time — much less agents that *reason* about which preferences or values are more sensible or justified to hold — it is unlikely that it will be up to the task of capturing human-like reflection about values. Instead, thicker approaches to human values and choice are likely necessary, as we will describe further below.

2. **Need to avoid manipulation of revealed preferences.** We've known since the debates in welfare economics (most closely associated with Amartya Sen) that revealed preference is quite limited as a measure of benefit. It's become ever clearer that businesses, governments, and other entities have indeed learned to exploit individuals under the guise of serving their preferences, using AI[2], and it's also become clear that current AI models are actively engaged in reward hacking[*].

    Since LLM-based AI is taking over much more of society even than recommenders did, there is, thankfully, much more appetite to overcome these problems with revealed preference than there was when Sen was working in development economics.[5]

    This seems to demand a deep economic shift, and one that's difficult to model using conventional microeconomics or to measure using welfare economics, because in these models humans are considered to be 'fulfilling their preferences' even when they are doomscrolling, addicted to AI pornography, etc.

3. **Preferences seem inadequate for sophisticated democracy.**

    Preference/utility frameworks in social choice fall short, here, for several reasons: (1) first, the impacted people may not have the time (or mental bandwidth) to express their detailed preferences about every possible outcome in time for the negotiation to occur; (2) second, while the representative agent could extrapolate from previous preferences, since preferences are divorced from reasons, it's reasoning will not be accountable to human reasons; (3) finally, preference frameworks assume preferences are static and previous-established, and cannot model the updating that often occurs as new circumstances are considered.

    To give but one example, the standard version of social choice is blind to the most powerful lever in deliberation: inspiration. The best mechanisms should not just accommodate existing preferences; they should allow for the formation and inspiration of new ones, by creating environments where individuals grow in their understanding of what is good.[6] Can mechanism design catch up with ancient Athens?

    1. **Need for new institutional forms.** The SIDT theories achieved their centrality because they are mathematically expressive and powerful, parsimonious, and they sat well with widespread philosophical intuitions. Plus, they seemed 'good enough' for the institution design challenges of their day. Yet, today, AI alignment challenges seem to require inventing new forms of governance, and many directions for institutional innovation are hard to motivate or analyze using the SIDT.
4. **Preferences, game theory and cooperation.**

    Addressing these challenges turns out to be a sore point for the SIDT. In the most classical solution concept in game theory — Nash equilibria — agents simply maximize their payoffs under the assumption that everyone's actions are independent an uncorrelated. On this view of "rational" multi-agent interaction, there is no room for shared social norms. Other equilibrium concepts, such as correlated equilibria, provide an entry point for shared norms [CITE], but no explanation for how people might select between or reason about which equilibria might be better [CITE]. Furthermore, game theory assumes that norms exist purely to coordinate ultimately self-interested behavior — yet many human norms both constitute and express our shared values and practices [CITE].

    As such, if autonomous agents are trained in accordance with a thin game-theoretic account of human normativity — as is typical in approaches like multi-agent RL — we will likely find them normatively incompetent: incapable of recognizing or following existing norms, incapable of reasoning about or adapting them, and incapable of understanding the reasons and functions of our norms and institutions. To build agents that are normatively competent, we will have to depart from the SIDT and its technical implementations.

    As in the case of AI-mediated institutional dysfunction ([Challenge 2](https://www.notion.so/Co-aligning-AI-Institutions-1d7c5bada1d0804e8a27c467305e7096?pvs=21)), standard game-theoretic accounts do not offer much hope for addressing this risk. In fact, game theory has long been criticized for its failure to predict cooperation in classic settings like the one-shot Prisoner's Dilemma, where many humans do successfully cooperate, or to capture humans' ability to make and maintain promises without external commitment devices. Instead, the kind of strategic rationality endorsed by conventional game theory is essentially Machiavellian: a form of rationality where deceptive "promises" are considered reasonable, and threats or strong-arm tactics are fair play. Such rationality often destroys the possibility of negotiating cooperative outcomes, and even when it does achieve stability, it may be through risky and threat-laden mechanisms such as mutually-assured destruction.

    How might these Machiavellian AI dynamics be avoided? While the ability to learn and understand norms ([Challenge 2](https://www.notion.so/Co-aligning-AI-Institutions-1d7c5bada1d0804e8a27c467305e7096?pvs=21)) provides part of answer, reasoning about preferable norms, contracts, and institutions often involves simulating what the relevant agents would agree to — a process of negotiation. Whether in actual or simulated negotiation then, we will need frameworks for negotiation and bargaining that make room for people's ability to credibly report the commitments and values that guide their actions, to model others as commitment-bound reasoners, or to universalize our decision procedures to other cooperators. Neither conventional game theory nor the SIDT provide these resources.

5. **Need to address higher goods.** Finally, the SIDT assumes agents have fixed preferences, disconnected from one another and from any broader notion of the good**.** This means, individuals, societies and AI systems cannot collectively aspire to ideals beyond preference satisfaction.

    However you understand our social embedding — whether as shared values, norms, or beliefs — to acknowledge it exists seems to suggest kinds of goodness beyond preference satisfaction. For example, if humans have shared values, this suggests moral progress or learning is possible. If humans have evolving norms, this suggest we could aim at game-theoretic notions of goodness, such as cooperation at higher scales, or across diverse ecosystems. If humans have shared beliefs, there's the aspiration to discover higher truths.[*]

    So long as individual preferences are the yardstick of the good, none of these other notions can be admitted, and no one is allowed to know better than anyone else.

    What's worse, so long as the satisfaction of reveal preference is our only social good—or the only one we measure and track—we'll see other social goods in decline. And there's broad agreement this has been happening:

    - Especially in domains like politics and science, there's widespread suspicion that our capacity for social cognition, converging on truth, has declined, via misinformation, media manipulation, etc.
    - Conservatives suspect we've suffered a decline in morals and aesthetics.
    - Both tend to say our norms and channels for cooperation have eroded.

    Whether such declines are happening or not, it doesn't seem likely that measures of consumption or engagement/revealed preference would show them, or that AIs and institutions tuned to maximize consumption / engagement / revealed preference would honor them.

    This becomes more intolerable the faster those agents or institutions operate, and the more power they wield.

6. **Fit?**

    The ultimate test of an idea about human nature is how the systems it informs *fit*. What we mean by this[10] is: any set of social theories implies certain skills and activities on the part of agents. Current mechanism design implies agents who optimize, calculate, strategize, collude, reduce values to numbers, estimate probabilities, etc. Standard theories of intelligent agency — which guide the design of both AI systems and their models of humans — do the same. These activities aren't foreign to human nature, but don't seem central either. So, we have to put in a kind of effort to participate in the institutions that emerged from this view of agency. (Other social theories have similarly poor fits: people don't effortlessly advocate for class or race interests, nor natural status maximizers, etc. That makes participating in class struggles or status games a bit exhausting.)

    We hope that the mechanisms and institutions implied by this new toolkit, with their explicit norms and values, will be different. We hope that norm-following, norm-intuiting, inspiration, and pluralist value-pursuit make a better account of human nature and rationality than the above, and that therefore algorithms, institutions and mechanisms built on this basis will fit our lives better.

    Ultimately, the proof here is experiential: as new context-aware institutions, algorithms, mechanisms, platforms, and laws develop, we'll see what it feels like to participate in them.


# Inadequacy of Prompt & Self-Critique-Based Approaches

- **Determining an Adequate Specification.** If you're gathering a prompt or a specification in one go, it's hard to get the level of detail right, or to know if users really said what they mean to say. Often, we misspecify our prompts, or we're vague, and we need to adjust them. This problem will get worse as agents take more actions on our behalf, or as more involved chains of reasoning and self-critique come between textual intents and actions taken.

    If agents instead come back with clarifying questions and follow-ups, we're just kicking the can down the road. It's hard to know when they should stop asking questions when they've said enough, if the result is just an arbitrary text ring, rather than some sharper notion of what it means to capture a value as used in choice, or a norm that applies within the context. When can the model be confident that it's understood what's important to a user or population, or what norms are right for a context?

    In more social contexts, we see additional barriers to adequate specification:

    - **Manipulation**. Additionally, once agents are asking follow-up statements, it becomes hard to know what information came from the user, and what information was supplied by the model. If the user appears happy with model behavior, does that amount to a successful information transfer from the user to the model? Or is it a manipulation of the user / ending prompt by the model?
    - **Bridging and vagueness.** These problems are further compounded. In social choice settings. Here, bridging structures make text strings even more vague than what'd be supplied by individual users. When you ask about political values, you often get statements that are vaguely positive, like Obama's "hope" - but relatively powerless in terms of shaping model behavioral policies.

        We wrote about how this problem affects CCAI in https://arxiv.org/abs/2404.10636:

        > However, these constitutional approaches are not fine-grained: principles are generally vague and can be interpreted in many ways. Many different principles might apply for a given output and there is no way of reconciling which principle should be prioritized in a given context. This also makes them less auditable, as it's difficult to determine which principles were used to produce a particular output.
        >
        >
        > For example, the comments below were surfaced as shared "values" by CCAI:
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
        > 
    - **Pollution of values statements by sloganeering.** Other "automatic deliberation" methods, like values profiles, end up polluting prompts and specs with preexisting ideological battles. You often see statements like "Killing babies is always wrong" or "family values" or "All cops are bastards" that don't really map to the kinds of values that users themselves would use in their choices, or what they would apply if they found themselves in a position of responsibility.
- **Verification of Good Reasoning.** Suppose you somehow manage to overcome the above, and get good information about norms or values into a free form text. Once it's in free form text, "reasoning" is allowed to hang off that free form text in arbitrary ways. It then becomes hard to check if it's good reasoning.

    In philosophy, logic, and cognitive science, there are formal models of what good reasoning about values and norms consists of (e.g., models of reasoning that connects values to improved values, values to actions, norms to permitted actions). Such models of good values- or norm-based reasoning can be useful to check justifications that models make. But these models of good reasoning aren't defined over arbitrary text strings. They act on structure data representing values, norms, options, etc.

- **Societal pressure to mis-specify.** Finally, since anything can be added to free-form text, and used as an input to self-critique, this opens up vectors by which alignment targets will be polluted (are already polluted), by tribal affiliations and ideological warfare, shaping model behavior away from what affected human populations would consider wise, towards adherence to various slogans and fads.

    The tribal affiliations and ideological signals we mentioned above which already pollute our prompts and specifications — these aren't just accidental. There's intense societal pressure to make people claim to have certain values and to espouse certain norms.

    The challenge is to avoid dragging socio-technical alignment into the same political morass/quagmire the entire political process has been stuck in, without being subject to any political bias.

    A great way to do that, is to have clear models of what norms and values *are,* which end-users can also understand, and see how they work and how they influence choices. This requires some kind of model about what should count as a value or norm, rather than just free text. Equipped as such, users can tell for themselves that they're not being skewed away from one set of values to another, but are engaging in a process that surfaces more of their true values and of other people's.

    There is prior art here wrt values; as we wrote in https://arxiv.org/abs/2404.10636:

    > If someone claims to have a value like "Defund the Police" or "Abortion is Murder", they are then
    asked about meaningful choices ( 4.5) they themselves have made, and what they paid attention to
    during the choice. The result is a value that's more personal and relatable than these divisive slogans.
    >

    (See also A.4 Elaboration on robustness to ideological rhethoric in https://arxiv.org/abs/2404.10636)
