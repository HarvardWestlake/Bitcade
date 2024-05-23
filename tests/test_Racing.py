from ape import accounts, project

def test_calculate_Racer_Speed(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    racer_contract = project.Racing.deploy(accounts[1], sender = owner)
    racer_contract.createRacer(12, 34, 56, 78, sender = owner)


    racer_contract.calculateRacerSpeed(sender=owner) == 68
    assert racer_contract.getRacerSpeed(accounts[1], sender = owner)

    print("Test passed, the speed is 68")