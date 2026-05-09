from decimal import Decimal

import allure

from utils import config
from pages.sports_betting_page import SportsBettingPage


@allure.title("E2E UI test - Single Bet Placement")
def test_single_bet_placement(driver):
    sports_betting_page = SportsBettingPage(driver)

    with allure.step("Navigate to Sports Betting QA Page"):
        sports_betting_page.open(config.SPORTS_BETTING_URL)
        sports_betting_page.wait_for_spinner_to_disappear()

    with allure.step("Get current Balance"):
        initial_balance = sports_betting_page.get_balance()

    with allure.step("Click odds to select outcome for betting"):
        bet_slip = sports_betting_page.select_home_odds_for_betting(home_team="Arsenal", away_team="Chelsea")

    with allure.step("Assert Bet Slip Data"):
        bet_slip.assert_bet_selection_teams("Arsenal vs Chelsea")
        bet_slip.assert_bet_selection_market("Home")
        bet_slip.assert_bet_odds("2.05")

    with allure.step("Enter stake value and Place Bet"):
        # validate if Place Bet action is active
        bet_slip.assert_place_bet_button_disabled()
        bet_slip.assert_potential_payout_inactive()
        # type stake value and validate data
        bet_slip.type_stake_value("10")
        bet_slip.assert_total_stake_value("10.00")
        bet_slip.assert_potential_payout_value("20.50")
        bet_slip.assert_potential_payout_green()
        # perform place bet
        modal_bet_placed = bet_slip.place_bet()
        # get bet placement timestamp
        bet_placed_at = modal_bet_placed.get_current_time_hhmm()

    with allure.step("Bet Placed Successfully validation"):
        modal_bet_placed.assert_title()
        modal_bet_placed.assert_match("Chelsea vs Arsenal")
        modal_bet_placed.assert_stake("10.00")
        modal_bet_placed.assert_odds("2.05")
        # modal_bet_placed.assert_potential_payout("20.50") reported defect as defect in bugs.md
        modal_bet_placed.assert_timestamp(f"TODAY, {bet_placed_at}")
        modal_bet_placed.close()

    with allure.step("Assert deducted Balance by the stake from the last bet placement"):
        sports_betting_page.reload_page() # reloading page is needed for fetching new data - reported as defect in bugs.md

        deducted_balance = sports_betting_page.get_deducted_balance(initial_balance, Decimal(str("10.00")))
        sports_betting_page.assert_balance(deducted_balance)
