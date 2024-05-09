from ape import accounts, project

def test_calculate_Movement(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    race_contract = project.Racing.deploy(sender=owner)

    race_contract.calculateMovement(sender=owner)

    # Check stats and assert speed changed
    for i in range(1, 8):
        Speed: speed = racers[accounts[i]].racer_speed

        assert race_contract.racers[accounts[i]].racer_speed == racer_speed * 2

    print("Test passed, racer speed changed.")

# Test the method you wrote to play the game
# Commit after you get this test working!