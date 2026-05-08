from locators.bet_slip_locators import BetSlipLocators
from locators.match_list_locators import MatchListLocators
from locators.locator_builder import LocatorBuilder
from pages.base_page import BasePage


class SportsBettingPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def open(self, base_url):
        self.driver.get(f"{base_url}")

    def wait_for_spinner_to_disappear(self):
        self.wait_for_loading_to_disappear(MatchListLocators.SPINNER, 10)

    # ------------- Match List -------------------
    def scroll_to_match(self, home_team, away_team):
        locator = LocatorBuilder.build(
            MatchListLocators.MATCH_CARD_BY_TEAMS,
            home_team=home_team,
            away_team=away_team
        )
        match = self.scroll_to_element(locator)
        return match

    def __select_match_odds(self, home_team, away_team, odds_button):
        # Locators initialization
        match_locator = LocatorBuilder.build(
            MatchListLocators.MATCH_CARD_BY_TEAMS,
            home_team=home_team,
            away_team=away_team
        )
        odds_btn_locator = LocatorBuilder.build(
            MatchListLocators.MATCH_ODDS_BUTTON,
            odds_button=odds_button
        )
        odds_locator = LocatorBuilder.append_xpath(
            match_locator,
            odds_btn_locator
        )
        self.scroll_to_match(home_team, away_team)
        self.find_visible(match_locator)
        self.find_visible(odds_locator)
        self.click(odds_locator)

    def select_home_odds_for_match(self, home_team, away_team):
        self.__select_match_odds(home_team, away_team, "home")

    def select_away_odds_for_match(self, home_team, away_team):
        self.__select_match_odds(home_team, away_team, "away")

    def select_draw_odds_for_match(self, home_team, away_team):
        self.__select_match_odds(home_team, away_team, "draw")

    # ------------ Bet Slip ------------
    def assert_bet_selection_teams(self, teams):
        self.assert_text(BetSlipLocators.BET_SELECTION_TEAMS, teams)

    def assert_bet_selection_market(self, winner):
        self.assert_text(BetSlipLocators.BET_SELECTION_MARKET, "Match Winner: ".join(winner))

    def assert_bet_odds(self, odds):
        self.assert_text(BetSlipLocators.BET_SELECTION_ODDS, odds)

    def type_stake_value(self, stake):
        self.type(BetSlipLocators.STAKE_INPUT, stake)
        self.assert_attribute_value(BetSlipLocators.STAKE_INPUT, "value", stake)

    def assert_total_stake_value(self, total_stake):
        self.assert_text(BetSlipLocators.TOTAL_STAKE_VALUE, total_stake)

    def assert_potential_payout_value(self, potential_payout):
        self.assert_text(BetSlipLocators.POTENTIAL_PAYOUT_VALUE, potential_payout)

    def assert_potential_payout_inactive(self, ):
        self.assert_attribute_value(BetSlipLocators.POTENTIAL_PAYOUT_VALUE,
                                    "class", "payoutInactive")

    def assert_potential_payout_green(self, ):
        self.assert_attribute_value(BetSlipLocators.POTENTIAL_PAYOUT_VALUE,
                                    "class", "payoutGreen")

    def place_bet(self):
        self.click(BetSlipLocators.PLACE_BET_BUTTON)

    def assert_place_bet_button_disabled(self):
        self.assert_disabled(BetSlipLocators.PLACE_BET_BUTTON)
