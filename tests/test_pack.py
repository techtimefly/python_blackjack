from python_blackjack.card import Card
from python_blackjack.game import Game
from python_blackjack.pack import Pack

import pytest
import random

class TestPack:

    def setup_class(cls):
        pass

    def test_generate_pack(self):
        pack = Pack(Game._ranks, Game._suits);

        assert(pack is not None and len(pack.cards) > 0)

        a=pack.cards.copy()
        pack.shuffle()
        b = pack.cards.copy()

        assert(str(a[0]) != str(b[0]))

    def test_shuffle_pack(self):
        pack = Pack(Game._ranks, Game._suits);

        a=pack.cards.copy()
        pack.shuffle()
        b = pack.cards.copy()

        assert(len(a) > 0 and len(b) > 0 and a != b)

    def test_add_card_to_pack(self):
        pack = Pack()
        pack.addCard(Card("2", "clubs"))

        assert(pack is not None and len(pack.cards) == 1)
