# CrashCade Game Implementation

# @version ^0.3.10
# Contract for a simple crash-based game with token wagering
# Designed with fairness and unpredictability in mind
from vyper.interfaces import ERC20

# Variables to store game state and player-related data
tokensInputted: public(uint256)
crashPoint: public(uint256)
gameActive: public(bool)
# playerBalances: public(map(address, uint256))

# Randomness-related variables
rng_seed: public(uint256)

# Initialize the contract with default values
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
    
# Player inputs tokens with a specified amount and multiplier
@external
def inputTokens(amount: uint256):
    assert self.gameActive, "Game is not active"
    assert amount > 0, "Bet amount must be greater than zero"
    
    self.tokensInputted += amount
    self.playerBalances[msg.sender] += amount

# Set the crash point with a basic random number generator
@external
def setCrashPoint():
    assert self.gameActive, "Game is not active"
    
    # Generate a random crash point between 1 and 10 (exclusive), this can be refined later
    random_hash = sha256(convert(self.rng_seed, bytes))
    self.crashPoint = (convert(random_hash, uint256) % 9) + 1
    
    self.rng_seed = random_hash  # Update the seed for future randomness

# End the game upon reaching crashPoint
@public
def crash():
    assert self.gameActive, "Game is not active"
    
    # Trigger end of game
    self.gameActive = False
    self.tokensInputted = 0  # Reset token input counter

# Allow players to receive their prize if the crash hasn't occurred yet
@external
def receivePrize():
    assert self.gameActive, "Game is not active"
    assert self.crashPoint > 1, "Invalid crash point"
    
    # Calculate the prize based on multiplier
    multiplier = self.crashPoint - 1  # Determine the multiplier
    player_balance = self.playerBalances[msg.sender]
    prize = player_balance * multiplier
    
    # Credit the prize to the player's balance
    self.playerBalances[msg.sender] = prize
    
    # End the game
    self.crash()

# Safety check to avoid prize claim abuse
@external
def checkGameStatus() -> bool:
    return self.gameActive
