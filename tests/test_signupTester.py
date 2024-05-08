from ape import accounts, project

def test_add_ID(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    example_contract = project.Signup.deploy(sender=owner)

    example_contract.register_wallet_id(accounts[0], sender=owner)

    assert accounts[0] == example_contract.id(accounts[0], sender=owner)

    print("wallet id added")
