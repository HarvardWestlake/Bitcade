from ape import accounts, project

#vyper ./contracts/AceArcade.vy
# pytest .tests/test_aceArcade/py

def test_start_game(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    player = accounts[1]  # Using the second account as the player
    game_contract = project.AceArcade.deploy(sender=owner)

    # Initialize variables for the test
    bet_amount = 1000  # This should be in the smallest unit of your chain's currency, e.g., wei

    # Start a game
    tx = game_contract.startGame(player.address, bet_amount, sender=player, value=bet_amount)

    # Use the returned transaction to access the game_id if it's emitted in an event or manage state
    game_id = game_contract.game_id()  # Accessing the latest game ID

    # Access player and computer hands using the new getter functions
    player_hand = game_contract.get_player_hand(game_id, player.address)
    computer_hand = game_contract.get_computer_hand(game_id)

    # Assertions
    assert len(player_hand) == 2, "Player hand does not have exactly two elements"
    assert len(computer_hand) == 2, "Computer hand does not have exactly two elements"
    
    print("Test passed, player and computer hands are of length 2")
