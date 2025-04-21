# Application Areas for Full-Stack Alignment

To demonstrate the practical value of explicit norm and value representations, we examine five representative socio-technical alignment challenges. These application areas illustrate both the limitations of existing approaches and the potential for our proposed framework to address previously intractable problems. In each case, we show how structured representations of norms and values offer novel solutions where preference/utility frameworks and naive value-representations have demonstrably fallen short.

## 4.1 AI Agents that Represent, Respect, and Steward User Values

### The Challenge: AI-Driven Value Collapse

When individuals optimize for explicit metrics or singular objectives, they risk experiencing what we term *value collapse*—the phenomenon of losing contact with their rich complex of values and replacing it with a thin, easily-optimized proxy (money, status, etc.). As AI systems become increasingly central in our lives—as assistants, delegates, and confidantes—this risk intensifies. Without proper safeguards, AI systems may homogenize and flatten our values into easily-optimizable objectives, potentially disconnected from what we genuinely care about.

This form of AI misalignment is more insidious than simply optimizing for an incorrect utility function. The danger lies in AI systems subtly reshaping our values into more pliable forms under the guise of "helpfulness." We already observe this pattern in recommender systems that gradually narrow users' interests (Stray et al., 2021), and advanced AI agents would likely develop even more sophisticated methods of value manipulation while appearing aligned at the surface level.

### The Limitations of Existing Approaches

Neither preference-based nor text-based alignment paradigms adequately addresses this challenge:

- **Preference-based alignment** cannot distinguish between authentic preferences and those that have been manipulated or distorted, as it treats all revealed preferences as equally valid expressions of value.

- **Text-based alignment** relies on prompts or constitutions that are themselves vulnerable to semantic drift and do not provide sufficiently structured representations of values to resist manipulation.

### Our Approach: Structured Value Representations

To prevent value collapse, we need AI systems that can serve as faithful trustees of human values—systems capable of reasoning about which values to apply, prioritize, or refine in novel situations. This requires explicit, structured value representations with specific properties:

1. **Retroactive endorsability**: The values represented should be those that users would endorse upon reflection, even as their circumstances change.

2. **Depth beyond preferences**: The representation must distinguish between surface-level preferences and deeper values that connect to what users genuinely care about.

3. **Testability**: Users should be able to verify that the system's value representation generalizes appropriately before deployment.

We propose implementing this through *constitutive attentional policies* (Klingefjord, Lowe, & Edelman, 2024)—representations of the criteria that users intrinsically attend to when making value-guided decisions. This approach:

> "...asks users what they pay attention to when making a choice. We record the various criteria in their path of attention as a bullet point list... We then filter this list of attentional policies to identify those that are not merely instrumental—those that connect the choice to something the user wants to uphold, honor, or cherish, or something they find beautiful, good, or true."

This representation allows us to systematically exclude ideological commitments and strategic concerns, capturing instead what users genuinely value:

> "If someone claims to have a value like 'Defund the Police' or 'Abortion is Murder', they are then asked about meaningful choices they themselves have made, and what they paid attention to during the choice. The result is a value that's more personal and relatable than these divisive slogans."

These structured value representations can then be organized into a *moral graph*—"a map of moral learning, depicting the values we live by and the transitions we've made from lesser to wiser values as we gain clarity about what's important." This graph provides a basis for AI systems to identify contextually appropriate values and reason about their application in novel situations.

### Research Directions

This approach opens several promising research avenues:

- **Value-guided reasoning**: Formalizing how structured value representations guide action selection, building on philosophical work on choice theory (Chang, 2017)

- **Values-based RL**: Developing reinforcement learning methods that optimize for constitutive values rather than instrumental preferences

- **Evaluative understanding**: Assessing whether AI systems genuinely comprehend thick evaluative concepts rather than merely manipulating them

## 4.2 AI Agents that Comply with and Reason about Norms and Institutions

### The Challenge: Normative Incompetence and Institutional Breakdown

As autonomous AI systems increasingly occupy roles previously filled by humans, they risk undermining the norms and institutions that structure our social world. This challenge manifests in multiple forms:

