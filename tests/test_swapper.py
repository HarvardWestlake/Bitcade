import pytest 
import ape 

def test_swapper_deployed(swapper): 
    assert hasattr(swapper, "buy") 
    assert hasattr(swapper, "withdraw") 
    print("Test passed, the Swapper contract has been deployed.") 
    
def test_buy_tokens(wolvercoin, swapper, kian): 
    # Buy tokens 
    bad_amount = 0 
    with ape.reverts(): 
        swapper.buy(value=bad_amount, sender=kian) 
        
    amount = 1000 
    swapper.buy(value=amount, sender=kian) 
        
    # Check balance 
    assert wolvercoin.balanceOf(kian) == amount 
    print("Test passed, the deployer has bought tokens.") 
    
def test_withdraw_eth(deployer, swapper, kian): 
    # Buy tokens 
    amount = 1000 * 10**18 
    swapper.buy(value=amount, sender=kian) 
    with ape.reverts(): 
        swapper.withdraw(sender=kian) 
        
    # Withdraw tokens 
    swapper.withdraw(sender=deployer) 
    
    # Check balance 
    assert swapper.balance == 0
    print("Test passed, the deployer has withdrawn tokens.") 
        
def test_wolvercoin_swapper(wolvercoin, swapper, kian, deployer): 
    assert wolvercoin.swapper() == swapper.address 
    with ape.reverts(): 
        wolvercoin.setSwapper(kian, sender=kian)
        
    print("Test passed, the Swapper contract has been set.") 
        
def test_wolvercoin_swapperMint(wolvercoin, swapper, kian): 
    # Buy tokens 
    amount = 1000 
    with ape.reverts(): 
        wolvercoin.swapperMint(kian, amount, sender=kian) 
        wolvercoin.swapperMint(kian, amount, sender=swapper.address) 
        
    assert wolvercoin.balanceOf(kian) == 0
    print("Test passed, the deployer has minted tokens.") 
    
def test_setOwner(swapper, kian): 
    # Change owner 
    with ape.reverts(): 
        swapper.setOwner(kian, sender=kian)
        swapper.setOwner(kian, sender=swapper.owner()) 
        assert swapper.owner() == kian 
        print("Test passed, the owner has been changed.")