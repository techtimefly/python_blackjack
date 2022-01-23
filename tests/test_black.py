import pytest
from python_blackjack.app import Card, Player, Deck

class TestBlackJack:

    def test_card(self):

        value  = 5

        card=Card(value, 0)

        assert(card.value == value)
        assert(str(card) == f"{card.value} of {card.suite}")

    def test_player(self):
        name = "Stephen"

        player=Player(name)

        assert(player.name == name)

    def test_new_deck(self):

        deck = Deck()

        assert(len(deck.cards) == 52)

    def test_shuffle_deck(self):

        deck = Deck()

        initial_cards = deck.cards.copy()
        deck.shuffle()
        shuffled_cards = deck.cards.copy()

        assert(initial_cards[0] != shuffled_cards[0])
