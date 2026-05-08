from selenium.webdriver.common.by import By


class HeaderLocators:
    WALLET_BALANCE_TEXT = (By.CSS_SELECTOR, "div#header-balance span:not(.icon)")
