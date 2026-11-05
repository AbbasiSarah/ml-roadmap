# Prompt engineering

*Choose a Specialisation › LLMs & Generative AI* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#prompting)

> **In one sentence:** Prompt engineering means giving an LLM clear instructions, context and examples so it does the task reliably.

## Key ideas
- Be specific: role, task, audience, format and length.
- Give examples of good output (few-shot).
- Ask for structured output (JSON, a table) when code will read it.
- Break big tasks into steps; ask the model to check its own answer.
- Test prompts on many inputs, not one lucky example.

## Example
```python
prompt = """You are a meeting assistant.
Turn the notes below into a task list.
Format: one line per task as "- [owner] task (due date or 'no date')".
Only include tasks actually agreed in the meeting.

Notes:
{notes}"""
```

## Common mistakes
- Vague prompts ("make it better").
- Trusting outputs without checking facts; LLMs can invent things.

## Learn more
- [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/) · Free · Course

## Practice project
Build a prompt that turns messy meeting notes into a clean task list.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
