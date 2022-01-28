from python_blackjack.game import Card

class TestGame:

    def setup_class(cls):
        pass

    
    def test_create_card(self):
        rank="ace"
        suit="clubs"

        card = Card(rank, suit)

        assert(card is not None)
        assert(card.rank == rank)
        assert(card.suit==suit)
        assert(str(card) == f"{rank} of {suit}")

    def test_set_card_value(self):
        rank="5"
        suit="clubs"

        card = Card(rank, suit)

        assert(card.value == 0)

        card.value=5

        assert(card.value == 5)