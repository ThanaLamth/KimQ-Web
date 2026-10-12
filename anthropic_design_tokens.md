# Anthropic Design Tokens — Extracted from real CSS
# Source: ant-brand.shared.0836b103a.min.css

## FONTS (Custom — self-hosted, NOT Google Fonts)

### Typefaces
- **Anthropic Sans** (display, UI, detail) — variable weight 300–800, Roman + Italic
  - URL: `AnthropicSans-Roman-Web.woff2` / `AnthropicSans-Italic-Web.woff2`
  - Fallback: `Arial, sans-serif`
- **Anthropic Serif** (paragraph/body text, display serif) — variable weight 300–800
  - URL: `AnthropicSerif-Roman-Web.woff2` / `AnthropicSerif-Italic-Web.woff2`
  - Fallback: `Georgia, sans-serif`
- **Anthropic Mono** (code, monospace) — variable weight 300–800
  - URL: `AnthropicMono-Roman-Web.woff2`
  - Fallback: `Arial, sans-serif`
- **JetBrains Mono** (code snippets) — weight 400 only
- **Tiempos Text** — mentioned as fallback serif

### Font usage roles
- `--font--display-sans` = "Anthropic Sans" → headings, UI labels, nav
- `--font--paragraph-text` = "Anthropic Serif" → body copy, long-form
- `--font--display-serif-family` = "Anthropic Serif" → editorial headings
- `--font--detail` = "Anthropic Sans" → captions, metadata, tags
- `--font--mono` = "Anthropic Mono" → code, dates, labels

### Font sizes (type scale)
```
display-xxxl: 6rem    (96px)
display-xxl:  4.5rem  (72px)
display-xl:   4rem    (64px)
display-l:    3rem    (48px)
display-m:    2rem    (32px)
display-s:    1.5rem  (24px)
display-xs:   1.25rem (20px)
paragraph-l:  1.5rem  (24px)
paragraph-m:  1.25rem (20px)
paragraph-s:  1.125rem(18px)
paragraph-xs: 1rem    (16px)
detail-xl:    1.25rem (20px)
detail-l:     1.125rem(18px)
detail-m:     1rem    (16px)
detail-s:     0.875rem(14px)
detail-xs:    0.75rem (12px)
monospace:    1.125rem(18px)
```

### Line heights
- 1.0, 1.05, 1.1 → display headings
- 1.3, 1.4, 1.5 → body text

### Letter spacing
- `-0.02em` → tight display
- `-0.005em` → slight tight
- `0em` → normal

### Font weights
- regular: 400
- medium: 500
- semibold: 600
- bold: 700

---

## COLORS (Swatch system)

### Base backgrounds
```
--swatch--ivory-light:   #faf9f5   ← homepage background
--swatch--ivory-medium:  #f0eee6   ← secondary bg, about strip
--swatch--ivory-dark:    #e8e6dc   ← card bg, hover states
--swatch--white:         white
```

### Text / slate scale
```
--swatch--slate-dark:    #141413   ← primary text, black
--swatch--slate-medium:  #3d3d3a   ← secondary heading
--swatch--slate-light:   #5e5d59   ← muted text, gray
--swatch--cloud-dark:    #87867f   ← placeholder, disabled
--swatch--cloud-medium:  #b0aea5   ← very muted
--swatch--cloud-light:   #d1cfc5   ← borders, dividers
```

### Transparent overlays
```
--swatch--slate-faded-10: #1414131a  (slate @ 10% opacity)
--swatch--slate-faded-20: #14141333  (slate @ 20% opacity)
--swatch--ivory-faded-10: #faf9f51a
--swatch--ivory-faded-20: #faf9f533
```

### Accent colors (used sparingly)
```
--swatch--clay:    #d97757   ← warm orange-red (primary accent)
--swatch--accent:  #c6613f   ← darker burnt orange
--swatch--coral:   #ebcece   ← soft pink bg
--swatch--fig:     #c46686   ← rose/mauve
--swatch--kraft:   #d4a27f   ← warm tan
--swatch--pencil:  #f0ac54   ← amber/yellow
--swatch--peach:   #ebc9b7
--swatch--oat:     #e3dacc
--swatch--manilla: #ebdbbc
```

