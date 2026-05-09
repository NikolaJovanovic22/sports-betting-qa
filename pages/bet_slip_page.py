from locators.bet_slip_locators import BetSlipLocators
from pages.base_page import BasePage


class BetSlipPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def assert_bet_selection_teams(self, teams):
        self.assert_text(BetSlipLocators.BET_SELECTION_TEAMS, teams)

    def assert_bet_selection_market(self, winner):
        self.assert_text(BetSlipLocators.BET_SELECTION_MARKET, f"Match Winner: {winner}")

    def assert_bet_odds(self, odds):
        self.assert_text(BetSlipLocators.BET_SELECTION_ODDS, f"Odds: {odds}")

    def type_stake_value(self, stake):
        self.type(BetSlipLocators.STAKE_INPUT, stake)
        self.assert_attribute_value(BetSlipLocators.STAKE_INPUT, "value", stake)

    def assert_total_stake_value(self, total_stake):
        self.assert_text(BetSlipLocators.TOTAL_STAKE_VALUE, f"€{total_stake}")

    def assert_potential_payout_value(self, potential_payout):
        self.assert_text(BetSlipLocators.POTENTIAL_PAYOUT_VALUE, f"€{potential_payout}")

    def assert_potential_payout_inactive(self, ):
        self.assert_attribute_value(BetSlipLocators.POTENTIAL_PAYOUT_VALUE,
                                    "class", "payoutInactive")

    def assert_potential_payout_green(self, ):
        self.assert_attribute_value(BetSlipLocators.POTENTIAL_PAYOUT_VALUE,
                                    "class", "payoutGreen")

    def place_bet(self):
        from pages.bet_placed_page import BetPlacedPage
        self.click(BetSlipLocators.PLACE_BET_BUTTON)
        self.wait_for_loading_to_disappear(BetSlipLocators.PLACING_BUTTON, 10)
        return (BetPlacedPage(self.driver)
                .find_modal_dialog_is_visible())

    def assert_place_bet_button_disabled(self):
        self.assert_disabled(BetSlipLocators.PLACE_BET_BUTTON)

    def assert_place_bet_button_enabled(self):
        self.assert_enabled(BetSlipLocators.PLACE_BET_BUTTON)
