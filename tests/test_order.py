import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


@allure.feature('Заказ самоката')
class TestOrder:
    @allure.title(
        'Успешный заказ через {button_name} кнопку'
    )
    @pytest.mark.parametrize(
        'order_button, button_name, order_data',
        [
            (
                MainPage.TOP_ORDER_BUTTON,
                'верхнюю',
                ORDER_DATA[0]
            ),
            (
                MainPage.BOTTOM_ORDER_BUTTON,
                'нижнюю',
                ORDER_DATA[1]
            ),
        ],
        ids=[
            'top-order-button',
            'bottom-order-button',
        ]
    )
    def test_create_order_success(
        self,
        driver,
        order_button,
        button_name,
        order_data
    ):
        driver.get(Urls.BASE_URL)

        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button(order_button)

        order_page = OrderPage(driver)
        order_page.fill_customer_form(order_data)
        order_page.fill_rental_form(order_data)
        order_page.submit_order()

        assert (
            'Заказ оформлен'
            in order_page.get_success_message()
        )