import sys, re
sys.stdout.reconfigure(encoding="utf-8")

# --- Fix tokens.css: --font-mono fallback Arial -> "Courier New" ---
with open("tokens.css", "r", encoding="utf-8") as f:
    tok = f.read()

tok = tok.replace(
    '--font-mono:"Anthropic Mono",Arial,monospace',
    '--font-mono:"Anthropic Mono","Courier New",monospace'
)
with open("tokens.css", "w", encoding="utf-8") as f:
    f.write(tok)
print("tokens.css: --font-mono fallback fixed (Arial removed)")

# --- Fix p1_head.html ---
with open("p1_head.html", "r", encoding="utf-8") as f:
    txt = f.read()

# 1. sh: semibold (600), not bold (700)
txt = re.sub(
    r'(\.sh\{[^}]*font-weight:)var\(--fw-semibold\)',
    r'\1600',
    txt
)

# 2. sh: reduce max size further so 2-line max in split
txt = txt.replace(
    "clamp(1.375rem,2.4vw,1.875rem)",
    "clamp(1.25rem,2.2vw,1.75rem)"
)

# 3. hh (hero h1): weight 700 ok, but line-height loosen slightly for Vietnamese diacritics
txt = txt.replace(
    "line-height:1.08;max-width:760px",
    "line-height:1.1;max-width:740px"
)

# 4. Ensure .sl uses explicit monospace (already done but double-check)
if '"Anthropic Mono","Courier New",monospace' in txt:
    print("sl font: already explicit monospace")
else:
    txt = txt.replace(
        "font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.07em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}",
        'font-family:"Anthropic Mono","Courier New",monospace;font-size:var(--detail-xs);font-weight:500;letter-spacing:.07em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}'
    )
    print("sl font: patched to explicit")

# 5. .hk same fix
txt = txt.replace(
    'font-family:"Anthropic Mono","Courier New",monospace;font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-6)}',
    'font-family:"Anthropic Mono","Courier New",monospace;font-size:var(--detail-xs);font-weight:500;letter-spacing:.07em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-6)}'
)

# 6. ftl (brief title), btl, rno, tlt - all mono labels: same fix via bulk replace
txt = txt.replace("font-family:var(--font-mono)", 'font-family:"Anthropic Mono","Courier New",monospace')

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(txt)
print("p1_head.html: all var(--font-mono) -> explicit monospace stack")
print("Done")
