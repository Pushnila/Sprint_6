import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage
from urls import Urls


@allure.feature('Вопросы о важном')
class TestFaq:
    @allure.title('Ответ соответствует вопросу №{index}')
    @pytest.mark.parametrize(
        'index, expected_answer',
        FAQ_DATA,
        ids=[
            'question-1',
            'question-2',
            'question-3',
            'question-4',
            'question-5',
            'question-6',
            'question-7',
            'question-8',
        ]
    )
    def test_question_opens_correct_answer(
        self,
        driver,
        index,
        expected_answer
    ):
        driver.get(Urls.BASE_URL)

        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.open_question(index)

        assert main_page.get_answer(index) == expected_answer