import urllib.request, re

CSS_URL = 'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/css/ant-brand.shared.0836b103a.min.css'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(CSS_URL, headers=headers)
css = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='replace')

print(f'CSS size: {len(css)} chars')

# 1. font-face blocks
font_faces = re.findall(r'@font-face\s*\{([^}]+)\}', css)
print(f'\n=== @font-face blocks: {len(font_faces)} ===')
for i, ff in enumerate(font_faces[:20]):
    print(f'--- {i+1} ---')
    print(ff[:400])

# 2. CSS custom properties (variables)
vars_all = re.findall(r'--([\w-]+)\s*:\s*([^;}]+)', css)
print(f'\n=== CSS Variables: {len(vars_all)} ===')
for k,v in vars_all[:60]:
    print(f'  --{k}: {v.strip()}')

# 3. All font-family declarations
ff_decls = re.findall(r'font-family\s*:\s*([^;}]{1,120})', css)
unique_ff = sorted(set(f.strip() for f in ff_decls))
print(f'\n=== font-family values: {len(unique_ff)} ===')
for f in unique_ff:
    print(' ', f)

# 4. color values (hex)
colors = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', css)
unique_colors = sorted(set('#'+c.upper() for c in colors))
print(f'\n=== Hex colors: {len(unique_colors)} ===')
for c in unique_colors[:40]:
    print(' ', c)

# 5. border-radius values
radii = re.findall(r'border-radius\s*:\s*([^;}]+)', css)
unique_r = sorted(set(r.strip() for r in radii))
print(f'\n=== border-radius: {len(unique_r)} ===')
for r in unique_r[:20]: print(' ', r)

# 6. Save first 8000 chars for manual inspection
with open(r'C:\Users\admin\kimq-web\anthropic.css.txt', 'w', encoding='utf-8') as f:
    f.write(css[:80000])
print('\nSaved first 80000 chars to anthropic.css.txt')
