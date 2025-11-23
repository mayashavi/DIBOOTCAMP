#Quiz

#Class: blueprint of objects
#Instance: an example/one instance of the example, structured as a dictionary
#Encapsulation: hiding the internal details of an object and only exposing what is necessary.
#Abstraction: showing only the essential features of an object and hiding unnecessary details.
#Inheritance: passing attributes or behavior from a "family" member to another
#Multiple Inheritance: inherits from more than one parent class.
#Polymorphism: Many forms.
#MRO: determines the order in which Python searches for methods and attributes, especially in multiple inheritance

#Deck of cards:
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()   # Automatically create & shuffle deck

    def shuffle(self):
        """Create a full deck of 52 cards and shuffle them."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # Create 52 cards
        self.cards = [Card(suit, value) for suit in suits for value in values]

        random.shuffle(self.cards)

    def deal(self):
        """Deal a single card. Remove it from the deck."""
        if not self.cards:
            return "No cards left in the deck."
        return self.cards.pop()