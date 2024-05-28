
import ape 
import pytest

def test_distributor_deployed(distributor, wolvercoin):
    assert hasattr(distributor, "addToDistribution")
    assert hasattr(distributor, "removeFromDistribution")
    assert hasattr(distributor, "startDistribution")
    assert hasattr(distributor, "claimDistribution")
    assert distributor.token() == wolvercoin.address
    assert wolvercoin.balanceOf(distributor.address) == 1000 * 10**18
    

    print("Test passed, the Swapper contract has been deployed.")
    
def test_change_deployer(distributor, deployer, kian):
    # Change deployer
    with ape.reverts():
        distributor.setDeployer(kian, sender=kian)
            
    distributor.setDeployer(kian, sender=deployer)

    # Check balance
    assert distributor.deployer() == kian

    print("Test passed, the deployer has been changed.")
    
def test_change_initiator(wolvercoin, deployer, kian):
    # Change owner
    with ape.reverts():
        wolvercoin.setInitiator(kian, sender=kian)
            
    wolvercoin.setInitiator(kian, sender=deployer)

    # Check balance
    assert wolvercoin.initiator() == kian

    print("Test passed, the owner has been changed.")
    
def test_add_to_distribution(distributor, deployer, kian):
    # Add to distribution
    with ape.reverts():
        distributor.addToDistribution(kian, sender=kian)
            
    distributor.addToDistribution(kian, sender=deployer)

    # Check balance
    assert distributor.distributions(kian) == True

    print("Test passed, kian has been added to distribution.")
    
def test_remove_from_distribution(distributor, deployer, kian):
    # Add to distribution
    distributor.addToDistribution(kian, sender=deployer)

    # Remove from distribution
    with ape.reverts():
        distributor.removeFromDistribution(kian, sender=kian)
            
    distributor.removeFromDistribution(kian, sender=deployer)

    # Check balance
    assert distributor.distributions(kian) == False

    print("Test passed, kian has been removed from distribution.")
    
def test_start_distribution(distributor, deployer, kian):
    # Add to distribution
    distributor.addToDistribution(kian, sender=deployer)

    # Start distribution
    with ape.reverts():
        distributor.startDistribution(sender=kian)
            
    distributor.startDistribution(sender=deployer)
        
    # Check balance
    assert distributor.distributionStarted() == True

    print("Test passed, distribution has started.")
    
def test_claim_distribution(wolvercoin, distributor, deployer, kian):
    # Add to distribution
    distributor.addToDistribution(kian, sender=deployer)
    distributor.startDistribution(sender=deployer)

    # Claim distribution
    distributor.claimDistribution(sender=kian)

    # Check balance
    assert distributor.distributions(kian) == False
    assert wolvercoin.balanceOf(kian) == 1000 * 10**18
    
    # Claim distribution Revert
    
    with ape.reverts():
        distributor.claimDistribution(sender=kian)

    print("Test passed, kian has claimed their distribution.")