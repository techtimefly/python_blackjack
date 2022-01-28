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

