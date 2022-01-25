_suites = ["clubs", "hearts", "diamonds", "spades"]

import random
from functools import reduce

class Card:
    def __init__(self, value, _suite_idx) -> None:
        self.value=value
        self.suite=_suites[_suite_idx]

    def __str__(self) -> str:
        return f"{self.value} of {self.suite}"
    

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

class Deck:
    def __init__(self) -> None:
        self.cards=[]
        self.new()
        

    def new(self):
        self.cards=[]

        tmp_deck = [[Card(value, suite_idx) for value in range(2, 15)] for suite_idx in range(len(_suites))]

        for x in tmp_deck:
            self.cards.extend(x)

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

    def newGame(self):
        self.reset()
        self.addPlayerLoop()
        self.dealInitialCards()

    def nextRound(self):
        pass

    def nextPlayer(self):

        i = self._current_player_index

        i+=1

        if i >= len(self.players):
            i = 0
        
        self._current_player_index = i 

        self._current_player=self.players[i]

    def addPlayerLoop(self):
        num = input("How many players?" )

        for x in range(int(num)):
            p = input("Player name: ")
            player = Player(p)
            self.addPlayer(player)


    def addPlayer(self, Player):
        self.players.append(Player)

    def updateActivePlayers(self):
        pass

    def dealInitialCards(self):

        for i in range(2):
            for x in range(len(self.players)):
                self.nextPlayer()
                self.hit()
                

    def checkForWinner(self):
        pass

    def blackjack(self)->bool:
        return self._current_player.total == 21 

    def hitLoop(self):
        #for every player give the chance to draw card
        #before drawing card player total must be less than 21

        for i in range(len(self.players)):
            p = self.player[i]

            if self.total > 21:
                continue

            print(f"Current Total is {p.total}")
            choice=input("Draw Card (y)? ")

            if choice.lower() != "y":
                continue

            card = self.hit(i)


    def hit(self)->bool:

        if (self.bust()): 
            return 

        card = self.deck.dealCard()

        self._current_player.addCard(card)


    def bust(self)->bool:
        return self._current_player.total > 21

    def maxPlayerScore(self)->int:
        return max([p.total for p in self.players])


if __name__=="__main__":
    game = Game()
    game.newGame()