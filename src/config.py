from src.fresh_cookies import get_fresh_cookies
from fake_useragent import UserAgent
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.autotrader.co.uk/at-gateway?opname=SearchResultsListingsGridQuery"

def get_app_version():
    """Fetch the latest X-Sauron-App-Version dynamically from the AutoTrader homepage."""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://www.autotrader.co.uk/")
            page.wait_for_load_state("networkidle")
            
            # Replace this with the actual JavaScript variable or DOM element that contains the version
            app_version = page.evaluate("() => window.someGlobalVarContainingVersion")  
            browser.close()
            
            if app_version:
                print(f"Fetched X-Sauron-App-Version: {app_version}")
                return app_version
    except Exception as e:
        print(f"Error fetching app version: {e}")
    
    # Fallback to a known version if fetching fails
    return "048835142d"

def get_dynamic_headers():
    """Generate fresh headers with dynamic values for each request."""
    ua = UserAgent()
    fresh_cookies = get_fresh_cookies() or ""  # Fetch fresh cookies

    headers = {
        "User-Agent": ua.random,  # Randomize User-Agent for each request
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Referer": "https://www.autotrader.co.uk/",
        "Origin": "https://www.autotrader.co.uk",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Google Chrome";v="133", "Chromium";v="133", "Not A;Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "X-Sauron-App-Name": "sauron-search-results-app",
        "X-Sauron-App-Version": get_app_version(),  # Fetch the latest version dynamically
        "Cookie": fresh_cookies  # Use freshly fetched cookies
    }
    return headers
