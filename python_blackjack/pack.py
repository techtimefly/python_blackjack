from python_blackjack.card import Card
from typing import Any, Iterable, final
import random

class Pack:
    
    """represents a deck of cards

    
    Attr:
        cards (Iterable(Card))  : an array of all the cards in the deck

    
    Methods
        __init__(self, ranks:Iterable, suits:Iterable):
            constructor
            builds the deck of cards

        addCard(card):
            add a new card to the deck

        clear():
            empty the deck of cards

        dealCard():Card
            returns the top card from the deck

        generate_cards(self, ranks:iter, suits:iter):
            builds the deck of cards

        shuffle():
            shuffle all the cards in place in random order

    """
    def __init__(self, ranks:Iterable=None, suits:Iterable=None):
        """Constructor that generates the cards

        Args:
            ranks (Iterable)    : for looping through the card ranks
            suits (Iterable)    : for looping through the suits
        """
        self._cards=[]

        if(ranks != None and suits != None):
            self.generate_cards(ranks, suits)

    @property
    def cards(self): return self._cards

    def addCard(self, card):
        """Adds a new card

        Args:
            card (Card) : a card object to add to the list or cards

        Raises:
            Exception   : raise an exception if trying to add an existing card back
        """
        if card in self._cards:
            raise Exception(f"the card already exists in the deck: {str(card)}")

        self._cards.append(card)

    def clear(self): 
        """Removes all cards
        """
        self._cards.clear

    def deal_card(self)->Card:
        """Takes a card top card

        Returns:
            Card: the top card in the list
        """
        card=None
        try:
            result=self._cards.pop()
        except IndexError:
            pass
        except Exception:
            pass
        finally:
            return card

    def generate_cards(self, ranks:Iterable, suits:Iterable):
        """Generates a new list of cards

        Args:
            ranks (Iterable)    : for looping through the card ranks
            suits (Iterable)    : for looping through the suits
        """
        self.clear()

        self._cards=[Card(r, s) for r in ranks for s in suits]


    def shuffle(self):
        """Shuffles the cards x number of times
        """
        for i in range(random.randint(1,50)):
            random.shuffle(self._cards)