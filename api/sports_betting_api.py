import json

from api.base.base_client import BaseApiClient
from api.base.endpoint.endpoints import MATCHES, BALANCE, PLACE_BET
from api.base.exception.sports_betting_api_exception import SportsBettingAPIException
from api.base.payload.profiles.place_bet_payload_profiles import place_bet_payload
from api.base.response.match_list_response import MatchListResponse
from api.base.response.place_bet_response import PlaceBetResponse


class SportsBettingApi(BaseApiClient):

    def get_matches(self):
        response = self.get(endpoint=MATCHES, params={}, headers=self.set_headers())
        if response is None:
            raise SportsBettingAPIException("Failed to return all matches!")
        response.raise_for_status()
        return MatchListResponse(response)

    def place_bet(self, match_id, selection, stake):
        response = self.post(endpoint=PLACE_BET,
                             params={},
                             headers=self.set_headers(),
                             data=json.dumps(place_bet_payload(match_id=match_id,
                                                               selection=selection,
                                                               stake=stake)))
        if response is None:
            raise SportsBettingAPIException("Failed to Place Bet!")
        return PlaceBetResponse(response)
