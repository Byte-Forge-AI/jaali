from shots2 import *
with sync_playwright() as pw:
    br=pw.chromium.launch(args=["--use-gl=swiftshader"])
    ctx,p=page(br,(360,640),3,True,{"lastDaily":"2026-11-20","streak":6,"dailyDone":False,"dailyDate":""})
    J(p,"window.__jaali.newGame('daily')"); p.wait_for_timeout(500)
    score_up(p,20); p.wait_for_timeout(1500)
    J(p,"window.__jaali.setGrid(%s)"%json.dumps(FULL)); J(p,"window.__jaali.setTray(['sq3','sq2','domino_h'])")
    p.wait_for_timeout(2500)
    p.screenshot(path="/tmp/over.png")
    J(p,"document.querySelector('#over button, .overlay button') && 0")
    print(J(p,"JSON.stringify(window.__jaali.state()).slice(0,200)"))
    br.close()
