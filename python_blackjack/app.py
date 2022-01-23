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

    def addCard(self, card):
        self.cards.append(card)

    def total(self):
        def add(cardA, cardB):
            return cardA.value + cardB.value

        return reduce(add, self.cards)
        

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
        pass