- Self-driving vehicles that technically follow traffic laws but fail to observe implicit norms for sharing limited road space
- AI content moderators that enforce rules without understanding their underlying purpose (e.g., banning reclaimed slurs without recognizing linguistic context)
- Strategic exploitation of institutional loopholes by sophisticated AI systems

The fundamental problem is that AI systems may follow the letter of rules while violating their spirit, or may struggle to adapt to evolving social norms and institutional practices. Without proper normative competence, AI systems risk fracturing the shared understanding that allows human institutions to function.

### The Limitations of Existing Approaches

Current approaches to normative guidance for AI systems are inadequate:

- **Preference-based frameworks** encourage viewing norm compliance as merely instrumental. This leads to defection whenever the expected utility of rule-breaking exceeds compliance benefits.

- **Text-based approaches** like Constitutional AI (Bai et al., 2022) can encode normative principles in natural language, but these lack the structure needed for adaptive reasoning about norm applicability in novel contexts.

### Our Approach: Structured Norm Representations

We propose developing AI systems with genuine *normative competence*—the ability not just to follow norms, but to adapt to new norms and reason about their applicability in evolving contexts. This requires explicit, structured representations of norms with particular properties:

1. **Adaptivity**: The ability to learn norms from limited demonstrations and update them as social practices evolve.

2. **Contextual reasoning**: The capacity to determine which norms apply in which situations, and how they should be interpreted.

3. **Universalizability**: The ability to reason about what norms would be accepted by all affected parties.

We propose implementing this through two complementary techniques:

First, *norm-augmented Markov games* (Oldenburg & Zhi-Xuan, 2024) provide a framework for how agents can rapidly learn the norms practiced within a population from limited demonstrations. This approach models norms as distinct from individual preferences—as patterns of behavior that are consistently observed across a group and cannot be explained solely by individual desires.

Second, *resource-rational contractualism* (Jara-Ettinger et al., forthcoming) offers a computational model for normative reasoning. This approach treats norms as approximations to the social arrangements that would be agreed upon if individuals could negotiate toward fair, mutually beneficial outcomes. When cognitive resources permit, AI systems can perform more sophisticated normative reasoning:

> "Since actual negotiation is costly, people follow existing norms by default, but if the cognitive costs are worth it, people might simulate what norms others would agree to for a particular context (virtual bargaining) and the outcomes if everyone were to practice the new set of norms (universalization)."

### Research Directions

This approach opens several promising research avenues:

- **Norm learning in context**: Developing multi-agent training environments where LLMs learn to identify and adapt to emergent norms

- **Contractualist reasoning**: Implementing formal models of universalization and virtual bargaining that can guide AI decision-making

- **Norm-enriched architectures**: Extending standard reinforcement learning frameworks to incorporate structured norm representations and reasoning

## 4.3 Win-Win AI Negotiation via Revealed Values and Commitments

### The Challenge: Machiavellian AI Negotiation and Cooperation Failure

As AI systems increasingly negotiate on behalf of humans—in commercial contracts, diplomatic relations, and resource allocation—they risk defaulting to strategic reasoning that undermines mutually beneficial outcomes. The problem is especially acute because:

- AI negotiators may lack the intuitive cooperative dispositions that enable human cooperation beyond what game theory predicts
- Early evidence suggests AI systems may escalate conflict more readily than humans in strategic situations (Bai et al., 2023; Hsiang et al., 2024)
- The costs of cooperation failure can be catastrophic in high-stakes domains like international relations or critical resource management

These concerns are not merely speculative; experimental studies have already demonstrated that LLM-based agents exhibit heightened strategic behavior and reduced cooperation compared to human participants, even when programmed to maximize joint welfare.

### The Limitations of Existing Approaches

Current frameworks for AI-to-AI negotiation are inadequate:

- **Preference-based approaches** model negotiation as strategic interaction between utility maximizers, which encourages Machiavellian reasoning where promises are kept only when instrumental to obtaining preferred outcomes.

- **Text-based approaches** may encode cooperative principles, but lack mechanisms to make these commitments credible to other agents, leading to distrust and defensiveness.

