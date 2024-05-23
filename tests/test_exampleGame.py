from ape import accounts, project

def test_get_account_balance(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    example_contract = project.ExampleGame.deploy(sender=owner)

    assert example_contract.getAccountBalance(sender=owner) == 1000

    print("Test passed, the balance is 1000")


def test_rand(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    example_contract = project.ExampleGame.deploy(sender=owner)

    assert example_contract.rand(sender=owner) == 42

    print("Test passed, the balance is 1000")


def test_play(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    example_contract = project.ExampleGame.deploy(sender=owner)

    txn = example_contract.play(sender=owner)
    assert txn.status == 1

def test_get_description(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    example_contract = project.ExampleGame.deploy(sender=owner)

    # Fetch the description
    description = example_contract.getDescription(sender=owner)

    # Expected description string
    expected_description = "This is a simple game where you can play and get a random result. The result can be either 'Win' or 'Lose'. Try your luck!"

    assert description == expected_description

    print("Test passed, the description matches the expected value")