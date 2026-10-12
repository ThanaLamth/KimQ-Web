import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("tokens.css", "r", encoding="utf-8") as f:
    txt = f.read()

# Change font-display:swap to optional for Mono (reduces layout shift on kickers)
# Keep swap for Sans/Serif (body text)
txt = txt.replace(
    'url("fonts/AnthropicMono-Roman.woff2") format("woff2");font-weight:300 800;font-style:normal;font-display:swap',
    'url("fonts/AnthropicMono-Roman.woff2") format("woff2");font-weight:300 800;font-style:normal;font-display:block'
)
txt = txt.replace(
    'url("fonts/AnthropicMono-Italic.woff2") format("woff2");font-weight:300 800;font-style:italic;font-display:swap',
    'url("fonts/AnthropicMono-Italic.woff2") format("woff2");font-weight:300 800;font-style:italic;font-display:block'
)

with open("tokens.css", "w", encoding="utf-8") as f:
    f.write(txt)
print("tokens.css: Mono font-display set to block")
