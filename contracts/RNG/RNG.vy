#Deployed on Sepolia at: 0x1Cf23132e4797310A3897aB0e0367D861bdFA678

lockedTimestamp: public(HashMap[address, uint256])

event returnRandomNumber:
    number: uint256

#maps sender address to current block number
@external
def lock() -> bool:
    assert self.lockedTimestamp[msg.sender] == 0, "Number is already locked"
    self.lockedTimestamp[msg.sender] = block.number
    return True

#returns the block number that occured after 2 blocks 
#were mined from the original locked block number
@external
def unlock(numberRange: uint256) -> uint256:
    assert self.lockedTimestamp[msg.sender] > 0, "No number locked"
    assert self.lockedTimestamp[msg.sender] + 2 <= block.number, "Unlocking number too early"
    randomNumber: uint256 = convert(blockhash(self.lockedTimestamp[msg.sender] + 2), uint256) % numberRange
    self.lockedTimestamp[msg.sender] = 0
    assert self.lockedTimestamp[msg.sender] == 0, "Failed to unlock number"
    log returnRandomNumber(randomNumber)
    return randomNumber

@external
def random_between(min_val: uint256, max_val: uint256) -> uint256:
    assert min_val < max_val, "Minimum value must be less than maximum value"
    assert self.lockedTimestamp[msg.sender] > 0, "No number locked"
    assert self.lockedTimestamp[msg.sender] + 2 <= block.number, "Unlocking number too early"
    diff: uint256 = max_val - min_val
    randomNumber: uint256 = convert(blockhash(self.lockedTimestamp[msg.sender] + 2), uint256) % (diff + 1)
    result: uint256 = min_val + randomNumber
    self.lockedTimestamp[msg.sender] = 0
    assert self.lockedTimestamp[msg.sender] == 0, "Failed to reset lock"
    log returnRandomNumber(result)
    return result

@external
def reset_lock() -> bool:
    self.lockedTimestamp[msg.sender] = 0
    return True
