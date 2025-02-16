import requests
import json
from datetime import datetime
from src.config import BASE_URL, HEADERS

def fetch_autotrader_data(filters, channel="cars", page=1, sort_by="relevance", search_id="default-search-id"):
    payload = {
        "operationName": "SearchResultsListingsGridQuery",
        "query": """
            query SearchResultsListingsGridQuery($filters: [FilterInput!]!, $channel: Channel!, $page: Int, $sortBy: SearchResultsSort, $listingType: [ListingType!], $searchId: String!) {
              searchResults(input: {facets: [], filters: $filters, channel: $channel, page: $page, sortBy: $sortBy, listingType: $listingType, searchId: $searchId}) {
                listings {
                  ... on SearchListing {
                    title
                  }
                }
              }
            }
        """,
        "variables": {
            "filters": filters,
            "channel": channel,
            "page": page,
            "sortBy": sort_by,
            "searchId": search_id
        }
    }

    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if response.status_code == 200:
        data = response.json()
        listing_count = len(data["data"]["searchResults"]["listings"])
        log_request(timestamp, response.status_code, listing_count)
        return f"Success: {listing_count} listings found"
    else:
        log_request(timestamp, response.status_code, 0)
        return f"Failed: Status Code {response.status_code}"

def log_request(timestamp, status_code, listing_count):
    """Log the request with timestamp, status, and number of listings."""
    with open("logs/debug_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} | Status: {status_code} | Listings: {listing_count}\n")
