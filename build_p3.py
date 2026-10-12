
# ============================================================
# logistics.html
# ============================================================
def build_logistics():
    html = head("KimQ AI \u00b7 Logistics", CSS)
    html += NAV
    html += """
<section class="phero">
  <div class="con">
    <p class="kicker">05 / \u1ee8ng d\u1ee5ng \u00b7 Logistics</p>
    <h1>AI agent cho v\u1eadn h\u00e0nh logistics</h1>
    <p class="sub">Agent theo d\u00f5i h\u1ed3 s\u01a1 th\u00f4ng quan, nh\u1eafc h\u1ea1n v\u00e0 ph\u1ed1i h\u1ee3p v\u1edbi h\u00e3ng v\u1eadn chuy\u1ec3n. \u0110\u1ed9i logistics t\u1eadp trung x\u1eed l\u00fd ngo\u1ea1i l\u1ec7.</p>
  </div>
</section>"""
    html += """

<div class="con">
  <div class="pgcnav">
    <span class="pgcnav-label">Ngành</span>
    <a href="ke-toan.html">Kế toán</a>
    <a href="logistics.html" class="pgactive">Logistics</a>
    <a href="tai-chinh.html">Tài chính</a>
    <a href="nhan-su.html">Nhân sự</a>
  </div>
</div>
"""
    html += """
<section class="sec" style="padding-bottom:0">
  <div class="con">
    <div class="statrow">
      <div>
        <div class="stat-v">5,8 ng\u00e0y</div>
        <div class="stat-l">th\u1eddi gian th\u00f4ng quan trung b\u00ecnh</div>
        <div class="stat-d" style="color:#999">Theo d\u00f5i</div>
      </div>
      <div>
        <div class="stat-v">2,1 ng\u00e0y</div>
        <div class="stat-l">c\u1ea3nh b\u00e1o khi ch\u1eadm h\u01a1n chu\u1ea9n</div>
        <div class="stat-d up-c">Ng\u01b0\u1ee1ng</div>
      </div>
      <div>
        <div class="stat-v">24/7</div>
        <div class="stat-l">theo d\u00f5i l\u1ecbch t\u00e0u v\u00e0 h\u1ed3 s\u01a1</div>
        <div class="stat-d" style="color:#999">Li\u00ean t\u1ee5c</div>
      </div>
      <div>
        <div class="stat-v">0</div>
        <div class="stat-l">l\u00f4 h\u00e0ng b\u1ecb b\u1ecf s\u00f3t deadline</div>
        <div class="stat-d dn-c">K\u1ef7 l\u1ee5c</div>
      </div>
    </div>
  </div>
</section>"""

    html += """
<section class="sec">
  <div class="con">
    <p class="sl">Quy tr\u00ecnh \u00b7 Th\u00f4ng quan</p>
    <h2 class="sh">T\u1eeb booking \u0111\u1ebfn th\u00f4ng quan kh\u00f4ng tr\u1ec5</h2>
    <div class="flowbox">
      <div class="frow">
        <span class="fnum">01</span>
        <div class="fbody"><strong>Agent nh\u1eadn l\u1ecbch t\u00e0u v\u00e0 h\u1ed3 s\u01a1 th\u00f4ng quan t\u1eeb h\u00e3ng v\u1eadn chuy\u1ec3n</strong><span>\u0110\u1ecdc email, c\u1ed5ng th\u00f4ng tin, API h\u00e3ng t\u00e0u</span></div>
        <div class="fbadge"><span class="badge b-auto">T\u1ef1 x\u1eed l\u00fd</span></div>
      </div>
      <div class="frow">
        <span class="fnum">02</span>
        <div class="fbody"><strong>\u0110\u1ed1i chi\u1ebfu v\u1edbi booking, ph\u00e1t hi\u1ec7n l\u1ec7ch th\u00f4ng tin ho\u1eb7c thi\u1ebfu ch\u1ee9ng t\u1eeb</strong><span>Ki\u1ec3m tra B/L, C/O, packing list</span></div>
        <div class="fbadge"><span class="badge b-auto">T\u1ef1 x\u1eed l\u00fd</span></div>
      </div>
      <div class="frow">
        <span class="fnum">03</span>
        <div class="fbody"><strong>C\u1ea3nh b\u00e1o th\u00f4ng quan ch\u1eadm 2,1 ng\u00e0y, so\u1ea1n nh\u00e1p email nh\u1eafc h\u00e3ng t\u00e0u</strong><span>K\u00e8m s\u1ed1 ch\u1ee9ng t\u1eeb v\u00e0 timeline c\u1ee5 th\u1ec3</span></div>
        <div class="fbadge"><span class="badge b-rev">C\u1ea7n duy\u1ec7t</span></div>
      </div>
      <div class="frow">
        <span class="fnum">04</span>
        <div class="fbody"><strong>Tr\u01b0\u1edfng logistics duy\u1ec7t v\u00e0 g\u1eedi email trong 2 click</strong><span>Kh\u00f4ng c\u1ea7n so\u1ea1n l\u1ea1i t\u1eeb \u0111\u1ea7u</span></div>
        <div class="fbadge"><span class="badge b-exec">Ng\u01b0\u1eddi duy\u1ec7t</span></div>
      </div>
      <div class="frow">
        <span class="fnum">05</span>
        <div class="fbody"><strong>Agent theo d\u00f5i ph\u1ea3n h\u1ed3i, c\u1eadp nh\u1eadt timeline, nh\u1eafc l\u1ea1i n\u1ebfu qu\u00e1 4 gi\u1edd</strong><span>T\u1ef1 \u0111\u1ed9ng leo thang n\u1ebfu kh\u00f4ng c\u00f3 ph\u1ea3n h\u1ed3i</span></div>
        <div class="fbadge"><span class="badge b-auto">T\u1ef1 x\u1eed l\u00fd</span></div>
      </div>
    </div>
  </div>
</section>"""

    html += f"""
<section class="sec" style="background:#f5f4f0;padding:80px 0">
  <div class="con">
    <p class="sl">Use case \u00b7 Chi ti\u1ebft</p>
    <h2 class="sh">Hai agent cho v\u1eadn h\u00e0nh ngo\u00e0i</h2>
    <div class="grid2">
      <div class="card">
        <p class="card-tag">AI Logistics Document Agent</p>
        <p class="card-t">H\u1ed3 s\u01a1 th\u00f4ng quan v\u00e0 v\u1eadn chuy\u1ec3n</p>
        <p class="card-d">Agent theo d\u00f5i h\u1ed3 s\u01a1 th\u00f4ng quan, nh\u1eafc h\u1ea1n, \u0111\u1ed1i chi\u1ebfu v\u1edbi h\u00e3ng v\u1eadn chuy\u1ec3n v\u00e0 so\u1ea1n nh\u00e1p ch\u1ee9ng t\u1eeb thay \u0111\u1ed9i logistics.</p>
        <div class="card-hl">5,8 ng\u00e0y TB \u00b7 C\u1ea3nh b\u00e1o khi ch\u1eadm h\u01a1n chu\u1ea9n</div>
        {SVG_SPARK}
      </div>
      <div class="card">
        <p class="card-tag">V\u1eadn h\u00e0nh b\u00ean ngo\u00e0i</p>
        <p class="card-t">K\u1ebft n\u1ed1i nh\u00e0 cung c\u1ea5p v\u00e0 h\u00e3ng t\u00e0u</p>
        <p class="card-d">Agent theo d\u00f5i, \u0111\u1ed1i chi\u1ebfu v\u00e0 ph\u1ed1i h\u1ee3p v\u1edbi nh\u00e0 cung c\u1ea5p, h\u00e3ng v\u1eadn chuy\u1ec3n. Nh\u1eafc h\u1ea1n t\u1ef1 \u0111\u1ed9ng, kh\u00f4ng c\u1ea7n g\u1ecdi \u0111i\u1ec7n th\u1ee7 c\u00f4ng.</p>
        <div class="card-hl">T\u1ef1 \u0111\u1ed9ng nh\u1eafc h\u1ea1n \u00b7 Gi\u1ea3m th\u1eddi gian x\u1eed l\u00fd th\u1ee7 c\u00f4ng</div>
        {SVG_BAR_BEFORE_AFTER}
      </div>
    </div>
  </div>
</section>"""

    html += """
<section class="sec">
  <div class="con">
    <p class="sl">D\u1eef li\u1ec7u \u00b7 H\u00f4m nay</p>
    <h2 class="sh">Tr\u1ea1ng th\u00e1i l\u00f4 h\u00e0ng \u0111ang theo d\u00f5i</h2>
    <table class="dtbl">
      <thead><tr><th>L\u00f4 h\u00e0ng</th><th>H\u00e3ng t\u00e0u</th><th>Th\u00f4ng quan</th><th>Tr\u1ea1ng th\u00e1i</th><th>H\u00e0nh \u0111\u1ed9ng agent</th></tr></thead>
      <tbody>
        <tr><td>VN2024-001</td><td>Evergreen</td><td>5,2 ng\u00e0y</td><td><span class="tag tag-green">\u0110\u00fang h\u1ea1n</span></td><td>Theo d\u00f5i</td></tr>
        <tr><td>VN2024-002</td><td>OOCL</td><td>7,9 ng\u00e0y</td><td><span class="tag tag-red">Ch\u1eadm 2,1 ng\u00e0y</span></td><td>\u0110\u00e3 nh\u1eafc h\u00e3ng t\u00e0u</td></tr>
        <tr><td>VN2024-003</td><td>MSC</td><td>4,8 ng\u00e0y</td><td><span class="tag tag-green">\u0110\u00fang h\u1ea1n</span></td><td>Theo d\u00f5i</td></tr>
        <tr><td>VN2024-004</td><td>CMA CGM</td><td>Ch\u1edd ch\u1ee9ng t\u1eeb</td><td><span class="tag tag-orange">C\u1ea7n b\u1ed5 sung</span></td><td>So\u1ea1n nh\u00e1p email</td></tr>
        <tr><td>VN2024-005</td><td>Yang Ming</td><td>6,1 ng\u00e0y</td><td><span class="tag tag-orange">C\u1ea7n xem x\u00e9t</span></td><td>Ch\u1edd x\u00e1c nh\u1eadn</td></tr>
      </tbody>
    </table>
  </div>
</section>"""

    html += """
<section class="sec" style="background:#f5f4f0;padding:80px 0">
  <div class="con">
    <p class="sl">B\u1ea3n tin \u00b7 \u0110i\u1ec1u h\u00e0nh</p>
    <h2 class="sh">T\u1ed5ng quan logistics h\u00f4m nay</h2>
    <div class="brief">
      <div class="brief-hd">B\u1ea3n tin Logistics \u00b7 Th\u1ee9 Hai 08:00 \u00b7 T\u1ef1 \u0111\u1ed9ng</div>
      <div class="brief-metrics">
        <div><div class="bm-v">5,8 ng\u00e0y</div><div class="bm-l">Th\u00f4ng quan TB</div><div class="bm-d bm-up">T\u0103ng 2,1 ng\u00e0y</div></div>
        <div><div class="bm-v">3 l\u00f4</div><div class="bm-l">\u0110ang x\u1eed l\u00fd</div><div class="bm-d" style="color:#999">B\u00ecnh th\u01b0\u1eddng</div></div>
        <div><div class="bm-v">1 l\u00f4</div><div class="bm-l">Ch\u1eadm h\u1ea1n</div><div class="bm-d bm-up">C\u1ea7n duy\u1ec7t</div></div>
        <div><div class="bm-v">0 l\u00f4</div><div class="bm-l">Qu\u00e1 h\u1ea1n critical</div><div class="bm-d bm-dn">T\u1ed1t</div></div>
      </div>
      <div class="dec-list">
        <div class="dec"><span class="dn2">1</span><span>Duy\u1ec7t email nh\u1eafc h\u00e3ng t\u00e0u OOCL v\u1ec1 l\u00f4 VN2024-002 ch\u1eadm 2,1 ng\u00e0y</span></div>
        <div class="dec"><span class="dn2">2</span><span>B\u1ed5 sung C/O v\u00e0 packing list cho l\u00f4 VN2024-004 tr\u01b0\u1edbc 17:00 h\u00f4m nay</span></div>
        <div class="dec"><span class="dn2">3</span><span>X\u00e1c nh\u1eadn ph\u00ed l\u01b0u b\u00e3i 100 tri\u1ec7u cho l\u00f4 h\u00e0ng gia h\u1ea1n</span></div>
      </div>
    </div>
  </div>
</section>"""

    html += """
<section class="cta-strip">
  <div class="con">
    <h2>Xem AI agent logistics ch\u1ea1y th\u1eadt</h2>
    <p>B\u1eaft \u0111\u1ea7u t\u1eeb theo d\u00f5i th\u00f4ng quan. K\u1ebft n\u1ed1i h\u1ec7 th\u1ed1ng trong 3 ng\u00e0y, ch\u1ea1y th\u1eadt ngay tu\u1ea7n \u0111\u1ea7u.</p>
    <a href="mailto:contact@kimq.tech" class="bpw bpw-clay">\u0110\u1eb7t l\u1ecbch trao \u0111\u1ed5i</a>
    <a href="index.html" class="bsw">V\u1ec1 trang ch\u1ee7</a>
  </div>
</section>"""
    html += FOOTER
    html += "\n</body>\n</html>"
    return html

lg = build_logistics()
with open(r'C:\Users\admin\kimq-web\logistics.html', 'w', encoding='utf-8') as f:
    f.write(lg)
print(f"logistics.html: {len(lg.encode('utf-8'))} bytes")
