class Card:
    """Represents and stores the information of a player card
    
    Attr:
        rank (str)   : the face value of the card
        suite (str)  : the suit the card belongs to
        value (int)  : the actual value of the card
    """
    
    def __init__(self, rank, suit:str):
        """Constructor that sets the details of the card

        Args:
            rank (str)  : usually the pip value of the card
            suit (str)  : the specific suit this card belongs to
        """
        self._rank=str(rank)
        self._suit=suit
        self._value=None

        if(self._rank.isdigit()):
            self._value = int(self._rank)

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
    def value(self)->int:
        return int(self._value)

    @value.setter
    def value(self, x:int):
        self._value = x

    def __str__(self):
        return f"{self._rank} of {self._suit}"