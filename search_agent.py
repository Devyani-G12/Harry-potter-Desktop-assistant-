"""Web Search Agent

Handles web search functionality via voice commands.
"""

import subprocess
import urllib.parse
import logging
import sys
from typing import Optional

logger = logging.getLogger(__name__)

# Search engine URLs
SEARCH_ENGINES = {
    "google": "https://www.google.com/search?q=",
    "bing": "https://www.bing.com/search?q=",
    "duckduckgo": "https://duckduckgo.com/?q=",
    "github": "https://github.com/search?q=",
    "stackoverflow": "https://stackoverflow.com/search?q="
}


def web_search(query: str, engine: str = "google") -> Optional[str]:
    """Perform a web search.
    
    Args:
        query: Search query text
        engine: Search engine to use (default: google)
    
    Returns:
        Status message or None on error
    """
    if not query or not isinstance(query, str):
        logger.warning("Invalid search query")
        return None
    
    query = query.strip()
    if not query:
        return None
    
    # Get search engine URL
    engine_lower = engine.lower().strip()
    search_url = SEARCH_ENGINES.get(engine_lower, SEARCH_ENGINES["google"])
    
    try:
        # Encode query for URL
        encoded_query = urllib.parse.quote(query)
        full_url = f"{search_url}{encoded_query}"
        
        # Open search in default browser
        if sys.platform.startswith('win'):
            subprocess.Popen(f"start {full_url}", shell=True)
        elif sys.platform == 'darwin':  # macOS
            subprocess.Popen(['open', full_url])
        else:  # Linux
            subprocess.Popen(['xdg-open', full_url])
        
        logger.info(f"Searching '{query}' on {engine_lower}")
        return f"Searching for: {query}"
    
    except Exception as e:
        logger.error(f"Error performing search: {e}")
        return "Could not perform search."


def search_on_github(query: str) -> Optional[str]:
    """Search on GitHub.
    
    Args:
        query: Search query
    
    Returns:
        Status message or None on error
    """
    return web_search(query, engine="github")


def search_on_stackoverflow(query: str) -> Optional[str]:
    """Search on Stack Overflow.
    
    Args:
        query: Search query
    
    Returns:
        Status message or None on error
    """
    return web_search(query, engine="stackoverflow")
