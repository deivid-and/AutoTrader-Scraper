from src.scraper import fetch_autotrader_data
from src.notifier import send_telegram_notification
from src.fresh_cookies import get_fresh_cookies
from src.config import get_dynamic_headers

def main():
    filters = [
        {"filter": "distance", "selected": ["10"]},
        {"filter": "make", "selected": ["Chevrolet"]},
        {"filter": "max_price", "selected": ["5000"]},
        {"filter": "min_price", "selected": ["2000"]},
        {"filter": "model", "selected": ["Orlando"]},
        {"filter": "postcode", "selected": ["SW1A1AA"]}, #S62 7QH
        {"filter": "price_search_type", "selected": ["total"]}
    ]

    print("Fetching AutoTrader data...")
    print("Cookies:", get_fresh_cookies())
    print("Headers:", get_dynamic_headers())
    listings = fetch_autotrader_data(filters)

    if listings:
        for listing in listings:
            if not listing:
                continue

            title = listing.get("title", "N/A")
            price = listing.get("price", "N/A")
            location = listing.get("location", listing.get("position", "N/A"))
            link = f"https://www.autotrader.co.uk{listing.get('fpaLink', '')}"

            message = f"Title: {title}\nPrice: {price}\nLocation: {location}\nLink: {link}\n{'-' * 50}"
            print(message)
            send_telegram_notification(message)
    else:
        print("No listings found.")

if __name__ == "__main__":
    main()
