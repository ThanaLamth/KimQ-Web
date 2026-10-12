import sys, re
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html","r",encoding="utf-8") as f: t=f.read()
with open("tokens.css","r",encoding="utf-8") as f: tok=f.read()

print("=== tokens.css ===")
for m in re.finditer(r"--font-[a-z]+:[^;]+", tok): print(" ", m.group())

print("\n=== index.html: Arial occurrences (should be 0 in font stacks) ===")
arial = [m.start() for m in re.finditer("Arial", t)]
for pos in arial:
    print(" ", repr(t[max(0,pos-40):pos+40]))

print("\n=== sh weight (should be 600) ===")
m = re.search(r"\.sh\{[^}]+\}", t)
if m:
    fw = re.search(r"font-weight:[^;]+", m.group())
    print(" ", fw.group() if fw else "NOT FOUND")

print("\n=== mono explicit count in index.html ===")
print(" ", t.count('"Anthropic Mono","Courier New",monospace'))
