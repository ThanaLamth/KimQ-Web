import os

# Read shared parts
head = open(r'C:\Users\admin\kimq-web\shared_head.html', encoding='utf-8').read()
nav_raw = open(r'C:\Users\admin\kimq-web\shared.html', encoding='utf-8').read()
# strip comment line from nav
nav = '\n'.join(l for l in nav_raw.splitlines() if not l.strip().startswith('<!--'))

pages = ['ke-toan', 'logistics', 'tai-chinh', 'nhan-su']

for page in pages:
    src = open(rf'C:\Users\admin\kimq-web\{page}.html', encoding='utf-8').read()
    # replace placeholders
    out = src.replace('SHARED_HEAD_PLACEHOLDER\n', head + '\n')
    out = out.replace('SHARED_NAV_PLACEHOLDER', nav)
    with open(rf'C:\Users\admin\kimq-web\{page}.html', 'w', encoding='utf-8') as f:
        f.write(out)
    size = os.path.getsize(rf'C:\Users\admin\kimq-web\{page}.html')
    print(f'Built {page}.html  {size} bytes')

print('All sub-pages done.')
