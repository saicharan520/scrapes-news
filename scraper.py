import requests
from bs4 import BeautifulSoup

def scrape_verge():
    url = "https://www.theverge.com"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = []

    for item in soup.select('a.gs-c-promo-heading'):
        title = item.get_text(strip=True)
        link = item['href']
        if not link.startswith("http"):
            link = "https://www.theverge.com" + link
        articles.append({'title': title, 'link': link})
    print(f"Scraped {len(articles)} articles")
    return articles
