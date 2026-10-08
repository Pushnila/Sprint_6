import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    ORDER_BUTTONS = {
        'top': MainPageLocators.TOP_ORDER_BUTTON,
        'bottom': MainPageLocators.BOTTOM_ORDER_BUTTON,
    }

    @allure.step(
        'Принять cookies, если уведомление отображается'
    )
    def accept_cookies(self):
        self.click_if_visible(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Нажать выбранную кнопку «Заказать»')
    def click_order_button(self, button_position):
        locator = self.ORDER_BUTTONS[button_position]
        self.scroll_to(locator)
        self.click(locator)

    @allure.step('Открыть вопрос с индексом {index}')
    def open_question(self, index):
        locator = MainPageLocators.question(index)
        self.scroll_to(locator, block='start', offset=-100)
        self.click_via_script(locator)

    @allure.step('Получить ответ на вопрос с индексом {index}')
    def get_answer(self, index):
        return self.get_text(
            MainPageLocators.answer(index)
        )
