#Deployed on Sepolia at: 0x1Cf23132e4797310A3897aB0e0367D861bdFA678

#simply a transaction
@external
def lock() -> uint256:
    return block.number

#returns the block number that occured after 2 blocks 
#were mined from the original locked block number
@external
@view
def unlock(blockNumber: uint256, numberRange: uint256) -> uint256:
    assert blockNumber + 2 < block.number, "Unlocking number too early"
    randomNumber: uint256 = convert(blockhash(blockNumber + 2), uint256) % numberRange
    return randomNumber
