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
    briefCaseValue: uint256

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
    return 2

@external
def openBriefcase (briefCase_number: uint256):
    briefcase_value: uint256 = self.chosen_briefcases[msg.sender][briefCase_number]
    
    




