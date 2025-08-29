import os
import requests
from dotenv import load_dotenv

load_dotenv()

def tavily_search(query: str, max_results: int = 5) -> list:
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables.")

    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "max_results": max_results
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Tavily API request failed with status {response.status_code}: {response.text}")

    data = response.json()
    return [f"{item['title']} - {item['url']}" for item in data.get("results", [])]
