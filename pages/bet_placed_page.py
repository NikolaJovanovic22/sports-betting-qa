from locators.modal_card_locators import BetPlacedLocators
from pages.base_page import BasePage
from pages.sports_betting_page import SportsBettingPage


class BetPlacedPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def find_modal_dialog_is_visible(self):
        self.find_visible(BetPlacedLocators.MODAL_PANEL)
        return self

    def find_modal_dialog_is_not_visible(self):
        self.find_not_visible(BetPlacedLocators.MODAL_PANEL)
        return self

    def assert_title(self):
        self.assert_text(BetPlacedLocators.TITLE, "Bet Placed Successfully!")
        return self

    def assert_bet_id(self, bet_id):
        self.assert_text(BetPlacedLocators.SUCCESS_BET_ID, bet_id)
        return self

    def assert_match(self, match):
        self.assert_text(BetPlacedLocators.SUCCESS_MATCH, match)
        return self

    def assert_stake(self, stake):
        self.assert_text(BetPlacedLocators.SUCCESS_STAKE, f"€{stake}")
        return self

    def assert_odds(self, odds):
        self.assert_text(BetPlacedLocators.SUCCESS_ODDS, odds)
        return self

    def assert_potential_payout(self, potential_payout):
        self.assert_text(BetPlacedLocators.SUCCESS_POTENTIAL_PAYOUT, f"€{potential_payout}")
        return self

    def assert_timestamp(self, timestamp):
        self.assert_text(BetPlacedLocators.SUCCESS_PLACED_AT, timestamp)
        return self

    def close(self) -> SportsBettingPage:
        self.click(BetPlacedLocators.BUTTON_CLOSE)
        self.find_modal_dialog_is_not_visible()
        from pages.sports_betting_page import SportsBettingPage
        return SportsBettingPage(self.driver)
