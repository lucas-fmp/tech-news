from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from pytest_mock import MockerFixture
import pytest

mock_db_news = [
    {"title": "Notícia 1", "reading_time": 2},
    {"title": "Notícia 2", "reading_time": 4},
    {"title": "Notícia 3", "reading_time": 6},
    {"title": "Notícia 4", "reading_time": 8},
]

mock_function_response = {
    "readable": [
        {
            "unfilled_time": 1,
            "chosen_news": [("Notícia 1", 2), ("Notícia 2", 4)],
        },
        {
            "unfilled_time": 1,
            "chosen_news": [("Notícia 3", 6)],
        },
    ],
    "unreadable": [("Notícia 4", 8)],
}


def test_reading_plan_group_news(mocker: MockerFixture):
    mocker.patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=mock_db_news
    )

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    function_response = ReadingPlanService.group_news_for_available_time(7)

    assert function_response == mock_function_response
