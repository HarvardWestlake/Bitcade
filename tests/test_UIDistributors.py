from ape import accounts, project

def test_play_game(accounts):
    
    # Assign accounts for different roles
    owner = accounts[0]  # Account 0 is designated as the owner of the contract
    distributor = accounts[1]  # Account 1 is designated as the distributor
    player = accounts[2]  # Account 2 is designated as the player
    
    # Step 2: Deploy the contract
    game_contract = project.UIDistributors.deploy(owner, sender=owner)
    
    # Step 3: Register a game within the contract
    game_id = 1
    game_contract.register_game(game_id, owner, distributor, sender=owner)
    
    # Step 4: Simulate playing the game
    payment_amount = 1000  # The cost in wei for playing the game
    
    # Capture initial balances
    initial_distributor_balance = distributor.balance
    initial_owner_balance = owner.balance
    
    game_contract.play_game(game_id, sender=player, value=payment_amount)
    
    expected_distributor_payment = payment_amount * 60 // 100  # Distributor gets 60%
    expected_owner_payment = payment_amount - expected_distributor_payment  # Owner gets the rest 40%
    
    assert distributor.balance == initial_distributor_balance + expected_distributor_payment, "Distributor payment incorrect."
    assert owner.balance == initial_owner_balance + expected_owner_payment, "Owner payment incorrect."
