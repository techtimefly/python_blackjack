
from typing import Sequence


class Token:

    """Represents game currency

    Attr:
        value (any)  : a value defined by the game, usually an int
    """

    def __init__(self, value) -> None:
        """Constructor

        Args:
            value (any) : sets the value of the token
        """
        self._value=value

    @property

    def value(self): return self._value

    @value.setter
    def value(self, x): self._value = x

class TokenMultiplier:
    """Used to create several tokens of the same value
    """
    
    def __init__(self, value:int, multiplier:int):
        """[summary]

        Args:
            value (int): The value that should be assigned to every token in the bag
            multiplier (int): how many tokens to generate
        """
        self._multiplier=multiplier
        self._tokens=[Token(value)] * self.multiplier

    @property
    def tokens(self): return self._tokens

    @property
    def multiplier(self): return self._multiplier