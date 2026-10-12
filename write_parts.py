# Write all HTML parts with exact Anthropic design tokens
import os

def w(path, content):
    open(path, 'w', encoding='utf-8').write(content)
    print(f'wrote {os.path.basename(path)} ({len(content)} chars)')

# ── p1_head.html ─────────────────────────────────────────────
w(r'C:\Users\admin\kimq-web\p1_head.html', '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KimQ \u00d7 Doanh nghi\u1ec7p \u2014 AI-native software</title>
<link rel="stylesheet" href="tokens.css">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font-serif);background:var(--ivory-light);color:var(--slate-dark);line-height:var(--lh-body);-webkit-font-smoothing:antialiased}
.con{max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter)}
.pill{display:inline-block;padding:.25rem .875rem;border:var(--border);border-radius:var(--r-pill);font-size:var(--detail-xs);font-family:var(--font-sans);color:var(--slate-light);letter-spacing:var(--ls-normal)}
/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h);background:rgba(250,249,245,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:var(--border);display:flex;align-items:center}
.ni{display:flex;align-items:center;width:100%;max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter)}
.nl{font-family:var(--font-sans);font-size:var(--detail-l);font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);color:var(--slate-dark);text-decoration:none;margin-right:auto;display:flex;align-items:center;gap:var(--sp-2)}
.lm{width:28px;height:28px;background:var(--slate-dark);border-radius:var(--r-xs);display:flex;align-items:center;justify-content:center;color:var(--white);font-size:13px;font-weight:900;flex-shrink:0}
.nlinks{display:flex;gap:var(--sp-7)}
.nlinks a{font-family:var(--font-sans);font-size:var(--detail-s);color:var(--slate-dark);text-decoration:none;opacity:.6;transition:var(--t-color)}
.nlinks a:hover{opacity:1}
.ncta{margin-left:var(--sp-7);padding:.5rem 1.25rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-medium);text-decoration:none;transition:var(--t-color);white-space:nowrap}
.ncta:hover{opacity:.82}
/* HERO */
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;padding-top:var(--nav-h);position:relative;overflow:hidden}
.hn{position:absolute;inset:0;background:radial-gradient(ellipse 90% 70% at 65% 35%,var(--slate-10),transparent 65%);pointer-events:none}
.hi{position:relative;z-index:1;padding:var(--sp-12) 0}
.hk{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-6)}
.hh{font-family:var(--font-sans);font-size:clamp(2.5rem,5.5vw,var(--text-xl));font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);line-height:var(--lh-display);max-width:820px;margin-bottom:var(--sp-6);color:var(--slate-dark)}
.word{display:inline-block;opacity:0;transform:translateY(.875rem);animation:wIn .5s ease forwards}
@keyframes wIn{to{opacity:1;transform:translateY(0)}}
.hsub{font-family:var(--font-serif);font-size:var(--para-m);color:var(--slate-light);max-width:480px;line-height:var(--lh-loose);margin-bottom:var(--sp-9)}
.hbtns{display:flex;align-items:center;gap:var(--sp-4);flex-wrap:wrap}
.bp{padding:.875rem 1.75rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-medium);text-decoration:none;display:inline-block;transition:var(--t-base)}
.bp:hover{opacity:.82}
.bs{padding:.875rem 1.75rem;background:transparent;color:var(--slate-dark);border:var(--border-cloud);border-radius:var(--r-sm);font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-regular);text-decoration:none;display:inline-block;transition:var(--t-base)}
.bs:hover{border-color:var(--slate-dark)}
.htags{display:flex;gap:var(--sp-2);flex-wrap:wrap;margin-top:var(--sp-10)}
.dv{height:1px;background:var(--slate-10)}
/* SECTIONS */
.sec{padding:var(--section-gap) 0}
.sl{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-4)}
.sh{font-family:var(--font-sans);font-size:clamp(1.5rem,3.2vw,var(--text-m));font-weight:var(--fw-semibold);letter-spacing:var(--ls-tight);line-height:var(--lh-heading);max-width:600px;margin-bottom:var(--sp-4);color:var(--slate-dark)}
.sp{font-family:var(--font-serif);font-size:var(--para-s);color:var(--slate-light);max-width:480px;line-height:var(--lh-loose);margin-bottom:var(--sp-9)}
/* ABOUT STRIP */
.astrip{background:var(--ivory-medium);border-top:var(--border);border-bottom:var(--border);padding:var(--sp-11) 0}
.sgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--sp-8);margin-bottom:var(--sp-9)}
.snum{font-family:var(--font-sans);font-size:var(--text-l);font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);line-height:1}
.slbl{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);margin-top:var(--sp-2);line-height:var(--lh-body)}
.clients{display:flex;flex-wrap:wrap;gap:var(--sp-2)}
.ctag{padding:.4rem 1rem;border:var(--border);border-radius:var(--r-pill);font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-medium);background:var(--white);color:var(--slate-dark)}
/* PRODUCTS */
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--sp-5)}
.pcard{background:var(--white);border:var(--border);border-radius:var(--r-md);padding:var(--sp-9) var(--sp-8);display:flex;flex-direction:column;gap:var(--sp-4);transition:var(--t-base)}
.pcard:hover{box-shadow:0 8px 32px var(--slate-10);transform:translateY(-2px)}
.pno{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark)}
.pico{font-size:1.5rem;line-height:1}
.pname{font-family:var(--font-sans);font-size:var(--text-xs);font-weight:var(--fw-semibold);letter-spacing:var(--ls-snug);color:var(--slate-dark)}
.pdesc{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}
.pfoot{margin-top:auto;padding-top:var(--sp-4);border-top:1px solid var(--ivory-dark);font-family:var(--font-mono);font-size:var(--detail-xs);color:var(--cloud-dark)}
/* APPROACH */
.split{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-12);align-items:start}
.ctbl{width:100%;border-collapse:collapse;margin-top:var(--sp-5)}
.ctbl th{text-align:left;font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.06em;text-transform:uppercase;color:var(--cloud-dark);padding:var(--sp-3) 0;border-bottom:var(--border-cloud)}
.ctbl td{font-family:var(--font-serif);padding:var(--sp-3) 0;font-size:var(--detail-s);border-bottom:1px solid var(--ivory-dark);vertical-align:top}
.ctbl tr td:first-child{color:var(--slate-light);padding-right:var(--sp-5);width:30%;font-family:var(--font-sans)}
.bbold{display:inline-block;padding:.125rem .5rem;background:var(--ivory-dark);border-radius:var(--r-xs);font-family:var(--font-mono);font-size:var(--detail-xs);color:var(--slate-light)}
.bnew{display:inline-block;padding:.125rem .5rem;background:var(--slate-dark);color:var(--white);border-radius:var(--r-xs);font-family:var(--font-mono);font-size:var(--detail-xs)}
.flow{display:flex;flex-direction:column;gap:var(--sp-5);margin-top:var(--sp-5)}
.fr{display:flex;gap:var(--sp-5);align-items:flex-start}
.fn{width:2rem;height:2rem;border-radius:50%;background:var(--slate-dark);color:var(--white);display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-bold);flex-shrink:0;margin-top:.2rem}
.ft{font-family:var(--font-sans);font-size:var(--detail-m);font-weight:var(--fw-semibold);margin-bottom:var(--sp-1);color:var(--slate-dark)}
.fd{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}
/* TRUST */
.tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--sp-5)}
.tcard{border:var(--border);border-radius:var(--r-md);padding:var(--sp-8) var(--sp-7);background:var(--white)}
.tico{font-size:1.375rem;margin-bottom:var(--sp-4)}
.tt{font-family:var(--font-sans);font-size:var(--detail-l);font-weight:var(--fw-semibold);margin-bottom:var(--sp-3);color:var(--slate-dark)}
.tul{list-style:none}
.tul li{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);padding:var(--sp-2) 0;border-bottom:1px solid var(--ivory-dark);display:flex;gap:var(--sp-2);align-items:baseline}
.tul li:last-child{border-bottom:none}
/* TABS */
.utabs{display:flex;gap:var(--sp-2);flex-wrap:wrap;margin-bottom:var(--sp-9)}
.tb{padding:.5rem 1.125rem;border-radius:var(--r-pill);border:var(--border);background:transparent;font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-medium);cursor:pointer;color:var(--slate-light);transition:var(--t-color)}
.tb.act,.tb:hover{background:var(--slate-dark);color:var(--white);border-color:var(--slate-dark)}
.up{display:none}
.up.act{display:grid;grid-template-columns:1fr 1fr;gap:var(--sp-5)}
.uc{background:var(--white);border:var(--border);border-radius:var(--r-md);padding:var(--sp-7) var(--sp-6)}
.utag{font-family:var(--font-mono);font-size:var(--detail-xs);letter-spacing:.06em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-3)}
.uct{font-family:var(--font-sans);font-size:var(--detail-l);font-weight:var(--fw-semibold);margin-bottom:var(--sp-3);color:var(--slate-dark)}
.ucd{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}
.uhl{background:var(--ivory-dark);border-radius:var(--r-sm);padding:var(--sp-3) var(--sp-4);margin-top:var(--sp-3);font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-medium);color:var(--slate-dark)}
.ulink{display:inline-block;margin-top:var(--sp-3);font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-semibold);color:var(--slate-dark);text-decoration:none;border-bottom:1px solid var(--cloud-light);transition:var(--t-base)}
.ulink:hover{border-color:var(--slate-dark)}
/* PROOF */
.pbg{background:var(--ivory-medium);border-top:var(--border);border-bottom:var(--border)}
.pgrd{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--sp-6)}
.prc{background:var(--white);border:var(--border);border-radius:var(--r-md);padding:var(--sp-7) var(--sp-6)}
.pra{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-3);letter-spacing:.06em}
.prc p{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}
/* TIMELINE */
.tl{border:var(--border);border-radius:var(--r-md);overflow:hidden;background:var(--white)}
.tlr{display:grid;grid-template-columns:88px 1fr 180px;align-items:stretch;border-bottom:1px solid var(--ivory-dark)}
.tlr:last-child{border-bottom:none}
.tlt{padding:1.125rem 1.375rem;font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-bold);color:var(--cloud-dark);border-right:1px solid var(--ivory-dark);display:flex;align-items:center}
.tla{padding:1.125rem 1.375rem;font-family:var(--font-serif);font-size:var(--detail-s);line-height:var(--lh-body);display:flex;align-items:center;color:var(--slate-dark)}
.tls{padding:1.125rem 1.25rem;font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);border-left:1px solid var(--ivory-dark);display:flex;align-items:center;justify-content:center;text-align:center;letter-spacing:.06em;text-transform:uppercase}
.sa{color:#4a7c59;background:#f0faf3}.sr{color:#92520b;background:#fef9ee}.se{color:#1a4fad;background:#eff4ff}
/* BRIEF */
.bc{background:var(--white);border:var(--border);border-radius:var(--r-md);padding:var(--sp-9) var(--sp-9)}
.btl{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--cloud-dark);margin-bottom:var(--sp-6)}
.mg{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--sp-5);margin-bottom:var(--sp-8);padding-bottom:var(--sp-8);border-bottom:1px solid var(--ivory-dark)}
.mv{font-family:var(--font-sans);font-size:var(--text-xs);font-weight:var(--fw-bold);letter-spacing:var(--ls-tight);line-height:1}
.mlbl{font-family:var(--font-serif);font-size:var(--detail-xs);color:var(--slate-light);margin-top:var(--sp-2);line-height:var(--lh-body)}
.md{font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);margin-top:var(--sp-1)}
.du{color:#c0392b}.dd{color:#27ae60}
.dh{font-family:var(--font-sans);font-size:var(--detail-s);font-weight:var(--fw-semibold);margin-bottom:var(--sp-4);color:var(--slate-dark)}
.dr{display:flex;align-items:flex-start;gap:var(--sp-3);padding:var(--sp-3) 0;border-bottom:1px solid var(--ivory-dark);font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-dark);line-height:var(--lh-body)}
.dr:last-child{border-bottom:none}
.dn{width:1.375rem;height:1.375rem;border-radius:50%;background:var(--slate-dark);color:var(--white);font-family:var(--font-mono);font-size:10px;font-weight:var(--fw-bold);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.125rem}
/* ROADMAP */
.rg{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--sp-4)}
.rcard{background:var(--white);border:var(--border);border-radius:var(--r-md);padding:var(--sp-7) var(--sp-6)}
.rno{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;color:var(--cloud-dark);margin-bottom:var(--sp-3)}
.rt{font-family:var(--font-sans);font-size:var(--detail-l);font-weight:var(--fw-semibold);margin-bottom:var(--sp-2);color:var(--slate-dark)}
.rd{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--slate-light);line-height:var(--lh-loose)}
/* CTA DARK */
.ctas{background:var(--slate-dark);color:var(--white);padding:var(--sp-12) 0;text-align:center}
/* FOOTER */
footer{background:var(--footer-bg);color:var(--footer-text);padding:var(--sp-11) 0 var(--sp-9)}
.fg{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:var(--sp-9);margin-bottom:var(--sp-10)}
.flo{font-family:var(--font-sans);font-size:var(--detail-l);font-weight:var(--fw-bold);display:block;margin-bottom:var(--sp-3)}
.ftag{font-family:var(--font-serif);font-size:var(--detail-s);color:var(--footer-muted);line-height:var(--lh-loose);max-width:260px}
.fc h4{font-family:var(--font-mono);font-size:var(--detail-xs);font-weight:var(--fw-medium);letter-spacing:.08em;text-transform:uppercase;color:var(--footer-muted);margin-bottom:var(--sp-4)}
.fc a{font-family:var(--font-sans);display:block;font-size:var(--detail-s);color:var(--footer-text);text-decoration:none;margin-bottom:var(--sp-2);transition:var(--t-color)}
.fc a:hover{color:var(--white)}
.fb{border-top:var(--footer-border) solid rgba(250,249,245,.10);padding-top:var(--sp-6);display:flex;align-items:center;justify-content:space-between}
.fc2,.fct{font-family:var(--font-mono);font-size:var(--detail-xs);color:var(--footer-muted)}
.fct a{color:var(--footer-text);text-decoration:none}
.fct a:hover{color:var(--white)}
.ar{display:flex;flex-wrap:wrap;gap:var(--sp-2);margin-top:var(--sp-9)}
@media(max-width:900px){:root{--section-gap:5rem}.con{padding:0 1.25rem}.nlinks{display:none}.sgrid,.pgrid,.tgrid,.rg,.fg{grid-template-columns:1fr 1fr}.split,.up.act,.mg{grid-template-columns:1fr}.tlr{grid-template-columns:80px 1fr}.tls{display:none}}
@media(max-width:550px){.sgrid,.rg,.fg{grid-template-columns:1fr}}
</style>
</head>
<body>''')

print('p1_head.html done')
