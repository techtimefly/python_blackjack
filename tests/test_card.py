import pytest
from python_blackjack.app import Card

class TestBlackJack:

    def test_card(self):

        card=Card(2, "diamonds")

        assert(str(card) == "2 of diamonds")