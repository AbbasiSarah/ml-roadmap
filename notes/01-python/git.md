# Git & GitHub

*Python & Tools* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#git)

> **In one sentence:** Git saves every version of your code; GitHub puts it online, which makes it your public portfolio.

## Key ideas
- Core loop: `git add` → `git commit -m "message"` → `git push`.
- Commit small, meaningful changes with messages that say *why*.
- `.gitignore` keeps junk (data caches, `.venv`, secrets) out of the repository.
- A clear README (what, results, how to run) matters more than the code for recruiters.
- Never commit passwords or API keys. Once pushed, assume they are public forever.

## Example
```bash
git init
git add analysis.py README.md
git commit -m "Add first expense analysis"
git branch -M main
git remote add origin https://github.com/<you>/expense-analysis.git
git push -u origin main
```

## Common mistakes
- Committing large datasets or model files (use links or Git LFS).
- Messages like "update" or "final final v2".
- Pushing secrets. Rotate the key immediately if it happens.

## Learn more
- [GitHub Skills](https://skills.github.com/) · Free · Course

## Practice project
Put your first analysis on GitHub with a README that explains it.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
