struct Stats:
    nft_id: uint256
    racer_speed: uint256
    distance_traveled: uint256
    position: uint256
racers: public(HashMap[address, Stats])
nft_contract: address

# constructs the racing contract
@external
def __init__(_contract: address):
    self.nft_contract = _contract

@external
def calculateRacerSpeed(racer_address: address) -> uint256:
    # Retrieve racer's stats from the HashMap
    racer_stats: Stats = self.racers[racer_address]

    # Get a random number
    random_number: uint256 = 2

    # Calculate racer's speed based on random number, distance traveled, and position
    speed: uint256 = racer_stats.racer_speed
    speed *= random_number

    # Update racer's speed in the stats struct
    self.racers[racer_address].racer_speed = speed

    # Return the calculated racer's speed
    return self.racers[racer_address].racer_speed

@external
def createRacer(_id: uint256, _speed: uint256, distance: uint256, _position: uint256):
    exampleStruct: Stats = Stats({nft_id: _id, racer_speed: _speed, distance_traveled: distance, position: _position})
    self.racers[self.nft_contract] = exampleStruct