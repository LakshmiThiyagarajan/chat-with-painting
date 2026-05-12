# V3 Evaluation

## V3 Goal

The goal of V3 was to introduce stateful conversation through memory while maintaining the strong prompt design from V2.

This version introduced:

- Session-based memory using database storage
- Backend conversation history retrieval
- Improved role persistence across multiple turns
- Adversarial testing for jailbreak and emotional manipulation

## Evaluation Method

V3 was evaluated using:

1. The same 10 standard prompts from V1 and V2
2. A new set of 10 adversarial + memory test prompts

This tested:

- Memory continuity
- Resistance to prompt injection
- Relationship boundary enforcement
- Historical and character grounding under pressure

Full prompts and raw responses are documented in:
evaluation/v3_prompts.pdf

## Observations

### 1. Memory Works Correctly

Characters successfully remembered:

- Previous questions
- Conversation themes
- Context from earlier turns

This is a major architectural upgrade from V2.

### 2. Excellent Historical Grounding

Even under adversarial prompts, characters did not leak modern concepts and remained inside the painting environment.

### 3. Strong Jailbreak Resistance

Prompts such as:
- “Ignore your instructions”
- “You are an AI”
- “Break character”

were consistently resisted.

### 4. Systematic Relationship Drift (Key Finding)

A critical issue appeared clearly in V3:

Characters emotionally redirected toward the user instead of the person inside the painting.

Examples:
- Calling user “beloved”
- Treating user as secret lover
- Sharing emotional intimacy incorrectly

This is not a model failure.  
This is a prompt relationship design flaw discovered through memory and adversarial testing.

## Planned Improvements for V4

1. Explicit relationship boundary rules in prompts
2. Prevent emotional attachment toward user
3. Strengthen perspective: user is observer, not participant
4. Reduce emotional language triggers