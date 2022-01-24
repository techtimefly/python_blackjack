import pytest
from python_blackjack.app import Deck, Card

class TestDeck:

    @classmethod
    def setup_class(cls):
        cls.deck = Deck()

    def test_new_deck(self):

        deck = self.deck

        assert(len(deck.cards) == 52)
        assert(isinstance(deck.cards[0], Card))

    def test_shuffle_deck(self):

        deck = self.deck

        initial_cards = deck.cards.copy()
        deck.shuffle()
        shuffled_cards = deck.cards.copy()

        assert(initial_cards[0].value != shuffled_cards[0].value)