from ape import accounts, project

def test_calculate_Movement(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.Racing.deploy(sender=owner)

    token_contract.calculateMovement(sender=owner)

    # Check balances and assert correct token amounts
    for i in range(1, 8):
        assert token_contract.balanceOf(accounts[i]) == 1000

    print("Test passed, each of the first 10 users received 1000 tokens.")

# Test the method you wrote to play the game
# Commit after you get this test working!