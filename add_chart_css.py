import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    h = f.read()

chart_css = """
/* MINI CHARTS */
.mini-chart{margin-top:var(--sp-5);padding:var(--sp-4);background:var(--ivory-light);border:1px solid var(--ivory-dark);border-radius:8px}
"""

if ".mini-chart" not in h:
    h = h.replace("/* CLIENT LOGO ROW */", chart_css + "/* CLIENT LOGO ROW */")
    print("chart CSS added")

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(h)
print("done")
