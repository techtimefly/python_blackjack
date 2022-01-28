
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
