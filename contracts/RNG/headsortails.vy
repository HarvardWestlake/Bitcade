# RNG Contract Interface
interface IRNGContract:
    def lock() -> bool: nonpayable
    def unlock(numberRange: uint256) -> uint256: nonpayable

# Event for Heads or Tails result
event HeadsOrTails:
    result: String[5]

# Heads or Tails Contract
@external
def play(rng_address: address):
    # Create an instance of the RNG contract using its address
    rng_contract: IRNGContract = IRNGContract(rng_address)

    # Lock the number in RNG
    success: bool = rng_contract.lock()
    assert success, "Failed to lock the number"

    # Assuming we need to wait for some blocks to be mined here;
    # This should be handled off-chain or in a different manner to meet the 2 block condition.

    # Unlock the number with 2 as the range since we need a binary choice (0 or 1)
    random_number: uint256 = rng_contract.unlock(2)

    # Determine heads or tails based on the random number
    if random_number == 0:
        log HeadsOrTails("Heads")
    else:
        log HeadsOrTails("Tails")
