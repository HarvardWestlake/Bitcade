from vyper.interfaces import ERC20

# Define constants and types
MIN_SLIDER: constant(int128) = 1
MAX_SLIDER: constant(int128) = 100

interface RandomNumberInterface:
    def lockCurrent() -> bool: nonpayable
    def unlockLatest(numberRange: uint256) -> uint256: nonpayable

# Contract storage
random_number_generator: public(address)
last_calculated_multiplier: public(decimal)  # Added to store the last calculated payout multiplier
bets: public(HashMap[address, uint256])

# Events
event PayoutCalculated:
    slider: int128
    roll_above: bool
    payout_multiplier: decimal

event PayoutMultiplierCalculated:
    multiplier: decimal

event BetPlaced:
    player: address
    amount: uint256
    slider: int128
    roll_above: bool

event BetResult:
    player: address
    amount: uint256
    slider: int128
    roll_above: bool
    random_number: int128
    won: bool
    payout: uint256

event LogMessage:
    message: String[64]  # Using String type with a maximum length of 64

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
    assert sliderInt >= MIN_SLIDER, "Slider out of range"
    assert sliderInt <= MAX_SLIDER, "Slider out of range"
    if rollAbove:
        return MAX_SLIDER - sliderInt
    else:
        return sliderInt - MIN_SLIDER

@internal
def internal_calculate_payout(sliderInt: int128, rollAbove: bool) -> decimal:
    percent_chance: int128 = self.calculate_percent_chance(sliderInt, rollAbove)
    assert percent_chance > 0, "Percent chance must be positive"
    payout_multiplier: decimal = 98.0 / convert(percent_chance, decimal)
    self.last_calculated_multiplier = payout_multiplier  # Store the result for test validation
    log PayoutMultiplierCalculated(payout_multiplier)
    return payout_multiplier

@external
def calculate_payout(sliderInt: int128, rollAbove: bool) -> decimal:
    return self.internal_calculate_payout(sliderInt, rollAbove)

@payable
@external
def place_bet(sliderInt: int128, rollAbove: bool):
    """
    Place a bet on the outcome of a dice roll.
    """
    assert msg.value > 0, "Bet amount must be greater than zero"
    assert sliderInt >= MIN_SLIDER, "Slider out of range"
    assert sliderInt <= MAX_SLIDER, "Slider out of range"

    # Store the bet details
    self.bets[msg.sender] = msg.value

    # Lock the current block number for RNG
    success: bool = RandomNumberInterface(self.random_number_generator).lockCurrent()
    assert success, "Failed to lock current block"

    log BetPlaced(msg.sender, msg.value, sliderInt, rollAbove)

@external
def resolve_bet(sliderInt: int128, rollAbove: bool):
    """
    Resolve the bet placed by the user.
    """
    bet_amount: uint256 = self.bets[msg.sender]
    assert bet_amount > 0, "No bet placed"

    # Get the random number
    random_number: uint256 = RandomNumberInterface(self.random_number_generator).unlockLatest(100)
    random_number_int: int128 = convert(random_number, int128)

    # Determine if the bet is won or lost
    won: bool = (rollAbove and random_number_int > sliderInt) or (not rollAbove and random_number_int < sliderInt)

    # Calculate payout
    payout: uint256 = 0
    if won:
        payout_multiplier: decimal = self.internal_calculate_payout(sliderInt, rollAbove)
        payout = convert(convert(bet_amount, decimal) * payout_multiplier, uint256)
        send(msg.sender, payout)

    # Clear the bet
    self.bets[msg.sender] = 0

    log BetResult(msg.sender, bet_amount, sliderInt, rollAbove, random_number_int, won, payout)

@payable
@external
def __default__():
    pass
