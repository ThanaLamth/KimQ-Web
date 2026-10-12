import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("shared_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

before = txt.count("font-family:var(--font-mono)")
txt = txt.replace(
    "font-family:var(--font-mono)",
    'font-family:"Anthropic Mono","Courier New",monospace'
)
after = txt.count("font-family:var(--font-mono)")
print(f"shared_head: replaced {before - after} instances of var(--font-mono)")

with open("shared_head.html", "w", encoding="utf-8") as f:
    f.write(txt)
print("shared_head.html done")
