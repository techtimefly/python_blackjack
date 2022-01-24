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
        card_string=""

        for c in self.cards:
            card_string += str(c) + "\n"

        return f"{self.name}: {self.total}\n{card_string}"

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
                self.hit(x)

    def checkForWinner(self):
        pass

    def has21(self, player_idx)->bool:
        return self.players[player_idx].total == 21 

    def hit(self, player_idx)->bool:

        if (self.bust(player_idx)): 
            return 

        p = self.players[player_idx]

        card = self.deck.dealCard()

        p.addCard(card)

        self.players[player_idx] = p


    def bust(self, player_idx)->bool:
        return self.players[player_idx].total > 21

    def maxPlayerScore(self)->int:
        return max([p.total for p in self.players])


if __name__=="__main__":
    game = Game()
    game.newGame()