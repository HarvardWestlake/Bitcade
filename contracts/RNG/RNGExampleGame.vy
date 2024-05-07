# @version ^0.3.10

interface RandomNumberGenerator:
    def lock() -> bool: nonpayable
    def unlock(numberRange : uint256) -> uint256: nonpayable

bets: public(HashMap[address, uint256])

# Event to log game results
event Play:
    player: address
    result: bool
    randomNumber : uint8
    multiplier : decimal

rng : RandomNumberGenerator

@payable
@external
def __init__(randomContract : address):
    self.rng = RandomNumberGenerator(randomContract)

@external
def play(diceValue : uint8) -> bool:
    assert diceValue > 0, "too small"
    assert diceValue < 100, "too big"

    multiplier : decimal = 110.0 / (convert(diceValue, decimal) + 5.0)
    randomNumber : uint8 = convert(self.rng.unlock(100), uint8)

    assert randomNumber > 0, "randomNumber is fucked"
    result : bool = False

    if (randomNumber < diceValue):
        result = True
        send(msg.sender, convert(convert(self.bets[msg.sender], decimal) * multiplier, uint256))

    log Play(msg.sender, result, randomNumber, multiplier)
    
    return result

@external
@payable
def bet():
    assert self.balance > msg.value, "we're poor"
    self.rng.lock()
    self.bets[msg.sender] = msg.value
