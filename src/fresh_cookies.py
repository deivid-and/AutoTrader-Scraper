from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import time

def get_fresh_cookies():
    """Fetch fresh cookies with retries and CAPTCHA detection."""
    with sync_playwright() as p:
        for attempt in range(3):  # Retry up to 3 times
            print(f"Attempt {attempt + 1} to fetch fresh cookies...")
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            stealth_sync(page)  # Enable stealth mode
            page.goto("https://www.autotrader.co.uk/")
            page.wait_for_load_state("networkidle")

            # Check for CAPTCHA
            if "Are you a human?" in page.content():
                print("CAPTCHA detected! Manual intervention required.")
                browser.close()
                time.sleep(5)  # Wait and retry
                continue

            cookies = context.cookies()
            browser.close()

            if cookies:
                formatted_cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
                return formatted_cookies

        print("Failed to fetch fresh cookies after multiple attempts.")
        return None
