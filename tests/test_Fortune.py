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
    # Initialize the game
    fortune_game.init_game(player.address, sender=player)

    # Mint some WolverCoin tokens to the player
    wolver_coin.mint(player.address, 10000, sender=player)

    # Approve the Fortune Game contract to spend WolverCoin tokens on behalf of the player
    wolver_coin.approve(fortune_game.address, 1000, sender=player)

    # Start the game by paying entry fee in WolverCoin tokens
    entry_fee = 100
    fortune_game.start_game(sender=player, value=entry_fee)  # Start the game

    # Choose briefcases
    fortune_game.choose_briefcases(sender=player)

    # Open a briefcase
    briefcase_number = 0  # Assuming the briefcase number is 0
    fortune_game.open_briefcase(briefcase_number, sender=player)

    # Ensure BriefCaseOpened event is emitted
    events_open_briefcase = fortune_game.get_logs(event_name="BriefCaseOpened")
    assert len(events_open_briefcase) == 1  # Ensure there's only one BriefCaseOpened event
