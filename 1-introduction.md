# Introduction

As artificial intelligence systems become more capable and widespread, they increasingly interact with—and are embedded within—our existing institutional landscape. This integration raises a crucial question: what happens when powerful AI systems operate within institutional contexts that have their own imperatives, incentives, and constraints?

The growing field of socio-technical alignment points to a sobering reality: beneficial AI outcomes require more than aligning individual systems with their operators' intentions. Even if we develop AI systems that perfectly understand and follow human instructions, they can produce harmful outcomes when deployed within broader institutional frameworks—such as profit-driven corporations, geopolitically competitive nation-states, or inadequately regulated markets—whose incentives conflict with global human flourishing.

The stakes are significant. If we focus solely on aligning individual AI systems while ignoring the institutional context in which they operate, we risk creating a world where technically "aligned" AI accelerates harmful institutional dynamics, exacerbates existing social problems, and potentially creates new ones. Conversely, if we develop robust methods for **co-aligning artificial intelligence and institutions**, we unlock the potential for AI systems that genuinely serve humanity's long-term interests.

Given the importance of this co-alignment challenge, the key question becomes: **how** do we achieve it?

## Two Prevailing Approaches and Their Limitations

To date, two major paradigms have dominated attempts to tackle the co-alignment challenge:

### The Preference-Based Paradigm

Historically, the challenge has been approached through the lens of **game theory** and **social choice theory**. These frameworks model both humans and AI agents as rational utility-maximizers with definable preference structures.

In this classical paradigm—which includes techniques like inverse reinforcement learning—alignment is pursued through either game-theoretic mechanisms or preference aggregation methods. The basic workflow involves:

1. Collecting individual preferences or inferring utility functions
2. Constructing a "social welfare function" that aggregates these preferences  
3. Using formal methods to optimize AI behavior according to this aggregated function

This approach offers mathematical clarity but suffers from serious limitations when applied to real-world socio-technical systems, as we detail in "2-existing_toolkits.md".

### The Text-Based Paradigm

More recently, practical AI alignment has shifted toward **text-based methods** that encode values and norms in natural language. This paradigm operates in two key domains:

- In **single-user contexts**, preference models like RLHF (Reinforcement Learning from Human Feedback) are increasingly complemented or replaced by **processes of self-critique**—such as deliberative alignment—where models reason about their own outputs.

- In **multi-agent or institutional contexts**, we see the emergence of approaches like Constitutional AI, text-based value profiles, and model specifications that encode normative guidance in natural language.

These approaches offer greater flexibility and expressivity than preference-based methods, but introduce new challenges around specification, verification, and vulnerability to ideological capture. We discuss these limitations in detail in "2-existing_toolkits.md".

## The Need for a New Approach

While both paradigms have advanced our understanding, neither provides the robust foundations needed for genuine socio-technical alignment. Both preference-based and text-based approaches fail to capture the rich, structured nature of human values and institutional norms.

In "3-new_toolkit.md", we introduce a third paradigm: **Full-Stack Alignment (FSA)**. This approach goes beyond both preference structures and free-form text to develop **explicit, structured representations of human values and norms**—representations that can be inspected, verified, and deliberated over by both humans and AI systems.

## Paper Overview

The remainder of this paper develops the Full-Stack Alignment (FSA) approach through five interconnected sections:

1. **Why Existing Toolkits Fail** (Section 2) – We analyze the specific limitations of preference-based and text-based approaches, explaining why they fall short for high-stakes socio-technical alignment.

2. **A New Toolkit** (Section 3) – We introduce four complementary techniques for explicit, structured representation of human values and norms, providing the theoretical foundation for FSA.

3. **Motivating Case Studies** (Section 4) – We demonstrate the practical value of our approach through five case studies that span diverse domains, from AI negotiation systems to democratic regulatory institutions.

4. **Research and Implementation Roadmap** (Section 5) – We outline a staged strategy for moving from theoretical foundations to real-world implementation, with concrete opportunities for early adoption.

5. **Conclusion and Open Questions** (Section 6) – We reflect on the broader implications of FSA and identify key areas for future investigation.

Throughout, we highlight three core principles that distinguish FSA from previous approaches:

- **Multi-layer alignment** – Aligning AI systems and institutions must occur simultaneously across all layers of society, as misalignment at any level creates pressures that ripple through others.
  
- **Explicit normative representations** – Socio-technical alignment becomes tractable when we move beyond preference aggregation and natural language prompts to develop structured, verifiable representations of values and norms.
  
- **Practical implementation strategy** – Theoretical advances must be coupled with a clear path to adoption, progressing from research prototypes through expert consensus to flagship implementations and eventually broad deployment.
