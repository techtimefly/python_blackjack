from python_blackjack.game import *
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


class TestDealer:
    def setup_class(cls):
        pass

    def test_should_dealer_hit(self):
        d = Dealer("Dealer", 17, 21)

        assert(d.shouldHit(Card("21", "clubs")))
        assert(not d.shouldHit(Card("12", "clubs")))

class TestPack:

    def setup_class(cls):
        pass

    def test_generate_pack(self):
        pack = Pack(list(range(2,15)), ["clubs", "hearts", "diamonds", "spades"])

        assert(pack is not None and len(pack.cards) > 0)

        a=pack.cards.copy()
        pack.shuffle()
        b = pack.cards.copy()

        assert(str(a[0]) != str(b[0]))

    def test_shuffle_pack(self):
        pack = Pack(list(range(2,15)), ["clubs", "hearts", "diamonds", "spades"])

        a=pack.cards.copy()
        pack.shuffle()
        b = pack.cards.copy()

        assert(len(a) > 0 and len(b) > 0 and a != b)

    def test_add_card_to_pack(self):
        pack = Pack()
        pack.addCard(Card("2", "clubs"))

        assert(pack is not None and len(pack.cards) == 1)
