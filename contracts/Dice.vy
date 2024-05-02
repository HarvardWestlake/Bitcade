from vyper.interfaces import ERC20

# Define constants and types
MIN_SLIDER: constant(int128) = 1
MAX_SLIDER: constant(int128) = 100

interface RandomNumberInterface:
    def get_random_number() -> int128: view

# Contract storage
random_number_generator: public(address)

# Events
event PayoutCalculated:
    slider: int128
    roll_above: bool
    payout_multiplier: decimal

@external
def set_random_number_generator(_addr: address):
    """
    Set the address of the random number generator contract.
    """
    self.random_number_generator = _addr

@internal
def calculate_percent_chance(sliderInt: int128, rollAbove: bool) -> int128:
    """
    Calculate the percent chance of winning based on sliderInt and rollAbove.
    """
    assert MIN_SLIDER <= sliderInt and sliderInt <= MAX_SLIDER, "Slider out of range"
    if rollAbove:
        return MAX_SLIDER - sliderInt
    else:
        return sliderInt - MIN_SLIDER

@external
def calculate_payout(sliderInt: int128, rollAbove: bool) -> decimal:
    """
    Calculate the payout multiplier based on the sliderInt and rollAbove.
    Uses the formula 98 / percent chance of winning.
    """
    percent_chance: int128 = self.calculate_percent_chance(sliderInt, rollAbove)
    assert percent_chance > 0, "Percent chance must be positive"
    
    # Convert percent_chance to decimal before division
    payout_multiplier: decimal = 98.0 / convert(percent_chance, decimal)
    log PayoutCalculated(sliderInt, rollAbove, payout_multiplier)
    
    return payout_multiplier

