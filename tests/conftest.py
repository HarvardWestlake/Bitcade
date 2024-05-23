#!/usr/bin/python3

import pytest
import boa

# . This runs before ALL tests


# Deployer

@pytest.fixture
def deployer():
    deployer = boa.env.generate_address()
    boa.env.set_balance(deployer, 1000*10**18)
    return deployer


@pytest.fixture
def kian():
    kian = boa.env.generate_address()
    boa.env.set_balance(kian, 1000*10**18)
    return kian


# Tokens

@pytest.fixture
def wolvercoin(deployer):
    with boa.env.prank(deployer):
        token = boa.load("./contracts/Wolvercoin.vy", "Wolvercoin", "WCoin", 18, 10**18 * 1000)
        return token
    
    
# Distributor

@pytest.fixture
def distributor(deployer, wolvercoin):
    with boa.env.prank(deployer):
        distributor = boa.load("./contracts/Distributor.vy", wolvercoin)
        wolvercoin.sendToDistributor(distributor)
        return distributor


# Swapper

@pytest.fixture
def swapper(wolvercoin, deployer):
    with boa.env.prank(deployer):
        swapper = boa.load("./contracts/Swapper.vy", wolvercoin)
        wolvercoin.setSwapper(swapper)
        return swapper