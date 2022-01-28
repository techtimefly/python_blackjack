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
        self.rank=rank
        self.suit=suit
        self.value=0

    @property
    def rank(self)->str:
        return self.rank

    rank.setter
    def rank(self, x:str):
        self.rank=x

    @property
    def suit(self)->str:
        return self.suit

    suit.setter
    def suit(self, x:str):
        self.suit = x
    
    @property
    def value(self):
        return self.value

    value.setter
    def value(self, x:int):
        self.value = x

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Pack:
    """
    represents a deck of cards
    """
    pass

class Player:
    pass

class Dealer(Player):
    pass

class Game:
    pass
