from copy import deepcopy


class BasePayloadBuilder:
    def __init__(self, defaults: dict):
        self._defaults = deepcopy(defaults)
        self._payload = deepcopy(defaults)

    def set(self, key, value):
        self._payload[key] = value
        return self

    def remove(self, key):
        self._payload.pop(key, None)
        return self

    def reset(self):
        self._payload = deepcopy(self._defaults)
        return self

    def build(self):
        return self._payload
