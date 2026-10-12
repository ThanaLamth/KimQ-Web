import urllib.request, re

css = open(r'C:\Users\admin\kimq-web\anthropic.css.txt', encoding='utf-8').read()

# Get all swatch (color) variables
swatches = re.findall(r'--(swatch--[\w-]+)\s*:\s*([^;}]+)', css)
print('=== SWATCHES ===')
for k,v in sorted(set((k,v.strip()) for k,v in swatches)):
    print(f'  --{k}: {v}')

# Get all size/spacing
sizes = re.findall(r'--(size--[\w.-]+)\s*:\s*([^;}]+)', css)
print('\n=== SIZES ===')
for k,v in sorted(set((k,v.strip()) for k,v in sizes)):
    print(f'  --{k}: {v}')

# Get typography vars
typo = re.findall(r'--(_typography---[\w-]+)\s*:\s*([^;}]+)', css)
print('\n=== TYPOGRAPHY VARS ===')
for k,v in sorted(set((k,v.strip()) for k,v in typo)):
    print(f'  --{k}: {v}')

# Get animation keyframes
anims = re.findall(r'@keyframes\s+([\w-]+)\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', css)
print(f'\n=== KEYFRAMES: {len(anims)} ===')
for name, body in anims[:15]:
    print(f'\n  @keyframes {name}')
    print('  ' + body[:300])

# Get transition values
transitions = re.findall(r'transition\s*:\s*([^;}]{1,100})', css)
unique_t = sorted(set(t.strip() for t in transitions))
print(f'\n=== TRANSITIONS ({len(unique_t)}) ===')
for t in unique_t[:20]: print(' ', t)
