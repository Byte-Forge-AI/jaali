import math
from playwright.sync_api import sync_playwright
OUT="/mnt/user-data/outputs/jaali/store/"
cx,sy=512,500   # arch centre, spring line
Ro,Ri=290,212
base=905
def arch(R,y0):  # path of arch with semicircle top, down to y0
    return f"M{cx-R} {y0}V{sy}A{R} {R} 0 0 1 {cx+R} {sy}V{y0}Z"
outer=arch(Ro,base); inner=arch(Ri,base-48)
ring=arch(Ro-26,base-20)
def star(ox,oy,ro,ri,n=8):
    pts=[]
    for k in range(n*2):
        a=-math.pi/2+k*math.pi/n; r=ro if k%2==0 else ri
        pts.append(f"{ox+r*math.cos(a):.1f} {oy+r*math.sin(a):.1f}")
    return "M"+"L".join(pts)+"Z"
J={'ruby':('#ff9aa8','#d93a55','#7d1230'),'blue':('#9ccaff','#2f74e8','#16358f'),'emer':('#86f0c6','#1fae82','#0b5a45'),
   'gold':('#fff0a8','#f5b02e','#9a5d0c'),'teal':('#97f3f7','#18b4c4','#0a5f73'),'orange':('#ffd0a2','#f2733a','#a03a10')}
defs=''.join(f'<linearGradient id="g_{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset=".5" stop-color="{b}"/><stop offset="1" stop-color="{c}"/></linearGradient>' for k,(a,b,c) in J.items())
h=96; sh_=84
def dia(x,y,r): return f"M{x} {y-r}L{x+r} {y}L{x} {y+r}L{x-r} {y}Z"
layout={ (300,512):'gold',(396,416):'ruby',(396,608):'blue',(492,320):'teal',(492,512):None,(492,704):'orange',
 (588,416):'emer',(588,608):'ruby',(684,320):'blue',(684,512):'gold',(684,704):'emer',(780,416):'orange',(780,608):None,(876,512):'teal',(204,512):'blue'}
panes='';glows='';sv=''
for (y,x),k in layout.items():
    if k is None:
        panes+=f'<path d="{dia(x,y,sh_)}" fill="url(#night)" stroke="#3a2210" stroke-width="6"/>'
        sv+=f'<path d="{star(x,y,50,24)}" fill="#ffd27a" stroke="#fff3c4" stroke-width="3" stroke-linejoin="round" filter="url(#glow2)"/>'
        continue
    glows+=f'<path d="{dia(x,y,sh_+10)}" fill="{J[k][1]}" filter="url(#blur)" opacity=".8"/>'
    panes+=(f'<path d="{dia(x,y,sh_)}" fill="url(#g_{k})" stroke="#3a2210" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M{x} {y-sh_+10}L{x+sh_-10} {y}L{x+ (sh_-10)*0.2} {y-(sh_-10)*0.2}Z" fill="#fff" opacity=".22"/>'
            f'<path d="{dia(x,y,sh_-12)}" fill="none" stroke="#fff" stroke-opacity=".4" stroke-width="3"/>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>{defs}
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a0e2b"/><stop offset=".55" stop-color="#1b2766"/><stop offset=".85" stop-color="#6a4a78"/><stop offset="1" stop-color="#e08a4a"/></linearGradient>
<radialGradient id="horizon" cx=".5" cy="1.05" r=".75"><stop offset="0" stop-color="#ffb35c" stop-opacity=".95"/><stop offset=".5" stop-color="#e2663e" stop-opacity=".35"/><stop offset="1" stop-color="#e2663e" stop-opacity="0"/></radialGradient>
<linearGradient id="sand" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6dfb4"/><stop offset=".45" stop-color="#d8aa70"/><stop offset="1" stop-color="#9c6a3c"/></linearGradient>
<linearGradient id="night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1240"/><stop offset="1" stop-color="#2b2f78"/></linearGradient>
<clipPath id="ic"><path d="{inner}"/></clipPath>
<filter id="blur" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="22"/></filter>
<filter id="glow2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#000" flood-opacity=".55"/></filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/><rect width="1024" height="1024" fill="url(#horizon)"/>
<g fill="#fff"><circle cx="120" cy="140" r="4"/><circle cx="880" cy="110" r="3"/><circle cx="930" cy="300" r="3.5"/><circle cx="90" cy="360" r="3"/><circle cx="200" cy="60" r="2.5"/><circle cx="820" cy="420" r="2.5"/></g>
<path d="M512 120L534 168L512 216L490 168Z" fill="url(#sand)" stroke="#3f2410" stroke-width="6" stroke-linejoin="round"/>
<g filter="url(#sh)"><path d="{outer}" fill="url(#sand)" stroke="#3f2410" stroke-width="10" stroke-linejoin="round"/></g>
<path d="{ring}" fill="none" stroke="#6b4526" stroke-width="7"/><path d="{ring}" fill="none" stroke="#fbe6bd" stroke-opacity=".7" stroke-width="3" transform="translate(4 4)"/>
<g clip-path="url(#ic)"><rect x="280" y="240" width="470" height="680" fill="url(#sand)"/><circle cx="512" cy="880" r="230" fill="#ffb35c" opacity=".55" filter="url(#blur)"/>
{glows}{panes}{sv}
</g>
<path d="{inner}" fill="none" stroke="#3a2210" stroke-width="10"/><path d="{inner}" fill="none" stroke="#ffe5b0" stroke-opacity=".55" stroke-width="3" transform="translate(0 -5)"/>
<path d="M{cx-Ro-34} {base-26}H{cx+Ro+34}V{base+36}H{cx-Ro-34}Z" fill="url(#sand)" stroke="#3f2410" stroke-width="8" stroke-linejoin="round"/>
<path d="M{cx-Ro-20} {base-14}H{cx+Ro+20}" stroke="#fbe6bd" stroke-opacity=".7" stroke-width="3"/>
</svg>'''
open(OUT+"icon.svg","w").write(svg)
with sync_playwright() as pw:
    br=pw.chromium.launch()
    for s in (1024,512,64):
        ctx=br.new_context(viewport={"width":s,"height":s}); p=ctx.new_page()
        p.goto("about:blank")
        SVGS=svg.replace('width="1024" height="1024"','width="%d" height="%d"'%(s,s),1)
        p.set_content(f'<body style="margin:0;background:#000">{SVGS}')
        p.wait_for_timeout(300)
        p.screenshot(path=(OUT+f"icon-{s}.png" if s!=64 else "/tmp/icon64.png"))
        ctx.close()
    br.close()
