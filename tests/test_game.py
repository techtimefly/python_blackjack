from python_blackjack.game import Game
from python_blackjack.player import Player
from python_blackjack.token import Token
import pytest
import random

from python_blackjack.token import Token

class TestGame:
    def setup_class(cls):
        game=Game()
        players=[]
        tokens=[]

    def test_add_players_to_game_with_balance(self):
        #TODO: test adding players to the game
        players = self.newPlayers()

        assert(players != None and len(players) > 0)
        assert(players[0].balance() > 0)


    def test_deal_initial_two_cards(self):
        #TODO: test dealing the intial two cards to every players
        pass

    def test_cycle_through_players(self):
        #TODO: test cycling through the players
        pass

    def test_dealer_is_last_player(self):
        #TODO: test that the dealer is the last player
        pass

    def test_dealer_hide_one_card(self):
        #TODO: test hide one of the dealer's initial cards
        pass

    def test_move_to_first_player(self):
        #TODO: test moving to the first player
        pass

    def test_player_hit(self):
        #TODO test the player getting a new card, aka a "hit"
        pass

    def test_player_stay(self):
        #TODO test the player not getting a new card
        pass

    def test_player_has_natural(self):
        #TODO test that the player has blackjack with their first two cards
        pass

    def test_player_has_blackjack_after_3rd_card(self):
        #TODO test that the player has blackjack after pulling the third iteration or higher
        pass

    def test_player_bust(self):
        #TODO test that the player gone over the maximum score
        pass

    def test_place_bet(self):
        #TODO: test that the player can place a bet
        pass

    def test_place_bet_over_balance(self):
        #TODO: test that the player tries to place a bet over the balance
        pass

    def test_test_exchance_tokens(self):
        #TODO: test that the player can exchance tokens
        pass

    def newPlayers(self):
        players=["Steve", "Michael", "Carlos", "Will", "Beth"]

        
        tokens=[Token(i) for i in [25, 50, 100, 250, 500]*5]

        return [Player(p, tokens.copy()) for p in players]