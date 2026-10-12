import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("p1_head.html", "r", encoding="utf-8") as f:
    h = f.read()

# ============================================================
# UI/UX UPGRADES based on Be Vietnam Pro + modern SaaS patterns
# ============================================================

# 1. Hero heading: Be Vietnam Pro looks best at 700-800 weight, tight tracking
h = h.replace(
    '.hh{font-family:var(--font-sans);font-size:clamp(2.25rem,4.5vw,3.5rem);font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);line-height:1.1;max-width:740px;margin-bottom:var(--sp-6);color:var(--slate-dark)}',
    '.hh{font-family:var(--font-sans);font-size:clamp(2rem,4vw,3.25rem);font-weight:800;letter-spacing:-0.03em;line-height:1.1;max-width:720px;margin-bottom:var(--sp-6);color:var(--slate-dark)}'
)

# 2. Section heading .sh: tight, confident
old_sh = re.search(r'\.sh\{[^}]+\}', h)
if old_sh:
    h = h.replace(old_sh.group(), '.sh{font-family:var(--font-sans);font-size:clamp(1.375rem,2.4vw,2rem);font-weight:700;letter-spacing:-0.025em;line-height:1.15;max-width:620px;margin-bottom:var(--sp-4);color:var(--slate-dark)}')
    print("sh updated")

# 3. Body text .sp: Be Vietnam Pro 400 at 16px is very readable
h = h.replace(
    '.sp{font-family:var(--font-serif);font-size:var(--para-s);color:var(--slate-light);max-width:480px;line-height:var(--lh-loose);margin-bottom:var(--sp-9)}',
    '.sp{font-family:var(--font-sans);font-size:1rem;font-weight:400;color:var(--slate-light);max-width:480px;line-height:1.65;margin-bottom:var(--sp-9)}'
)

# 4. Hero subtitle .hsub: same sans, larger, airy
h = h.replace(
    '.hsub{font-family:var(--font-serif);font-size:var(--para-m);color:var(--slate-light);max-width:480px;line-height:var(--lh-loose);margin-bottom:var(--sp-9)}',
    '.hsub{font-family:var(--font-sans);font-size:1.0625rem;font-weight:400;color:var(--slate-light);max-width:500px;line-height:1.7;margin-bottom:var(--sp-9)}'
)

# 5. Buttons: Be Vietnam Pro looks great at medium weight, generous padding
h = h.replace(
    '.bp{padding:.9375rem 2rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-semibold);text-decoration:none;display:inline-block;transition:var(--t-base)}',
    '.bp{padding:.875rem 1.875rem;background:var(--slate-dark);color:var(--white);border-radius:6px;font-family:var(--font-sans);font-size:.9375rem;font-weight:600;letter-spacing:-.01em;text-decoration:none;display:inline-flex;align-items:center;transition:all .2s}'
)
h = h.replace(
    '.bs{padding:.9375rem 1.75rem;background:transparent;color:var(--slate-dark);border:var(--border-cloud);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-regular);text-decoration:none;display:inline-block;transition:var(--t-base)}',
    '.bs{padding:.875rem 1.75rem;background:transparent;color:var(--slate-dark);border:1px solid var(--cloud-light);border-radius:6px;font-family:var(--font-sans);font-size:.9375rem;font-weight:400;letter-spacing:-.01em;text-decoration:none;display:inline-flex;align-items:center;transition:all .2s}'
)
h = h.replace('.bs:hover{border-color:var(--slate-dark)}',
              '.bs:hover{border-color:var(--slate-dark);background:var(--ivory-medium)}')
h = h.replace('.bp:hover{opacity:.82}', '.bp:hover{opacity:.88;transform:translateY(-1px)}')

# 6. Nav CTA button
h = h.replace(
    '.ncta{margin-left:var(--sp-7);padding:.5rem 1.25rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-medium);text-decoration:none;transition:var(--t-color);white-space:nowrap}',
    '.ncta{margin-left:var(--sp-7);padding:.4375rem 1.125rem;background:var(--slate-dark);color:var(--white);border-radius:6px;font-family:var(--font-sans);font-size:.875rem;font-weight:500;letter-spacing:-.01em;text-decoration:none;transition:all .2s;white-space:nowrap}'
)

# 7. Product cards .pcard: cleaner padding, softer hover
h = h.replace(
    '.pcard{background:var(--white);border:var(--border);border-radius:var(--r-md);padding:var(--sp-9) var(--sp-8);display:fl',
    '.pcard{background:var(--white);border:1px solid var(--cloud-light);border-radius:12px;padding:var(--sp-8) var(--sp-7);display:fl'
)
h = h.replace(
    '.pcard:hover{box-shadow:0 8px 32px var(--slate-10);transform:translateY(-2px)}',
    '.pcard:hover{box-shadow:0 4px 24px rgba(20,20,19,.08);transform:translateY(-1px)}'
)

# 8. .pname - product card title
h = h.replace(
    '.pname{font-family:var(--font-sans);font-size:var(--text-xs);font-weight:var(--fw-semibold);letter-spacing:var(--ls-snug',
    '.pname{font-family:var(--font-sans);font-size:1.125rem;font-weight:700;letter-spacing:-0.02em'
)

