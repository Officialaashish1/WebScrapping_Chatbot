import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract headings and paragraphs
        content = []
        for tag in soup.find_all(['h1', 'h2', 'p']):
            content.append(tag.get_text(strip=True))
        
        return "\n".join(content)
    except Exception as e:
        return f"Error: {e}"
