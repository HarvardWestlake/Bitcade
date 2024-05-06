import pytest
from brownie import Wolvercoin, accounts

def test_mint():
    # Deploy the contract
    my_token = MyToken.deploy("Wolvercoin", "MTK", 18, {'from': accounts[0]})
    
    # Perform tests
    initial_supply = my_token.totalSupply()
    my_token.mint(accounts[1], 100)
    assert my_token.totalSupply() == initial_supply + 100
    assert my_token.balanceOf(accounts[1]) == 100
