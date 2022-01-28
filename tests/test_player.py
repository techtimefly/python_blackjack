from python_blackjack.game import *
import pytest
import random

class TestPlayer:

    def setup_class(cls):
        cls.player = Player('JDoe')

    def test_new_player(self):
        p=self.player

        assert(p is not None)
        assert(p.name == "JDoe")
        assert(p.cards is None)
        assert(p.cardTotal() == 0)
        assert(p.balance() == 0)

    def test_add_chips_to_player(self):
        
        p=self.player
        total=0

        for i in range(random.randint(2,5)):
            value=random.randint(1,500)

            p.addToken(Token(value))

            total+=value

        assert(total > 0 and p.balance() == total)

    def test_add_cards_to_player(self):
        
        p=self.player

        cards=[Card(str(x), y) for x in range(2,10) for y in ["clubs", "hearts", "diamonds", "spades"]]

        total = 0
        for c in cards: 
            p.hit(c)
            total+=c.value

        card_total=p.cardTotal()

        assert(p.cards != None and len(p.cards) > 0)
        assert(card_total > 0 and card_total == total)

    def test_place_bet(self):
        p=Player("p1", [Token(100), Token(100)])
        bet1 = p.betTokens(200)

        p=Player("p1", [Token(50), Token(25)])
        bet2 = p.betTokens(75)

        p=Player("p1", [Token(25)])
        bet3 = p.betTokens(25)
        

        p._tokens=[]
        p.addToken(Token(10))
        p.addToken(Token(10))
        bet4 = p.betTokens(20)

        p._tokens=[]
        p.addToken(Token(100))
        p.addToken(Token(100))
        p.addToken(Token(100))
        p.addToken(Token(100))
        bet5 = p.betTokens(400)


        assert(bet1 is not None and len(bet1) == 2)
        assert(bet2 is not None and len(bet2) == 2)
        assert(bet3 is not None and len(bet3) == 1)
        assert(bet4 is not None and len(bet4) == 2)
        assert(bet5 is not None and len(bet5) == 4)