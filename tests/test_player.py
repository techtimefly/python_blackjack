import pytest
from python_blackjack.app import Card, Player, Deck

class TestPlayer:

    @classmethod
    def setup_class(cls):
        cls.player = Player("foo")

    def test_player(self):
        assert(self.player.name == "foo")

    def test_player_total(self):

        player = self.player

        deck = Deck()
        deck.shuffle()

        cardA = deck.dealCard()
        cardB = deck.dealCard()

        player.addCard(cardA)
        player.addCard(cardB)

        assert(player.total() == (cardA.value + cardB.value))

    def test_reset_player(self):
        player = self.player

        player.addCard(Card(2, 0))
        player.addCard(Card(5, 1))

        assert(len(player.cards) > 0)

        player.reset()

        assert(len(player.cards) == 0)