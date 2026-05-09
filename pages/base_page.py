from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expectedCondition
from datetime import datetime


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ----------- Utils -------------
    def _resolve_element(self, target):
        """
        Resolve locator tuple or WebElement into WebElement.
        """
        if isinstance(target, WebElement):
            return target

        return self.driver.find_element(*target)

    def get_current_time_hhmm(self):
        return datetime.now().strftime("%H:%M")

    def refresh_page(self):
        self.driver.refresh()

    # ---------- Element Finders ----------
    def find(self, locator):
        return self.wait.until(expectedCondition.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(expectedCondition.visibility_of_element_located(locator))

    def find_not_visible(self, locator):
        return self.wait.until(expectedCondition.invisibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(expectedCondition.element_to_be_clickable(locator))

    # ---------- Element Actions ----------
    def click(self, locator):
        self.find_clickable(locator).click()

    def type(self, locator, text, clear_first=True):
        element = self.find_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def scroll_to_element(self, locator, center: bool = True):
        """
        Wait for element and scroll to it.
        """
        element = self.find(locator)

        block = "center" if center else "nearest"

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: arguments[1],
                inline: 'nearest'
            });
            """,
            element,
            block
        )

        return element

    # ---------- Assertions ----------
    def assert_text(self, locator, expected_text):
        """Assert that element text matches expected"""
        actual_text = self.get_text(locator)
        assert actual_text == expected_text, (
            f"Text assertion failed! Expected: '{expected_text}', Got: '{actual_text}'"
        )

    def assert_text_contains(self, locator, expected_substring):
        """Assert that element text contains substring"""
        actual_text = self.get_text(locator)
        assert expected_substring in actual_text, (
            f"Text assertion failed! '{expected_substring}' not in '{actual_text}'"
        )

    def assert_attribute_value(
            self,
            target,
            attribute_name: str,
            expected_value: str
    ):

        element = self._resolve_element(target)
        actual_value = element.get_attribute(attribute_name)

        assert actual_value == expected_value, (
            f"Attribute assertion failed for '{attribute_name}'. "
            f"Expected='{expected_value}', Actual='{actual_value}'"
        )

    def assert_enabled(self, target):
        """Assert element is enabled"""
        element = self._resolve_element(target)
        assert element.is_enabled(), (
            f"Expected element to be enabled, but it is disabled: {target}"
        )

    def assert_disabled(self, target):
        """Assert element is disabled"""
        element = self._resolve_element(target)
        assert not element.is_enabled(), (
            f"Expected element to be disabled, but it is enabled: {target}"
        )

    def assert_element_visible(self, locator):
        """Assert element is visible"""
        element = self.find_visible(locator)
        assert element.is_displayed(), f"Element {locator} is not visible!"

    def assert_element_not_visible(self, locator):
        """Assert element is not visible"""
        try:
            self.find_not_visible(locator)
            return True
        except Exception:
            f" Element {locator} is visible but should not be!"

    # ---------- Loading waiters ----------
    def wait_for_loading_to_disappear(self, locator, timeout):
        """Waits for loading spinner to disappear"""
        # find element visible
        element = self.wait.until(expectedCondition.visibility_of_element_located(locator))
        element.is_displayed(), f" Element {locator} is not visible!"
        # find element not visible
        try:
            WebDriverWait(self.driver, timeout).until(expectedCondition.invisibility_of_element_located(locator))
        except Exception:
            f" Element {locator} is visible but should not be!"
