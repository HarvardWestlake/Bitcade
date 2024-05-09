# @version ^0.3.10

#NOTE for now we are using eth, once the token is done use the token
# This is a dummy balance variable since we don't have a Token contract yet
accountBalance: public(HashMap[address, uint256])

@external
def initBalance(_balance: uint256):
    self.accountBalance[msg.sender] = _balance

@external
@view
def getAccountBalance() -> uint256:
    
    return self.accountBalance[msg.sender]

ROCK: constant(uint256) = 1
PAPER: constant(uint256) = 2
SCISSORS: constant(uint256) = 3

#choice of player is hidden by combining the public key, a random number of players choosing, and the choice itself, then hashing
struct Player:
    addr: address
    choice: uint256
    revealed: bool
    hashedChoice: bytes32


player1: public(Player)
player2: public(Player)
betAmount: public(uint256)
winner: public(address)
gameOver: public(bool)
gameDraw: public(bool)

@external
def __init__(_betAmount: uint256):
    assert _betAmount > 0, "Bet amount must be greater than 0"

    self.betAmount = _betAmount
    self.winner = ZERO_ADDRESS
    self.gameOver = False
    self.gameDraw = False

@external
def joinGame(_choice: uint256, _rand: uint256):
    assert self.accountBalance[msg.sender] >= self.betAmount, "You must send the correct bet amount to join the game"
    assert _choice == ROCK or _choice == PAPER or _choice == SCISSORS, "Invalid choice. Must be 1 (ROCK), 2 (PAPER), or 3 (SCISSORS)"

    if(self.player1.addr == ZERO_ADDRESS):
        self.player1 = Player({
            addr: msg.sender,
            choice: _choice,
            revealed: False,
            #hashes using the three values
            hashedChoice: keccak256(_abi_encode(msg.sender, _rand, _choice))
        })
        self.accountBalance[msg.sender] = self.accountBalance[msg.sender] - self.betAmount

    elif(self.player2.addr == ZERO_ADDRESS):
        assert self.player1.addr != msg.sender, "You cannot play against yourself"
        self.player2 = Player({
            addr: msg.sender,
            choice: _choice,
            revealed: False,
            hashedChoice: keccak256(_abi_encode(msg.sender, _rand, _choice))
        })
        self.accountBalance[msg.sender] = self.accountBalance[msg.sender] - self.betAmount
    else:
        raise "Game is full"

@external
def revealChoice(_choice: uint256, _rand: uint256):
    assert not self.gameOver, "Game is already over"
    assert self.player1.addr != ZERO_ADDRESS and self.player2.addr != ZERO_ADDRESS, "Both players must join the game before revealing their choices"
    
    if(msg.sender == self.player1.addr):
        assert self.player1.revealed == False, "You have already revealed your choice"
        assert keccak256(_abi_encode(msg.sender, _rand, _choice)) == self.player1.hashedChoice, "Hash does not match"
        self.player1.choice = _choice
        self.player1.revealed = True
    elif(msg.sender == self.player2.addr):
        assert self.player2.revealed == False, "You have already revealed your choice"
        assert keccak256(_abi_encode(msg.sender, _rand, _choice)) == self.player2.hashedChoice, "Hash does not match"
        self.player2.choice = _choice
        self.player2.revealed = True
    else:
        raise "You are not part of this game"

    if(self.player1.revealed and self.player2.revealed):
        self.winner = self.determineWinner()
        if(self.winner == ZERO_ADDRESS):
            self.gameDraw = True
        self.gameOver = True
        self.distributePrizes()

@internal
@view
def determineWinner() -> address:
    assert self.player1.revealed and self.player2.revealed, "Both players must reveal their choices before determining the winner"

    if(self.player1.choice == self.player2.choice):
        return ZERO_ADDRESS
    elif(self.player1.choice == ROCK and self.player2.choice == SCISSORS):
        return self.player1.addr
    elif(self.player1.choice == PAPER and self.player2.choice == ROCK):
        return self.player1.addr
    elif(self.player1.choice == SCISSORS and self.player2.choice == PAPER):
        return self.player1.addr
    else:
        return self.player2.addr

@internal 
def distributePrizes():
    assert self.gameOver, "Game is not over yet"
    
    if(self.gameDraw):
        self.accountBalance[self.player1.addr] = self.accountBalance[self.player1.addr] + self.betAmount
        self.accountBalance[self.player2.addr] = self.accountBalance[self.player2.addr] + self.betAmount
    else:
        self.accountBalance[self.winner] = self.accountBalance[self.winner] + (self.betAmount * 2)