# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
content = open('build_kimq.py','r',encoding='utf-8').read()
for bp in ['build_p2.py','build_p3.py','build_p4.py','build_p5.py']:
    content += open(bp,'r',encoding='utf-8').read()
exec(content)
