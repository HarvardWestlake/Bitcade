from ape import accounts, project, test
from pytest import raises

@test
def test_has_won(accounts):
    owner = accounts[0]  # Assuming the first account is the owner
    rng_contract = project.MockRNG.deploy(sender=owner)
    dice_game_contract = project.DiceGame.deploy(sender=owner)

    # Mock RNG response directly if possible, or adjust deployment to use mock RNG
    rng_contract.get_random_number.override(lambda seed: (seed % 100) + 1)  # Provides predictable "random" results

    # Test scenarios
    scenarios = [
        (1234, 50, True, 51, True),   # Win: random number is over the player choice
        (1234, 50, False, 49, True),  # Win: random number is under the player choice
        (1234, 50, True, 49, False),  # Lose: random number is not over the player choice
        (1234, 50, False, 51, False), # Lose: random number is not under the player choice
    ]

    for seed, choice, over, expected_random, expected_result in scenarios:
        rng_contract.get_random_number.override(lambda seed: expected_random)  # Setting expected random number
        result = dice_game_contract.hasWon(choice, over, seed)
        assert result == expected_result, f"Failed on seed {seed} with choice {choice} betting {'over' if over else 'under'}. Expected {expected_result} but got {result}"

    print("All test scenarios passed successfully.")