### Nature/muted accents
```
--swatch--cactus:  #bcd1ca   ← sage green
--swatch--mineral: #629987   ← forest green
--swatch--olive:   #788c5d   ← olive
--swatch--matcha:  #ced6bf   ← light green
--swatch--sky:     #6a9bcc   ← steel blue
--swatch--cloud:   #c5d3e0   ← light blue
--swatch--plum:    #827dbd   ← purple
--swatch--heather: #cbcadb   ← lavender
--swatch--orchid:  #e5cada   ← soft purple
--swatch--poppy:   #de6262   ← red
```

---

## SPACING (size scale)
```
--size--0.25rem: 0.25rem  (4px)
--size--0.5rem:  0.5rem   (8px)
--size--0.75rem: 0.75rem  (12px)
--size--1rem:    1rem     (16px)
--size--1.5rem:  1.5rem   (24px)
--size--2rem:    2rem     (32px)
--size--2.5rem:  2.5rem   (40px)
--size--3rem:    3rem     (48px)
--size--4rem:    4rem     (64px)
--size--5rem:    5rem     (80px)
--size--6rem:    6rem     (96px)
--size--7.5rem:  7.5rem   (120px)
```

### Named spacing tokens
```
space--1: 0.25rem
space--2: 0.5rem
space--3: 0.75rem
space--4: 1rem      ← default gap
space--5: 1.5rem
space--6: 2rem      ← site gutter
space--7: 2.5rem
space--8: 3rem
space--9: 4rem      ← section gap XL
```

---

## BORDER RADIUS
```
--radius--small: 0.25rem  (4px)
--radius--main:  0.5rem   (8px)   ← default cards
--radius--large: 1rem     (16px)
--radius--round: 100vw           ← pills/badges
```

---

## CONTAINERS
```
--container--main:  var(--site--width)  ← max-width main
--container--small: 56.25rem (900px)    ← narrow content
--container--full:  100vw
--site--gutter:     2rem
```

---

## BORDER
```
--border-width--main: 0.0625rem (1px)
Border color: var(--swatch--slate-faded-10) = rgba(20,20,19,0.1)
```

---

## TRANSITIONS
- Default: `all .3s`
- Color only: `background-color .1s, color .1s`

---

## UX PATTERNS (từ navigation qua tất cả pages)

### Navigation
- Fixed top, blur backdrop, 1px border bottom
- Logo left (ANTHROPIC text + Lottie animation), links right, CTA button far right
- Hover dropdown với mouseover trigger, `w--open` class
- Skip links: "Skip to main content", "Skip to footer"

### Animations
- Hero word animation: `.word` class, translateY(14px) → 0, opacity 0→1, staggered delay
- Only 1 @keyframe in CSS: `spin` (logo loading)
- Card hover: translateY(-2px) + box-shadow — NOT in CSS vars, inline style
- Nav dropdown: CSS class toggle, no keyframe animation

### Card design
- Background: `--swatch--ivory-medium` or `--swatch--white`
- Border: `1px solid var(--swatch--slate-faded-10)`
- Radius: `--radius--main` (0.5rem = 8px) or `--radius--large` (1rem = 16px)
- No default shadow — shadow only on hover

### Buttons
- Primary (dark): `--swatch--slate-dark` bg, white text
- Secondary: transparent bg, `--swatch--slate-faded-10` border
- Tertiary: no border, text only ("See more")
- Radius: `--radius--round` (pill) for small buttons, `--radius--main` for large

### Layout
- Body font: Anthropic Serif (body copy) → KHÔNG phải sans-serif!
- Heading font: Anthropic Sans
- Mono labels: Anthropic Mono (dates, categories, code)
- Max-width: site--width variable
- Gutter: 2rem (32px)

## WOFF2 FONT URLS (có thể tải về để dùng local)
- Sans Roman: https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a00a3295036497e1a28_AnthropicSans-Roman-Web.woff2
- Sans Italic: https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a016067bf14b9b8f48d_AnthropicSans-Italic-Web.woff2
- Serif Roman: https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a1551eb6cda0d656e8a_AnthropicSerif-Roman-Web.woff2
- Serif Italic: https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a15a9fb8c1107a3570e_AnthropicSerif-Italic-Web.woff2
- Mono Roman:   https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/69971a2e55d24d61bc045b1a_AnthropicMono-Roman-Web.woff2
