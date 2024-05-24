# Card struct
struct Card:
    suit: uint256
    value: uint256

# Array of cards
deck: public(Card[52])

@external
def __init__():
    suits: uint256[4] = [0, 1, 2, 3]  # 0: Hearts, 1: Diamonds, 2: Clubs, 3: Spades
    values: uint256[13] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # 1: Ace, 2-10: Number cards, 11: Jack, 12: Queen, 13: King

    card_index: uint256 = 0
    for suit in suits:
        for value in values:
            self.deck[card_index] = Card({suit: suit, value: value})
            card_index += 1

@external
@view
def get_card(index: uint256) -> (uint256, uint256):
    """
    Returns the suit and value of the card at the specified index.
    """
    return (self.deck[index].suit, self.deck[index].value)

@external
@view
def get_suit(index: uint256) -> uint256:
    """
    Returns the suit of the card at the specified index.
    """
    return self.deck[index].suit
    
@external
@view
def get_value(index: uint256) -> uint256:
    """
    Returns the value of the card at the specified index.
    """
    return self.deck[index].value

@internal
@view
def get_random_number(upper_limit: uint256) -> uint256:
    """
    Returns a pseudo-random number between 0 and upper_limit-1.
    """
    return block.timestamp % upper_limit

@external
def shuffle_deck():
    """
    Shuffles the deck using the Fisher-Yates shuffle algorithm.
    """
    for i in range(52):
        j: uint256 = self.get_random_number(52 - i) + i
        temp: Card = self.deck[i]
        self.deck[i] = self.deck[j]
        self.deck[j] = temp
        // Code Written by Ahren Bhatia
