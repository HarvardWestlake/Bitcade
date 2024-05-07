from vyper.interfaces import ERC20

# Define constants and types
MIN_SLIDER: constant(int128) = 1
MAX_SLIDER: constant(int128) = 100

interface RandomNumberInterface:
    def get_random_number() -> int128: view

# Contract storage
random_number_generator: public(address)
last_calculated_multiplier: public(decimal)  # Added to store the last calculated payout multiplier

# Events
event PayoutCalculated:
    slider: int128
    roll_above: bool
    payout_multiplier: decimal

event PayoutMultiplierCalculated:
    multiplier: decimal

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

<<<<<<< HEAD
@internal
def hasWon(player_choice: int128, bet_over: bool, seed: uint256) -> bool:
    # Fetch random number using the RNG contract
    random_number = VyperRNG.get_random_number(seed)
    
    # Determine win condition based on player's bet
    if bet_over:
        # Player bets the result will be over the chosen number
        return random_number > player_choice
    else:
        # Player bets the result will be under the chosen number
        return random_number < player_choice

# Dummy VyperRNG interface implementation for testing purposes

@external
def get_random_number(seed: uint256) -> int128:
    # A simple deterministic "random" number generator for testing
    # This dummy method uses a simple algorithm to generate a pseudo-random number
    # based on the seed. This is not secure and only for testing purposes.
    return (seed % 100) + 1  # Generates a number between 1 and 100

deploy
=======
@external
def calculate_payout(sliderInt: int128, rollAbove: bool) -> decimal:
    percent_chance: int128 = self.calculate_percent_chance(sliderInt, rollAbove)
    assert percent_chance > 0, "Percent chance must be positive"
    payout_multiplier: decimal = 98.0 / convert(percent_chance, decimal)
    self.last_calculated_multiplier = payout_multiplier  # Store the result for test validation
    log PayoutMultiplierCalculated(payout_multiplier)
    return payout_multiplier
>>>>>>> ac9dd312982b19b3ec4b42c8f43c1c908883ba35
