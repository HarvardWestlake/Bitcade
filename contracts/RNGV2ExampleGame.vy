interface RandomNumberGenerator:
    def lock() -> uint256: nonpayable
    def unlock(blockNumber : uint256, numberRange : uint256) -> uint256: nonpayable

bets: public(HashMap[address, uint256])

# Event to log game results
event Betted:
    blockNumber : uint256
    msgValue : uint256

rng : RandomNumberGenerator

@payable
@external
def __init__(randomContract : address):
    self.rng = RandomNumberGenerator(randomContract)

@external
def play(blockNumber : uint256, diceValue : uint8) -> uint256:
    assert diceValue > 0, "too small"
    assert diceValue < 100, "too big"

    multiplier : decimal = 110.0 / (convert(diceValue, decimal) + 5.0)
    randomNumber : uint8 = convert(self.rng.unlock(blockNumber, 100), uint8)

    assert randomNumber > 0, "randomNumber is fucked"
    result : bool = False
    winnings : uint256 = 0

    if (randomNumber < diceValue):
        result = True
        winnings = convert(convert(self.bets[msg.sender], decimal) * multiplier, uint256)

    send(msg.sender, winnings)
    
    return winnings

@external
@payable
def bet():
    assert self.balance > msg.value, "we're poor"
    self.bets[msg.sender] = msg.value
    blockNumber : uint256 = self.rng.lock()
    log Betted(self.bets[msg.sender], blockNumber)
