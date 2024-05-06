#Deployed on Sepolia at: 0x1Cf23132e4797310A3897aB0e0367D861bdFA678

lockedTimestamp: public(HashMap[address, uint256])

event returnRandomNumber:
    number: uint256

#maps sender address to current block number
@external
@payable
def lockCurrent() -> bool:
    assert self.lockedTimestamp[msg.sender] == 0, "Number is already locked"
    self.lockedTimestamp[msg.sender] = block.number
    return True

@external
@payable
def updateLock(numberRange : uint256) -> (uint256, uint256, uint256):
    #unlock previous lock
    assert self.lockedTimestamp[msg.sender] > 0, "No number locked"
    assert self.lockedTimestamp[msg.sender] + 2 < block.number, "Unlocking number too early"
    prevBlock : uint256 = self.lockedTimestamp[msg.sender]
    randomNumber: uint256 = convert(blockhash(prevBlock + 2), uint256)

    #update new lock
    self.lockedTimestamp[msg.sender] = block.number

    log returnRandomNumber(randomNumber)
    return prevBlock, block.number, randomNumber

#returns the block number that occured after 2 blocks 
#were mined from the original locked block number
@external
def unlockLatest(numberRange: uint256) -> uint256:
    assert self.lockedTimestamp[msg.sender] > 0, "No number locked"
    assert self.lockedTimestamp[msg.sender] + 2 <= block.number, "Unlocking number too early"
    randomNumber: uint256 = convert(blockhash(self.lockedTimestamp[msg.sender] + 2), uint256) % numberRange
    self.lockedTimestamp[msg.sender] = 0
    log returnRandomNumber(randomNumber)
    return randomNumber

