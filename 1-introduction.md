# Introduction

The growing field of socio-technical alignment argues that beneficial AI outcomes require more than aligning individual systems with operators' intentions. Even perfectly intent-aligned AI systems will become misaligned if deployed within broader institutions—such as profit-driven corporations, competitive nation-states, or inadequately regulated markets—that conflict with global human flourishing.

This fundamental observation—that AI alignment cannot be solved by focusing on single systems in a vacuum—necessitates a broader conception of alignment that encompasses both AI systems and the institutional contexts in which they operate. Without such co-alignment, we risk deploying technically "intent-aligned" systems that nevertheless accelerate institutional dynamics at odds with human values, resulting in emergent misalignment at scale.

Once we agree that it is important to **co-align artificial intelligence and institutions**, the key question becomes **how** to achieve this integration.

Historically, this has been treated as a problem in **game theory** and **social choice**, where both human beings and AI agents are modeled as **rational choice**, **expected utility maximizers**, or as having **utility functions** or **preference relations**.

In the classical paradigm—which includes techniques like inverse reinforcement learning—we find game-theoretic approaches to alignment, and preference aggregation approaches from social choice theory, where **preferences are first collected** from a large group of individuals, and a **social welfare function** is then constructed to aggregate them into a single decision or policy. The idea is that once you know each agent's utility function or ranked preferences, you can use formal methods to align collective action or optimize AI behavior accordingly.

We cover the inadequacies of preference and utility-based approaches for co-alignment in "2-existing_toolkits.md", detailing six core limitations: unstable preferences, manipulability of revealed preference, inadequacy for sophisticated democracy, thin accounts of cooperation, blindness to higher goods, and poor fit with human nature.

More recently, in practical applications, we're seeing a shift away from preference-based alignment toward **text-based methods**. In **single-user alignment**, preference models like RLHF (Reinforcement Learning from Human Feedback) are being replaced by **processes of self-critique**—such as **deliberative alignment**—where the model engages in a kind of reasoning or self-evaluation in response to a prompt.

In **multi-agent or institutional contexts**, the basic unit is no longer the preference or utility function, but rather **text strings**: this includes considerations drawn from **Constitutional AI (CCAI)**, text-based **values profiles** (https://arxiv.org/abs/2503.15484), **model specs** upon which reasoning models deliberate (https://arxiv.org/abs/2412.16339) to train themselves. These strings are taken to encode **norms**, **intent**, or **values**, and are then processed by the model through self-critique or adherence routines.

Although these methods are more flexible and richer than preference-based ones, they suffer from their own set of limitations, covered in "2-existing_toolkits.md": specification fragility, verification difficulties, and vulnerability to societal pressure and ideological pollution.

Thus, despite their flexibility, **text strings and self-critique lack the rigor** required for high-stakes socio-technical alignment. Neither preference/utility nor text-based paradigms offer the necessary foundations for robust socio-technical alignment.

In "3-new_toolkit.md", we introduce four practical alignment techniques that go beyond preferences and free-form textual 'intents' to capture **deeper, more structured representations of human values and norms**—representations that can be inspected, verified, and deliberated over within a framework we term **Full-Stack Alignment (FSA)**.

We coin **Full-Stack Alignment (FSA)** to capture three core ideas:

1. Aligning AI systems and institutions must occur simultaneously across the stack; misalignment at one layer (e.g. geopolitical) creates pressure elsewhere.
2. Migration from preference/utility frameworks to explicit norm-and-value models makes many alignment challenges tractable.
3. A staged strategy is required—from foundational theory through expert consensus, pilot institutions, and eventual societal adoption.

The paper is structured as follows:

**Sections 2.1 and 2.2** analyze why existing toolkits fail, examining the limitations of both preference/utility frameworks and prompt-based alignment. We show why neither meets the demands of high-stakes alignment.

**Section 3** introduces a richer toolkit centered on explicit, structured representations of human norms and values, surveying four complementary techniques: well-defined attractor points in training or deliberation space, formally specified and verifiable text, programmatic specifications, and utility functions enriched by deeper investigation of the normative landscape.

**Sections 4.1–4.5** present five case studies demonstrating how these techniques can address previously intractable alignment challenges, from AI agents that steward user values to democratic regulatory institutions that act at the speed of AI.

**Section 5** details a research and implementation roadmap toward institutions and AI systems that co-evolve for global human flourishing, progressing from fundamental research through expert consensus to flagship implementations.

We close in **Section 6** with reflections on open questions, including interfaces with pluralistic societies, resistance to manipulation, and governance structures for maintaining norm and value representations over time.
