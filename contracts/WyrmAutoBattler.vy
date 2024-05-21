from BattleWyrmToken import Token

token_contract : Token
id1 : uint256
id2 : uint256

@external
def battle(_player1 : address, _id1 : uint256, _player2 : address, _id2 : uint256) -> address:
    assert self.token_contract.ownerOf(_id1) == _player1
    assert self.token_contract.ownerOf(_id2) == _player2
    self.id1 = _id1
    self.id2 = _id2

    damage1 : uint256 = 0
    damage2 : uint256 = 0

    hp1 : uint256 = 0
    attack1 : uint256 = 0
    defense1 : uint256 = 0
    crit1 : uint256 = 0
    
    hp1, attack1, defense1, crit1 = self.getStats(_id1)

    hp2 : uint256 = 0
    attack2 : uint256 = 0
    defense2 : uint256 = 0
    crit2 : uint256 = 0
    
    hp2, attack2, defense2, crit2 = self.getStats(_id2)

    for i in range(1, 100):
        round_damage1 : uint256 = 0
        round_damage2 : uint256 = 0
        round_damage1, round_damage2 = self.playRound(hp1, attack1, defense1, crit1, hp2, attack2, defense2, crit2)
        damage1 += round_damage1
        damage2 += round_damage2

        if damage1 > hp1 and damage2 > hp2:
            if damage1 - hp1 < damage2 - hp2:
                return _player1
            else:
                return _player2
        if damage1 > hp1:
            return _player2
        if damage2 > hp2:
            return _player1

    return _player1

@internal
def playRound(hp1 : uint256, attack1 : uint256, defense1 : uint256, crit1 : uint256, hp2 : uint256, attack2 : uint256, defense2 : uint256, crit2 : uint256) -> (uint256, uint256):
    rand1: uint256 = self._rand()
    rand2: uint256 = convert(keccak256(uint2str(rand1)), uint256)
    rand3: uint256 = convert(keccak256(uint2str(rand2)), uint256)
    rand4: uint256 = convert(keccak256(uint2str(rand3)), uint256)


    damage1 : uint256 = 0
    damage2 : uint256 = 0

    if rand1 % 100 < crit1:
        damage2 = attack1 * 2
    
    if rand2 % 100 < crit2:
        damage1 = attack2 * 2
    
    if rand3 % 100 < defense1:
        damage1 = 0
    
    if rand4 % 100 < defense2:
        damage2 = 0

    return damage1, damage2

@external
def getStats(_id : uint256) -> (uint256, uint256, uint256, uint256):
    stats : uint64 = self.token_contract.tokenURI(_id)

    hp : uint256 = convert(stats/10000000, uint256)
    attack : uint256 = convert((stats % 10000000)/10000, uint256)
    defense : uint256 = convert((stats & 10000)/100, uint256)
    crit : uint256 = convert((stats & 100), uint256)

    return hp, attack, defense, crit

@internal
def _rand() -> uint256:
    return 42