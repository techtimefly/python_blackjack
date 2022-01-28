from logging import raiseExceptions
from typing import Any, Iterable, final
from attrs import setters
import random

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
        self._value=rank

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

class Pack:
    """represents a deck of cards

    
    Attr:
        cards (Iterable(Card))  : an array of all the cards in the deck

    
    Methods
        __init__(self, ranks:Iterable, suits:Iterable):
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
        """Constructor that generates the cards

        Args:
            ranks (Iterable)    : for looping through the card ranks
            suits (Iterable)    : for looping through the suits
        """
        self._cards=[]

        if(ranks != None and suits != None):
            self.generate_cards(ranks, suits)

    @property
    def cards(self): return self._cards

    def addCard(self, card):
        """Adds a new card

        Args:
            card (Card) : a card object to add to the list or cards

        Raises:
            Exception   : raise an exception if trying to add an existing card back
        """
        if card in self._cards:
            raise Exception(f"the card already exists in the deck: {str(card)}")

        self._cards.append(card)

    def clear(self): 
        """Removes all cards
        """
        self._cards.clear

    def deal_card(self)->Card:
        """Takes a card top card

        Returns:
            Card: the top card in the list
        """
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
        """Generates a new list of cards

        Args:
            ranks (Iterable)    : for looping through the card ranks
            suits (Iterable)    : for looping through the suits
        """
        self.clear()

        all_cards=[[Card(r, s) for r in ranks for s in suits]]

        for row in all_cards:
            self._cards.extend(row)

    def shuffle(self):
        """Shuffles the cards in random order
        """
        for i in range(random.randint(1,10)):
            random.shuffle(self._cards)
    

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
    
    def shouldHit(self, card:Card)->bool:
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

class Game:
    # TODO: define the game
    """Will handle the logic of the game

    Methods
        addPlayers(Iterable[Player])    : adds players to the game
        nextPlayer()                    : make the next active player the current player
        playerTurn()                    : 
        reset()                         :
        distributeInitialChips()        :
    """

    #TODO: refine how the tokens are distributed from the player when placing a bet
    # def placeBet(player:Player, amount:int)->list(Token):
    #     if amount > player.balance():
    #         raise Exception("player doesn't have enough tokens to place the bet")
    
    #     
    pass
