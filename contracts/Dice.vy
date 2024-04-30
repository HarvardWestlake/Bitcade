from vyper.interfaces import ERC20

# Interface for the Vyper RNG algorithm - placeholder for actual contract
interface VyperRNG:
    def get_random_number(seed: uint256) -> int128: view

# Dice Gambling Game Contract
@external
def __init__():
    pass

@internal
def _calculate_multiplier(sliderInt: int256) -> decimal:
    # Calculates multiplier based on the sliderInt (probability of winning)
    return 98.0 / (100.0 - abs(50 - sliderInt) * 2.0)
