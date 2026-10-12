# SVG icon definitions (Lucide style, 20x20)
def svg(paths, size=20):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{paths}</svg>'

MSG_SQ = svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>')
BAR    = svg('<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>')
BRANCH = svg('<line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>')
ZAP    = svg('<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>')
UCHECK = svg('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>')
LOCK   = svg('<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>')

# Small inline SVG for card-tag labels (14x14)
def svgs(paths):
    return f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:4px;flex-shrink:0">{paths}</svg>'

ZAP_SM    = svgs('<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>')
UCHECK_SM = svgs('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>')

# --- p4_products.html ---
with open('p4_products.html', 'r', encoding='utf-8') as f:
    p4 = f.read()
p4 = p4.replace('<span class="pico">\U0001f4ac</span>', f'<span class="pico">{MSG_SQ}</span>')
p4 = p4.replace('<span class="pico">\U0001f4ca</span>', f'<span class="pico">{BAR}</span>')
p4 = p4.replace('<span class="pico">\U0001f504</span>', f'<span class="pico">{BRANCH}</span>')
with open('p4_products.html', 'w', encoding='utf-8') as f:
    f.write(p4)
print('p4_products.html done')

# --- p6_trust.html ---
with open('p6_trust.html', 'r', encoding='utf-8') as f:
    p6 = f.read()
p6 = p6.replace('<div class="tico">\u26a1</div>', f'<div class="tico">{ZAP}</div>')
p6 = p6.replace('<div class="tico">\U0001f464</div>', f'<div class="tico">{UCHECK}</div>')
p6 = p6.replace('<div class="tico">\U0001f512</div>', f'<div class="tico">{LOCK}</div>')
with open('p6_trust.html', 'w', encoding='utf-8') as f:
    f.write(p6)
print('p6_trust.html done')

# --- ke-toan.html ---
with open('ke-toan.html', 'r', encoding='utf-8') as f:
    kt = f.read()
kt = kt.replace('<div class="card-tag">\u26a1 Agent t\u1ef1 l\u00e0m</div>', f'<div class="card-tag" style="display:flex;align-items:center">{ZAP_SM}Agent t\u1ef1 l\u00e0m</div>')
kt = kt.replace('<div class="card-tag">\U0001f464 Ng\u01b0\u1eddi duy\u1ec7t</div>', f'<div class="card-tag" style="display:flex;align-items:center">{UCHECK_SM}Ng\u01b0\u1eddi duy\u1ec7t</div>')
with open('ke-toan.html', 'w', encoding='utf-8') as f:
    f.write(kt)
print('ke-toan.html done')

# --- nhan-su.html ---
with open('nhan-su.html', 'r', encoding='utf-8') as f:
    ns = f.read()
ns = ns.replace('<div class="card-tag">\u26a1 Agent t\u1ef1 l\u00e0m</div>', f'<div class="card-tag" style="display:flex;align-items:center">{ZAP_SM}Agent t\u1ef1 l\u00e0m</div>')
ns = ns.replace('<div class="card-tag">\U0001f464 Ng\u01b0\u1eddi duy\u1ec7t</div>', f'<div class="card-tag" style="display:flex;align-items:center">{UCHECK_SM}Ng\u01b0\u1eddi duy\u1ec7t</div>')
with open('nhan-su.html', 'w', encoding='utf-8') as f:
    f.write(ns)
print('nhan-su.html done')

print('All emoji replaced!')