# 9. .pdesc
h = h.replace(
    '.pdesc{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}',
    '.pdesc{font-family:var(--font-sans);font-size:.9375rem;font-weight:400;color:var(--slate-light);line-height:1.65;margin-top:var(--sp-3)}'
)

# 10. Trust section cards
h = h.replace(
    '.tcard{border:var(--border);border-radius:var(--r-md);padding:var(--sp-8) var(--sp-7);background:var(--white)}',
    '.tcard{border:1px solid var(--cloud-light);border-radius:12px;padding:var(--sp-8) var(--sp-6);background:var(--white)}'
)
h = h.replace(
    '.tul li{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);padding:var(--sp-2) 0;border-bo',
    '.tul li{font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--slate-light);padding:var(--sp-2) 0;border-bo'
)

# 11. Timeline text
h = h.replace(
    '.tla{padding:1.125rem 1.375rem;font-family:var(--font-serif);font-size:var(--detail-s);line-height:var(--lh-body)',
    '.tla{padding:1.125rem 1.375rem;font-family:var(--font-sans);font-size:.875rem;font-weight:400;line-height:1.55'
)

# 12. Proof cards
h = h.replace(
    '.prc p{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}',
    '.prc p{font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--slate-light);line-height:1.65}'
)

# 13. Use case description
h = h.replace(
    '.ucd{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}',
    '.ucd{font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--slate-light);line-height:1.65}'
)

# 14. Brief decision text
h = h.replace(
    'font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-dark);line-height:var(--lh-body)}',
    'font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--slate-dark);line-height:1.55}'
)

# 15. Flow description .fd
h = h.replace(
    '.fd{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}',
    '.fd{font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--slate-light);line-height:1.6}'
)

# 16. Roadmap card desc
h = h.replace(
    '.rd{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}',
    '.rd{font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--slate-light);line-height:1.6}'
)

# 17. Footer tag
h = h.replace(
    '.ftag{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--footer-muted);line-height:var(--lh-loose);max-width:260px}',
    '.ftag{font-family:var(--font-sans);font-size:.875rem;font-weight:400;color:var(--footer-muted);line-height:1.65;max-width:260px}'
)

# 18. CMP list (comparison cards)
h = h.replace(
    '.cmplist li{font-family:var(--font-serif);font-size:var(--detail-s);',
    '.cmplist li{font-family:var(--font-sans);font-size:.875rem;'
)

# 19. Roadmap cards border-radius
h = h.replace(
    '.rcard{background:var(--white);border:var(--border);border-radius:var(--r-md);',
    '.rcard{background:var(--white);border:1px solid var(--cloud-light);border-radius:12px;'
)

# 20. Proof cards
h = h.replace(
    '.prc{background:var(--white);border:var(--border);border-radius:var(--r-md);',
    '.prc{background:var(--white);border:1px solid var(--cloud-light);border-radius:12px;'
)

# 21. Use case card .uc
h = h.replace(
    '.uc{background:var(--white);border:var(--border);border-radius:var(--r-md);',
    '.uc{background:var(--white);border:1px solid var(--cloud-light);border-radius:12px;'
)

# 22. Brief .bc card
h = h.replace(
    '.bc{background:var(--white);border:var(--border);border-radius:var(--r-md);',
    '.bc{background:var(--white);border:1px solid var(--cloud-light);border-radius:12px;'
)

# 23. Nav links font
h = h.replace(
    '.nlinks a{font-family:var(--font-sans);font-size:var(--detail-s);color:var(--slate-dark);text-decoration:none;opacity:.6;transition:var(--t-color)}',
    '.nlinks a{font-family:var(--font-sans);font-size:.875rem;font-weight:500;color:var(--slate-dark);text-decoration:none;opacity:.6;transition:all .2s;letter-spacing:-.01em}'
)

# 24. Pill tags
h = h.replace(
    '.pill{display:inline-block;padding:.25rem .875rem;border:var(--border);border-radius:var(--r-pill);font-size:var(--detail-xs);font-family:var(--font-sans);color:var(--slate-light);letter-spacing:var(--ls-normal)}',
    '.pill{display:inline-block;padding:.3rem 1rem;border:1px solid var(--cloud-light);border-radius:100vw;font-size:.8125rem;font-family:var(--font-sans);font-weight:500;color:var(--slate-light);letter-spacing:.01em}'
)

with open("p1_head.html", "w", encoding="utf-8") as f:
    f.write(h)
print("p1_head.html UX upgrade complete")

# Also do shared_head for subpages
with open("shared_head.html", "r", encoding="utf-8") as f:
    sh = f.read()

# Replace all font-serif body text with font-sans
sh = sh.replace('font-family:var(--font-serif);', 'font-family:var(--font-sans);')
# card-d, stat-l, etc descriptions
sh = sh.replace(';font-family:var(--font-serif);', ';font-family:var(--font-sans);')
sh = sh.replace('line-height:var(--lh-loose)', 'line-height:1.65')
sh = sh.replace('line-height:var(--lh-body)', 'line-height:1.55')

with open("shared_head.html", "w", encoding="utf-8") as f:
    f.write(sh)
print("shared_head.html UX upgrade complete")
