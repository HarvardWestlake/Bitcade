#!/usr/bin/python3
import pytest
from ape import accounts, project

#. This runs before ALL tests
# Deployer

@pytest.fixture 
def deployer(accounts): 
    deployer = accounts[0] 
    return deployer 

@pytest.fixture 
def kian(accounts): 
    kian = accounts[1] 
    return kian 


# Tokens 
@pytest.fixture 
def wolvercoin(deployer): 
    token = project.Wolvercoin.deploy("Wolvercoin", "WCoin", 18, 10**18 * 1000, sender=deployer) 
    return token


# Distributor 
@pytest.fixture 
def distributor(deployer, wolvercoin): 
    distributor = project.Distributor.deploy(wolvercoin, sender=deployer) 
    wolvercoin.sendToDistributor(distributor, sender=deployer) 
    return distributor 

# Swapper 
@pytest.fixture 
def swapper(wolvercoin, deployer): 
    swapper = project.Swapper.deploy(wolvercoin, sender=deployer) 
    wolvercoin.setSwapper(swapper, sender=deployer) 
    return swapper