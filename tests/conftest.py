#!/usr/bin/python3

import pytest
import boa

# . This runs before ALL tests


# Deployer

@pytest.fixture
def deployer():
    deployer = boa.env.generate_address()
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
        return boa.load("./contracts/Wolvercoin.vy", "Wolvercoin", "WCoin", 18)


# Swapper

@pytest.fixture
def swapper(wolvercoin, deployer):
    with boa.env.prank(deployer):
        swapper = boa.load("./contracts/Swapper.vy", wolvercoin)
        wolvercoin.setSwapper(swapper)
        return swapper