import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
f = open(r'C:\Users\admin\kimq-web\index.html', encoding='utf-8')
c = f.read()
f.close()
checks = [u'T\u1eeb d\u1eef li\u1ec7u', u'K\u1ebf to\u00e1n', u'Nh\u00e2n s\u1ef1', u'L\u1ed9 tr\u00ecnh', u'B\u1ea3n tin \u0111i\u1ec1u h\u00e0nh', u'V\u0169 \u0110\u1ee9c Long']
labels = ['Tu du lieu', 'Ke toan', 'Nhan su', 'Lo trinh', 'Ban tin dieu hanh', 'Vu Duc Long']
for x, lbl in zip(checks, labels):
    print('OK' if x in c else 'MISSING', lbl)
print('Total chars:', len(c))
