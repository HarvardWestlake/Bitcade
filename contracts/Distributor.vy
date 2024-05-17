# @version ^0.3.10

interface Wolvercoin:
    def transfer(_to: address, _value: uint256): nonpayable
    def balanceOf(_owner: address) -> uint256: view

token: public(Wolvercoin)
deployer: public(address)
distributions: public(HashMap[address, bool])
distributionsStarted: public(bool)
distributionClaimers: public(uint256)
totalDistributions: public(uint256)


@external
def __init__(_token: address):
    self.token = Wolvercoin(_token)
    self.deployer = msg.sender
    self.distributionsStarted = False
    self.totalDistributions = self.token.balanceOf(self)

# Calls the swapperMint function of the token contract and mints
# tokens to the sender based on the amount of ETH sent
@external
def addToDistribution(_to: address):
    assert not self.distributionsStarted == False, "Distribution has not started"
    assert msg.sender == self.deployer, "Only the deployer can add to the distribution"
    self.distributions[_to] = True

@external
def removeFromDistribution(_to: address):
    assert self.distributionsStarted == False, "Distribution has not started"
    assert msg.sender == self.deployer, "Only the deployer can remove from the distribution"
    self.distributions[_to] = False

@external
def startDistribution():
    assert msg.sender == self.deployer, "Only the deployer can start the distribution"
    self.distributionsStarted = True

@external
def claimDistribution():
    assert self.distributions[msg.sender] == True, "No distribution to claim"
    _value: uint256 = self.totalDistributions / self.distributionClaimers
    self.token.transfer(msg.sender, _value)