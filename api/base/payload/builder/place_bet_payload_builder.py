from api.base.payload.builder.base_payload_builder import BasePayloadBuilder
from api.base.payload.defaults.place_bet_payload_defaults import DEFAULT_PLACE_BET_PAYLOAD


class PlaceBetPayloadBuilder(BasePayloadBuilder):
    REQUIRED_FIELDS = ["matchId", "selection", "stake"]

    def __init__(self):
        super().__init__(DEFAULT_PLACE_BET_PAYLOAD)

    def with_match_id(self, match_id: str):
        return self.set("matchId", match_id)

    def with_selection(self, selection: str):
        return self.set("selection", selection)

    def with_stake(self, stake):
        return self.set("stake", stake)

    def build(self) -> dict:
        missing = [
            field for field in self.REQUIRED_FIELDS
            if not self._payload.get(field)
        ]

        if missing:
            raise ValueError(f"Missing required fields: {missing}")

        return self._payload
