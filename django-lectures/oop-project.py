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
    
    def still_has_cards(self):
        """Return True if the player has cards left, otherwise return False"""
        return len(self.hand) != 0
            
print("Welcome to War lets begin...")

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

#create both players
comp = Player("Computer", Hand(half1))
name = input("Enter your name: ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings:")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(comp.name + " has the count: " + str(len(comp.hand.cards)))
    print("Play a card!")
    print("\n")
    table_cards = []
    user_card = user.play_card()
    comp_card = comp.play_card()

    table_cards.append(user_card)
    table_cards.append(comp_card)

    if comp_card[1] == user_card[1]:
        war_count += 1

        print("WAR!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(comp_card[0]) < RANKS.index(user_card[0]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print(f"Game over, number of rounds: {total_rounds}")
print("A war happened {war_count} times")
print("Does the computer still have cards? " + str(comp.still_has_cards()))
print(str(comp.still_has_cards()))
print("Does the human player still have cards? " + str(user.still_has_cards()))
print(str(user.still_has_cards()))
