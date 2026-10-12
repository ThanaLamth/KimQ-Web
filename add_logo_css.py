import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    h = f.read()

# Insert logo-row CSS before media queries
logo_css = """
/* CLIENT LOGO ROW */
.logo-row{display:flex;align-items:center;gap:0;flex-wrap:wrap;border:1px solid var(--cloud-light);border-radius:12px;overflow:hidden;background:var(--white)}
.logo-cell{display:flex;align-items:center;justify-content:center;padding:1.25rem 2rem;flex:1;min-width:140px;border-right:1px solid var(--cloud-light);text-decoration:none;transition:background .15s;position:relative}
.logo-cell:last-child{border-right:none}
.logo-cell:hover{background:var(--ivory-medium)}
.logo-cell img{height:28px;width:auto;max-width:110px;object-fit:contain;filter:grayscale(100%);opacity:.65;transition:all .2s}
.logo-cell:hover img{filter:grayscale(0%);opacity:1}
.logo-fallback{display:none;font-family:var(--font-sans);font-size:.875rem;font-weight:700;color:var(--slate-light);letter-spacing:-.01em}
.logo-text{padding:1rem 1.75rem}
"""

insert_before = "@media(max-width:900px)"
if ".logo-row" not in h:
    h = h.replace(insert_before, logo_css + insert_before)
    print("logo CSS added")
else:
    print("logo CSS already present")

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(h)
print("done")
