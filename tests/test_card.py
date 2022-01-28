from python_blackjack.card import Card
import pytest
import random

class TestCard:

    def setup_class(cls):
        pass

    def test_create_card(self):
        rank="queen"
        suit="clubs"

        card = Card(rank, suit)

        assert(card is not None)
        assert(card.rank == rank)
        assert(card.suit==suit)
        assert(str(card) == f"{rank} of {suit}")

    def test_set_card_value(self):
        rank="5"
        suit="clubs"

        card = Card(rank, suit)

        assert(card.value == 5)