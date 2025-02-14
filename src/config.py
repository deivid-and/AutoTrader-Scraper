from src.fresh_cookies import get_fresh_cookies
from fake_useragent import UserAgent

ua = UserAgent()
BASE_URL = "https://www.autotrader.co.uk/at-gateway?opname=SearchResultsListingsGridQuery"
HEADERS = {
    "User-Agent": ua.random,
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Referer": "https://www.autotrader.co.uk/",
    "Origin": "https://www.autotrader.co.uk",
    "Connection": "keep-alive",
    "X-Sauron-App-Name": "sauron-search-results-app",
    "X-Sauron-App-Version": "3087",
    "Cookie": get_fresh_cookies()
}