from python_blackjack.card import Card
from python_blackjack.token import Token
from typing import Any, Iterable, final

class Player:
    """represents a player

    ...
    Attr::
        name: str
            the name of the player

        cards ([Card])  : the cards that the player current has

        chips ([Token]) : the chips the player has these can be used to place bets

    ...
    Methods:

        addChip(chip):
            give the player a chip

        balance(): int
            returns the total amount of money the player has

        betTokens(amount:int): Iterable[Token]
            returns the a list of tokens that represent how much the player wishes to bet

        cardTotal(): int
            returns the sum of all the cards

        hit(card):
            adds a new card to the players hand
    """
    def __init__(self, name:str, tokens=[]):
        """Constructor that creates a new player with optional tokens

        Args:
            name (str): the name of the player
            tokens (Iterable(Token), optional): an iterable of tokens so that the player may have a starting balance. Defaults to None.
        """
        self._name=name
        self._cards=[]
        self._tokens=tokens
    
    @property
    def name(self): return self._name

    @property
    def cards(self):
        if self._cards is None or len(self._cards) == 0:
            return None

        return self._cards

    @property
    def tokens(self): return self._tokens

    @name.setter
    def name(self, x): self._name = x


    @cards.setter
    def cards(self, x):  
        self._cards = x

    @tokens.setter
    def tokens(self, x):
        self._tokens = x

    def addToken(self, token:Token):
        """Add a token to the players tokens

        Args:
            token (Token): an ingame currency item that has a value
        """
        if self._tokens is None: 
            self._tokens = [token]
        else:
            if token not in self._tokens:
                self._tokens.append(token)
            else:
                raise Exception("Cannot give the player the same token")

    def balance(self)->int:
        """The sum of all the players tokens

        Returns:
            int: sum of all the players tokens
        """
        all_tokens = [token.value for token in self._tokens]

        return sum(all_tokens)

    def betTokens(self, amount:int)->Iterable[Token]:
        """Returns the tokens that make up the bet

        Args:
            amount (int): [description]

        Returns:
            Iterable[Token]: [description]
        """

        if self.balance() < amount: 
            raise Exception(f"Not enough to cover the bet! You have {self.balance()}")

        self._tokens.sort(key=lambda token: token.value, reverse=True)

        tokens_to_transfer = []

        amount_needed = amount

        mark_for_removal=[]
        
        iter_tokens=enumerate(self._tokens.copy())

        for (i,t) in iter_tokens:
            if t.value <= amount_needed:
                tokens_to_transfer.append(self._tokens.remove(t))
                amount_needed -= t.value

        return tokens_to_transfer


    def cardTotal(self)->int:
        """Gets the value of the cards that the player has

        Returns:
            int: sum of all the card values
        """
        all_values=[c.value for c in self._cards]

        return sum(all_values)

    def hit(self, card)->bool:
        """Adds a new card to the players cards

        Args:
            card (Card): an instance of a card

        Returns:
            bool: flag that determines if the card was added
        """
        if card in self._cards:
            #raise("The player already has this card")
            raise(Exception(f"the player already has this card: str(card)"))

        self._cards.append(card)
        
        return True
    