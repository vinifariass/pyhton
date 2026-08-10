from random import shuffle

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "H D C S".split()

mycards = [(rank, suit) for rank in RANKS for suit in SUITS]


class Deck:
    "This is the Deck Class. This object will create a deck of cards to play a game. You can use then use this Deck list of cards to split in half and give one half to a player and the other half to another player. It will use SUITE and RANKS to create the deck. It should also have a method for splitting/cutting the deck in half and Shuffling the deck."

    def __init__(self):
        print("Creating a new Deck...")
        self.allcards = mycards

    def shuffle(self):
        print("Shuffling the Deck...")
        shuffle(self.allcards)

    def split_in_half(self):
        # Go to the beggining of the list and split it in half
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    "This is the Hand Class. This object will create a hand of cards to play a game. It will use the Deck class to create the hand."

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Hand of {len(self.cards)} cards"

    def __len__(self):
        return len(self.cards)


def add(self, card):
    self.cards.append(card)

    def remove_card(self):
        return self.cards.pop()


class Player:
    "This is the Player Class. This object will create a player of the game. It will use the Hand class to create the player."

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed: {drawn_card}")
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards
            
print("Welcome to War lets begin...")

##Use the 3 class along with some logic to play a game of War!
