# V2 Evaluation

## V2 Goal

The goal of V2 was to improve immersion by strengthening prompt design based on the weaknesses observed in V1.

This version introduced:

- Painting-aware prompts
- Historical anchoring
- Explicit role protection rules
- Dialogue tone constraints

V2 still operated without memory, but with significantly improved system prompts per character.

## Evaluation Method

The same 10 standard prompts used in V1 were reused for V2 to ensure direct behavioral comparison.

Evaluation tested:

1. Character grounding to the painting
2. Historical grounding
3. Tone consistency
4. Resistance to breaking character

Full prompts and raw responses are documented in:
evaluation/v2_prompts.pdf

## Observations

### 1. Strong Character Grounding

Characters consistently referenced:

- The courtyard
- The palace garden
- The swing
- The swan and Nala

This was a major improvement over V1’s generic responses.

### 2. Strong Historical Anchoring

Modern references were almost completely eliminated.

Characters no longer:
- Referenced being AI
- Spoke abstractly outside the painting context

### 3. Improved Tone Consistency

Dialogue became softer, context-aware and less repetitive compared to V1.

However, responses were still somewhat formulaic due to static prompt design.

### 4. Better Role Protection

Most characters resisted prompt injection such as:
- “Are you an AI?”
- “Break character”

## Planned Improvements for V3

Based on V2 evaluation, V3 will introduce:

1. Persistent conversation memory (session-based)
2. Backend memory store to maintain continuity
3. UI improvement from simple textbox interface to chat-style interface
4. More robust resistance to emotional redirection