import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    # Поле «Имя»
    NAME_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    # Поле «Фамилия»
    SURNAME_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    # Поле «Адрес»
    ADDRESS_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    # Поле выбора станции метро
    METRO_FIELD = (
        By.CLASS_NAME,
        'select-search__input'
    )

    # Поле «Телефон»
    PHONE_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    # Кнопка перехода ко второму шагу
    NEXT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Далее']"
    )

    # Поле даты доставки
    DATE_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    # Выпадающий список срока аренды
    RENTAL_PERIOD = (
        By.CLASS_NAME,
        'Dropdown-control'
    )

    # Поле комментария
    COMMENT_FIELD = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    # Кнопка «Заказать» на втором шаге
    FINAL_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]"
        "//button[normalize-space()='Заказать']"
    )

    # Кнопка подтверждения заказа
    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]"
        "//button[normalize-space()='Да']"
    )

    # Сообщение об успешном оформлении заказа
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader')]"
    )

    # Станция метро с заданным названием
    @staticmethod
    def metro_option(station):
        return (
            By.XPATH,
            f"//button[normalize-space()='{station}']"
        )

    # Вариант срока аренды
    @staticmethod
    def duration_option(duration):
        return (
            By.XPATH,
            "//div[contains(@class, 'Dropdown-option') "
            f"and normalize-space()='{duration}']"
        )

    # Чекбокс цвета самоката
    @staticmethod
    def color_checkbox(color):
        return By.ID, color

    @allure.step('Заполнить первый шаг формы заказа')
    def fill_customer_form(self, data):
        self.set_text(
            self.NAME_FIELD,
            data['name']
        )
        self.set_text(
            self.SURNAME_FIELD,
            data['surname']
        )
        self.set_text(
            self.ADDRESS_FIELD,
            data['address']
        )

        self.click(self.METRO_FIELD)
        self.click(
            self.metro_option(data['metro'])
        )

        self.set_text(
            self.PHONE_FIELD,
            data['phone']
        )
        self.click(self.NEXT_BUTTON)

    @allure.step('Заполнить второй шаг формы заказа')
    def fill_rental_form(self, data):
        date_field = self.wait_for_visible(
            self.DATE_FIELD
        )
        date_field.send_keys(data['date'])
        date_field.send_keys(Keys.ESCAPE)

        self.click(self.RENTAL_PERIOD)
        self.click(
            self.duration_option(data['duration'])
        )
        self.click(
            self.color_checkbox(data['color'])
        )
        self.set_text(
            self.COMMENT_FIELD,
            data['comment']
        )

    @allure.step('Оформить и подтвердить заказ')
    def submit_order(self):
        self.click(self.FINAL_ORDER_BUTTON)
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step(
        'Получить сообщение об успешном заказе'
    )
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)