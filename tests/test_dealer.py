from python_blackjack.game import *
import pytest
import random

class TestDealer:
    def setup_class(cls):
        pass

    def test_should_dealer_hit(self):
        d = Dealer("Dealer", 17, 21)

        assert(d.shouldHit(Card("21", "clubs")))
        assert(not d.shouldHit(Card("12", "clubs")))