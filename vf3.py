import sys, re
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html","r",encoding="utf-8") as f: t=f.read()
with open("tokens.css","r",encoding="utf-8") as f: tok=f.read()

print("=== Font variables in tokens.css ===")
for m in re.finditer(r"--font-[a-z]+:[^;]+", tok): print(" ", m.group())

print("\n=== @font-face blocks remaining (should be 0) ===")
print(" ", tok.count("@font-face"))

print("\n=== Google Fonts in index.html ===")
print(" googleapis:", "fonts.googleapis.com" in t)
print(" Be Vietnam Pro:", "Be Vietnam Pro" in t)
print(" JetBrains Mono:", "JetBrains Mono" in t)

print("\n=== Anthropic font refs remaining ===")
print(" Anthropic Sans:", t.count("Anthropic Sans"))
print(" Anthropic Serif:", t.count("Anthropic Serif"))
print(" Anthropic Mono:", t.count("Anthropic Mono"))

print("\n=== Body text (should be font-sans not font-serif) ===")
serif_body = t.count('font-family:var(--font-serif)')
sans_body = t.count('font-family:var(--font-sans)')
print(f" font-serif uses: {serif_body}")
print(f" font-sans uses: {sans_body}")

print("\n=== .sh rule ===")
m = re.search(r"\.sh\{[^}]+\}", t)
print(" ", m.group() if m else "MISSING!")

print("\n=== Button .bp ===")
m = re.search(r"\.bp\{[^}]+\}", t)
print(" ", m.group() if m else "MISSING!")
