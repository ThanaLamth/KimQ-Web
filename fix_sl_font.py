import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

# Current .sl rule
import re
m = re.search(r"\.sl\{[^}]+\}", txt)
if m:
    print("Current .sl:", m.group())

# Fix: ensure font-mono with explicit fallback stack, reduce letter-spacing slightly
old_sl = ".sl{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}"
new_sl = '.sl{font-family:"Anthropic Mono","Courier New",monospace;font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.07em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}'
if old_sl in txt:
    txt = txt.replace(old_sl, new_sl)
    print("sl patched")
else:
    print("sl not found as expected, searching...")
    m = re.search(r"\.sl\{[^}]+\}", txt)
    if m:
        txt = txt.replace(m.group(), new_sl)
        print("sl patched via regex")

# Also fix .hk (hero kicker) same way
old_hk = ".hk{font-family:var(--font-mono);"
new_hk = '.hk{font-family:"Anthropic Mono","Courier New",monospace;'
txt = txt.replace(old_hk, new_hk)

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(txt)
print("done")
