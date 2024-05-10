# Vyper code for a simple NFT race

# NFT contract representing a racer
struct Racer:
    max_speed: uint256 # Maximum speed of the racer
    acceleration: uint256 # Acceleration of the racer
    velocity: uint256 # Current velocity of the racer
    distance_remaining: uint256 # Remaining distance to the finish line

# Function to simulate a race between two NFTs
@public
def race(nft1_max_speed: uint256, nft1_acceleration: uint256,
         nft2_max_speed: uint256, nft2_acceleration: uint256) -> address:
    # Create NFTs
    nft1: Racer = Racer({
        max_speed: nft1_max_speed,
        acceleration: nft1_acceleration,
        velocity: 0,
        distance_remaining: 1000
    })
    nft2: Racer = Racer({
        max_speed: nft2_max_speed,
        acceleration: nft2_acceleration,
        velocity: 0,
        distance_remaining: 1000
    })

    # Race loop
    while nft1.distance_remaining > 0 and nft2.distance_remaining > 0:
        # Adjust velocity based on acceleration
        if nft1.velocity < nft1.max_speed:
            nft1.velocity += nft1.acceleration
        if nft2.velocity < nft2.max_speed:
            nft2.velocity += nft2.acceleration

        # Update distance remaining
        nft1.distance_remaining -= nft1.velocity
        nft2.distance_remaining -= nft2.velocity

    # Determine winner
    if nft1.distance_remaining <= 0:
        return msg.sender
    else:
        return self
