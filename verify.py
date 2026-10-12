import sys
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html", "r", encoding="utf-8") as f:
    txt = f.read()

print("Emoji still present?")
print("  chat emoji:", "\U0001f4ac" in txt)
print("  chart emoji:", "\U0001f4ca" in txt)
print("  cycle emoji:", "\U0001f504" in txt)
print("  zap emoji:", "\u26a1" in txt)
print("  person emoji:", "\U0001f464" in txt)
print("  lock emoji:", "\U0001f512" in txt)

print("\nSVG icons present?")
print("  pico containers:", txt.count('class="pico"'))
print("  tico containers:", txt.count('class="tico"'))
print("  Zap polygon:", txt.count("polygon points"))
print("  UserCheck polyline:", txt.count("polyline points"))
print("  Lock rect:", txt.count("rect x="))
print("  MessageSquare path:", txt.count("M21 15"))
print("  BarChart lines:", txt.count('x1="18" y1="20"'))
print("  GitBranch branch:", txt.count("M18 9"))
