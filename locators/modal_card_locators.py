from selenium.webdriver.common.by import By


class BetPlacedLocators:
    MODAL_PANEL = (By.CSS_SELECTOR, "div.modalPanel")
    TITLE = (By.CSS_SELECTOR, "div.modalPanel h2.modalTitle")
    SUCCESS_BET_ID = (By.CSS_SELECTOR, "div.modalPanel span#modal-success-bet-id")
    SUCCESS_MATCH = (By.CSS_SELECTOR, "div.modalPanel div#modal-success-match")
    SUCCESS_STAKE = (By.CSS_SELECTOR, "div.modalPanel div#modal-success-stake")
    SUCCESS_ODDS = (By.CSS_SELECTOR, "div.modalPanel div#modal-success-odds")
    SUCCESS_POTENTIAL_PAYOUT = (By.CSS_SELECTOR, "div.modalPanel span#modal-success-payout")
    SUCCESS_PLACED_AT = (By.CSS_SELECTOR, "div#modal-success-placed-at")
    BUTTON_CLOSE = (By.CSS_SELECTOR, "button#modal-success-close")
