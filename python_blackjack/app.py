_suites = ["clubs", "hearts", "diamonds", "spades"]

import random

class Card:
    def __init__(self, value, _suite_idx) -> None:
        self.value=value
        self.suite=_suites[_suite_idx]

    def __str__(self) -> str:
        return f"{self.value} of {self.suite}"
    

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.deck = []

class Deck:
    def __init__(self) -> None:
        self.cards=[]
        self.new()

    def new(self):
        self.cards=[]

        tmp_deck = [[x for x in range(2, 15)] for y in range(len(_suites))]

        for x in tmp_deck:
            self.cards.extend(x)

    def shuffle(self):
        self.tmp_cards = self.cards.copy()

        random.shuffle(self.tmp_cards)

        self.cards = self.tmp_cards

    def addCard(self):
        pass

    def drawCard(self):
        pass

class Game:
    def __init__(self) -> None:
        pass