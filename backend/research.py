
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def search_web(topic: str, max_results: int = 5) -> list[dict]:
    """
    Search the web using the Tavily API.

    Args:
        topic: The subject to research.
        max_results: Maximum number of results to return.

    Returns:
        A list containing source titles, URLs and snippets.
    """

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError(
            "TAVILY_API_KEY is missing. Please add it to your .env file."
        )

    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": api_key,
            "query": topic,
            "search_depth": "basic",
            "max_results": max_results,
            "include_answer": False,
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    sources = []

    for result in data.get("results", []):
        sources.append({
            "title": result.get("title", "Untitled source"),
            "url": result.get("url", ""),
            "snippet": result.get("content", ""),
        })

    return sources
