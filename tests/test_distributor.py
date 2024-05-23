
import boa

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
    with boa.env.prank(kian):
        with boa.reverts():
            distributor.setDeployer(kian)
            
    with boa.env.prank(deployer):
        distributor.setDeployer(kian)

    # Check balance
    assert distributor.deployer() == kian

    print("Test passed, the deployer has been changed.")
    
def test_change_initiator(wolvercoin, deployer, kian):
    # Change owner
    with boa.env.prank(kian):
        with boa.reverts():
            wolvercoin.setInitiator(kian)
            
    with boa.env.prank(deployer):
        wolvercoin.setInitiator(kian)

    # Check balance
    assert wolvercoin.initiator() == kian

    print("Test passed, the owner has been changed.")
    
def test_add_to_distribution(distributor, deployer, kian):
    # Add to distribution
    with boa.env.prank(kian):
        with boa.reverts():
            distributor.addToDistribution(kian)
            
    with boa.env.prank(deployer):
        distributor.addToDistribution(kian)

    # Check balance
    assert distributor.distributions(kian) == True

    print("Test passed, kian has been added to distribution.")
    
def test_remove_from_distribution(distributor, deployer, kian):
    # Add to distribution
    with boa.env.prank(deployer):
        distributor.addToDistribution(kian)

    # Remove from distribution
    with boa.env.prank(kian):
        with boa.reverts():
            distributor.removeFromDistribution(kian)
            
    with boa.env.prank(deployer):
        distributor.removeFromDistribution(kian)

    # Check balance
    assert distributor.distributions(kian) == False

    print("Test passed, kian has been removed from distribution.")
    
def test_start_distribution(distributor, deployer, kian):
    # Add to distribution
    with boa.env.prank(deployer):
        distributor.addToDistribution(kian)

    # Start distribution
    with boa.env.prank(kian):
        with boa.reverts():
            distributor.startDistribution()
            
    with boa.env.prank(deployer):
        distributor.startDistribution()
        
    # Check balance
    assert distributor.distributionStarted() == True

    print("Test passed, distribution has started.")
    
def test_claim_distribution(wolvercoin, distributor, deployer, kian):
    # Add to distribution
    with boa.env.prank(deployer):
        distributor.addToDistribution(kian)
        distributor.startDistribution()

    # Claim distribution
    with boa.env.prank(kian):
        distributor.claimDistribution()

    # Check balance
    assert distributor.distributions(kian) == False
    assert wolvercoin.balanceOf(kian) == 1000 * 10**18
    
    # Claim distribution Revert
    
    with boa.env.prank(kian):
        with boa.reverts():
            distributor.claimDistribution()

    print("Test passed, kian has claimed their distribution.")