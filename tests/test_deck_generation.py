from ape import accounts, project


def test_card_gen():
    # Load the project's contracts
    contract_container = project.DeckOfCards

    # Get a test account for deploying the contract
    deployer_account = accounts.test_accounts[0]

    # Deploy the contract
    deck_of_cards = deployer_account.deploy(contract_container)

    # We know the deck should have 52 cards, thus we use 52 directly in the test
    expected_card_count = 52

    # Test for correct suits and values
    suits = {0, 1, 2, 3}  # Expected suits
    values = set(range(1, 14))  # Expected values (1-13)

    seen_cards = set()

    for i in range(expected_card_count):
        # Retrieve the card details using .call() correctly
        suit, value = deck_of_cards.get_card(i, sender=deployer_account)

        # Ensure all cards are unique
        card_tuple = (suit, value)
        if card_tuple in seen_cards:
            print(
                f"Duplicate card found: Suit {suit}, Value {value} at index {i}")
        else:
            seen_cards.add(card_tuple)

        # Assertions for suit and value range
        assert suit in suits, f"Unexpected suit {suit}"
        assert value in values, f"Unexpected value {value}"

    # Check completeness of the deck
    assert len(
        seen_cards) == expected_card_count, "There should be 52 unique cards"

    # Additional debug to ensure all cards are checked if assertion fails
    if len(seen_cards) != expected_card_count:
        print("Cards checked: ", seen_cards)
        print("Number of unique cards: ", len(seen_cards))
