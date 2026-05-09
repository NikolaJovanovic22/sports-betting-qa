from api.base.response.api_response import BaseApiResponse
from api.base.response.match_response import MatchResponse


class MatchListResponse(BaseApiResponse):
    def __init__(self, response):
        super().__init__(response)

        if not isinstance(self._data, list):
            raise TypeError(
                f"Expected list response, got {type(self._data).__name__}"
            )

        self._matches = [
            MatchResponse.from_data(match_data)
            for match_data in self._data
        ]

    @property
    def first(self) -> MatchResponse:
        if not self._matches:
            raise AssertionError("Match list is empty")

        return self._matches[0]

    @property
    def items(self) -> list[MatchResponse]:
        return self._matches

    @property
    def ids(self) -> list[str]:
        return [match.id for match in self._matches]

    def get_by_id(self, match_id: str) -> MatchResponse | None:
        return next(
            (match for match in self._matches if match.id == match_id),
            None
        )

    def assert_not_empty(self):
        assert self._matches, "Expected match list not to be empty"
        return self

    def __getitem__(self, index: int) -> MatchResponse:
        return self._matches[index]

    def __len__(self) -> int:
        return len(self._matches)