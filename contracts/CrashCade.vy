# SPDX-License-Identifier: MIT
# @version ^0.3.10

# CrashCade Game Contract

# Define Events
event GameStarted:
    game_id: uint256

event GameEnded:
    game_id: uint256
    crash_point: uint256

event TokensInputted:
    player: indexed(address)
    amount: uint256

event PrizeClaimed:
    player: indexed(address)
    amount: uint256

# State variables with public getters
tokensInputted: public(uint256)
crashPoint: public(uint256)
gameActive: public(bool)
playerBalances: public(map(address, uint256))

# Randomness-related variables
rng_seed: public(uint256)

# Initialize the game with default values
@external
def __init__():
    self.gameActive = False
    self.rng_seed = block.number  # Seed the RNG with the current block number

# Start a new game round
@external
def startGame():
    assert not self.gameActive, "Game is already active"
    self.gameActive = True
    self.tokensInputted = 0  # Reset the token input counter
    self.setCrashPoint()  # Set a new crash point
    log GameStarted(block.number)

# Player inputs tokens with a specified amount
@external
def inputTokens(amount: uint256):
    assert self.gameActive, "Game is not active"
    assert amount > 0, "Bet amount must be greater than zero"
    
    self.tokensInputted += amount
    self.playerBalances[msg.sender] += amount
    log TokensInputted(msg.sender, amount)

# Set the crash point with a basic random number generator
@external
def setCrashPoint():
    assert self.gameActive, "Game is not active"
    
    # Generate a random crash point between 1 and 10 (exclusive)
    random_hash = sha256(convert(self.rng_seed, bytes))
    self.crashPoint = (convert(random_hash, uint256) % 9) + 1
    
    self.rng_seed = random_hash  # Update the seed for future randomness

# End the game upon reaching crashPoint
@external
def crash():
    assert self.gameActive, "Game is not active"
    
    self.gameActive = False
    self.tokensInputted = 0  # Reset token input counter
    log GameEnded(block.number, self.crashPoint)

# Allow players to receive their prize if the crash hasn't occurred yet
@external
def receivePrize():
    assert self.gameActive, "Game is not active"
    assert self.crashPoint > 1, "Invalid crash point"
    
    multiplier = self.crashPoint - 1  # Determine the multiplier
    player_balance = self.playerBalances[msg.sender]
    prize = player_balance * multiplier
    
    self.playerBalances[msg.sender] = prize
    log PrizeClaimed(msg.sender, prize)
    
    self.crash()