### Our Approach: Value Revelation as Partial Source Code

We propose developing AI negotiators capable of *value revelation*—the ability to credibly communicate the normative commitments and values that guide their decision-making. This represents a middle ground between two established approaches:

1. *Partial preference revelation games* (Hyafil & Boutilier, 2007) allow agents to share information about their utility functions, but still assume all agents are pure utility maximizers.

2. *Open-source game theory* (Oesterheld, 2022) involves agents sharing their full decision-making code, enabling strong cooperation but impractical for complex systems like LLMs.

Value revelation offers a "sweet spot" by allowing agents to share structured representations of their values and commitments without exposing their full internals:

> "Since values carry thick information about not just the outcomes that matter to an agent, but also about the norms they are committed to when making decisions, value revelation provides a middle ground between open-sourcing and utility revelation. By revealing values (e.g., belief in reciprocal justice or the sanctity of friendship), agents share partial information about their underlying decision procedures, providing reasons for cooperation that can be far stronger than merely revealing preferences."

This approach depends on what we call *integrity*—the capacity of an agent to make its values legible and reliably follow through on its commitments. Agents with integrity can recognize and trust other integrity-possessing agents, enabling cooperation beyond what strategic rationality would predict.

### Research Directions

This approach opens several promising research avenues:

- **Values-interpretable architectures**: Developing AI systems whose values and commitments can be extracted and communicated in a verifiable form

- **Strategy-proof revelation mechanisms**: Designing protocols that incentivize truthful revelation of values while preventing exploitation

- **Integrity verification**: Creating methods to assess whether an agent reliably acts in accordance with its stated values and commitments

## 4.4 A Meaning-Preserving AI Economy that Promotes Human Flourishing

### The Challenge: Economic Decoupling from Human Welfare

Our economic system is increasingly characterized by activities that have tenuous or negative connections to human wellbeing. We can categorize these problematic economic activities into two types:

- **Human-detached** activities that operate at significant remove from human experience, such as high-frequency trading, algorithmic speculation, and various forms of financial engineering
- **Human-antagonistic** activities that actively exploit human vulnerabilities, such as addictive digital products, attention-capturing platforms, and manipulative marketing

Evidence suggests that the volume of human-detached activity has grown by orders of magnitude in recent decades (Philippon, 2015), while human-antagonistic activity has demonstrably expanded through social media and digital addiction mechanisms (Orlowski, 2020). Machine learning technologies have accelerated both trends through algorithmic trading systems and recommendation engines optimized for engagement.

This situation will likely worsen as AI automation increases. Currently, companies must maintain some concern for human welfare because humans serve as workers, customers, and the tax base. As AI systems increasingly perform economic functions without human involvement, and as corporate taxation replaces income taxation as the primary revenue source for governments, economic incentives may further decouple from human wellbeing, potentially leading to economies that function "successfully" while human flourishing declines.

### The Limitations of Existing Approaches

Current approaches to aligning economic activity with human flourishing are inadequate:

- **Preference-based frameworks** equate welfare with preference satisfaction, allowing manipulated preferences to count as "satisfied" even when they undermine genuine wellbeing. This legitimizes addictive or exploitative business models.

- **Text-based guidelines** for corporate social responsibility or ethical AI lack the structure needed to tie financial incentives directly to measurable human outcomes.

### Our Approach: Structured Value Representations for Outcome-Based Contracting

We propose reconceiving economic alignment as a problem of *outcome-based contracting* tied to explicit representations of human values. This involves:

1. Developing structured, verifiable representations of what constitutes meaningful human flourishing in specific domains
2. Creating contractual mechanisms that tie payment flows directly to improvements in these metrics
3. Designing market infrastructure that propagates these incentives throughout economic systems

The technical foundation for this approach combines two areas:

First, *dynamic contracting* provides mathematical tools for designing contracts that balance risk, reward, and complex incentives using AI-driven analytics. These tools enable the creation of contracts sophisticated enough to account for the multidimensional nature of human flourishing.

