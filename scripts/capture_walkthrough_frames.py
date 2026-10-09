import os
import sys
import asyncio
from playwright.sync_api import sync_playwright

def capture_website_walkthrough_frames():
    output_dir = r"C:\Skillwallet\evidence\walkthrough_frames"
    os.makedirs(output_dir, exist_ok=True)
    
    url = "https://avish-beep.github.io/Skill-wallet-project/"
    
    print("Launching Chromium to capture real website walkthrough...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 1920x1080 Full HD
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)
        
        scenes = [
            {"id": "w01_hero", "scroll": 0, "name": "Homepage Header & Hero Overview"},
            {"id": "w02_problem", "selector": "text=Problem Statement & Research Scope", "name": "Problem Statement & Analytical Scope"},
            {"id": "w03_methodology", "selector": "#methodology", "name": "End-to-End Methodology Pipeline"},
            {"id": "w04_dashboard", "selector": "#dashboard", "name": "Tableau Public Dashboard Section"},
            {"id": "w05_findings", "selector": "#findings", "name": "Reproducible Analytical Findings Cards"},
            {"id": "w06_story", "selector": "#story", "name": "Project Story Scrollytelling"},
            {"id": "w07_video", "selector": "#video", "name": "Presentation Video Player & Chapter Markers"},
            {"id": "w08_docs", "selector": "#docs", "name": "Repository Artifacts & Documentation Grid"}
        ]
        
        for sc in scenes:
            if "selector" in sc:
                el = page.locator(sc["selector"]).first
                if el.count() > 0:
                    el.scroll_into_view_if_needed()
                    page.wait_for_timeout(1000)
            elif "scroll" in sc:
                page.evaluate(f"window.scrollTo(0, {sc['scroll']})")
                page.wait_for_timeout(1000)
                
            frame_path = os.path.join(output_dir, f"{sc['id']}.png")
            page.screenshot(path=frame_path)
            print(f"Captured: {sc['name']} -> {frame_path}")
            
        browser.close()
    print("All walkthrough frames captured successfully!")

if __name__ == "__main__":
    asyncio.run(capture_website_walkthrough_frames())
