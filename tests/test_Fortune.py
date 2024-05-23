import pytest
from ape import project, accounts

@pytest.fixture
def test_account(accounts):
    # Use a test account for deployment and funding
    return accounts[0]

@pytest.fixture
def fortune_game_contract(test_account):
    # Deploy the contract from the first available account
    contract_instance = project.FortuneGame.deploy({'from': test_account})
    yield contract_instance

@pytest.fixture
def player_account(accounts, test_account):
    # Use another predefined account as the player account
    player = accounts[1]
    # Fund the new account with some initial balance from the test account
    test_account.transfer(player, "10 ether")
    return player

def test_start_game(fortune_game_contract, player_account):
    # Retrieve the contract instance from the fixture
    fortune_game = fortune_game_contract

    # Get the player's balance before starting the game
    player_balance_before = fortune_game.token_balance(player_account)
    entry_fee = fortune_game.GAME_ENTRY_FEE()

    # Start the game
    fortune_game.start_game({'from': player_account, 'value': entry_fee})

    # Get the player's balance after starting the game
    player_balance_after = fortune_game.token_balance(player_account)

    # Ensure the entry fee has been deducted from the player's balance
    assert player_balance_after == player_balance_before - entry_fee

# Add more test functions to test other methods of the contract
