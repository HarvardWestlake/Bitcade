locks: public(HashMap[address, uint256])

#stars a betting session
@external
def lock() -> uint256:
    self.locks[msg.sender] = block.number
    return block.number

#ends a betting session/withdraw wins
@external
def unlock(numberRange: uint256) -> uint256:
    prevBlockNumber: uint256 = self.locks[msg.sender]
    assert prevBlockNumber + 2 < block.number, "Unlocking number too early"
    assert prevBlockNumber > 0, "No lock found"
    randomNumber: uint256 = convert(blockhash(prevBlockNumber + 2), uint256) % numberRange
    self.locks[msg.sender] = 0
    return randomNumber

#returns the block number that occured after 2 blocks
@external
def lockAndUnlock(numberRange: uint256) -> uint256:
    #if self.locks[msg.sender] == 0:
    #    self.locks[msg.sender] = block.number
    #    return False, 0
    #else:
        prevBlockNumber: uint256 = self.locks[msg.sender]
        assert prevBlockNumber + 2 < block.number, "Unlocking number too early"
        assert prevBlockNumber > 0, "No lock found"
        randomNumber: uint256 = convert(blockhash(prevBlockNumber + 2), uint256) % numberRange
        self.locks[msg.sender] = block.number
        #return True, randomNumber
        return randomNumber