import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
files = ['p4_products.html','p6_trust.html','p7_usecases.html',
         'p8_proof_timeline.html','p9_brief_roadmap.html','p10_cta_footer.html',
         'ke-toan.html','logistics.html','tai-chinh.html','nhan-su.html']
for f in files:
    path = rf'C:\Users\admin\kimq-web\{f}'
    if not os.path.exists(path): continue
    txt = open(path, encoding='utf-8').read()
    found = [(m.start(), m.group()) for m in re.finditer(r'[\U0001F000-\U0001FFFF\u26A0-\u27BF\u2600-\u26FF\u2300-\u23FF]', txt)]
    if found:
        print(f'\n{f}:')
        for pos, ch in found:
            ctx = txt[max(0,pos-60):pos+60].replace('\n',' ')
            print(f'  U+{ord(ch):04X} {repr(ch)}  ...{ctx}...')
