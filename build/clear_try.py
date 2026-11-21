import shots
from shots2 import *
with sync_playwright() as pw:
    br=pw.chromium.launch(args=["--use-gl=swiftshader"])
    for seed in (12345,777):
        shots.RSEED=seed
        for t in (180,300):
            ctx,p=page(br,(360,640),3,True)
            J(p,"window.__jaali.newGame('classic')"); p.wait_for_timeout(300)
            score_up(p,34); p.wait_for_timeout(1500)
            J(p,"window.__jaali.setGrid(%s)"%json.dumps(G1)); J(p,"window.__jaali.setTray(['mono','mono','l4_0'])"); p.wait_for_timeout(300)
            J(p,"window.__jaali.place(0,7,4)"); p.wait_for_timeout(1500)
            J(p,"window.__jaali.setGrid(%s)"%json.dumps(G2)); J(p,"window.__jaali.setTray(['mono','l4_0','domino_h'])"); p.wait_for_timeout(500)
            J(p,"window.__jaali.place(0,5,3)"); p.wait_for_timeout(t)
            p.screenshot(path="/tmp/c_%d_%d.png"%(seed,t),scale="css")
            ctx.close()
    br.close()
