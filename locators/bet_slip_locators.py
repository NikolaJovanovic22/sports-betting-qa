from selenium.webdriver.common.by import By


class BetSlipLocators:
    # header
    BET_SLIP_REMOVE_ALL = (By.CSS_SELECTOR, "div#bet-slip-header button#bet-slip-remove-all")
    # bet selection card
    BET_SELECTION_TEAMS = (By.CSS_SELECTOR, "div#bet-slip div.betSelectionTeams")
    BET_SELECTION_MARKET = (By.CSS_SELECTOR, "div#bet-slip div.betSelectionMarket")
    BET_SELECTION_ODDS = (By.CSS_SELECTOR, "div#bet-slip div.betSelectionOdds")
    BET_SLIP_SELECTION_REMOVE = (By.CSS_SELECTOR, "div#bet-slip button#bet-slip-selection-remove")
    # stake block
    STAKE_INPUT = (By.CSS_SELECTOR, "div#bet-slip input#bet-slip-stake-input")
    # footer
    TOTAL_STAKE_VALUE = (By.CSS_SELECTOR, "div.betSlipFooter span#bet-slip-total-stake")
    PLACE_BET_BUTTON = (By.CSS_SELECTOR, "div.betSlipFooter button#bet-slip-place-bet")
    # proveri da li je place bet button enabled/disabled
    POTENTIAL_PAYOUT_VALUE = (By.CSS_SELECTOR, "div#bet-slip span#bet-slip-potential-payout")
    # proveri class value za potential payload, da li je inactive ili green
