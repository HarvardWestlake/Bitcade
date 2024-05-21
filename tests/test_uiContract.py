from ape import accounts, project, TestAccounts

def test_register_ui():
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    arcade_contract = project.Arcade.deploy(sender=owner)

    # Register the first 5 user accounts as UI distributors
    for i in range(1, 6):
        user = accounts[i]
        arcade_contract.register_ui(user, sender=owner)

        # Verify that each user is registered
        assert arcade_contract.ui_distributors(user) == True, f"User {i} should be registered."

    # Try to register a user that's already registered and catch the assertion error
    try:
        arcade_contract.register_ui(accounts[1], sender=owner)
        assert False, "Should have raised an exception for registering an already registered user."
    except AssertionError as e:
        assert str(e) == "This wallet is already registered as a UI distributor."

    print("Test passed, all users correctly registered, and duplicate registration was prevented.")

# Deploy and test the registration functionality
test_register_ui()
