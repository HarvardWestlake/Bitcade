from ape import accounts, project, chain
from array import array

def test_input_tokens(accounts):
    # Deploy the contract
    owner = accounts[0]  # Assuming the first account is the owner
    game_contract = project.CrashCade.deploy(sender=owner)

    # Start the game to allow token input
    game_contract.startGame(sender=owner)

    # # Assume each user will input 100 tokens
    # input_amount = 100
    input_amounts = array ('l',[3, 20 , 2, 10, 5, 40, 30, 1])

    # Input tokens from multiple users
    for i in range(0, 7):
        user = accounts[i]
        initial_balances = game_contract.getPlayerBalance(user, sender=user)
        game_contract.inputTokens(input_amounts[i], sender=user)

    # # Check balances and assert correct input amounts
    for i in range(0, 7):
        user = accounts[i]
        assert game_contract.getPlayerBalance(user) == initial_balances + input_amounts [i], f"Balance mismatch for user {i}"

    # # Ensure the game's total tokensInputted is correct
    # expected_total_input = input_amount * 7  # 7 users, each inputting 100 tokens
    # assert game_contract.tokensInputted() == expected_total_input, "Total inputted tokens mismatch"

    # # End the game to reset state
    # game_contract.crash(sender=owner)  # Assuming you have permissions setup to allow this

    print("Test passed, each of the users inputted their given number of tokens correctly.")