interface RandomNumberGenerator:
    def lockCurrent() -> uint256: nonpayable
    def unlockLatest(numberRange: uint256) -> uint256: nonpayable
    def updateLock(numberRange: uint256) -> uint256: nonpayable

event Play:
    result : bool
    winnings : uint256
    randomNumber : uint8
    multiplier : decimal
    player : address
    
rng : RandomNumberGenerator

bets : HashMap[address, uint256]

@payable
@external
def __init__(randomContract : address):
    self.rng = RandomNumberGenerator(randomContract)

@external
@payable
def playGame(diceValue : uint8) -> uint8:
    assert diceValue > 0, "too small"
    assert diceValue < 100, "too big"

    multiplier : decimal = 110.0 / (convert(diceValue, decimal) + 5.0)
    randomNumber : uint8 = convert(self.rng.updateLock(100), uint8)
    result : bool = False
    winnings : uint256 = 0

    assert randomNumber >= 0, "randomNumber is fucked"
    assert randomNumber <= 100, "randomNumber is fucked"

    if (randomNumber < diceValue):
        result = True
        winnings = convert(convert(msg.value, decimal) * multiplier, uint256)
        send(msg.sender, winnings)

    self.bets[msg.sender] = msg.value
    log Play(result, winnings, randomNumber, multiplier, msg.sender)
    return randomNumber
    
@external
def cashOut(diceValue : uint8) -> uint8:
    assert diceValue > 0, "too small"
    assert diceValue < 100, "too big"
    multiplier : decimal = 110.0 / (convert(diceValue, decimal) + 5.0)
    randomNumber : uint8 = convert(self.rng.unlockLatest(100), uint8)
    result : bool = False
    winnings : uint256 = 0

    if (randomNumber < diceValue):
        result = True
        winnings = convert(convert(self.bets[msg.sender], decimal) * multiplier, uint256)
        send(msg.sender, winnings)

    log Play(result, winnings, randomNumber, multiplier, msg.sender)
    return randomNumber


@external
@payable
def startGame():
    self.rng.lockCurrent()
    self.bets[msg.sender] = msg.value