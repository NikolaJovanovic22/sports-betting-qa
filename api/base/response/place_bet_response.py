from api.base.response.api_response import BaseApiResponse
from api.base.response.json_accessor import get_by_path


class PlaceBetResponse(BaseApiResponse):

    def __init__(self, response):
        super().__init__(response)

    @property
    def error(self):
        return get_by_path(self._data, "error")

    @property
    def message(self):
        return get_by_path(self._data, "message")

    @property
    def match_id(self):
        return get_by_path(self._data, "matchId")

    @property
    def selection(self):
        return get_by_path(self._data, "selection")

    @property
    def stake(self):
        return get_by_path(self._data, "stake")

    @property
    def odds(self):
        return get_by_path(self._data, "odds")

    @property
    def payout(self):
        return get_by_path(self._data, "payout")

    @property
    def balance(self):
        return get_by_path(self._data, "balance")

    @property
    def currency(self):
        return get_by_path(self._data, "currency")
