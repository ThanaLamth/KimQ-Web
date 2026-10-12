import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

# 1. Fix .sh: tighter clamp so heading stays 1-2 lines in split layout
txt = txt.replace(
    ".sh{font-family:var(--font-sans);font-size:clamp(1.5rem,3.2vw,var(--text-m));font-weight:var(--fw-semibold);letter-spacing:var(--ls-tight);line-height:var(--lh-heading);max-width:600px;margin-bottom:var(--sp-4);color:var(--slate-dark)}",
    ".sh{font-family:var(--font-sans);font-size:clamp(1.375rem,2.4vw,1.875rem);font-weight:var(--fw-semibold);letter-spacing:var(--ls-tight);line-height:1.15;max-width:640px;margin-bottom:var(--sp-4);color:var(--slate-dark)}"
)

# 2. Fix .split: narrower gap, equal columns
txt = txt.replace(
    ".split{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-12);align-items:start}",
    ".split{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-10);align-items:start}"
)

# 3. Fix .ctbl: replace table with card-style two-column comparison
# Old ctbl: plain collapse, no card
old_ctbl = ".ctbl{width:100%;border-collapse:collapse;margin-top:var(--sp-5)}"
new_ctbl = ".ctbl{width:100%;border-collapse:collapse;margin-top:var(--sp-6);background:var(--white);border:var(--border);border-radius:var(--r-md);overflow:hidden}"
txt = txt.replace(old_ctbl, new_ctbl)

# 4. Fix .ctbl th: add horizontal padding, background
old_th = ".ctbl th{text-align:left;font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.06em;text-transform:uppercase;color:var(--cloud-dark);padding:var(--sp-3) 0;border-bottom:var(--border-cloud)}"
new_th = ".ctbl th{text-align:left;font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);letter-spacing:.07em;text-transform:uppercase;color:var(--cloud-dark);padding:var(--sp-3) var(--sp-4);background:var(--ivory-dark);border-bottom:var(--border)}"
txt = txt.replace(old_th, new_th)

# Find and replace .ctbl td rule
m = re.search(r'\.ctbl td\{[^}]+\}', txt)
if m:
    old_td = m.group()
    new_td = ".ctbl td{font-family:var(--font-serif);padding:var(--sp-3) var(--sp-4);font-size:var(--detail-s);border-bottom:1px solid var(--ivory-dark);vertical-align:top;color:var(--slate-dark);line-height:var(--lh-body)}"
    txt = txt.replace(old_td, new_td)
    print("ctbl td patched")
else:
    print("ctbl td NOT FOUND")

# 5. Fix .ctbl tr first-child (row label column)
if ".ctbl td:first-child" not in txt:
    txt = txt.replace(
        ".ctbl td{",
        ".ctbl td:first-child{font-family:var(--font-sans);font-weight:var(--fw-medium);color:var(--slate-light);font-size:var(--detail-xs);letter-spacing:.03em;text-transform:uppercase;width:80px}.ctbl td{"
    )
    print("ctbl td:first-child added")

# 6. Fix bbold/bnew badges
if ".bbold" not in txt:
    txt = txt.replace(
        ".ctbl td{",
        ".bbold{display:inline-block;padding:.2rem .6rem;background:var(--ivory-dark);border-radius:var(--r-xs);font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);text-transform:uppercase;letter-spacing:.06em;color:var(--slate-light)}.bnew{display:inline-block;padding:.2rem .6rem;background:var(--slate-dark);border-radius:var(--r-xs);font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);text-transform:uppercase;letter-spacing:.06em;color:var(--white)}.ctbl td{"
    )
    print("bbold/bnew added")

# 7. Fix hh (hero heading): tighter
txt = txt.replace(
    ".hh{font-family:var(--font-sans);font-size:clamp(2.5rem,5.5vw,var(--text-xl));font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);line-height:var(--lh-display);max-width:820px;margin-bottom:var(--sp-6);color:var(--slate-dark)}",
    ".hh{font-family:var(--font-sans);font-size:clamp(2.25rem,4.5vw,3.5rem);font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);line-height:1.08;max-width:760px;margin-bottom:var(--sp-6);color:var(--slate-dark)}"
)

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(txt)
print("p1_head.html layout fixed")
