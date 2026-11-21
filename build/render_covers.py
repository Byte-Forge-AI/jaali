from playwright.sync_api import sync_playwright
O="/mnt/user-data/outputs/jaali/store/covers/"
with sync_playwright() as pw:
    br=pw.chromium.launch(args=["--allow-file-access-from-files"])
    def r(html,vw,vh,dsf,out):
        ctx=br.new_context(viewport={"width":vw,"height":vh},device_scale_factor=dsf);p=ctx.new_page()
        p.goto("file:///home/claude/jaali/build/"+html);p.wait_for_timeout(500);p.screenshot(path=O+out);ctx.close()
    r("cover.html",1920,1080,1,"cover-1920x1080.png")
    r("cover.html",1920,1080,800/1920,"thumb-800x450.png")
    r("cover43.html",1024,768,0.5,"thumb-512x384.png")
    br.close()
