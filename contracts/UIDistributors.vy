# Events for logging actions
event PaymentReceived:
    sender: indexed(address)
    value: uint256
    game_id: uint256

event DistributorPaid:
    distributor: indexed(address)
    amount: uint256

event OwnerPaid:
    owner: indexed(address)
    amount: uint256

# Struct to hold game information
struct Game:
    owner: address
    distributor: address
    isActive: bool

# Mapping from game ID to Game structs
games: HashMap[uint256, Game]

# Owner address (can be a multisig wallet for further decentralization)
owner: public(address)

@external
def __init__(_owner: address):
    """
    Initializes the contract with the contract owner's address.
    """
    self.owner = _owner

@external
def register_game(game_id: uint256, _owner: address, distributor: address):
    """
    Register a new game with its owner and UI distributor.
    Only the contract owner can register games.
    """
    assert msg.sender == self.owner, "Only owner can register games."
    assert not self.games[game_id].isActive, "Game already registered."
    self.games[game_id] = Game({
        owner: _owner,
        distributor: distributor,
        isActive: True
    })

@payable
@external
def play_game(game_id: uint256):
    """
    Handle payments for playing a game.
    Distributes revenue between game owner and UI distributor.
    """
    assert self.games[game_id].isActive, "Game not active."
    game: Game = self.games[game_id]  # Declare the type of 'game' explicitly

    # Calculate payments
    distributor_payment: uint256 = msg.value * 60 / 100  # 60%
    owner_payment: uint256 = msg.value - distributor_payment  # 40%
    
    # Transfer payments
    send(game.distributor, distributor_payment)
    send(game.owner, owner_payment)
    
    # Emit events for transparency
    log PaymentReceived(msg.sender, msg.value, game_id)
    log DistributorPaid(game.distributor, distributor_payment)
    log OwnerPaid(game.owner, owner_payment)

@external
def deactivate_game(game_id: uint256):
    """
    Deactivate a game, preventing further plays.
    Only the game owner can deactivate their game.
    """
    assert msg.sender == self.games[game_id].owner, "Only game owner can deactivate."
    self.games[game_id].isActive = False
