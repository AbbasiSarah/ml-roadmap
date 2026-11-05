# AI agents

*Choose a Specialisation › LLMs & Generative AI* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#agents)

> **In one sentence:** An AI agent is an LLM in a loop that plans, calls tools (search, code, APIs) and acts until a task is done.

## Key ideas
- Loop: think → choose a tool → read the result → repeat → final answer.
- Tools are functions with clear names, descriptions and input schemas.
- Guardrails: limit steps, check tool inputs, and require human approval for risky actions.
- Log every step so you can debug what the agent did.
- Start with one or two tools; most failures come from vague tool descriptions.

## Example
```python
TOOLS = {"calculator": lambda expr: str(eval(expr, {"__builtins__": {}})),   # demo only
         "search_notes": lambda q: "Exams start on 1 June."}

def run_agent(llm, task, max_steps=5):
    history = [f"Task: {task}"]
    for _ in range(max_steps):
        action = llm("\n".join(history) + "\nReply TOOL:<name>:<input> or FINAL:<answer>")
        if action.startswith("FINAL:"):
            return action[6:]
        _, name, arg = action.split(":", 2)
        history.append(f"{name}({arg}) -> {TOOLS[name](arg)}")
```

## Common mistakes
- Giving agents powerful tools (payments, deleting files) without approval steps.
- No step limit, so it loops forever and costs money.

## Learn more
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) · Free · Course

## Practice project
An agent that searches the web and writes a short research summary with sources.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
