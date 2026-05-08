from typing import TypeAlias

from selenium.webdriver.common.by import By

Locator: TypeAlias = tuple[str, str]


class LocatorBuilder:
    @staticmethod
    def build(locator_template: Locator, **params) -> Locator:
        by, pattern = locator_template
        return by, pattern.format(**params)

    @staticmethod
    def append_xpath(parent_locator: Locator, child_locator: Locator) -> Locator:
        parent_by, parent_xpath = parent_locator
        child_by, child_xpath = child_locator

        if parent_by != By.XPATH or child_by != By.XPATH:
            raise ValueError("append_xpath supports XPath locators only")

        return By.XPATH, f"{parent_xpath}{child_xpath}"
