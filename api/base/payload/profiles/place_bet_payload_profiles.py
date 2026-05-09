from api.base.payload.builder.place_bet_payload_builder import PlaceBetPayloadBuilder


def place_bet_payload(match_id: str,
                      selection: str,
                      stake
                      ):
    return (
        PlaceBetPayloadBuilder()
        .with_match_id(match_id)
        .with_selection(selection)
        .with_stake(stake)
        .build()
    )
