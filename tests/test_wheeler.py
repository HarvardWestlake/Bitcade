from ape import accounts, project

#def setup_environment(accounts):
    #test_account = accounts[0]
    # Deploy the Wolvercoin contract
#wolvercoin_contract = project.Wolvercoin.deploy("Wolvercoin", "WVC", 18, sender=test_account)

    # Mint tokens to the deployer's account
    #wolvercoin_contract.mint(test_account, 1000)

    # Assuming 'Wheeler' is another contract you need to deploy
#wheeler_contract = project.Wheeler.deploy(wolvercoin_contract.address, sender=test_account)

    #return test_account, wolvercoin_contract, wheeler_contract

#user, wolvercoin_contract, wheeler_contract = setup_environment(accounts)

# Define tests here
def test_wheel_initial_state(accounts):
    test_account = accounts[0]
    user = accounts[1]
    wolvercoin_contract = project.Wolvercoin.deploy("Wolvercoin", "WVC", 18, sender=test_account)
    wheeler_contract = project.Wheeler.deploy(wolvercoin_contract.address, sender=test_account)
    wolvercoin_contract.mint(wheeler_contract.address,10000, sender=test_account)
    wolvercoin_contract.approve(wheeler_contract.address, 1000, sender=user)
    assert wheeler_contract.wheel_speed() == 0, "Initial wheel speed should be 0"
    assert not wheeler_contract.wheel_is_spinning(), "Wheel should not be spinning initially"
    print("Test passed, wheel is initialized correctly.")

def test_spin_wheel(accounts):
    test_account = accounts[0]
    user = accounts[1]
    wolvercoin_contract = project.Wolvercoin.deploy("Wolvercoin", "WVC", 18, sender=test_account)
    wheeler_contract = project.Wheeler.deploy(wolvercoin_contract.address, sender=test_account)
    wolvercoin_contract.mint(wheeler_contract.address,10000, sender=test_account)
    wolvercoin_contract.approve(wheeler_contract.address, 1000, sender=test_account)
    wheeler_contract.spin_wheel(sender=user)
    assert wheeler_contract.wheel_speed() == 1000, "Wheel should have the set speed of 1000 after spinning"
    assert wheeler_contract.wheel_is_spinning(), "Wheel should be spinning after spin_wheel call"
    print("Test passed, wheel is spinning.")

def test_token_commit_and_win(accounts):
    test_account = accounts[0]
    user = accounts[1]
    wolvercoin_contract = project.Wolvercoin.deploy("Wolvercoin", "WVC", 18, sender=test_account)
    wheeler_contract = project.Wheeler.deploy(wolvercoin_contract.address, sender=test_account)
    wolvercoin_contract.mint(test_account,10000, sender=test_account)
    wolvercoin_contract.approve(wheeler_contract.address, 1000, sender=test_account)
    color = "green"
    bet_amount = 5
    wheeler_contract.token_commit(bet_amount, test_account, color, sender = test_account)
    assert wheeler_contract.token_amount() == bet_amount, "Bet amount should match committed amount"
    print("Test passed, token commit successful.")

    wheeler_contract.spin_wheel(sender=test_account)
    initial_balance = wolvercoin_contract.balanceOf(test_account)
    wheeler_contract.win_tokens(sender=test_account)
    expected_winning = bet_amount * 2  # Assuming win_multiplier is 2
    assert wolvercoin_contract.balanceOf(test_account) == initial_balance + expected_winning, "User balance should increase by the expected winning amount"
    print("Test passed, user won tokens after spinning the wheel.")