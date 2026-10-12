# Anthropic UI/UX Deep Dive — Ghi chú từ tất cả các sections

## 1. HOMEPAGE (đã học trước)
- Ivory `#F5F0E8` background, dark charcoal footer
- Word-by-word hero animation, Lottie logo
- Hover dropdown nav, card grid, monospace for dates/tags
- Minimal palette: black / white / ivory, no gradients

## 2. RESEARCH PAGE
**Layout:** Team cards theo chiều ngang (Alignment, Economics, Frontier Red Team, Interpretability, Societal Impacts)
**Featured articles:** Large card trái + side cards phải (giống homepage news)
**Publications list:** Bullet list đơn giản, mỗi item là link
**Design notes:**
- Section headings nhỏ (###), không dùng hero lớn
- Không có image nhiều — text-first, research vibe
- Màu uniform — không có accent color riêng cho Research
- Sub-team cards: tên + 1-2 câu mô tả, không có icon

## 3. NEWS / NEWSROOM PAGE
**Layout:** 2 cột — content chính trái, sidebar phải (Press/Media contacts)
**Featured section:** 1 card lớn + 2-3 card nhỏ bên phải, có abstract geometric image
**News list:** Dạng table — DATE | CATEGORY | TITLE, phân cách bằng thin horizontal lines
**Category labels:** Announcements, Science, Features (text only, không clickable filter)
**Pagination:** "See more" button tertiary, không có numbered pages
**Date format:** "Oct 7, 2026" — Month Day, Year
**Image style:** Abstract geometric shapes (yellow, purple, blue trên beige)
**Search:** Input field ẩn/nhỏ, không prominent
**Sidebar cards:** Border cards với light beige — Press inquiries / Non-media / Media assets

## 4. COMPANY / ABOUT PAGE
**Hero:** "Making AI systems you can rely on" — bold, short
**Sub:** "Anthropic is an AI safety and research company..."
**Our Purpose section:** Large statement, không có image
**Values:** Numbered 01–07, mỗi value có ### heading + paragraph
  - Act for the global good
  - Hold light and shade
  - Be good to our users
  - Ignite a race to the top on safety
  - Do the simple thing that works
  - Be helpful, honest, and harmless
  - Put the mission first
**Teams section:** Research / Policy / Product / Operations — card grid
**Governance:** Text-only, Board of Directors listed as comma-separated names
**CTA:** "Want to help us build the future of safe AI? Join us" — simple, no button style

## 5. CAREERS PAGE
**Benefits sections:**
- Health: Medical/dental/vision, mental health, fertility, 22 weeks parental leave
- Compensation: Competitive salary + equity, equity donation matching 1:1 up to 25%, retirement matching
- Additional: $500/month wellness stipend, commuter, education, home office, relocation, daily meals
**Interview process:** 3 headings: What we're looking for / The interview process / Your safety matters
**FAQs:** Accordion-style Q&A (internships, feedback, re-apply, offer deadline, visa, remote)
**Design notes:**
- Rất text-heavy, document-like
- Không có team photos section (khác với typical careers pages)
- CTA cuối: "Explore open roles" button

## 6. POLICY PAGE
**Hero:** "AI will be one of the most transformative technologies in history."
**Sub-sections:** Policy on the AI Exponential / Economic Policy Framework / Advanced AI Framework / 2028 scenarios
**Philosophy block:** Long-form editorial text, rất dài
**Policy priorities:** Numbered list, text-heavy
**Design:** Document-like, editorial — không phải marketing
**Tone:** Authoritative, academic

## 7. CLAUDE PRODUCT PAGE (claude.com/product/overview)
**Hero CTA:** "Get to work" — action-oriented
**Features organized thành groups:**
- "Put it to work": Files/tools access, create real files (docs/sheets/slides), check in from anywhere
- "Make it yours": Skills, Plugins, Custom connectors/MCPs
- "Stay in control": Permissions control, Access controls, Admin tools, Cloud providers
- "Work where you want": Desktop/web/mobile, Chrome extension, Microsoft 365, Slack Tag
- "Don't start over": Memory, Projects, Instructions
**FAQ section:** Dài, conversational
**Tone:** Practical, "hand off work", không phải "chat with AI"
**Positioning:** "More than an AI assistant: it's a helpful, intuitive, and powerful collaborator"

## KEY DESIGN PATTERNS RÚT RA ĐỂ ÁP DỤNG CHO KIMQ

### News/Bài viết list:
- DATE | CATEGORY | TITLE format với thin dividers
- "See more" thay vì pagination
- Sidebar với contact info cards

### Company/About:
- Numbered values (01–07) với short title + paragraph
- Board/governance dạng text list, không fancy
- "Join us" CTA đơn giản

### Product features:
- Group features thành clusters có tên ("Put it to work", "Stay in control")
- Bullet list trong mỗi cluster, không phải card grid
- FAQ dạng conversational

### Careers:
- Benefits 3 columns: Health / Compensation / Additional
- Interview process dạng 3 steps text
- FAQs accordion

### Research/Content pages:
- Sub-team cards: name + 1-2 sentences
- Publications: simple bullet list
- Text-first, minimal images
