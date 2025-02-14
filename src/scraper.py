import requests
import json
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
                    price
                    location
                    fpaLink
                  }
                  ... on LeasingListing {
                    title
                    price
                    position
                    fpaLink
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

    if response.status_code == 200:
        data = response.json()
        return data["data"]["searchResults"]["listings"]
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        print(response.text)
        return []
