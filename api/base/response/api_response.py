class BaseApiResponse:

    def __init__(self, response):
        self._response = response
        self._data = response.json()

    @property
    def status_code(self):
        return self._response.status_code

    def assert_status(self, expected_status: int):
        assert self.status_code == expected_status, (
            f"Expected status {expected_status}, "
            f"got {self.status_code}. "
            f"Response: {self._response.text}"
        )

    @property
    def raw(self):
        return self._response

    @property
    def data(self):
        return self._data