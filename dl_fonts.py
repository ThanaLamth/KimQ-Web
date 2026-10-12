import urllib.request, os

os.makedirs(r'C:\Users\admin\kimq-web\fonts', exist_ok=True)

fonts = {
    'AnthropicSans-Roman.woff2':  'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a00a3295036497e1a28_AnthropicSans-Roman-Web.woff2',
    'AnthropicSans-Italic.woff2': 'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a016067bf14b9b8f48d_AnthropicSans-Italic-Web.woff2',
    'AnthropicSerif-Roman.woff2': 'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a1551eb6cda0d656e8a_AnthropicSerif-Roman-Web.woff2',
    'AnthropicSerif-Italic.woff2':'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a15a9fb8c1107a3570e_AnthropicSerif-Italic-Web.woff2',
    'AnthropicMono-Roman.woff2':  'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a2e55d24d61bc045b1a_AnthropicMono-Roman-Web.woff2',
    'AnthropicMono-Italic.woff2': 'https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a2eb93743112c30fe9c_AnthropicMono-Italic-Web.woff2',
}

h = {'User-Agent': 'Mozilla/5.0'}
for name, url in fonts.items():
    dest = rf'C:\Users\admin\kimq-web\fonts\{name}'
    req = urllib.request.Request(url, headers=h)
    data = urllib.request.urlopen(req, timeout=20).read()
    open(dest, 'wb').write(data)
    print(f'  {name}  {len(data)//1024}KB')
print('Done.')
