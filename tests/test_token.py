from python_blackjack.token import Token, TokenMultiplier
import random

class TestToken:
    def setup_class(self):
        pass

    def test_create_token(self):
        token_values=[25, 50, 100, 200, 500]

        tokens=[Token(v) for v in token_values]

        for token in tokens:
            assert(token != None and token.value != 0)

    def test_create_bags_of_tokens(self):
        bag=[]
        bag.extend(TokenMultiplier(25, 10).tokens)
        bag.extend(TokenMultiplier(50, 10).tokens)
        bag.extend(TokenMultiplier(100, 3).tokens)
        bag.extend(TokenMultiplier(500, 2).tokens)


        assert(len(bag) > 0)

        tokens = [t for t in bag]

        assert(len(tokens) > 0)

        assert(tokens[0].value == 25)

