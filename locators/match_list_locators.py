from selenium.webdriver.common.by import By


class MatchListLocators:
    SPINNER = (By.CSS_SELECTOR, ".matchListSpinner")
    MATCH_CARDS = (By.CSS_SELECTOR, "div#match-list > div.matchCard")
    MATCH_CARD_BY_TEAMS = (By.XPATH,
                           "//div[@class='teams']/div[1]//span[@class='teamName'][text()='{home_team}']"
                           "//ancestor::div[@class='teams']/div[2]//span[@class='teamName'][text()='{away_team}']"
                           "/ancestor::div[contains(@class, 'matchCard')]")
    MATCH_ODDS_BUTTON = (
        By.XPATH,
        "//div[@class='oddsGrid']//button[contains(@id, '{odds_button}')]"
    )
