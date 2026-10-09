from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        errors = []
        page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
        
        page.goto('https://avish-beep.github.io/Skill-wallet-project/', wait_until='domcontentloaded')
        page.wait_for_timeout(3000)
        
        title = page.title()
        print('Live Title:', title)
        print('Console Errors:', errors)
        
        video_src = page.evaluate('() => document.querySelector("video source") ? document.querySelector("video source").src : null')
        track_src = page.evaluate('() => document.querySelector("video track") ? document.querySelector("video track").src : null')
        print('Live Video Source:', video_src)
        print('Live Track Source:', track_src)
        
        page.screenshot(path='evidence/live_github_pages_verified.png', full_page=True)
        print('Captured live deployment evidence to evidence/live_github_pages_verified.png')
        browser.close()

if __name__ == '__main__':
    verify()
