import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HeaderPage(BasePage):
    # Логотип «Самоката»
    SCOOTER_LOGO = (
        By.CLASS_NAME,
        'Header_LogoScooter__3lsAR'
    )

    # Логотип Яндекса
    YANDEX_LOGO = (
        By.CLASS_NAME,
        'Header_LogoYandex__3TSOI'
    )

    @allure.step('Нажать на логотип «Самоката»')
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step(
        'Нажать на логотип Яндекса и перейти в новую вкладку'
    )
    def click_yandex_logo_and_switch_window(self):
        old_window = self.driver.current_window_handle

        self.click(self.YANDEX_LOGO)
        self.switch_to_new_window(old_window)

    def wait_for_url_contains(self, url_fragment):
        WebDriverWait(
            self.driver,
            self.WAIT_TIMEOUT
        ).until(
            expected_conditions.url_contains(url_fragment)
        )