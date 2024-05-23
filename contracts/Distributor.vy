# @version ^0.3.10

interface Wolvercoin:
    def transfer(_to: address, _value: uint256): nonpayable
    def balanceOf(_owner: address) -> uint256: view

token: public(Wolvercoin)
deployer: public(address)
distributions: public(HashMap[address, bool])
distributionStarted: public(bool)
distributionClaimers: public(uint256)
totalDistributions: public(uint256)

@external
def __init__(_token: address):
    self.token = Wolvercoin(_token)
    self.deployer = msg.sender
    self.distributionStarted = False

@external
def setDeployer(_deployer: address):
    assert msg.sender == self.deployer, "Only the deployer can set the deployer"
    self.deployer = _deployer

# Calls the swapperMint function of the token contract and mints
# tokens to the sender based on the amount of ETH sent
@external
def addToDistribution(_to: address):
    assert self.distributionStarted == False, "Distribution has not started"
    assert msg.sender == self.deployer, "Only the deployer can add to the distribution"
    assert self.distributions[_to] == False, "Address is already in the distribution"
    self.distributions[_to] = True
    self.distributionClaimers += 1

@external
def removeFromDistribution(_to: address):
    assert self.distributionStarted == False, "Distribution has not started"
    assert msg.sender == self.deployer, "Only the deployer can remove from the distribution"
    assert self.distributions[_to] == True, "Address is not in the distribution"
    self.distributions[_to] = False
    self.distributionClaimers -= 1

@external
def startDistribution():
    assert self.distributionStarted == False, "Distribution has already started"
    assert msg.sender == self.deployer, "Only the deployer can start the distribution"
    self.totalDistributions = self.token.balanceOf(self)
    self.distributionStarted = True

@external
def claimDistribution():
    assert self.distributions[msg.sender] == True, "No distribution to claim"
    _value: uint256 = 10000 * self.totalDistributions / self.distributionClaimers / 10000
    self.token.transfer(msg.sender, _value)
    self.distributions[msg.sender] = False