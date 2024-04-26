from vyper.interfaces import ERC20

# Interface for interacting with ERC20 tokens
interface IERC20:
    def balanceOf(_owner: address) -> uint256: view

@external
@view
def get_token_balance(token_addr: address, owner: address) -> uint256:
    """
    @dev Return the balance of an ERC20 token for a given owner address.
    @param token_addr The address of the ERC20 token contract.
    @param owner The address whose balance to query.
    @return The balance of the token for the given address.
    """
    return IERC20(token_addr).balanceOf(owner)

# Maps user addresses to their respective locked timestamps
lockedTimestamp: public(HashMap[address, int256])

@external
def lock() -> bool:
    """
    Locks the current block number for the sender to allow future RNG.
    Ensures that no previous number is locked.
    """
    assert self.lockedTimestamp[msg.sender] < 0, "Number is already locked"
    # Convert block.number to int256 before assignment
    self.lockedTimestamp[msg.sender] = convert(block.number, int256)
    return True

@external
def unlock(numberRange: int128) -> int128:
    """
    Unlocks a random number within the specified range if the number was locked exactly 2 blocks ago.
    """
    assert self.lockedTimestamp[msg.sender] > 0, "No number locked"
    # Convert block.number to int256 before comparison
    assert convert(block.number, int256) == self.lockedTimestamp[msg.sender] + 2, "Unlocking number too early"

    # Calculate random number using blockhash and modulo operation
    randomNumber: int128 = convert(blockhash(block.number - 1), int128) % numberRange
    self.lockedTimestamp[msg.sender] = -1  # Reset the locked timestamp

    # Confirm the number has been successfully unlocked
    assert self.lockedTimestamp[msg.sender] == -1, "Failed to unlock number"

    return randomNumber
