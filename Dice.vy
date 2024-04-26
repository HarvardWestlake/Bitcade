from vyper.interfaces import ERC20

# Interface for the Vyper RNG algorithm - placeholder for actual contract
interface VyperRNG:
    def get_random_number(seed: uint256) -> int128: view

# Dice Gambling Game Contract
@external
def __init__():
    pass

@internal
def _calculate_multiplier(sliderInt: int128) -> decimal:
    # Calculates multiplier based on the sliderInt (probability of winning)
    return 98.0 / (100.0 - abs(50 - sliderInt) * 2.0)

@internal
def _has_won(sliderInt: int128, randomNumber: int128, rollAbove: bool) -> bool:
    # Determines if the player has won based on their roll preference
    if rollAbove:
        return sliderInt < randomNumber
    else:
        return sliderInt >= randomNumber

@external
def play_game(sliderInt: int128, betAmount: uint256, rollAbove: bool):
    # Ensure the player has enough tokens and has approved them to the contract
    token: ERC20 = ERC20(msg.sender)
    assert token.balanceOf(msg.sender) >= betAmount, "Insufficient balance"
    assert token.allowance(msg.sender, self) >= betAmount, "Bet not approved"

    # Call external RNG and place bet
    rng: VyperRNG = VyperRNG(<address_of_rng_contract>)
    randomNumber: int128 = rng.get_random_number(uint256(block.timestamp))

    # Calculate result and payout
    player_won: bool = self._has_won(sliderInt, randomNumber, rollAbove)
    multiplier: decimal = self._calculate_multiplier(sliderInt)
    payout: uint256 = convert(multiplier * betAmount, uint256)

    if player_won:
        # Transfer winnings
        assert token.transfer(msg.sender, payout), "Payout failed"
    else:
        # Collect the lost bet
        assert token.transferFrom(msg.sender, self, betAmount), "Collection failed"
