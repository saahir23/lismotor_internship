import requests
import json

def google_search(query, api_key, search_engine_id, max_results=4):
    search_url = "https://www.googleapis.com/customsearch/v1"
    results_dict = {'query': query, 'urls': []}
    params = {
        'q': query,
        'key': api_key,
        'cx': search_engine_id,
        'num': max_results  # Request up to max_results per query
    }
    response = requests.get(search_url, params=params)
    results = response.json()
    # Define keywords for filtering URLs
    keywords = ['canoo', 'nasdaq', 'goev']
    # Extract URLs from the results and filter by keywords
    for item in results.get('items', []):
        url = item['link'].lower()  # Convert URL to lowercase for case-insensitive comparison
        if any(keyword in url for keyword in keywords):  # Check if any keyword is in the URL
            results_dict['urls'].append(item['link'])  # Use the original URL for saving
    return results_dict

def save_results_to_file(results, filename="search_results.json"):
    with open(filename, 'w') as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    api_key = ''
    cse_id = ''
    queries = [
        "CanooInc company overview", 
        "analysis of the Industry in which the Canoo inc operates", 
        "Canoo Inc's main competitors analysis growth,trends",
        "Canoo inc's key trends in the market analysis",
        "Canoo inc's financial performance, including its revenue, profit margins, return on investment, and expense structure analysis"
    ]
    
    all_results = []
    for query in queries:
        result = google_search(query, api_key, cse_id)
        if result['urls']:  # Only add to the results if URLs were found
            all_results.append(result)
    
    save_results_to_file(all_results)
