import os

os.makedirs(r'C:\Users\admin\kimq-web', exist_ok=True)

CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:"Be Vietnam Pro",system-ui,sans-serif;background:#faf9f5;color:#141413;line-height:1.6;-webkit-font-smoothing:antialiased;font-size:15px}
.con{max-width:1200px;margin:0 auto;padding:0 40px}
nav{position:fixed;top:0;left:0;right:0;z-index:100;height:64px;background:rgba(250,249,245,.92);backdrop-filter:blur(12px);border-bottom:1px solid #d1cfc5;display:flex;align-items:center}
.ni{display:flex;align-items:center;width:100%;max-width:1200px;margin:0 auto;padding:0 40px}
.nl{font-size:1.125rem;font-weight:800;letter-spacing:-.03em;color:#141413;text-decoration:none;margin-right:auto;display:flex;align-items:center;gap:8px}
.lm{width:28px;height:28px;background:#141413;border-radius:4px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:900;flex-shrink:0}
.nlinks{display:flex;gap:28px}
.nlinks a{font-size:.875rem;font-weight:500;color:#141413;text-decoration:none;opacity:.6;transition:opacity .2s}
.nlinks a:hover{opacity:1}
.ncta{margin-left:28px;padding:.4375rem 1.125rem;background:#141413;color:#fff;border-radius:6px;font-size:.875rem;font-weight:500;text-decoration:none}
.phero{padding:calc(64px + 72px) 0 72px;border-bottom:1px solid #d1cfc5}
.kicker{font-family:"JetBrains Mono","Courier New",monospace;font-size:.6875rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:#999;margin-bottom:16px}
.phero h1{font-size:clamp(1.875rem,4vw,3rem);font-weight:800;letter-spacing:-.04em;line-height:1.08;max-width:720px;margin-bottom:20px;color:#141413}
.phero .sub{font-size:1.0625rem;font-weight:400;color:#5e5d59;max-width:520px;line-height:1.72}
.sec{padding:80px 0}
.sl{font-family:"JetBrains Mono","Courier New",monospace;font-size:.6875rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:#999;margin-bottom:14px}
.sh{font-size:clamp(1.25rem,2.4vw,1.875rem);font-weight:700;letter-spacing:-.025em;line-height:1.15;max-width:640px;margin-bottom:16px;color:#141413}
.sp{font-size:1rem;font-weight:400;color:#5e5d59;max-width:520px;line-height:1.65;margin-bottom:44px}
.dv{height:1px;background:#d1cfc5}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{background:#fff;border:1px solid #d1cfc5;border-radius:12px;padding:28px 24px}
.card-tag{font-family:"JetBrains Mono","Courier New",monospace;font-size:.625rem;font-weight:600;text-transform:uppercase;color:#999;margin-bottom:12px;letter-spacing:.08em}
.card-t{font-size:1.0625rem;font-weight:700;margin-bottom:10px;letter-spacing:-.02em;color:#141413}
.card-d{font-size:.875rem;font-weight:400;color:#5e5d59;line-height:1.65}
.card-hl{background:#f0eee6;border-radius:8px;padding:11px 14px;margin-top:13px;font-size:.8125rem;font-weight:500;line-height:1.5;color:#141413}
.statrow{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:44px 0;border-bottom:1px solid #d1cfc5}
.stat-v{font-size:2.25rem;font-weight:800;letter-spacing:-.04em;line-height:1;color:#141413}
.stat-l{font-size:.75rem;color:#5e5d59;margin-top:6px;line-height:1.5}
.stat-d{font-family:"JetBrains Mono","Courier New",monospace;font-size:.625rem;font-weight:600;margin-top:3px}
.up-c{color:#c0392b}.dn-c{color:#27ae60}
.flowbox{display:flex;flex-direction:column;border:1px solid #d1cfc5;border-radius:12px;overflow:hidden;background:#fff}
.frow{display:grid;grid-template-columns:2.75rem 1fr auto;align-items:stretch;border-bottom:1px solid #e8e6dc}
.frow:last-child{border-bottom:none}
.fnum{padding:18px 0 18px 18px;font-family:"JetBrains Mono","Courier New",monospace;font-size:.6875rem;font-weight:700;color:#bbb;display:flex;align-items:center}
.fbody{padding:18px 20px;font-size:.875rem;line-height:1.55;display:flex;flex-direction:column;gap:3px}
.fbody strong{font-weight:600;color:#141413}
.fbody span{font-size:.8125rem;color:#5e5d59}
.fbadge{padding:18px 20px;display:flex;align-items:center;justify-content:center;min-width:120px}
.badge{padding:4px 12px;border-radius:100px;font-family:"JetBrains Mono","Courier New",monospace;font-size:.5625rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}
.b-auto{background:#f0faf3;color:#2d7d46}
.b-rev{background:#fef9ee;color:#b45309}
.b-exec{background:#eff6ff;color:#1d4ed8}
.dtbl{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d1cfc5;border-radius:12px;overflow:hidden}
.dtbl th{text-align:left;font-family:"JetBrains Mono","Courier New",monospace;font-size:.5625rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#999;padding:12px 20px;background:#e8e6dc;border-bottom:1px solid #d1cfc5}
.dtbl td{padding:14px 20px;font-size:.875rem;border-bottom:1px solid #e8e6dc;vertical-align:top;color:#141413;line-height:1.55}
.dtbl tr:last-child td{border-bottom:none}
.dtbl tr td:first-child{font-weight:600}
.tag{display:inline-block;padding:2px 10px;border-radius:100px;font-family:"JetBrains Mono","Courier New",monospace;font-size:.5625rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.tag-green{background:#f0faf3;color:#2d7d46}
.tag-orange{background:#fef9ee;color:#b45309}
.tag-red{background:#fff5f5;color:#c0392b}
.tag-blue{background:#eff6ff;color:#1d4ed8}
.brief{background:#fff;border:1px solid #d1cfc5;border-radius:12px;padding:36px 32px}
.brief-hd{font-family:"JetBrains Mono","Courier New",monospace;font-size:.625rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#999;margin-bottom:24px}
.brief-metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding-bottom:28px;border-bottom:1px solid #e8e6dc;margin-bottom:24px}
.bm-v{font-size:1.5rem;font-weight:800;letter-spacing:-.03em;line-height:1;color:#141413}
.bm-l{font-size:.75rem;color:#5e5d59;margin-top:5px;line-height:1.4}
.bm-d{font-family:"JetBrains Mono","Courier New",monospace;font-size:.5625rem;font-weight:600;margin-top:3px}
.bm-up{color:#c0392b}.bm-dn{color:#27ae60}
.dec-list{display:flex;flex-direction:column}
.dec{display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-bottom:1px solid #e8e6dc;font-size:.875rem;color:#141413;line-height:1.55}
.dec:last-child{border-bottom:none}
.dn2{width:1.375rem;height:1.375rem;border-radius:50%;background:#141413;color:#fff;font-family:"JetBrains Mono","Courier New",monospace;font-size:.5625rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.mini-chart{margin-top:20px;padding:16px;background:#faf9f5;border:1px solid #e8e6dc;border-radius:8px}
.cta-strip{background:#141413;color:#fff;padding:80px 0;text-align:center}
.cta-strip h2{font-size:clamp(1.375rem,2.8vw,2rem);font-weight:700;letter-spacing:-.03em;margin-bottom:16px;color:#fff}
.cta-strip p{font-size:1rem;color:rgba(250,249,245,.55);margin-bottom:36px}
.bpw{padding:.875rem 1.875rem;background:#fff;color:#141413;border-radius:6px;font-size:.9375rem;font-weight:600;text-decoration:none;display:inline-block;letter-spacing:-.01em}
.bsw{padding:.875rem 1.75rem;background:transparent;color:#fff;border:1px solid rgba(250,249,245,.3);border-radius:6px;font-size:.9375rem;font-weight:400;text-decoration:none;display:inline-block;margin-left:12px}
footer{background:#1f1e1d;color:#faf9f5;padding:64px 0 40px}
.fg{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:48px}
.flo{font-size:1.125rem;font-weight:800;display:block;margin-bottom:12px;color:#faf9f5}
.ftag{font-size:.875rem;color:rgba(250,249,245,.45);line-height:1.65;max-width:260px}
.fc h4{font-family:"JetBrains Mono","Courier New",monospace;font-size:.5625rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:rgba(250,249,245,.35);margin-bottom:16px}
.fc a{display:block;font-size:.875rem;color:rgba(250,249,245,.65);text-decoration:none;margin-bottom:8px}
.fc a:hover{color:#faf9f5}
.fb{border-top:1px solid rgba(250,249,245,.1);padding-top:24px;display:flex;align-items:center;justify-content:space-between}
.fc2,.fct{font-family:"JetBrains Mono","Courier New",monospace;font-size:.6875rem;color:rgba(250,249,245,.35)}
.fct a{color:rgba(250,249,245,.55);text-decoration:none}
@media(max-width:900px){.con{padding:0 20px}.nlinks{display:none}.grid2,.grid3,.statrow,.brief-metrics,.fg{grid-template-columns:1fr 1fr}.frow{grid-template-columns:2.5rem 1fr}.fbadge{display:none}}
@media(max-width:550px){.grid2,.grid3,.statrow,.brief-metrics,.fg{grid-template-columns:1fr}}"""

GF = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">'

NAV = """<nav>
  <div class="ni">
    <a href="index.html" class="nl"><span class="lm">K</span>KimQ</a>
    <div class="nlinks">
      <a href="index.html#about">Ve KimQ</a>
      <a href="index.html#products">San pham AI</a>
      <a href="index.html#usecases">Ung dung</a>
      <a href="index.html#roadmap">Lo trinh</a>
    </div>
    <a href="mailto:contact@kimq.tech" class="ncta">Lien he tu van</a>
  </div>
</nav>"""

FOOTER = """<footer>
  <div class="con">
    <div class="fg">
      <div>
        <span class="flo">KimQ</span>
        <p class="ftag">Studio san pham so tai Viet Nam. Xay dung AI agent chay ngay tren du lieu va quy trinh doanh nghiep dang co.</p>
      </div>
      <div class="fc"><h4>San pham</h4><a href="index.html#products">KimQ Work</a><a href="index.html#products">KimQ Insight</a><a href="index.html#products">KimQ Flow</a></div>
      <div class="fc"><h4>Ung dung</h4><a href="ke-toan.html">Ke toan</a><a href="logistics.html">Logistics</a><a href="tai-chinh.html">Tai chinh</a><a href="nhan-su.html">Nhan su</a></div>
      <div class="fc"><h4>Cong ty</h4><a href="index.html#about">Ve KimQ</a><a href="index.html#roadmap">Lo trinh</a><a href="mailto:contact@kimq.tech">Lien he</a></div>
    </div>
    <div class="fb">
      <span class="fc2">&copy; 2026 KimQ. All rights reserved.</span>
      <span class="fct"><a href="mailto:contact@kimq.tech">contact@kimq.tech</a></span>
    </div>
  </div>
</footer>"""

print("Helpers OK, CSS len:", len(CSS))
