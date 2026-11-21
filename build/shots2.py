import json, sys
from shots import *
MID=["..2.....",
     ".22.5...",
     "1.2.555.",
     "11.34.46",
     "13334466",
     "1.3.4.36",
     "12.33.66",
     "1122.566"]
G1=["........","........","........","........","........","........","........","1122.566"]
G2=["...5....","..45....",".1.5.22.",".1.5.2..","331566.2","112.6622","12.3.562","1123.566"]
DAILY=["........","..6.....",".666.3..","1.63.33.","11.3.344","1122.544","11.22.54","1122.566"]
FULL=["11221122","33443344","11221122","33443344","11221122","33443344","11221122","3344.344"]
def score_up(p,n):
    p.evaluate("""n=>{for(let i=0;i<n;i++){window.__jaali.setTray(['i5_h','i3_h','mono']);window.__jaali.place(0,0,0);window.__jaali.place(1,0,5);}}""",n)
def run(p,name,vp):
    out=lambda n: OUT+n
    # 1 home
    p.screenshot(path=out(f"{name}_01_home.png"))
    # 2 mid
    J(p,"window.__jaali.newGame('classic')"); p.wait_for_timeout(400)
    score_up(p,34); p.wait_for_timeout(1600)
    J(p,"window.__jaali.setGrid(%s)"%json.dumps(MID)); J(p,"window.__jaali.setTray(['l4_1','t_0','domino_h'])")
    p.wait_for_timeout(900)
    p.screenshot(path=out(f"{name}_02_midgame.png"))
    # 3 line clear
    J(p,"window.__jaali.setGrid(%s)"%json.dumps(G1)); J(p,"window.__jaali.setTray(['mono','mono','l4_0'])"); p.wait_for_timeout(300)
    J(p,"window.__jaali.place(0,7,4)"); p.wait_for_timeout(1500)
    J(p,"window.__jaali.setGrid(%s)"%json.dumps(G2)); J(p,"window.__jaali.setTray(['mono','l4_0','domino_h'])"); p.wait_for_timeout(500)
    J(p,"window.__jaali.place(0,5,3)"); p.wait_for_timeout(380)
    p.screenshot(path=out(f"{name}_03_lineclear.png"))
    p.wait_for_timeout(1500)
    # 4 daily
    J(p,"window.__jaali.newGame('daily')"); p.wait_for_timeout(500)
    J(p,"window.__jaali.setGrid(%s)"%json.dumps(DAILY)); J(p,"window.__jaali.setTray(['corner3_1','i3_h','sq2'])"); p.wait_for_timeout(800)
    p.screenshot(path=out(f"{name}_04_daily.png"))
if __name__=="__main__":
    with sync_playwright() as pw:
        br=pw.chromium.launch(args=["--use-gl=swiftshader"])
        for name,vp,dsf,mob in [("p",(360,640),3,True)]:
            ctx,p=page(br,vp,dsf,mob); run(p,name,vp); ctx.close()
        br.close()
