
from python_blackjack.player import Player
from python_blackjack.token import Token

from logging import raiseExceptions
from typing import Any, Iterable, final
from attrs import setters
import random

class Dealer(Player):
    """A subclass of Player.  Will handle the dealer logic

    Methods:
        shouldHit(Card):bool
         determine if the dealer should take a card
    """
    def __init__(self, name: str, min_score:int, max_score:int, tokens:Iterable[Token]=None):
        """Constructor that sets up the dealer

        Args:
            name (str): the dealer's name
            min_score (int): the minimum score threshold
            max_score (int): the maximum score threshold
            tokens (Iterable(Token), optional): tokens to start the dealer off with
        """
        super().__init__(name, tokens)
        
        self._min_score=min_score
        self._max_score=max_score
    
    def shouldHit(self)->bool:
        """Determine if the dealer should hit

        Args:
            card (Card): a Card object

        Returns:
            bool: should the Dealer get another card
        """

        return self.cardTotal() in range(self._min_score, self._max_score + 1)
