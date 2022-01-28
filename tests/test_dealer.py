from python_blackjack.card import Card
from python_blackjack.dealer import Dealer
import pytest
import random

class TestDealer:
    def setup_class(cls):
        pass

    def test_should_dealer_hit(self):
        d = Dealer("Dealer", 17, 21)

        d.cards=[]
        d.hit(Card("21", "clubs"))
        assert(d.shouldHit())

        
        d.cards=[]
        d.hit(Card("22", "clubs"))
        assert(not d.shouldHit())