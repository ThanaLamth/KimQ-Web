
# ============================================================
# ke-toan.html
# ============================================================
def build_ke_toan():
    html = head("KimQ AI \u00b7 K\u1ebf to\u00e1n", CSS)
    html += NAV
    html += """
<section class="phero">
  <div class="con">
    <p class="kicker">05 / \u1ee8ng d\u1ee5ng \u00b7 K\u1ebf to\u00e1n</p>
    <h1>AI agent cho \u0111\u1ed9i k\u1ebf to\u00e1n</h1>
    <p class="sub">Agent t\u1ef1 \u0111\u1ed9ng \u0111\u1ed1i chi\u1ebfu sao k\u00ea, kh\u1edbp h\u00f3a \u0111\u01a1n v\u00e0 b\u00e1o c\u00e1o kho\u1ea3n treo tr\u01b0\u1edbc gi\u1edd l\u00e0m vi\u1ec7c. K\u1ebf to\u00e1n ch\u1ec9 xem v\u00e0 quy\u1ebft \u0111\u1ecbnh.</p>
  </div>
</section>"""
    html += """

<div class="con">
  <div class="pgcnav">
    <span class="pgcnav-label">Ngành àp dụng</span>
    <a href="ke-toan.html" class="pgactive">Kế toán</a>
    <a href="logistics.html">Logistics</a>
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
        <div class="stat-v">38/41</div>
        <div class="stat-l">giao d\u1ecbch t\u1ef1 kh\u1edbp m\u1ed7i ng\u00e0y</div>
        <div class="stat-d dn-c">T\u1ef1 \u0111\u1ed9ng</div>
      </div>
      <div>
        <div class="stat-v">06:00</div>
        <div class="stat-l">b\u1eaft \u0111\u1ea7u \u0111\u1ed1i so\u00e1t sao k\u00ea</div>
        <div class="stat-d" style="color:#999">M\u1ed7i s\u00e1ng</div>
      </div>
      <div>
        <div class="stat-v">3</div>
        <div class="stat-l">kho\u1ea3n treo b\u00e1o c\u00e1o ngay</div>
        <div class="stat-d up-c">C\u1ea7n xem</div>
      </div>
      <div>
        <div class="stat-v">0</div>
        <div class="stat-l">l\u1ea7n b\u1ecf s\u00f3t deadline</div>
        <div class="stat-d dn-c">K\u1ef7 l\u1ee5c</div>
      </div>
    </div>
  </div>
</section>"""

    html += """
<section class="sec">
  <div class="con">
    <p class="sl">Quy tr\u00ecnh \u00b7 H\u1eb1ng ng\u00e0y</p>
    <h2 class="sh">T\u1eeb sao k\u00ea \u0111\u1ebfn b\u1ea3n tin trong 1 gi\u1edd</h2>
    <div class="flowbox">
      <div class="frow">
        <span class="fnum">01</span>
        <div class="fbody"><strong>06:00 Agent k\u1ebft n\u1ed1i sao k\u00ea ng\u00e2n h\u00e0ng \u0111\u00eam qua</strong><span>T\u1ef1 \u0111\u1ed9ng t\u1ea3i d\u1eef li\u1ec7u t\u1eeb VCB, Techcombank, BIDV</span></div>
        <div class="fbadge"><span class="badge b-auto">T\u1ef1 x\u1eed l\u00fd</span></div>
      </div>
      <div class="frow">
        <span class="fnum">02</span>
        <div class="fbody"><strong>Agent kh\u1edbp t\u1eebng giao d\u1ecbch v\u1edbi h\u00f3a \u0111\u01a1n trong h\u1ec7 th\u1ed1ng</strong><span>So s\u00e1nh s\u1ed1 ti\u1ec1n, ng\u00e0y, m\u00e3 tham chi\u1ebfu</span></div>
        <div class="fbadge"><span class="badge b-auto">T\u1ef1 x\u1eed l\u00fd</span></div>
      </div>
      <div class="frow">
        <span class="fnum">03</span>
        <div class="fbody"><strong>38 giao d\u1ecbch kh\u1edbp t\u1ef1 \u0111\u1ed9ng, ghi nh\u1eadt k\u00fd ki\u1ec3m to\u00e1n</strong><span>Ghi timestamp v\u00e0 ngu\u1ed3n d\u1eef li\u1ec7u</span></div>
        <div class="fbadge"><span class="badge b-auto">T\u1ef1 x\u1eed l\u00fd</span></div>
      </div>
      <div class="frow">
        <span class="fnum">04</span>
        <div class="fbody"><strong>3 kho\u1ea3n kh\u00f4ng kh\u1edbp: ph\u00e2n lo\u1ea1i v\u00e0 so\u1ea1n c\u00e2u h\u1ecfi</strong><span>K\u00e8m b\u1eb1ng ch\u1ee9ng c\u1ee5 th\u1ec3 cho t\u1eebng kho\u1ea3n</span></div>
        <div class="fbadge"><span class="badge b-rev">C\u1ea7n x\u00e1c nh\u1eadn</span></div>
      </div>
      <div class="frow">
        <span class="fnum">05</span>
        <div class="fbody"><strong>K\u1ebf to\u00e1n nh\u1eadn danh s\u00e1ch kho\u1ea3n treo l\u00fac 07:00, x\u00e1c nh\u1eadn 2 kho\u1ea3n</strong><span>Thao t\u00e1c trong 2 click</span></div>
        <div class="fbadge"><span class="badge b-exec">Ng\u01b0\u1eddi duy\u1ec7t</span></div>
      </div>
      <div class="frow">
        <span class="fnum">06</span>
        <div class="fbody"><strong>1 kho\u1ea3n treo chuy\u1ec3n k\u1ebf to\u00e1n tr\u01b0\u1edfng k\u00e8m b\u1eb1ng ch\u1ee9ng \u0111\u1ea7y \u0111\u1ee7</strong><span>B\u00e1o c\u00e1o t\u1ef1 \u0111\u1ed9ng so\u1ea1n s\u1eb5n</span></div>
        <div class="fbadge"><span class="badge b-exec">Ng\u01b0\u1eddi duy\u1ec7t</span></div>
      </div>
    </div>
  </div>
</section>"""

    html += f"""
<section class="sec" style="background:#f5f4f0;padding:80px 0">
  <div class="con">
    <p class="sl">Use case \u00b7 Chi ti\u1ebft</p>
    <h2 class="sh">Hai agent ch\u1ea1y song song</h2>
    <div class="grid2">
      <div class="card">
        <p class="card-tag">AI Invoice / AP Agent</p>
        <p class="card-t">X\u1eed l\u00fd h\u00f3a \u0111\u01a1n v\u00e0 c\u00f4ng n\u1ee3</p>
        <p class="card-d">Agent tra h\u00f3a \u0111\u01a1n, kh\u1edbp c\u00f4ng n\u1ee3, g\u1ee3i \u00fd b\u01b0\u1edbc ti\u1ebfp theo v\u00e0 so\u1ea1n nh\u00e1p. K\u1ebf to\u00e1n ki\u1ec3m tra kho\u1ea3n treo, kh\u00f4ng c\u1ea7n nh\u1eadp li\u1ec7u l\u1ea1i.</p>
        <div class="card-hl">41 giao d\u1ecbch \u00b7 38 t\u1ef1 kh\u1edbp \u00b7 3 kho\u1ea3n treo b\u00e1o c\u00e1o</div>
        {SVG_BAR}
      </div>
      <div class="card">
        <p class="card-tag">AI Reconciliation Agent</p>
        <p class="card-t">\u0110\u1ed1i so\u00e1t ng\u00e2n h\u00e0ng h\u1eb1ng ng\u00e0y</p>
        <p class="card-d">06:00 s\u00e1ng, agent \u0111\u1ed1i chi\u1ebfu sao k\u00ea \u0111\u00eam qua, ph\u00e2n lo\u1ea1i giao d\u1ecbch v\u00e0 b\u00e1o c\u00e1o kho\u1ea3n treo tr\u01b0\u1edbc gi\u1edd l\u00e0m vi\u1ec7c.</p>
        <div class="card-hl">B\u00e1o c\u00e1o ho\u00e0n t\u1ea5t tr\u01b0\u1edbc 07:00 \u00b7 Kh\u00f4ng c\u1ea7n nh\u00e2n s\u1ef1 v\u00e0o s\u1edbm</div>
        {SVG_SPARK}
      </div>
    </div>
  </div>
</section>"""

    html += """
<section class="sec">
  <div class="con">
    <p class="sl">D\u1eef li\u1ec7u \u00b7 Ph\u00e2n lo\u1ea1i</p>
    <h2 class="sh">Ph\u00e2n lo\u1ea1i giao d\u1ecbch theo agent</h2>
    <table class="dtbl">
      <thead><tr><th>Lo\u1ea1i giao d\u1ecbch</th><th>Tr\u1ea1ng th\u00e1i</th><th>X\u1eed l\u00fd b\u1edfi</th><th>Th\u1eddi gian</th></tr></thead>
      <tbody>
        <tr><td>Thanh to\u00e1n nh\u00e0 cung c\u1ea5p</td><td><span class="tag tag-green">Kh\u1edbp t\u1ef1 \u0111\u1ed9ng</span></td><td>Agent</td><td>2 gi\u00e2y</td></tr>
        <tr><td>Ho\u00e0n ti\u1ec1n kh\u00e1ch h\u00e0ng</td><td><span class="tag tag-green">Kh\u1edbp t\u1ef1 \u0111\u1ed9ng</span></td><td>Agent</td><td>2 gi\u00e2y</td></tr>
        <tr><td>Ph\u00ed ng\u00e2n h\u00e0ng</td><td><span class="tag tag-green">Ph\u00e2n lo\u1ea1i t\u1ef1 \u0111\u1ed9ng</span></td><td>Agent</td><td>2 gi\u00e2y</td></tr>
        <tr><td>Giao d\u1ecbch ch\u01b0a c\u00f3 h\u00f3a \u0111\u01a1n</td><td><span class="tag tag-orange">C\u1ea7n x\u00e1c nh\u1eadn</span></td><td>K\u1ebf to\u00e1n</td><td>5 ph\u00fat</td></tr>
        <tr><td>Giao d\u1ecbch tr\u00f9ng s\u1ed1 ti\u1ec1n</td><td><span class="tag tag-red">Chuy\u1ec3n k\u1ebf to\u00e1n tr\u01b0\u1edfng</span></td><td>K\u1ebf to\u00e1n tr\u01b0\u1edfng</td><td>15 ph\u00fat</td></tr>
      </tbody>
    </table>
  </div>
</section>"""

    html += """
<section class="sec" style="background:#f5f4f0;padding:80px 0">
  <div class="con">
    <p class="sl">B\u1ea3n tin \u00b7 07:00 s\u00e1ng</p>
    <h2 class="sh">B\u00e1o c\u00e1o \u0111i\u1ec1u h\u00e0nh k\u1ebf to\u00e1n</h2>
    <div class="brief">
      <div class="brief-hd">B\u1ea3n tin k\u1ebf to\u00e1n \u00b7 Th\u1ee9 Hai 07:00 \u00b7 T\u1ef1 \u0111\u1ed9ng</div>
      <div class="brief-metrics">
        <div><div class="bm-v">21,4 t\u1ef7</div><div class="bm-l">Chi ph\u00ed v\u1eadn h\u00e0nh</div><div class="bm-d bm-up">T\u0103ng 7%</div></div>
        <div><div class="bm-v">3,6 t\u1ef7</div><div class="bm-l">C\u00f4ng n\u1ee3 qu\u00e1 h\u1ea1n</div><div class="bm-d bm-up">T\u0103ng 28%</div></div>
        <div><div class="bm-v">38</div><div class="bm-l">Giao d\u1ecbch kh\u1edbp</div><div class="bm-d bm-dn">T\u1ef1 \u0111\u1ed9ng</div></div>
        <div><div class="bm-v">3</div><div class="bm-l">Kho\u1ea3n treo</div><div class="bm-d bm-up">C\u1ea7n xem</div></div>
      </div>
      <div class="dec-list">
        <div class="dec"><span class="dn2">1</span><span>Ph\u00e1t h\u00e0nh l\u1ea1i 14 h\u00f3a \u0111\u01a1n: agent \u0111\u00e3 x\u00e1c \u0111\u1ecbnh nguy\u00ean nh\u00e2n v\u00e0 so\u1ea1n s\u1eb5n n\u1ed9i dung</span></div>
        <div class="dec"><span class="dn2">2</span><span>Ph\u00ea duy\u1ec7t ph\u00ed l\u01b0u b\u00e3i 100 tri\u1ec7u: l\u00f4 h\u00e0ng th\u00f4ng quan ch\u1eadm, h\u00e3ng t\u00e0u \u0111\u1ec1 ngh\u1ecb gia h\u1ea1n</span></div>
        <div class="dec"><span class="dn2">3</span><span>X\u00e1c nh\u1eadn chuy\u1ec3n kho\u1ea3n treo 85 tri\u1ec7u t\u1eeb VCB ch\u01b0a kh\u1edbp v\u1edbi h\u00f3a \u0111\u01a1n n\u00e0o</span></div>
      </div>
    </div>
  </div>
</section>"""

    html += """
<section class="cta-strip">
  <div class="con">
    <h2>Xem AI agent k\u1ebf to\u00e1n ch\u1ea1y th\u1eadt</h2>
    <p>B\u1eaft \u0111\u1ea7u t\u1eeb nghi\u1ec7p v\u1ee5 \u0111\u1ed1i so\u00e1t. Ch\u00fang t\u00f4i k\u1ebft n\u1ed1i, ch\u1ea1y th\u1eed v\u00e0 b\u00e0n giao trong tu\u1ea7n \u0111\u1ea7u.</p>
    <a href="mailto:contact@kimq.tech" class="bpw bpw-clay">\u0110\u1eb7t l\u1ecbch trao \u0111\u1ed5i</a>
    <a href="index.html" class="bsw">V\u1ec1 trang ch\u1ee7</a>
  </div>
</section>"""
    html += FOOTER
    html += "\n</body>\n</html>"
    return html

kt = build_ke_toan()
with open(r'C:\Users\admin\kimq-web\ke-toan.html', 'w', encoding='utf-8') as f:
    f.write(kt)
print(f"ke-toan.html: {len(kt.encode('utf-8'))} bytes")
