import pytest
from python_blackjack.app import Card, Player, Deck

class TestGame:

    @classmethod
    def setup_class(cls):
        cls.deck = Deck()
        cls.player = []

    def test_deal_card(self):

        deck = self.deck
        
        initial_length = len(deck.cards)

        card = deck.dealCard()

        new_length = len(deck.cards)

        assert(isinstance(card, Card))
        assert(initial_length != new_length)

    


