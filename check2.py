import sys
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html", "r", encoding="utf-8") as f:
    txt = f.read()
print("Em-dash:", txt.count("\u2014"))
print("cmpgrid:", "cmpgrid" in txt)
print("flow-title:", "flow-title" in txt)
print("ctbl card border:", "border:var(--border);border-radius" in txt)
print("sh clamp:", "clamp(1.375rem" in txt)
print("Anthropic Mono explicit:", '"Anthropic Mono"' in txt)
