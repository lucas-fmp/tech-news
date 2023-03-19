from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    categories_dict = {}

    news_list = find_news()

    for news in news_list:
        category = news["category"]
        if category in categories_dict:
            categories_dict[category] += 1
        else:
            categories_dict[category] = 1

    sorted_categories = sorted(
        categories_dict.items(), key=lambda x: (-x[1], x[0])
    )
    top_categories = [x[0] for x in sorted_categories][:5]

    return top_categories
