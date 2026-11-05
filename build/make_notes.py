import yaml, sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from notes_a import NOTES as A
from notes_b import NOTES as B
NOTES = {**A, **B}
ROOT = Path(__file__).resolve().parents[1]
road = yaml.safe_load(open("/home/claude/site2/_data/roadmap.yml"))
SITE = "https://abbasisarah.github.io/roadmap/"
STAGE_PROJECT = {"python": "01-expense-analyser", "math": "02-gradient-descent", "data": "03-data-cleaning",
                 "classic-ml": "04-model-comparison", "deep-learning": "05-neural-net-from-scratch",
                 "specialise": "06-forecasting-and-rag", "deploy": "07-model-api", "career": "08-portfolio-readme"}
index, links = [], []
def lang(code):
    if code.lstrip().startswith(("SELECT", "WITH")): return "sql"
    if code.lstrip().startswith(("git ", "pip ")): return "bash"
    if code.lstrip().startswith(("##", "Post template", "|")): return "markdown"
    return "python"
def leaves(node, trail):
    for c in node.get("children", []):
        if c.get("children"): yield from leaves(c, trail + [c["title"]])
        else: yield c, trail
for i, stage in enumerate(road, 1):
    folder = f"{i:02d}-{stage['id']}"
    (ROOT / "notes" / folder).mkdir(parents=True, exist_ok=True)
    rows = []
    for t, trail in leaves(stage, [stage["title"]]):
        n = NOTES[t["id"]]
        res = "\n".join(f"- [{r['name']}]({r['url']}) · {'Free' if r.get('cost') != 'paid' else 'Paid'} · {r.get('kind','')}" for r in t.get("resources", []))
        for r in t.get("resources", []): links.append((stage["title"], t["title"], r))
        md = f"""# {t['title']}

*{' › '.join(trail)}* · [Open in the interactive roadmap]({SITE}#{t['id']})

> **In one sentence:** {n['one']}

## Key ideas
{chr(10).join('- ' + x for x in n['ideas'])}

## Example
```{lang(n['code'])}
{n['code']}
```

## Common mistakes
{chr(10).join('- ' + x for x in n['mistakes'])}

## Learn more
{res}

## Practice project
{t.get('project','')}{f"{chr(10)}{chr(10)}Example: {t['example']}" if t.get('example') else ''}

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
"""
        (ROOT / "notes" / folder / f"{t['id']}.md").write_text(md)
        rows.append(f"[{t['title']}](notes/{folder}/{t['id']}.md){' 🔥' if t.get('trending') else ''}")
    proj = STAGE_PROJECT[stage["id"]]
    index.append(f"| {i} | **{stage['title']}** ({stage['weeks']}) | {' · '.join(rows)} | [{proj}](projects/{proj}) |")
(ROOT / "build" / "index_rows.md").write_text("\n".join(index))
seen, out = set(), []
for st, top, r in links:
    if r["url"] in seen: continue
    seen.add(r["url"]); out.append(f"| {st} | {top} | [{r['name']}]({r['url']}) | {'Free' if r.get('cost') != 'paid' else 'Paid'} | {r.get('kind','')} |")
(ROOT / "RESOURCES.md").write_text("# Every resource in the roadmap\n\nAll the courses, books, videos and docs linked from the [SheCodesAI ML Roadmap](" + SITE + "), in one list.\n\n| Stage | Topic | Resource | Cost | Type |\n|---|---|---|---|---|\n" + "\n".join(out) + "\n")
print(len(NOTES), "notes;", len(out), "unique resources")
