# Maps user addresses to their respective locked timestamps
lockedTimestamp: public(HashMap[address, uint256])

event returnRandomNumber:
    number: uint256

# Interface for interacting with ERC20 tokens

@external
def lock() -> bool:
    #map sender address to current block number
    assert self.lockedTimestamp[msg.sender] == 0, "Number is already locked"
    self.lockedTimestamp[msg.sender] = block.number
    return True

@external
def unlock(numberRange: uint256) -> uint256:
    #returns the block number that occured after 2 blocks were mined from the orriginal locked block number
    assert self.lockedTimestamp[msg.sender] > 0, "No number locked"
    
    assert self.lockedTimestamp[msg.sender] + 2 <= block.number, "Unlocking number too early"

    randomNumber: uint256 = convert(blockhash(self.lockedTimestamp[msg.sender] + 2), uint256) % numberRange
    self.lockedTimestamp[msg.sender] = 0

    # confirm that the users address has been reset
    assert self.lockedTimestamp[msg.sender] == 0, "Failed to unlock number"

    #returns an event of with the random number  
    log returnRandomNumber(randomNumber)

    return randomNumber
