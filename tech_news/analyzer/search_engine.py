from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)

    return [(new["title"], new["url"]) for new in news]


# Requisito 8
def search_by_date(date):
    try:
        formated_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    news = search_news({"timestamp": formated_date})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
