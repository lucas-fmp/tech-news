import time
import requests
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(text=html_content)

    dict_news = {}

    dict_news["url"] = selector.css(
        "head link[rel='canonical']::attr(href)"
    ).get()

    dict_news["title"] = (
        selector.css(".entry-header-inner .entry-title::text").get().strip()
    )

    dict_news["timestamp"] = selector.css(".post-meta .meta-date::text").get()

    dict_news["writer"] = selector.css(".meta-author .author a::text").get()

    dict_news["reading_time"] = int(
        selector.css(".post-meta .meta-reading-time::text").re_first(r"\d+")
    )

    dict_news["summary"] = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()

    dict_news["category"] = selector.css(
        ".meta-category .category-style .label::text"
    ).get()

    return dict_news


# Requisito 5
def get_tech_news(amount):
    BASE_URL = "https://blog.betrybe.com/"
    page_html = fetch(BASE_URL)

    list_of_url_news = scrape_updates(page_html)

    while amount > len(list_of_url_news):
        page_html = fetch(scrape_next_page_link(page_html))
        list_of_url_news.extend(scrape_updates(page_html))

    list_of_url_news = list_of_url_news[:amount]

    news_data = []
    for news in list_of_url_news:
        news_data.append(scrape_news(fetch(news)))

    create_news(news_data)
    return news_data
