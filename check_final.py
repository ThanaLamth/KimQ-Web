import sys, re
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html", "r", encoding="utf-8") as f:
    txt = f.read()
print("Em-dash in index.html:", txt.count("\u2014"))
m = re.search(r"\.bp\{padding:[^;]+", txt)
print("bp padding:", m.group() if m else "not found")
m2 = re.search(r"\.bs\{padding:[^;]+", txt)
print("bs padding:", m2.group() if m2 else "not found")
print("ulink present:", ".ulink" in txt)
print("No Zalo in hero:", "Zalo" not in txt[:txt.find("id=\"products\"")])
