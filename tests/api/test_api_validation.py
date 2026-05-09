import allure


@allure.title("API test - base actions and validation")
def test_api_validation(betting_api):
    with allure.step("GET: all matches"):
        matches_response = betting_api.get_matches()
        matches_response.assert_status(200)
        matches_response.assert_not_empty()
    with allure.step("Validate data for first match"):
        first_match = matches_response.first
        assert first_match.id is not None
        assert first_match.competition == "Premier League"
        assert first_match.home_team == "Manchester Utd"
        assert first_match.away_team == "Chelsea"
        assert first_match.kickoff_date == "2026-02-27"
        assert first_match.home_odds == 2.45
        assert first_match.away_odds == 2.8
        assert first_match.draw_odds == 3.1

    with allure.step("Place Bet Successfully"):
        first_match_id = first_match.id
        place_bet_response = betting_api.place_bet(first_match_id, "HOME", 22.00)
        place_bet_response.assert_status(200)
        assert place_bet_response.message == "Bet placed successfully"
        assert place_bet_response.match_id == first_match_id
        assert place_bet_response.selection == "HOME"
        assert place_bet_response.stake == 22
        assert place_bet_response.odds == 2.45
        assert place_bet_response.payout != ""
        assert place_bet_response.balance != ""
        # assert place_bet_response.currency != "EUR" # bug: current currency is USD

    with allure.step("Place Bet with exceeded Stake max value"):
        place_bet_error_response = betting_api.place_bet(first_match_id, "HOME", 101.00)
        assert place_bet_error_response.error == "invalid_stake_max"
        assert place_bet_error_response.message == "Stake must be at most 100.00."
