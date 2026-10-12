import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

# .sh is missing - inject it after .sl rule
# Find .sl rule and insert .sh right after
sl_match = re.search(r'(\.sl\{[^}]+\})', txt)
if sl_match:
    sl_rule = sl_match.group(1)
    sh_rule = '\n.sh{font-family:"Anthropic Sans",Arial,sans-serif;font-size:clamp(1.25rem,2.2vw,1.75rem);font-weight:600;letter-spacing:-0.02em;line-height:1.15;max-width:640px;margin-bottom:var(--sp-4);color:var(--slate-dark)}'
    if '.sh{' not in txt:
        txt = txt.replace(sl_rule, sl_rule + sh_rule)
        print("sh rule inserted after .sl")
    else:
        print("sh already present - ok")
else:
    print("ERROR: .sl not found either")

# Also fix .sp if missing
if '.sp{' not in txt:
    sp_rule = '\n.sp{font-family:"Anthropic Serif",Georgia,serif;font-size:var(--para-s);color:var(--slate-light);max-width:480px;line-height:var(--lh-loose);margin-bottom:var(--sp-9)}'
    txt = txt.replace('\n.sh{', sp_rule + '\n.sh{')
    print("sp rule also re-added")

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(txt)

# Verify
with open("p1_head.html", "r", encoding="utf-8") as f:
    check = f.read()
print(".sh present:", ".sh{" in check)
print(".sp present:", ".sp{" in check)
m = re.search(r"\.sh\{[^}]+\}", check)
if m: print("sh rule:", m.group())
