import pytest
from python_blackjack.app import Card

class TestBlackJack:

    def test_card(self):

        value  = 5

        card=Card(value, 0)

        assert(card.value == value)
        assert(str(card) == f"{card.value} of {card.suite}")