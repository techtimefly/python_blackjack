import pytest
from python_blackjack.app import Card, Player, Deck, Game

class TestGame:

    @classmethod
    def setup_class(cls):
        cls.game = Game()
        cls.game.reset()

        p1 = Player("Steve")
        p2 = Player("Mike")
        p3 = Player("Kevin")

        cls.game.addPlayers([p1,p2,p3])

    def test_dealInitialCardsToPlayers(self):

        game = self.game

        game.dealInitialCards()


        assert(len(game.players[0].cards)==2)
    
    def test_show_players(self):

        game = self.game

        game.dealInitialCards()


        for p in self.game.players:
            card_str=[f"{str(c)}\n" for c in p.cards]

            player_str=f"{p.name}: {p.total}\n{card_str}"

            assert(str(p) == player_str)

        
            
    # def test_deal_card(self):

    #     deck = self.deck

    #     initial_length = len(deck.cards)

    #     card = deck.dealCard()

    #     new_length = len(deck.cards)

    #     assert(isinstance(card, Card))
    #     assert(initial_length != new_length)

    def test_downgrade_ace_card(self):
        g=self.game

        g.nextRound()

        p = g.players[0]

        g.nextPlayer()
        
        g.hit(Card("ace", "hearts"))
        g.hit(Card("ace", "clubs"))

        assert(g.players[0].total == 12)

    def test_get_max_player_score(self):
        pass
        
