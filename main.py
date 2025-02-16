import time
import random
from src.scraper import fetch_autotrader_data
import os

LOG_FILE = "logs/debug_log.txt"

def log_message(message):
    """Append a message to the debug log file."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")
    print(message)  # Also print it to the console for real-time feedback

def main():
    filters = [
        {"filter": "distance", "selected": ["10"]},
        {"filter": "make", "selected": ["Chevrolet"]},
        {"filter": "max_price", "selected": ["5000"]},
        {"filter": "min_price", "selected": ["2000"]},
        {"filter": "model", "selected": ["Orlando"]},
        {"filter": "postcode", "selected": ["SW1A1AA"]},
        {"filter": "price_search_type", "selected": ["total"]}
    ]

    for i in range(10):  
        log_message(f"\nRequest {i + 1} | Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        result = fetch_autotrader_data(filters)
        listings_count = result.get("listings_count", 0) if isinstance(result, dict) else 0
        status_code = result.get("status", "403") if isinstance(result, dict) else "403"
        
        log_message(f"Status: {status_code} | Listings Found: {listings_count}")

        if status_code == "403":  
            log_message("Blocked!")
            delay = random.uniform(10, 20)
        else:
            delay = random.uniform(60, 120)
        
        log_message(f"Next request in {int(delay)} seconds...\n")
        time.sleep(delay)

if __name__ == "__main__":
    main()
