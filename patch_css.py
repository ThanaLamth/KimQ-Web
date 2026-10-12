import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

# Primary button: slightly more generous, semibold
txt = txt.replace(
    ".bp{padding:.875rem 1.75rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-medium);text-decoration:none;display:inline-block;transition:var(--t-base)}",
    ".bp{padding:.9375rem 2rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-semibold);text-decoration:none;display:inline-block;transition:var(--t-base)}"
)
# Secondary button: same height, lighter weight
txt = txt.replace(
    ".bs{padding:.875rem 1.75rem;background:transparent;color:var(--slate-dark);border:var(--border-cloud);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-regular);text-decoration:none;display:inline-block;transition:var(--t-base)}",
    ".bs{padding:.9375rem 1.75rem;background:transparent;color:var(--slate-dark);border:var(--border-cloud);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-regular);text-decoration:none;display:inline-block;transition:var(--t-base)}"
)

# Add .ulink style (use case "Xem demo" links) if not present
if ".ulink" not in txt:
    insert_after = ".bs:hover{border-color:var(--slate-dark)}"
    new_rule = ".ulink{display:inline-flex;align-items:center;gap:var(--sp-1);margin-top:var(--sp-4);font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-medium);color:var(--slate-dark);text-decoration:none;border-bottom:1px solid var(--cloud-light);padding-bottom:1px;transition:var(--t-color)}.ulink:hover{border-color:var(--slate-dark)}"
    txt = txt.replace(insert_after, insert_after + new_rule)
    print("ulink added")
else:
    print("ulink already present")

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(txt)
print("p1_head.html patched")
