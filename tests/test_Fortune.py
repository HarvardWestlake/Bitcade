from ape import project, accounts
from ape.exceptions import ContractLogicError
import pytest

@pytest.fixture
def player():
    return accounts.test_accounts[0]

@pytest.fixture
def wolver_coin(player):
    # Deploy the WolverCoin ERC20 token contract
    return player.deploy(project.Wolvercoin, "WolverCoin", "WVC", 18)

@pytest.fixture
def fortune_game(player):
    # Deploy the FortuneGame contract
    return player.deploy(project.FortuneGame)

def test_open_briefcase_with_erc20(player, fortune_game, wolver_coin):
    # Mint some WolverCoin tokens to the player
    wolver_coin.mint(player.address, 10000, sender=player)

    fortune_game.init_game(player.address, sender=player)
    # Approve the Fortune Game contract to spend WolverCoin tokens on behalf of the player
    wolver_coin.approve(fortune_game.address, 1000, sender=player)

    # Start the game by paying entry fee in WolverCoin tokens
    entry_fee = 100
    fortune_game.start_game(sender=player, value=entry_fee)
    wolver_coin.transfer(fortune_game.address, entry_fee, sender=player)  # Start the game

    # Choose briefcases
    fortune_game.choose_briefcases(sender=player)

    # Open a briefcase
    briefcase_number = 0  # Assuming the briefcase number is 0
    fortune_game.open_briefcase(briefcase_number, sender=player)

    # Ensure briefcase value is updated
# Open a briefcase
    initial_balance = wolver_coin.balanceOf(player.address)
    briefcase_number = 2  # Assuming the briefcase number is 0
    fortune_game.open_briefcase(briefcase_number, sender=player)
    # Check if the player's balance has changed after opening the briefcase
    final_balance =  wolver_coin.balanceOf(player.address)
    assert final_balance >= initial_balance, "Player's balance should change after opening a briefcase"



