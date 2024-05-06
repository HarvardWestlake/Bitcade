locks : public(HashMap[address, uint256])

#returns the block number that occured after 2 blocks
@external
def lockAndUnlock(numberRange: uint256) -> (bool, uint256, uint256, uint256):
    assert self.locks[msg.sender] + 2 < block.number, "Unlocking number too early"
    assert self.locks[msg.sender] > 0, "No lock found"

    randomNumber: uint256 = convert(blockhash(self.locks[msg.sender] + 2), uint256)
    self.locks[msg.sender] = block.number
    return self.locks[msg.sender] == block.number, self.locks[msg.sender], block.number, randomNumber 

#stars a betting session
@external
def lock() -> uint256:
    self.locks[msg.sender] = block.number
    return block.number

#ends a betting session/withdraw wins
@external
def unlock(numberRange: uint256) -> uint256:
    assert self.locks[msg.sender] + 2 < block.number, "Unlocking number too early"
    assert self.locks[msg.sender] > 0, "No lock found"
    randomNumber: uint256 = convert(blockhash(self.locks[msg.sender] + 2), uint256) % numberRange
    self.locks[msg.sender] = 0
    return randomNumber

@external
@view
def getLockedBlock() -> uint256:
    return self.locks[msg.sender]