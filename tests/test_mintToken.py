from ape import accounts, project

def test_mint_tokens(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.Wolvercoin.deploy("Wolvercoin", "WVC", 18, sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 8):
        user = accounts[i]
        token_contract.mint(user, 1000, sender=owner)

    # Check balances and assert correct token amounts
    for i in range(1, 8):
        assert token_contract.balanceOf(accounts[i]) == 1000

    print("Test passed, each of the first 10 users received 1000 tokens.")

# Test the method you wrote to play the game
# Commit after you get this test working!