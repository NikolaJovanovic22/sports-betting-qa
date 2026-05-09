class BaseApiException(Exception):
    def __init__(self, message=None, response=None):
        super().__init__(message, response)
