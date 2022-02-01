from python_blackjack.token import Token
from logging import raiseExceptions
from typing import Any, Iterable, final
from attrs import setters
import random

class Game:

    _suits=['♣','♦','❤','♠']
    _ranks=['2','4','5','6','7','8','9','10','j','q','k','a']
    
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

    def resetTokenPool(self, tokens:Iterable[Token]):
        self._tokens = tokens

    def shouldHit(self, card)->bool:
        """Determine if the dealer should hit

        Args:
            card (Card): a Card object

        Returns:
            bool: should the Dealer get another card
        """
        current_total = self.cardTotal()
        card_total=card.value
        future_total=current_total + card_total

        return future_total in list(range(self._min_score, self._max_score + 1))
    pass
