from typing import Iterable, final
from attrs import setters
import random

class Token:
    def __init__(self, value) -> None:
        self._value=value

    @property
    def value(self): return self._value

    @value.setter
    def value(self, x): self._value = x


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

    def __init__(self, rank:str, suit:str):
        self._rank=rank
        self._suit=suit
        self._value=rank

        # if(rank.isdigit):
        #     self.value = int(rank)

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

class Pack:
    """
    represents a deck of cards

    ...
    Attributes:
        cards: [Card]
            an array of all the cards in the deck

    ...
    Methods
        __init__(self, ranks:iter, suits:iter):
            constructor
            builds the deck of cards

        addCard(card):
            add a new card to the deck

        clear():
            empty the deck of cards

        dealCard():Card
            returns the top card from the deck

        generate_cards(self, ranks:iter, suits:iter):
            builds the deck of cards

        shuffle():
            shuffle all the cards in place in random order

    """
    def __init__(self, ranks:Iterable=None, suits:Iterable=None):
        self._cards=[]

        if(ranks != None and suits != None):
            self.generate_cards(ranks, suits)

    @property
    def cards(self): return self._cards

    def addCard(self, card):
        if card in self._cards:
            raise ValueError(f"the card already exists in the deck: {str(card)}")

        self._cards.append(card)

    def clear(self): 
        self._cards.clear

    def deal_card(self):
        card=None
        try:
            result=self._cards.pop()
        except IndexError:
            pass
        except Exception:
            pass
        finally:
            return card

    def generate_cards(self, ranks:Iterable, suits:Iterable):
        self.clear()

        all_cards=[[Card(r, s) for r in ranks for s in suits]]

        for row in all_cards:
            self._cards.extend(row)

    def shuffle(self):
        random.shuffle(self._cards)
    

class Player:
    """
    represents a player

    ...
    Attributes:
        name: str
            the name of the player

        cards: [Card]
            the cards that the player current has

        chips: [Chip]
            the chips the player has
            these can be used to place bets

    ...
    Methods:

        addChip(chip):
            give the player a chip

        balance(): int
            returns the total amount of money the player has

        cardTotal(): int
            returns the sum of all the cards

        hit(card):
            adds a new card to the players hand
    """
    def __init__(self, name):
        self._name=name
        self._cards=[]
        self._tokens=[]
    
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
        if self._tokens is None: 
            self._tokens = [token]
        else:
            self._tokens.append(token)

    def balance(self):
        all_tokens = [token.value for token in self._tokens]

        return sum(all_tokens)

    def cardTotal(self):
        all_values=[c.value for c in self._cards]

        return sum(all_values)

    def hit(self, card)->bool:

        if card in self._cards:
            #raise("The player already has this card")
            raise(ValueError(f"the player already has this card: str(card)"))

        self._cards.append(card)
    

class Dealer(Player):
    # TODO: define the dealer
    pass

class Game:
    # TODO: define the game

    #TODO: refine how the tokens are distributed from the player when placing a bet
    # def placeBet(player:Player, amount:int)->list(Token):
    #     if amount > player.balance():
    #         raise Exception("player doesn't have enough tokens to place the bet")
    
    #     
    pass
