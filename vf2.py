import sys, re
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html","r",encoding="utf-8") as f: t=f.read()

m = re.search(r"\.sh\{[^}]+\}", t)
print("sh rule:", m.group() if m else "MISSING!")

m2 = re.search(r"\.sl\{[^}]+\}", t)
print("sl rule:", m2.group() if m2 else "MISSING!")

print("Arial in mono stacks:", t.count('"Anthropic Mono",Arial'))
print("Courier New in mono:", t.count('"Courier New"'))
print("font-weight:600 count:", t.count("font-weight:600"))
print("em-dash:", t.count("\u2014"))
