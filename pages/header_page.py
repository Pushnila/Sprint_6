import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Нажать на логотип «Самоката»')
    def click_scooter_logo(self):
        self.click(HeaderPageLocators.SCOOTER_LOGO)

    @allure.step(
        'Нажать на логотип Яндекса и перейти в новую вкладку'
    )
    def click_yandex_logo_and_switch_window(self):
        old_window = self.get_current_window_handle()
        self.click(HeaderPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(old_window)
