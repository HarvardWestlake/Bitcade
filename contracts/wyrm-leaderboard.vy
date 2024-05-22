# @version ^0.3.10

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

@external
def getTotal(id: uint256) -> uint256:
    # Declare and initialize variables
    total: uint256 = 0

    total = WyrmAutoBattler.getTotalStats(id)
    
