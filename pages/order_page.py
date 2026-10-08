import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнить первый шаг формы заказа')
    def fill_customer_form(self, data):
        self.set_text(
            OrderPageLocators.NAME_FIELD,
            data['name']
        )
        self.set_text(
            OrderPageLocators.SURNAME_FIELD,
            data['surname']
        )
        self.set_text(
            OrderPageLocators.ADDRESS_FIELD,
            data['address']
        )

        self.click(OrderPageLocators.METRO_FIELD)
        self.click(
            OrderPageLocators.metro_option(data['metro'])
        )

        self.set_text(
            OrderPageLocators.PHONE_FIELD,
            data['phone']
        )
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить второй шаг формы заказа')
    def fill_rental_form(self, data):
        date_field = self.wait_for_visible(
            OrderPageLocators.DATE_FIELD
        )
        date_field.send_keys(data['date'])
        date_field.send_keys(Keys.ESCAPE)

        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.click(
            OrderPageLocators.duration_option(data['duration'])
        )
        self.click(
            OrderPageLocators.color_checkbox(data['color'])
        )
        self.set_text(
            OrderPageLocators.COMMENT_FIELD,
            data['comment']
        )

    @allure.step('Оформить и подтвердить заказ')
    def submit_order(self):
        self.click(OrderPageLocators.FINAL_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step(
        'Получить сообщение об успешном заказе'
    )
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
