# @version ^0.3.10

# Interface definition for WyrmAutoBattler
interface WyrmAutoBattler:
    def getStats(_id: uint256) -> (uint256, uint256, uint256, uint256): view
    def getTotalStats(tokenId: uint256) -> uint256: view

# State variable to hold the ID
id: uint256

# Sort wyrms (placeholder)
@external
def sortWorms():
    pass

# Function to get the total stats from an external contract
@external
def getTotal(wyrm_auto_battler: address, id: uint256) -> uint256:
    # Create an instance of the WyrmAutoBattler interface at the given address
    battler: WyrmAutoBattler = WyrmAutoBattler(wyrm_auto_battler)
    
    # Call getTotalStats on the instance
    total: uint256 = battler.getTotalStats(id)
    
    return total
