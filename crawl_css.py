import urllib.request, re, json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request('https://www.anthropic.com/', headers=headers)
html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')

# Find all CSS links
css_links = re.findall(r'href="([^"]+\.css[^"]*)"', html)
# Find font links
font_links = re.findall(r'href="([^"]+(?:font|typekit|googleapis)[^"]*)"', html, re.I)
# Find script links
js_links = re.findall(r'src="([^"]+_app[^"]*\.js[^"]*)"', html)
# Find inline font-face or @font-face
font_face = re.findall(r'font-face[^}]+}', html)
# Find any mentions of font names in style tags
style_tags = re.findall(r'<style[^>]*>(.*?)</style>', html, re.S)
font_mentions = []
for s in style_tags:
    font_mentions += re.findall(r'font-family\s*:\s*([^;}]+)', s)

print('=== CSS FILES ===')
for l in css_links[:20]: print(l)
print('\n=== FONT LINKS ===')
for l in font_links: print(l)
print('\n=== FONT-FACE in HTML ===')
for f in font_face[:5]: print(f[:200])
print('\n=== FONT-FAMILY in style tags ===')
for f in font_mentions[:10]: print(f.strip())
print('\n=== FIRST 3000 chars of HTML ===')
print(html[:3000])
