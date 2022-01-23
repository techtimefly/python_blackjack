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
        assert(isinstance(deck.cards[0], Card))

    def test_shuffle_deck(self):

        deck = Deck()

        initial_cards = deck.cards.copy()
        deck.shuffle()
        shuffled_cards = deck.cards.copy()

        assert(initial_cards[0].value != shuffled_cards[0].value)

    def test_deal_card(self):
        deck = Deck()

        initial_length = len(deck.cards)

        card = deck.dealCard()

        new_length = len(deck.cards)

        assert(isinstance(card, Card))
        assert(initial_length != new_length)

    def test_player_total(self):
        player = Player("Tre")

        deck = Deck()
        deck.shuffle()

        cardA = deck.dealCard()
        cardB = deck.dealCard()

        player.addCard(cardA)
        player.addCard(cardB)

        assert(player.total() == (cardA.value + cardB.value))

