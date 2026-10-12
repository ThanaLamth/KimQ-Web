import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    h = f.read()

mockup_css = """
/* HERO SPLIT */
.hero-split{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-12);align-items:center}
.hero-left{}
/* HERO MOCKUP */
.hero-mockup{background:var(--white);border:1px solid var(--cloud-light);border-radius:16px;overflow:hidden;box-shadow:0 16px 64px rgba(20,20,19,.1),0 4px 16px rgba(20,20,19,.06)}
.hm-bar{display:flex;align-items:center;gap:6px;padding:.625rem 1rem;background:var(--ivory-dark);border-bottom:1px solid var(--cloud-light)}
.hm-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.hm-dot.r{background:#ff5f57}.hm-dot.y{background:#febc2e}.hm-dot.g{background:#28c840}
.hm-title{font-family:var(--font-mono);font-size:10px;font-weight:500;color:var(--slate-light);margin-left:4px;letter-spacing:.04em}
.hm-body{padding:1.25rem}
.hm-metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;margin-bottom:1rem}
.hm-metric{background:var(--ivory-light);border:1px solid var(--cloud-light);border-radius:8px;padding:.75rem .625rem}
.hm-val{font-family:var(--font-sans);font-size:.9375rem;font-weight:700;color:var(--slate-dark);letter-spacing:-.02em;line-height:1}
.hm-lbl{font-family:var(--font-sans);font-size:10px;color:var(--slate-light);margin-top:3px;line-height:1.3}
.hm-delta{font-family:var(--font-mono);font-size:10px;font-weight:600;margin-top:4px}
.hm-delta.up{color:#c0392b}.hm-delta.ok{color:#27ae60}
.hm-chart-wrap{margin-bottom:.875rem}
.hm-chart-label{font-family:var(--font-mono);font-size:10px;color:var(--slate-light);margin-bottom:.375rem;letter-spacing:.04em}
.hm-sparkline{display:block}
.hm-decisions{border-top:1px solid var(--ivory-dark);padding-top:.875rem;display:flex;flex-direction:column;gap:.5rem}
.hm-dec-label{font-family:var(--font-mono);font-size:10px;font-weight:600;color:var(--slate-light);text-transform:uppercase;letter-spacing:.06em;margin-bottom:.25rem}
.hm-dec{display:flex;align-items:center;gap:.5rem;font-family:var(--font-sans);font-size:.8125rem;color:var(--slate-dark);line-height:1.4}
.hm-badge{flex-shrink:0;padding:.15rem .5rem;border-radius:4px;font-family:var(--font-mono);font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.badge-rev{background:#fef9ee;color:#92520b}
.badge-auto{background:#f0faf3;color:#4a7c59}
"""

insert_before = "/* CLIENT LOGO ROW */"
if ".hero-split" not in h:
    h = h.replace(insert_before, mockup_css + insert_before)
    print("hero mockup CSS added")

# Fix hero section to allow split layout
old_hi = ".hi{position:relative;z-index:1;padding:var(--sp-12) 0}"
new_hi = ".hi{position:relative;z-index:1;padding:var(--sp-12) 0}.hero-right{opacity:0;animation:fadeInRight .7s .3s ease forwards}@keyframes fadeInRight{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}"
if ".hero-right" not in h:
    h = h.replace(old_hi, new_hi)
    print("hero-right animation added")

# Update media query to stack hero on mobile
old_media = "@media(max-width:900px){:root{--section-gap:5rem}.con{padding:0 1.25rem}.nlinks{display:none}.sgrid,.pgrid,.tgrid,.rg,.fg{grid-template-columns:1fr 1fr}.split,.up.act,.mg{grid-template-columns:1fr}.tlr{grid-template-columns:80px 1fr}.tls{display:none}}"
new_media = "@media(max-width:900px){:root{--section-gap:5rem}.con{padding:0 1.25rem}.nlinks{display:none}.sgrid,.pgrid,.tgrid,.rg,.fg{grid-template-columns:1fr 1fr}.split,.up.act,.mg,.hero-split,.cmpgrid{grid-template-columns:1fr}.hero-right{display:none}.tlr{grid-template-columns:80px 1fr}.tls{display:none}.logo-row{flex-wrap:wrap}.logo-cell{flex:0 0 50%;border-bottom:1px solid var(--cloud-light)}}"
h = h.replace(old_media, new_media)

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(h)
print("done")
