import random
from functools import reduce

class Card:
    def __init__(self, rank, suit) -> None:
        self.rank=str(rank)
        self.suit=suit
        self.updateValue()

    def updateValue(self, newValue=None):

        value=-1

        if newValue:
            value = newValue
            
        elif self.rank.isdigit():
            value = self.rank
        
        elif self.rank.lower() in ["jack", "queen", "king"]:
            value = 10
            
        elif self.rank == "ace":
            value = 11

        self.value = int(value)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.total = 0

    def addCard(self, card):
        self.cards.append(card)
        self.total += card.value

    # def total(self):
    #     def add(cardA, cardB):
    #         return cardA.value + cardB.value

    #     return reduce(add, self.cards)
        
    def __str__(self) -> str:
        card_str=[f"{str(c)}\n" for c in self.cards]

        return f"{self.name}: {self.total}\n{card_str}"

    def reset(self):
        self.cards = []
        self.total = 0

class Deck:
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _ranks=list(range(2,11))
    _ranks.extend(["jack", "queen", "king", "ace"])

    def __init__(self) -> None:
        self.cards=[]
        self.new()
        

    def new(self):
        self.cards=[]

        cards = [[Card(rank, suit) for rank in self._ranks for suit in self._suits]]

        for c in cards:
            self.cards.extend(c)

    def shuffle(self):
        self.tmp_cards = self.cards.copy()

        random.shuffle(self.tmp_cards)

        self.cards = self.tmp_cards

    def dealCard(self):
        return self.cards.pop()

class Game:
    def __init__(self) -> None:
        self.players=[]
        self._current_player=None
        self._current_player_index=-1

        self.deck=Deck()

    def reset(self):
        self.deck = Deck()
        self.deck.shuffle()

    def nextRound(self):
        self.reset()

        for p in self.players:
            p.reset()

    def nextPlayer(self):

        i = self._current_player_index

        i+=1

        if i >= len(self.players):
            i = 0
        
        self._current_player_index = i 

        self._current_player=self.players[i]

    def addPlayers(self, players):

        for p in players:
            self.players.append(p)


    def updateActivePlayers(self):
        pass

    def dealInitialCards(self):

        for i in range(2):
            for x in range(len(self.players)):
                self.nextPlayer()
                self.hit()
                

    def player_will_bust(self, card):

        if self._current_player.total + card.value > 21:
            return True

        return False

    def checkForWinner(self):
        pass

    def blackjack(self)->bool:
        return self._current_player.total == 21 


    def hit(self, specific_card=None)->bool:

        if (self.bust()): 
            return 

        card = None

        if(specific_card):
            card=specific_card

        else:
            card = self.deck.dealCard()

        if(card.rank == "ace" and self.player_will_bust(card)):
            card.value = 1

        self._current_player.addCard(card)


    def bust(self)->bool:
        return self._current_player.total > 21

    def maxPlayerScore(self)->int:
        return max([p.total for p in self.players])
