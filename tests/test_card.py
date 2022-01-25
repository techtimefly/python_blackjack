import pytest
from python_blackjack.app import Card

class TestBlackJack:

    def test_card(self):

        card=Card(2, "diamonds")

        assert(str(card) == f"{card.rank} of {card.suit}")