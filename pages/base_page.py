from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    WAIT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

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

    def click_via_script(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script(
            'arguments[0].click();',
            element
        )

    def set_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def click_if_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements and elements[0].is_displayed():
            elements[0].click()

    def scroll_to(self, locator, block='center', offset=0):
        element = self.wait_for_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: arguments[1]});",
            element,
            block
        )
        if offset:
            self.driver.execute_script(
                'window.scrollBy(0, arguments[0]);',
                offset
            )

    def is_url(self, url):
        try:
            WebDriverWait(
                self.driver,
                self.WAIT_TIMEOUT
            ).until(expected_conditions.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def is_url_contains(self, url_fragment):
        try:
            WebDriverWait(
                self.driver,
                self.WAIT_TIMEOUT
            ).until(
                expected_conditions.url_contains(url_fragment)
            )
            return True
        except TimeoutException:
            return False

    def get_current_window_handle(self):
        return self.driver.current_window_handle

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
