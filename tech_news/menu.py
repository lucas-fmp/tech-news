import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_title,
    search_by_date,
)
from tech_news.scraper import get_tech_news


def popular_banco():
    amount = input("Digite quantas notícias serão buscadas: ")
    get_tech_news(int(amount))


def buscar_por_titulo():
    title = input("Digite o título: ")
    print(search_by_title(title))


def buscar_por_data():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(date))


def buscar_por_categoria():
    category = input("Digite a categoria: ")
    search_by_category(category)


def listar_top_categorias():
    print(top_5_categories())


def sair():
    print("Encerrando script")
    return


menu = {
    "0": popular_banco,
    "1": buscar_por_titulo,
    "2": buscar_por_data,
    "3": buscar_por_categoria,
    "4": listar_top_categorias,
    "5": sair,
}


def analyzer_menu():
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por categoria;")
    print(" 4 - Listar top 5 categorias;")
    print(" 5 - Sair.")

    option = input("Opção escolhida: ")

    function = menu.get(option)
    if function:
        try:
            function()
        except Exception as exception:
            print(exception, file=sys.stderr)

    else:
        print("Opção inválida", file=sys.stderr)
