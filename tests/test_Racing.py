from ape import accounts, project

def test_calculate_Racer_Speed(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    racer_contract = project.Racing.deploy(1)
    racer_contract.createRacer(12, 34, 56, 78)


    assert calculateMovement.calculateRacerSpeed(sender=owner) == 68

    print("Test passed, the speed is 2")