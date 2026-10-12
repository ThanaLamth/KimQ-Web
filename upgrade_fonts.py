import sys, re
sys.stdout.reconfigure(encoding="utf-8")

# ============================================================
# STRATEGY:
# Replace Anthropic fonts (no Vietnamese support) with:
#   --font-sans  -> "Be Vietnam Pro" (headings, UI, labels, buttons)
#   --font-serif -> "Be Vietnam Pro" (body, same family, weight 400)
#   --font-mono  -> "JetBrains Mono" (kickers, tags, timestamps)
# Load via Google Fonts CDN - guaranteed Vietnamese support
# ============================================================

# 1. tokens.css - swap font variables + @font-face
with open("tokens.css", "r", encoding="utf-8") as f:
    tok = f.read()

# Remove old @font-face blocks
tok = re.sub(r'@font-face\{[^}]+\}\n?', '', tok)

# Replace font variables
tok = tok.replace(
    '--font-sans:"Anthropic Sans",Arial,sans-serif',
    '--font-sans:"Be Vietnam Pro",system-ui,sans-serif'
)
tok = tok.replace(
    '--font-serif:"Anthropic Serif",Georgia,serif',
    '--font-serif:"Be Vietnam Pro",system-ui,sans-serif'
)
tok = tok.replace(
    '--font-mono:"Anthropic Mono","Courier New",monospace',
    '--font-mono:"JetBrains Mono","Courier New",monospace'
)

# Add Google Fonts preconnect note (handled in HTML head)
with open("tokens.css", "w", encoding="utf-8") as f:
    f.write(tok)
print("tokens.css: font vars updated, @font-face removed")

# 2. p1_head.html - remove Anthropic font-family hardcoded refs + add Google Fonts link
with open("p1_head.html", "r", encoding="utf-8") as f:
    h = f.read()

# Replace hardcoded Anthropic font refs with variables
h = h.replace('"Anthropic Sans",Arial,sans-serif', 'var(--font-sans)')
h = h.replace('"Anthropic Mono","Courier New",monospace', 'var(--font-mono)')

# Also fix .sh which was hardcoded
h = h.replace(
    'font-family:"Anthropic Sans",Arial,sans-serif;font-size:clamp(1.25rem,2.2vw,1.75rem)',
    'font-family:var(--font-sans);font-size:clamp(1.25rem,2.2vw,1.75rem)'
)

# Add Google Fonts link right before </head> - preconnect + font load
gf_link = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=JetBrains+Mono:wght@400;500;600&display=swap">'''

# Insert before </head>
if "fonts.googleapis.com" not in h:
    h = h.replace('<link rel="stylesheet" href="tokens.css">', gf_link + '\n<link rel="stylesheet" href="tokens.css">')
    print("Google Fonts link added to p1_head.html")

# Tune body font-weight for Be Vietnam Pro (400 = regular, crisp)
h = h.replace(
    'body{font-family:var(--font-serif);background:var(--ivory-light);color:var(--slate-dark);line-height:var(--lh-body)',
    'body{font-family:var(--font-serif);background:var(--ivory-light);color:var(--slate-dark);line-height:1.6;font-size:15px'
)

# Fix letter-spacing on kicker .sl and .hk - Be Vietnam Pro needs slightly less LS
h = h.replace('letter-spacing:.07em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}',
              'letter-spacing:.12em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}')

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(h)
print("p1_head.html: fonts updated")
print("Hardcoded Anthropic Mono left:", h.count('"Anthropic Mono"'))

# 3. shared_head.html - same treatment for subpages
with open("shared_head.html", "r", encoding="utf-8") as f:
    sh = f.read()

sh = sh.replace('"Anthropic Mono","Courier New",monospace', 'var(--font-mono)')
sh = sh.replace('"Anthropic Sans",Arial,sans-serif', 'var(--font-sans)')

if "fonts.googleapis.com" not in sh:
    sh = sh.replace('<link rel="stylesheet" href="tokens.css">', gf_link + '\n<link rel="stylesheet" href="tokens.css">')
    print("Google Fonts link added to shared_head.html")

sh = sh.replace(
    'body{font-family:var(--font-serif);background:var(--ivory-light);color:var(--slate-dark);line-height:var(--lh-body)',
    'body{font-family:var(--font-serif);background:var(--ivory-light);color:var(--slate-dark);line-height:1.6;font-size:15px'
)

with open("shared_head.html", "w", encoding="utf-8") as f:
    f.write(sh)
print("shared_head.html: fonts updated")
print("Done - all font replacements complete")
