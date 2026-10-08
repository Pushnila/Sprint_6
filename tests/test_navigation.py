import allure

from pages.header_page import HeaderPage
from urls import Urls


@allure.feature('Навигация по логотипам')
class TestLogoNavigation:
    @allure.title(
        'Логотип Самоката ведёт на главную страницу'
    )
    def test_scooter_logo_opens_main_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.open(Urls.ORDER_URL)
        header_page.click_scooter_logo()

        assert header_page.is_url(Urls.BASE_URL)

    @allure.title(
        'Логотип Яндекса открывает главную страницу Дзена'
    )
    def test_yandex_logo_opens_dzen(self, driver):
        header_page = HeaderPage(driver)
        header_page.open(Urls.BASE_URL)
        header_page.click_yandex_logo_and_switch_window()

        assert header_page.is_url_contains(
            Urls.DZEN_URL_FRAGMENT
        )
