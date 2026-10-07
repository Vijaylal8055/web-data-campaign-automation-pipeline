import requests
from bs4 import BeautifulSoup


class WebsiteScraper:
    def __init__(self, user_agent: str):
        self.headers = {
            "User-Agent": user_agent
        }

    def scrape(self, url: str) -> dict:
        print(f"[SCRAPER] Scraping: {url}")

        response = requests.get(
            url,
            headers=self.headers,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = ""
        if soup.title:
            title = soup.title.get_text(strip=True)

        meta_description = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        description = ""

        if meta_description:
            description = meta_description.get(
                "content",
                ""
            )

        return {
            "url": url,
            "title": title,
            "description": description
        }
    