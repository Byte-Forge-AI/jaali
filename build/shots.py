import json, sys
from playwright.sync_api import sync_playwright
URL="file:///home/claude/game/index.html"
OUT="/mnt/user-data/outputs/jaali/store/screenshots/"
DATE="2026-11-21"
RSEED=777
def seed(extra):
    d={"best":5240,"streak":6,"lastDaily":"2026-11-20","dailyDate":"2026-11-20","dailyScore":1480,"dailyDone":True,"dailyBest":1480,"sound":True,"overs":3,"seenHint":True,"dailySave":None}
    d.update(extra); return "try{localStorage.setItem('jaali.v1',%s)}catch(e){}" % json.dumps(json.dumps(d))
def page(br, vp, dsf, mobile, extra={}):
    ctx=br.new_context(viewport={"width":vp[0],"height":vp[1]},device_scale_factor=dsf,is_mobile=mobile,has_touch=mobile)
    ctx.add_init_script(seed(extra)); ctx.add_init_script('(function(){var s=%d;Math.random=function(){s=(s*1664525+1013904223)%%4294967296;return s/4294967296;}})()' % RSEED)
    p=ctx.new_page(); p.goto(URL+"?date="+DATE); p.wait_for_timeout(700); return ctx,p
J=lambda p,s: p.evaluate(s)
MID=["........",
     "..#.....",
     ".###..#.",
     "#####.##",
     "####..##",
     "######.#",
     "#.#####.",
     "########"]
# board with colours: use numbers 1..6
MIDC=["........",
      "..2.....",
      ".222..4.",
      "11333.44",
      "1133..44",
      "165333.4",
      "1.55633.",
      "11556633"]
# fixed: just make a pleasing board with numeric colours
BOARD=["........",
       "...5....",
       "..555.4.",
       ".3.5.444",
       "133..6.4",
       "13322661",
       "12222611",
       "12.22.11"]
# line clear setup: row 5 and col 1 nearly full
CLR=["........",
     "..4.....",
     ".1444.22",
     "11.....2",
     "33.55.62",
     "33.5.662",
     "1.2255.6",
     "1122.566"]
def stage(p, mode, grid, tray):
    J(p,"window.__jaali.newGame('%s')"%mode)
    p.wait_for_timeout(500)
    J(p,"window.__jaali.setGrid(%s)"%json.dumps(grid))
    J(p,"window.__jaali.setTray(%s)"%json.dumps(tray))
    p.wait_for_timeout(500)
def setscore(p,score):
    pass
if __name__=="__main__":
    with sync_playwright() as pw:
        br=pw.chromium.launch(args=["--use-gl=swiftshader"])
        for name,vp,dsf,mob in [("p",(360,640),3,True),("l",(1920,1080),1,False)]:
            ctx,p=page(br,vp,dsf,mob)
            p.screenshot(path="/tmp/%s_home.png"%name)
            stage(p,"classic",BOARD,["i3_h","l3_0","square"] if False else ["domino_h","mono","i3_v"])
            p.screenshot(path="/tmp/%s_mid.png"%name)
            print(J(p,"JSON.stringify(window.__jaali.state())")[:300])
            ctx.close()
        br.close()
