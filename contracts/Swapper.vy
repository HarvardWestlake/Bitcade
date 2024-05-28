# @version ^0.3.10

interface Wolvercoin:
    def swapperMint(_to: address, _value: uint256): nonpayable

token: public(Wolvercoin)
owner: public(address)


@external
def __init__(_token: address):
    self.token = Wolvercoin(_token)
    self.owner = msg.sender

# Calls the swapperMint function of the token contract and mints
# tokens to the sender based on the amount of ETH sent
@payable
@external
def buy():
    assert msg.value > 0, "Must send ETH to buy"
    self.token.swapperMint(msg.sender, msg.value)

# Withdraws the contract's ETH balance to the owner
@external
def withdraw():
    assert msg.sender == self.owner, "Only owner can withdraw"
    send(self.owner, self.balance)

@external
def setOwner(_owner: address):
    assert msg.sender == self.owner, "Only owner can set owner"
    self.owner = _owner