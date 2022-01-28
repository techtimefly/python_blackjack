from attrs import setters


class Card:
    """
    Represents and stores the information of a player card
    
    ...

    Attributes
    ----------
    rank: str
        the face value of the card
    suite: str
        the suit the card belongs to
    value: int
        the actual value of the card
    """

    def __init__(self, rank, suit):
        self._rank=rank
        self._suit=suit
        self._value=0

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, x:str):
        self._rank=x

    @property
    def suit(self)->str:
        return self._suit

    @suit.setter
    def suit(self, x:str):
        self._suit = x
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x:int):
        self._value = x

    def __str__(self):
        return f"{self._rank} of {self._suit}"

class Pack:
    """
    represents a deck of cards
    """
    pass

class Player:
    def __init__(self, name):
        self.name=name
    

class Dealer(Player):
    pass

class Game:
    pass
