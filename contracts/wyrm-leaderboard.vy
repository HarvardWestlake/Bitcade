# @version ^0.3.10

from vyper.interfaces import ERC20

implements: ERC20

# State variable to hold the ID
id: uint256

# Interface definition for WyrmAutoBattler
interface WyrmAutoBattler:
    def getStats(_id: uint256) -> (uint256, uint256, uint256, uint256): view

# Sort wyrms
@external
def sortWorms():
    # Placeholder function as there is no actual implementation provided
    pass

# Helper method to get the total stats of a wyrm
@internal
def getTotal(id: uint256) -> uint256:
    # Retrieve stats using the interface method
    attack: uint256
    defense: uint256
    speed: uint256
    health: uint256
    attack, defense, speed, health = WyrmAutoBattler.getStats(id)
    
    # Calculate the total stats
    total: uint256 = attack + defense + speed + health
    
    return total
