from api.base.response.json_accessor import get_by_path


class MatchResponse:

    def __init__(self, response=None, data: dict | None = None):
        self._response = response
        self._data = data if data is not None else response.json()

    @classmethod
    def from_data(cls, data: dict):
        return cls(data=data)

    @property
    def id(self):
        return get_by_path(self._data, "id")

    @property
    def competition(self):
        return get_by_path(self._data, "competition")

    @property
    def kickoff_date(self):
        return get_by_path(self._data, "kickoffDate")

    @property
    def home_team(self):
        return get_by_path(self._data, "homeTeam")

    @property
    def away_team(self):
        return get_by_path(self._data, "awayTeam")

    @property
    def home_odds(self):
        return get_by_path(self._data, "odds.home")

    @property
    def away_odds(self):
        return get_by_path(self._data, "odds.away")

    @property
    def draw_odds(self):
        return get_by_path(self._data, "odds.draw")
