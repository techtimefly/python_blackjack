
from python_blackjack.token import Token
from python_blackjack.card import Card
from python_blackjack.dealer import Dealer
from python_blackjack.pack import Pack

from logging import raiseExceptions
from typing import Any, Iterable, final
from attrs import setters
import random

class Game:

    _suits=['♣','♦','❤','♠']
    _ranks=['2','4','5','6','7','8','9','10','j','q','k','a']
    _num_of_packs=6
    _min_score=17
    _max_score=21

    # TODO: define the game
    """Will handle the logic of the game

    Methods
        addPlayers(Iterable[Player])    : adds players to the game
        nextPlayer()                    : make the next active player the current player
        playerTurn()                    : 
        reset()                         :
        distributeInitialChips()        :
        dealerTurn()
    """

    #TODO: refine how the tokens are distributed from the player when placing a bet
    # def placeBet(player:Player, amount:int)->list(Token):
    #     if amount > player.balance():
    #         raise Exception("player doesn't have enough tokens to place the bet")
    
    #     
    
    def __init__(self, tokens:Iterable[Token]) -> None:
        self._tokens = tokens
        self._pack = []
        self._players = []
        self.dealer=Dealer('Dealer', Game._min_score, Game._max_score)
        self.generateGameCards()
        

    def resetTokenPool(self, tokens:Iterable[Token]):
        self._tokens = tokens

    def generateGameCards(self):
        """Generates multiple packs of cards and stores in a single iterable
        """
        self._pack.clear()

        self._pack = Pack(Game._ranks*Game._num_of_packs, Game._suits)

        self._pack.shuffle()

        return self._pack