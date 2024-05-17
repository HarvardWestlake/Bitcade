# Blackjack-like game in Vyper

# Define a card as a struct
struct Card:
    suit: String[8]
    value: String[8]

# Define a deck of cards
deck: public(Card[52])

# Define a player's hand
player_hand: public(Card[11])
dealer_hand: public(Card[11])

# Index to keep track of the top of the deck
deck_index: public(int128)

# Initialize the contract with a deck of cards
@external
def __init__():
    suits: String[8][4] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values: String[8][13] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    deck_counter: int128 = 0
    for suit in suits:
        for value in values:
            self.deck[deck_counter] = Card({suit: suit, value: value})
            deck_counter += 1
    
    self.shuffle_deck()

# Shuffle the deck using Fisher-Yates algorithm
@internal
def shuffle_deck():
    for i in range(52, 1, -1):
        j: int128 = convert(floor(log(keccak256(concat([bytes32(self)], empty_bytes32)))), int128) % i
        temp: Card = self.deck[i-1]
        self.deck[i-1] = self.deck[j]
        self.deck[j] = temp
    
    self.deck_index = 0

# Deal a card from the deck
@internal
def deal_card() -> Card:
    assert self.deck_index < 52, "Deck is empty"
    card: Card = self.deck[self.deck_index]
    self.deck_index += 1
    return card

# Player's turn to hit
@external
def player_hit():
    new_card: Card = self.deal_card()
    for i in range(11):
        if self.player_hand[i].value == "":
            self.player_hand[i] = new_card
            break

# Dealer's turn to hit
@internal
def dealer_hit():
    new_card: Card = self.deal_card()
    for i in range(11):
        if self.dealer_hand[i].value == "":
            self.dealer_hand[i] = new_card
            break

# Function to start a new game
@external
def new_game():
    self.shuffle_deck()
    self.player_hand = empty(Card[11])
    self.dealer_hand = empty(Card[11])
    self.player_hand[0] = self.deal_card()
    self.player_hand[1] = self.deal_card()
    self.dealer_hand[0] = self.deal_card()
    self.dealer_hand[1] = self.deal_card()
