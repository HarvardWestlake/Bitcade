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


struct Game:
    player1: Player
    player2: Player
    betAmount: uint256
    winner: address
    gameOver: bool
    gameDraw: bool

games: public(HashMap[uint256, Game])
gameCounter: public(uint256)


@external
def __init__():
    self.gameCounter = 0

@external
def createGame(_betAmount: uint256) -> uint256:
    assert _betAmount > 0, "Bet amount must be greater than 0"

    gameID: uint256 = self.gameCounter

    self.games[gameID] = Game({
            player1: Player({addr: ZERO_ADDRESS, choice: 0, revealed: False, hashedChoice: EMPTY_BYTES32}),
            player2: Player({addr: ZERO_ADDRESS, choice: 0, revealed: False, hashedChoice: EMPTY_BYTES32}),
            betAmount: _betAmount,
            winner: ZERO_ADDRESS,
            gameOver: False,
            gameDraw: False
        })
    self.gameCounter += 1
    return gameID

@external
def joinGame(gameID: uint256, _choice: uint256, _rand: uint256):
    assert self.accountBalance[msg.sender] >= self.games[gameID].betAmount, "You must send the correct bet amount to join the game"
    assert _choice == ROCK or _choice == PAPER or _choice == SCISSORS, "Invalid choice. Must be 1 (ROCK), 2 (PAPER), or 3 (SCISSORS)"

    if self.games[gameID].player1.addr == ZERO_ADDRESS:
        self.games[gameID].player1 = Player({
            addr: msg.sender,
            choice: _choice,
            revealed: False,
            hashedChoice: keccak256(_abi_encode(msg.sender, _rand, _choice))
        })
        self.accountBalance[msg.sender] -= self.games[gameID].betAmount

    elif self.games[gameID].player2.addr == ZERO_ADDRESS:
        assert self.games[gameID].player1.addr != msg.sender, "You cannot play against yourself"
        self.games[gameID].player2 = Player({
            addr: msg.sender,
            choice: _choice,
            revealed: False,
            hashedChoice: keccak256(_abi_encode(msg.sender, _rand, _choice))
        })
        self.accountBalance[msg.sender] -= self.games[gameID].betAmount
    else:
        raise "Game is full"

@external
def revealChoice(gameID: uint256, _choice: uint256, _rand: uint256):
    assert not self.games[gameID].gameOver, "Game is already over"
    assert self.games[gameID].player1.addr != ZERO_ADDRESS and self.games[gameID].player2.addr != ZERO_ADDRESS, "Both players must join the game before revealing their choices"
    
    if msg.sender == self.games[gameID].player1.addr:
        assert not self.games[gameID].player1.revealed, "You have already revealed your choice"
        assert keccak256(_abi_encode(msg.sender, _rand, _choice)) == self.games[gameID].player1.hashedChoice, "Hash does not match"
        self.games[gameID].player1.choice = _choice
        self.games[gameID].player1.revealed = True
    elif msg.sender == self.games[gameID].player2.addr:
        assert not self.games[gameID].player2.revealed, "You have already revealed your choice"
        assert keccak256(_abi_encode(msg.sender, _rand, _choice)) == self.games[gameID].player2.hashedChoice, "Hash does not match"
        self.games[gameID].player2.choice = _choice
        self.games[gameID].player2.revealed = True
    else:
        raise "You are not part of this game"

    if self.games[gameID].player1.revealed and self.games[gameID].player2.revealed:
        self.games[gameID].winner = self.determineWinner(gameID)
        if self.games[gameID].winner == ZERO_ADDRESS:
            self.games[gameID].gameDraw = True
        self.games[gameID].gameOver = True
        self.distributePrizes(gameID)

@internal
@view
def determineWinner(gameID: uint256) -> address:
    assert self.games[gameID].player1.revealed and self.games[gameID].player2.revealed, "Both players must reveal their choices before determining the winner"

    if self.games[gameID].player1.choice == self.games[gameID].player2.choice:
        return ZERO_ADDRESS
    elif self.games[gameID].player1.choice == ROCK and self.games[gameID].player2.choice == SCISSORS:
        return self.games[gameID].player1.addr
    elif self.games[gameID].player1.choice == PAPER and self.games[gameID].player2.choice == ROCK:
        return self.games[gameID].player1.addr
    elif self.games[gameID].player1.choice == SCISSORS and self.games[gameID].player2.choice == PAPER:
        return self.games[gameID].player1.addr
    else:
        return self.games[gameID].player2.addr


@internal 
def distributePrizes(gameID: uint256):
    assert self.games[gameID].gameOver, "Game is not over yet"
    
    if self.games[gameID].gameDraw:
        self.accountBalance[self.games[gameID].player1.addr] += self.games[gameID].betAmount
        self.accountBalance[self.games[gameID].player2.addr] += self.games[gameID].betAmount
    else:
        self.accountBalance[self.games[gameID].winner] += (self.games[gameID].betAmount * 2)