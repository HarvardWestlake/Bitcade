from vyper.interfaces import ERC20
TOKEN_VALUES_RANGE: constant(uint256) = 50000
NUM_BRIEFCASES: constant (uint256) = 15
GAME_ENTRY_FEE: constant (uint256) = 100



chosen_briefcases: HashMap[address, HashMap[uint256, uint256]]
has_chosen: HashMap [address, bool]
random_seed: bytes32
token_balance: HashMap [address, uint256]


event BriefCaseOpened:
    playerAddress: address
    briefCaseNumber: uint256
    value: uint256

event OfferMade:

    playerAddress: address
    tokenOffer: uint256

event GameFinished:

    playerAddress: address
    winnings: uint256

event GameStarted:

    playerAddress: address
    entry_fee: uint256

current_val: public (uint256)
token_values: public (HashMap[uint256, uint256])
@payable
@external
def start_game ():
    assert msg.value >= GAME_ENTRY_FEE, "Insufficient entry fee"

    self.token_balance[msg.sender] -= GAME_ENTRY_FEE

    log GameStarted (msg.sender, GAME_ENTRY_FEE)

@internal
def random_number(maximum_value: uint256) -> uint256: 
    current_blockhash: bytes32 = blockhash(block.number)
    random_val: uint256 = convert (current_blockhash, uint256)
    self.current_val = random_val % maximum_value
    return self.current_val
@internal
def calculateAverageTokens() -> uint256: 
    total: uint256 = 0
    array: uint256[3] = [self.chosen_briefcases[msg.sender][0], self.chosen_briefcases[msg.sender][1], self.chosen_briefcases[msg.sender][2]]
    for i in array:
        total += i

    return total / 2

@external
def openBriefcase (briefCase_number: uint256):
    briefcase_value: uint256 = self.chosen_briefcases[msg.sender][briefCase_number]
@internal
def generateRandomTokenValues():
   remaining_tokens: uint256 = TOKEN_VALUES_RANGE * NUM_BRIEFCASES
   
   for i in range (1, NUM_BRIEFCASES + 1):
    if i == NUM_BRIEFCASES:
        self.token_values[i] = remaining_tokens
@view
@internal
def hasChosen (_player: address) -> bool:
    return self.has_chosen[_player]
@external
def accept_offer (_accept: bool, _player: address):
    if _accept:
            average_tokens: uint256 = self.calculateAverageTokens()
            self.token_balance[_player] += average_tokens
            self.has_chosen[_player] = True
    else:
        pass
@external
def get_random_number(seed: uint256) -> uint256:
    return (seed % 15) + 1
@external
def choose_briefcases():
    index: uint256 = 0
    values: uint256[3] = [0, 0, 0]
    briefcaseNumbers: uint256[3] = [0, 0, 0]
    for i in range(14):
        self.token_values[i] = self.random_number(TOKEN_VALUES_RANGE)
    
    for i in range (3):
        briefCase_num: uint256 = self.random_number(NUM_BRIEFCASES)
        values[i] = self.token_values[briefCase_num]
        self.chosen_briefcases[msg.sender][briefCase_num] = values[i]
        self.token_values[briefCase_num] = 0

@external
def open_briefcase(_briefcase_number: uint256):
    briefcase_value: uint256 = self.chosen_briefcases[msg.sender][_briefcase_number]
    self.chosen_briefcases[msg.sender][_briefcase_number] = 0
    log BriefCaseOpened (msg.sender, _briefcase_number, briefcase_value)
    average_tokens: uint256 = self.calculateAverageTokens()
    log OfferMade (msg.sender, average_tokens)


            
        

