Variables
    Hashmap - Racers: Stores the user’s address and the structure containing their racer stats. 
    Structure - RacerStats: [address: NFT Address, address: Wallet Address, unit256: Racer Speed, bool: IsBoosted, uint256: Position, uint256 Distance]
    NFT Address = An NFT address refers to the unique identifier for a specific non-fungible token on the blockchain. (worm, car, etc)
    Wallet address = A wallet address, on the other hand, is like an account number; it’s where you receive, store, and send cryptocurrencies and NFTs
    Racer Speed = distance/second
void calculateMovement(Racers)
    Calculates how much distance the racers will move each block by multiplying  a random number by the speed.
    Speed multiplied by 1.1 if they are boosted
    Updates the position value in the stats array for each racer if they change
    Calls displayMovement()

# Struct for stats
struct Stats:
    nft_address: address
    wallet_address: address
    racer_speed: uint256
    distance_traveled: uint256
    position: uint256

# HashMap with address as key and Stats struct as value
racers: public(HashMap[address, Stats])

# Random number variable
random_number: public(uint256)

# Define the contract
contract calculateMovement:

    # Method to calculate racer's speed
    def calculateRacerSpeed(self, racer_address: address) -> uint256:
        # Retrieve racer's stats from the HashMap
        racer_stats: Stats = self.racers[racer_address]

        # Get a random number
        random_number = 2

        # Calculate racer's speed based on random number, distance traveled, and position
        racer_speed: uint256 = racer_stats.racer_speed * random_number

        # Update racer's speed in the stats struct
        self.racers[racer_address].racer_speed = racer_speed

        # Return the calculated racer's speed
        return racer_speed

