import allure

from utils import config
from pages.sports_betting_page import SportsBettingPage


@allure.title("E2E UI test - Single Bet Placement")
def test_single_bet_placement(driver):
    betting_page = SportsBettingPage(driver)

    with allure.step("Navigate to Sports Betting QA Page"):
        betting_page.open(config.SPORTS_BETTING_URL)
        betting_page.wait_for_spinner_to_disappear()

    with allure.step("Click odds to select outcome for betting"):
        betting_page.select_home_odds_for_match(home_team="Arsenal", away_team="Chelsea")

    with allure.step("Set betting stake value"):
        betting_page




