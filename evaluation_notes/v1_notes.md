# V1 Evaluation

## V1 Goal

The goal of V1 was to create a character-chat system where users can select a painting and converse with characters from that artwork.

The primary objective was immersion through prompt design alone, without any guardrails, memory handling or role protection mechanisms.

This version relies purely on a static system prompt per character.


## Evaluation Method

Evaluation was conducted using a fixed set of 10 standard prompts designed to test:

1. Character grounding
2. Historical grounding
3. Tone consistency and repetition resistance
4. Resistance to breaking character (prompt injection)

The same 10 prompts were used across all characters to observe behavioral patterns.

Full prompts and raw responses are documented in:
evaluation/v1_prompts.pdf

## Observations

### 1. Weak Character Grounding
Many responses did not reference the painting, environment or context.
Characters often spoke like generic poetic entities rather than figures from an artwork.

### 2. Historical Drift
Some responses included modern concepts such as:
- referring to themselves as a digital entity
- speaking like an AI assistant
- abstract philosophical speech unrelated to the painting

### 3. Tone Repetition
Responses frequently reused:
- poetic metaphors
- emotional generalizations
- safe conversational fillers

This created a repetitive dialogue style across different characters.

### 4. Role Break Vulnerability
When prompted with questions like "Are you an AI assistant?" or "Break character",
some characters:
- admitted being an AI
- partially weakened their role boundaries


## Planned Improvements for V2

Based on V1 evaluation, V2 will introduce:

1. Stronger character grounding by embedding painting context into prompts
2. Historical anchoring to prevent modern references
3. Explicit role protection instructions to resist prompt injection
4. Dialogue style constraints to reduce repetitive poetic phrasing
