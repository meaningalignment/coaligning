# §1 Intro

The growing field of socio-technical alignment argues that beneficial AI outcomes require more than aligning individual systems with operators' intentions. Even perfectly intent-aligned AI systems will become misaligned if deployed within broader institutions—such as profit-driven corporations, competitive nation-states, or inadequately regulated markets—that conflict with global human flourishing.

Once we agree that it's important to **co-align artificial intelligence and institutions**, the key question becomes: **how** do we do that?

- Historically, this has been treated as a problem in **game theory** and **social choice**, where both human beings and AI agents are modeled as **rational choice**, **expected utility maximizers**, or as having **utility functions** or **preference relations**.

    In the classical paradigm—which includes techniques like inverse reinforcement learning—we find game-theoretic approaches to alignment, and preference aggregation approaches from social choice theory, where **preferences are first collected** from a large group of individuals, and a **social welfare function** is then constructed to aggregate them into a single decision or policy. The idea is that once you know each agent's utility function or ranked preferences, you can use formal methods to align collective action or optimize AI behavior accordingly.

    We cover some problems with preference and utility based approaches for FSA in the file "2-existing_toolkits.md".

- More recently, in practical applications, we're seeing a shift away from preference-based alignment toward **text-based** methods.

    In **single-user alignment**, preference models like RLHF (Reinforcement Learning from Human Feedback) are being replaced by **processes of self-critique**—such as **deliberative alignment**—where the model engages in a kind of reasoning or self-evaluation in response to a prompt.

    In **multi-agent or institutional contexts**, the basic unit is no longer the preference or utility function, but rather **text strings**: this includes considerations drawn from **Constitutional AI (CCAI)**, text-based **values profiles (**https://arxiv.org/abs/2503.15484**),** **model specs** upon which reasoning models deliberate (https://arxiv.org/abs/2412.16339) to train themselves.

    These strings are taken to encode **norms**, **intent**, or **values**, and are then processed by the model through self-critique or adherence routines. The hope is that models will exhibit behavior that conforms to or evaluates against these strings.

    Although these methods are more flexible and richer than preference-based ones, they suffer from their own set of limitations, covered in the second part of "2-existing_toolkits.md".

    Thus, despite their flexibility, **text strings and self-critique lack the rigor** required for high-stakes socio-technical alignment.


In "3-new_toolkit.md", we'll introduce four practical alignment techniques that go beyond preferences and free-form textual 'intents' to capture **deeper, more structured representations of human values and norms.**

## Paper Outline

Here, we introduce Full-Stack Alignment (FSA) to capture three core ideas:

- First, FSA recognizes that aligning AI systems and institutions must occur more-or-less simultaneously, across all layers of society, as misalignment at any single layer creates pressures that ripple through others.
- Second, FSA argues that socio-technical alignment challenges become tractable when we move beyond preference-based and prompt adherence frameworks and adopt a toolkit explicitly incorporating norms and values.
- Third, FSA outlines a clear strategy for research and societal transformation, systematically progressing from foundational research through expert consensus-building, targeted policy development, flagship implementations, and ultimately broad societal adoption.

<Outline rest of paper here>
