# Data structures
game_id: public(uint256)
games: public(HashMap[uint256, HashMap[address, bytes32]])
player_hands: public(HashMap[uint256, HashMap[address, uint256[2]]])
computer_hands: public(HashMap[uint256, uint256[2]])

@internal
@view
def getAccountBalance(player: address) -> uint256:
    # This will be handled in another contract
    # Will return the value of the user's account
    return 10000

@external
@payable
def startGame(player: address, bet: uint256):
    # Check if player has sufficient balance
    bal : uint256 = self.getAccountBalance(player) 
    assert bal >= bet, "Insufficient balance"

    # Create a new game with a unique game ID
    self.game_id += 1
    game_id: uint256 = self.game_id  # Local variable

    # Set a random seed using block timestamp
    seed: bytes32 = keccak256(concat(blockhash(block.number - 1), convert(block.timestamp, bytes32)))
    self.games[game_id][player] = seed

    # Distribute initial dice/cards
    player_hand: uint256[2] = [self.generate_random_number(), self.generate_random_number()]
    computer_hand: uint256[2] = [self.generate_random_number(), self.generate_random_number()]

    # Store the player's and computer's hands
    self.player_hands[game_id][player] = player_hand
    self.computer_hands[game_id] = computer_hand

@external
@view
def get_player_hand(game_id: uint256, player: address) -> uint256[2]:
    return self.player_hands[game_id][player]

@external
@view
def get_computer_hand(game_id: uint256) -> uint256[2]:
    return self.computer_hands[game_id]

# Placeholder for random number generation
@internal
def generate_random_number() -> uint256:
    # This function will be handled by another contract
    return 1  # Placeholder logic
