import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        content = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if content.status_code == 200:
            return content.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = []

    try:
        urls = selector.css(
            ".cs-overlay .cs-overlay-link::attr(href)"
        ).getall()
        return urls
    except ValueError:
        return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    try:
        url_net_page = selector.css(".nav-links .next::attr(href)").get()
        return url_net_page
    except ValueError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
