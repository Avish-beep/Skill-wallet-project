import os
import sys
import time
import subprocess
from playwright.sync_api import sync_playwright

def run_responsive_tests():
    evidence_dir = r"C:\Skillwallet\evidence\website_responsive"
    os.makedirs(evidence_dir, exist_ok=True)
    
    # 1. Start local preview server for website dist
    dist_dir = r"C:\Skillwallet\website\dist"
    server_process = subprocess.Popen(
        [sys.executable, "-m", "http.server", "5173", "--directory", dist_dir],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(2)
    
    target_url = "http://localhost:5173/Skill-wallet-project/"
    
    viewports = [
        {"name": "desktop_1920x1080", "width": 1920, "height": 1080},
        {"name": "laptop_1440x900", "width": 1440, "height": 900},
        {"name": "tablet_768x1024", "width": 768, "height": 1024},
        {"name": "mobile_390x844", "width": 390, "height": 844}
    ]
    
    results = []
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            
            for vp in viewports:
                context = browser.new_context(viewport={"width": vp["width"], "height": vp["height"]})
                page = context.new_page()
                
                # Navigate
                page.goto(target_url, wait_until="networkidle", timeout=15000)
                time.sleep(1)
                
                # Check title
                title = page.title()
                
                # Check for horizontal scroll / overflow
                scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
                client_w = page.evaluate("() => document.documentElement.clientWidth")
                has_overflow = scroll_w > client_w
                
                # Take screenshot
                ss_path = os.path.join(evidence_dir, f"{vp['name']}.png")
                page.screenshot(path=ss_path, full_page=True)
                
                status = "PASS" if not has_overflow else "FAIL (Overflow)"
                results.append({
                    "viewport": f"{vp['width']}x{vp['height']} ({vp['name']})",
                    "status": status,
                    "scroll_width": scroll_w,
                    "client_width": client_w,
                    "screenshot": ss_path
                })
                print(f"Tested {vp['name']}: {status} (scrollWidth: {scroll_w}, clientWidth: {client_w})")
                context.close()
                
            browser.close()
    finally:
        server_process.terminate()
        server_process.wait()
        
    print("\n=== RESPONSIVE TEST RESULTS ===")
    for r in results:
        print(f"[{r['status']}] {r['viewport']} -> Screenshot: {r['screenshot']}")

if __name__ == "__main__":
    run_responsive_tests()
