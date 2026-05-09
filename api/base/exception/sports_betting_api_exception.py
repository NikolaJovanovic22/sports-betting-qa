from api.base.exception.base_exception import BaseApiException


class SportsBettingAPIException(BaseApiException):
    def __init__(self, message, response=None):
        super().__init__(
            message=f"Sports Betting API exception. {message}",
            response=response)
