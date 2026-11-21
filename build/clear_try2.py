import shots
from shots2 import *
from PIL import Image
ts=[150,170,190,210,230,250]
with sync_playwright() as pw:
    br=pw.chromium.launch(args=["--use-gl=swiftshader"])
    for t in ts:
        ctx,p=page(br,(360,640),3,True)
        J(p,"window.__jaali.newGame('classic')"); p.wait_for_timeout(300)
        score_up(p,34); p.wait_for_timeout(1500)
        J(p,"window.__jaali.setGrid(%s)"%json.dumps(G1)); J(p,"window.__jaali.setTray(['mono','mono','l4_0'])"); p.wait_for_timeout(300)
        J(p,"window.__jaali.place(0,7,4)"); p.wait_for_timeout(1500)
        J(p,"window.__jaali.setGrid(%s)"%json.dumps(G2)); J(p,"window.__jaali.setTray(['mono','l4_0','domino_h'])"); p.wait_for_timeout(500)
        J(p,"window.__jaali.place(0,5,3)"); p.wait_for_timeout(t)
        p.screenshot(path="/tmp/d_%d.png"%t,scale="css"); ctx.close()
    br.close()
ims=[Image.open("/tmp/d_%d.png"%t) for t in ts];w,h=ims[0].size
c=Image.new('RGB',(w*6,h))
for i,im in enumerate(ims):c.paste(im,(i*w,0))
c.save('/tmp/d_all.png')
