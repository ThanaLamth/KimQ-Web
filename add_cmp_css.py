import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

# Insert comparison card CSS before the media query
insert_before = "@media(max-width:900px)"
new_css = """.cmpgrid{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-3)}
.cmpcard{border:var(--border);border-radius:var(--r-md);padding:var(--sp-6) var(--sp-5);background:var(--white)}
.cmp-new{border-color:var(--slate-dark);background:var(--slate-dark)}
.cmplabel{font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}
.cmp-new-label{color:rgba(250,249,245,.45)}
.cmplist{list-style:none;display:flex;flex-direction:column;gap:var(--sp-3)}
.cmplist li{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-body);padding-left:var(--sp-5);position:relative}
.cmplist li::before{content:"";position:absolute;left:0;top:.45em;width:10px;height:10px;border-radius:50%;background:var(--cloud-light)}
.cmp-new .cmplist li{color:rgba(250,249,245,.7)}
.cmp-new .cmplist li::before{background:rgba(250,249,245,.2)}
.flow-title{font-family:var(--font-sans);font-size:var(--detail-l);font-weight:var(--fw-semibold);letter-spacing:var(--ls-snug);margin-bottom:var(--sp-6);color:var(--slate-dark)}
"""
txt = txt.replace(insert_before, new_css + insert_before)

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(txt)
print("Comparison CSS added")

# Verify
print("cmpgrid present:", ".cmpgrid" in txt)
print("flow-title present:", ".flow-title" in txt)
