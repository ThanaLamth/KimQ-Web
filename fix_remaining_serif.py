import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    h = f.read()

before = h.count('font-family:var(--font-serif)')
h = h.replace('font-family:var(--font-serif)', 'font-family:var(--font-sans)')
after = h.count('font-family:var(--font-serif)')
print(f"p1_head: replaced {before-after} remaining font-serif -> font-sans")

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(h)
