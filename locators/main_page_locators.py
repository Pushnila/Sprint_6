from selenium.webdriver.common.by import By


class MainPageLocators:
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

    @staticmethod
    def question(index):
        """Локатор вопроса по его индексу."""
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def answer(index):
        """Локатор ответа по его индексу."""
        return By.ID, f'accordion__panel-{index}'
