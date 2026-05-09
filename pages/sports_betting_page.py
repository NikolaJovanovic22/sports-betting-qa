import re
from decimal import Decimal

from locators.header_locators import HeaderLocators
from locators.match_list_locators import MatchListLocators
from locators.locator_builder import LocatorBuilder
from pages.base_page import BasePage


class SportsBettingPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def open(self, base_url):
        self.driver.get(f"{base_url}")

    def reload_page(self):
        self.refresh_page()
        self.wait_for_spinner_to_disappear()


    # ------------- Header -------------------
    def get_balance(self):
        balance_text = self.get_text(HeaderLocators.WALLET_BALANCE_TEXT)
        amount = Decimal(re.search(r"[\d.]+", balance_text).group())
        return amount

    def get_deducted_balance(self, initial_balance: Decimal, stake: Decimal):
        deducted_balance = initial_balance - stake
        return deducted_balance

    def assert_balance(self, expected_balance: Decimal):
        actual_balance = self.get_balance()
        assert self.get_balance() == expected_balance, (
            f"Balance assertion failed! Expected: '{expected_balance}', Got: '{actual_balance}'"
        )

    # ------------- Match List -------------------
    def scroll_to_match(self, home_team, away_team):
        locator = LocatorBuilder.build(
            MatchListLocators.MATCH_CARD_BY_TEAMS,
            home_team=home_team,
            away_team=away_team
        )
        match = self.scroll_to_element(locator)
        return match

    def wait_for_spinner_to_disappear(self):
        self.wait_for_loading_to_disappear(MatchListLocators.SPINNER, 10)

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

    def select_home_odds_for_betting(self, home_team, away_team):
        self.__select_match_odds(home_team, away_team, "home")
        from pages.bet_slip_page import BetSlipPage
        return BetSlipPage(self.driver)

    def select_away_odds_for_match(self, home_team, away_team):
        self.__select_match_odds(home_team, away_team, "away")

    def select_draw_odds_for_match(self, home_team, away_team):
        self.__select_match_odds(home_team, away_team, "draw")
