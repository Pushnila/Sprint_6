from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def wait_for_visible(self, locator):
        return WebDriverWait(
            self.driver,
            self.WAIT_TIMEOUT
        ).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(
            self.driver,
            self.WAIT_TIMEOUT
        ).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def set_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def scroll_to(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def wait_for_url(self, url):
        WebDriverWait(
            self.driver,
            self.WAIT_TIMEOUT
        ).until(
            expected_conditions.url_to_be(url)
        )

    def switch_to_new_window(self, old_window):
        WebDriverWait(
            self.driver,
            self.WAIT_TIMEOUT
        ).until(
            expected_conditions.number_of_windows_to_be(2)
        )

        new_window = next(
            handle
            for handle in self.driver.window_handles
            if handle != old_window
        )

        self.driver.switch_to.window(new_window)