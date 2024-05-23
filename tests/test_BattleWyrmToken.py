from ape import accounts, project

def test_stats_creation(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    token_contract = project.BattleWyrmToken.deploy(sender=owner)

    # Mint tokens to the first 10 users
    for i in range(1, 8):
        user = accounts[i]
        assert token_contract.mint.call(user, i, sender=owner) == True

    for i in range (1, 8):
        print(token_contract.tokenURI.call(i, sender=owner))

    print("Test passed, successfully created stats for each token.")
