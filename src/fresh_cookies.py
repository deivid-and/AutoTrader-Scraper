from playwright.sync_api import sync_playwright

def get_fresh_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://www.autotrader.co.uk/")
        
        page.wait_for_load_state("networkidle")

        cookies = context.cookies()
        browser.close()
        
        formatted_cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        return formatted_cookies