from ape import accounts, project

def test_start_game(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    player = accounts[1]  # Using the second account as the player
    game_contract = project.AceArcade.deploy(sender=owner)  

    # Initialize variables for the test
    bet_amount = 1000

    # Start a game
    tx = game_contract.startGame(player, bet_amount, sender=player)

    # Retrieve player and computer hands to verify their lengths
    player_hand = game_contract.player_hands(game_contract.game_id(), player)
    computer_hand = game_contract.computer_hands(game_contract.game_id())

    # Assertions
    assert len(player_hand) == 2, "Player hand does not have exactly two elements"
    assert len(computer_hand) == 2, "Computer hand does not have exactly two elements"
    
    print("Test passed, player and computer hands are of length 2")