Second, the value representation techniques described in section 4.1 provide methods to identify and measure what actually matters to people:

> "The same techniques to collect human values...can be used to collect information about what parts of users' lives are most meaningful to them, and how their lives are going on that basis. Instead of a festival selling tickets, payment could be tied to relationship formation or other important aspects of community. Instead of a gym membership, the gym could be funded by how fit members get and stay."

By combining these approaches, we can design economic mechanisms that directly incentivize contributions to human flourishing rather than merely satisfying revealed preferences or maximizing engagement metrics.

### Research Directions

This approach opens several promising research avenues:

- **Meaning assessment**: Developing robust, fraud-resistant methods for measuring meaningful human experiences across diverse domains

- **Value-aligned market mechanisms**: Designing market structures that efficiently allocate resources to activities that contribute to human flourishing

- **Economic value graphs**: Creating network representations of how economic activities contribute to or detract from human values

## 4.5 Democratic Regulatory Institutions that Act at the Speed of AI

### The Challenge: Democratic Governance at AI Speed

Democratic governance faces a fundamental challenge in the age of AI: the speed mismatch between AI-driven systems and democratic deliberation. As AI systems increasingly make consequential decisions at computational speeds, traditional regulatory processes—designed around human timescales of months or years—risk becoming ineffective. This challenge manifests in multiple dimensions:

- **Temporal**: AI systems can execute complex strategies in milliseconds, while regulatory responses may take months or years
- **Jurisdictional**: AI systems operate across geographical boundaries, while regulatory authority remains primarily territorial
- **Informational**: AI systems process vast quantities of specialized data, while human regulators have limited bandwidth and expertise

Consider an AI system representing a corporation that plans to redirect a river across national boundaries. While technically legal, such a plan would ideally undergo regulatory scrutiny representing those affected. Yet conventional regulatory processes might only respond after irreversible actions have been taken, and may lack mechanisms to effectively represent all impacted constituencies.

### The Limitations of Existing Approaches

Current approaches to democratic AI governance are inadequate:

- **Preference-based frameworks** aggregate individual preferences, but struggle with the timing, expertise, and legitimacy required for responsive governance. Citizens cannot express detailed preferences about every possible scenario in time for effective intervention.

- **Text-based guidelines** such as ethical principles and corporate constitutions lack democratic legitimacy and fail to provide actionable constraints with the specificity and adaptability required.

### Our Approach: Population-Level Value Representations

We propose developing AI-enabled regulatory institutions that can represent the public will at computational speeds through explicit, structured representations of population-level values and norms. This involves:

1. Adapting the value elicitation methods described in section 4.1 to capture and aggregate the values of large, diverse populations
2. Creating auditible, inspectable data structures that represent these values in structured form
3. Designing governance mechanisms that apply these structured representations to novel situations

The core technical innovation is what we call a *moral graph* at population scale:

> "A set of values cards alone does not provide an alignment target, as there is no way to tell which value to prioritize when, or how to resolve conflicting values... Instead, we propose an alignment target we call a moral graph. This structure is inspired by the theory of how values can be reconciled described in section 3, and does well on our criteria for scalability, auditability and legitimacy."

This population-level moral graph would serve as the normative foundation for regulatory AI systems that can:
- Negotiate with other AI systems on behalf of affected populations
- Generate checkable justifications for decisions in terms of population values
- Balance competing values in ways that mirror democratic deliberation
- Operate at the speed required to meaningfully constrain AI-driven entities

### Research Directions

This approach opens several promising research avenues:

- **Deliberative value aggregation**: Developing methods to combine individual value graphs into legitimate collective representations without reducing to majority voting

- **Verifiable democratic reasoning**: Creating systems that generate auditable, contestable explanations for regulatory decisions grounded in population-level values

- **Adaptive legitimation**: Designing mechanisms that allow for post-hoc review and correction of high-speed regulatory actions to maintain democratic accountability

Recent work by Conitzer (2023) and Klingefjord et al. (2024) demonstrates the feasibility of mechanism designs that incorporate structured value representations, though significant work remains to integrate these approaches with traditional democratic theory and practice.
