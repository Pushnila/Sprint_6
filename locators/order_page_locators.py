from selenium.webdriver.common.by import By


class OrderPageLocators:
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

    @staticmethod
    def metro_option(station):
        """Станция метро с заданным названием."""
        return (
            By.XPATH,
            f"//button[normalize-space()='{station}']"
        )

    @staticmethod
    def duration_option(duration):
        """Вариант срока аренды."""
        return (
            By.XPATH,
            "//div[contains(@class, 'Dropdown-option') "
            f"and normalize-space()='{duration}']"
        )

    @staticmethod
    def color_checkbox(color):
        """Чекбокс цвета самоката."""
        return By.ID, color
