import random as random_module

# Contract Deployment Parameters
TOKEN_VALUES_RANGE: constant(uint256) = 50000  # Maximum token value for a briefcase
NUM_BRIEFCASES: constant(uint256) = 15
GAME_ENTRY_FEE: constant(uint256) = 100  # Entry fee in tokens to start a game

# Contract Storage
chosen_briefcases: HashMap[address, HashMap[uint256, uint256]]
has_chosen: HashMap[address, bool]
random_seed: bytes32
token_balance: HashMap[address, uint256]

# Events
event BriefcaseOpened(address, uint256, uint256):
    """
    Emitted when a briefcase is opened
    player: address of the player
    briefcase: number of the opened briefcase
    value: token value inside the briefcase
    """

event OfferMade(address, uint256):
    """
    Emitted when an offer is made to the player
    player: address of the player
    offer: token value offered
    """

event GameFinished(address, uint256):
    """
    Emitted when the game is finished
    player: address of the player
    winnings: token value won
    """

event GameStarted(address, uint256):
    """
    Emitted when a player starts a new game
    player: address of the player
    entry_fee: token value paid as entry fee
    """

@external
def __init__(_random_seed: bytes32):
    
    self.random_seed = _random_seed

@payable
@external
def start_game():
   
    assert msg.value >= GAME_ENTRY_FEE, "Insufficient entry fee"

    # Deduct the entry fee from the player's balance
    self.token_balance[msg.sender] -= GAME_ENTRY_FEE

    # Log the game start event
    log GameStarted(msg.sender, GAME_ENTRY_FEE)

@external
@external
def choose_briefcases():
    """
    Generates random token values for the briefcases and allows a player to choose 3 briefcases
    """
    assert len(self.chosen_briefcases[msg.sender]) == 0, "You have already chosen briefcases"

    # Generate random token values for the briefcases
    token_values: map(uint256, uint256) = self.generateRandomTokenValues()

    # Let the player choose 3 unique briefcases
    chosen_briefcases: map(uint256, uint256) = {}
    for i in range(3):
        briefcase_number: uint256 = random_module.sample(range(1, len(token_values) + 1), 1)[0]
        while briefcase_number in chosen_briefcases:
            briefcase_number = random_module.sample(range(1, len(token_values) + 1), 1)[0]
        chosen_briefcases[briefcase_number] = token_values[briefcase_number]
        del token_values[briefcase_number]  # Remove the chosen briefcase from token_values

    self.briefcases = token_values
    self.chosen_briefcases[msg.sender] = chosen_briefcases


@view
@internal
def _calculate_average_tokens(_chosen_briefcases: map(uint256, uint256)) -> uint256:
    total: uint256 = 0
    for briefcase_value in _chosen_briefcases.values():
        total += briefcase_value
    return total / 2

@external
def open_briefcase(_briefcase_number: uint256):
    assert _briefcase_number in self.chosen_briefcases[msg.sender], "Invalid briefcase number"

    briefcase_value: uint256 = self.chosen_briefcases[msg.sender][_briefcase_number]
    self.chosen_briefcases[msg.sender].remove(_briefcase_number)

    # Log the opened briefcase
    log BriefcaseOpened(msg.sender, _briefcase_number, briefcase_value)

    if len(self.chosen_briefcases[msg.sender]) == 2:
        # Make an offer after opening the first briefcase
        average_tokens: uint256 = self._calculate_average_tokens(self.chosen_briefcases[msg.sender])
        log OfferMade(msg.sender, average_tokens)

    elif len(self.chosen_briefcases[msg.sender]) == 1:
        # Open the last briefcase and finish the game
        remaining_briefcase: uint256 = list(self.chosen_briefcases[msg.sender].keys())[0]
        winnings: uint256 = self.chosen_briefcases[msg.sender][remaining_briefcase]
        log GameFinished(msg.sender, winnings)

        # Transfer winnings to the player
        self.token_balance[msg.sender] += winnings
        self.chosen_briefcases[msg.sender].clear()
        self.has_chosen[msg.sender] = True

@external
def accept_offer(_accept: bool):
    
    assert len(self.chosen_briefcases[msg.sender]) == 2, "Invalid game state"

    if _accept:
        # Calculate and transfer the offered tokens
        average_tokens: uint256 = self._calculate_average_tokens(self.chosen_briefcases[msg.sender])
        self.token_balance[msg.sender] += average_tokens
        self.chosen_briefcases[msg.sender].clear()
        self.has_chosen[msg.sender] = True
    else:
        # Continue the game
        pass

@view
@internal
def hasChosen(_player: address) -> bool:
    
    return self.has_chosen[_player]

@internal
def generateRandomTokenValues() -> map(uint256, uint256):
    token_values: map(uint256, uint256) = {}
    remaining_tokens: uint256 = TOKEN_VALUES_RANGE * NUM_BRIEFCASES

    for i in range(1, NUM_BRIEFCASES + 1):
        if i == NUM_BRIEFCASES:
            token_values[i] = remaining_tokens
        else:
            random_value: uint256 = random_module.sample_from_bytes(self.random_seed, remaining_tokens)
            token_values[i] = random_value
            remaining_tokens -= random_value

    return token_values