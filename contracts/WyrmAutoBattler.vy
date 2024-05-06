from ERC721 import Token

token_contract : Token
id1 : uint256
id2 : uint256

@external
def battle(_player1 : address, _id1 : uint256, _player2 : address, _id2 : uint256) -> address:
    assert self.token_contract.ownerOf(_id1) == _player1
    assert self.token_contract.ownerOf(_id2) == _player2
    self.id1 = _id1
    self.id2 = _id2

    return _player1

@external
def playRound(_id1 : uint256, _id2 : uint256) -> (uint256, uint256):
    return (0, 1)

@external
def rand() -> uint256:
    return 42