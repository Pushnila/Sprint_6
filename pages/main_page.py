import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    # Верхняя кнопка «Заказать»
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space()='Заказать'])[1]"
    )

    # Нижняя кнопка «Заказать»
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space()='Заказать'])[2]"
    )

    # Кнопка принятия cookies
    COOKIE_BUTTON = (
        By.ID,
        'rcc-confirm-button'
    )

    # Локатор вопроса по его индексу
    @staticmethod
    def question_locator(index):
        return By.ID, f'accordion__heading-{index}'

    # Локатор ответа по его индексу
    @staticmethod
    def answer_locator(index):
        return By.ID, f'accordion__panel-{index}'

    @allure.step(
        'Принять cookies, если уведомление отображается'
    )
    def accept_cookies(self):
        buttons = self.driver.find_elements(
            *self.COOKIE_BUTTON
        )

        if buttons and buttons[0].is_displayed():
            buttons[0].click()

    @allure.step('Нажать выбранную кнопку «Заказать»')
    def click_order_button(self, locator):
        self.scroll_to(locator)
        self.click(locator)

    @allure.step('Открыть вопрос с индексом {index}')
    def open_question(self, index):
        locator = self.question_locator(index)
        element = self.wait_for_visible(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'start'});",
            element
        )
        self.driver.execute_script(
            'window.scrollBy(0, -100);'
        )

        self.wait_for_clickable(locator).click()

    @allure.step('Получить ответ на вопрос с индексом {index}')
    def get_answer(self, index):
        return self.get_text(
            self.answer_locator(index)
        )