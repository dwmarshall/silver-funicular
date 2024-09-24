from enum import auto, Enum


class Cards:
    class Suit(Enum):
        CLUBS = ("c", auto())
        DIAMONDS = ("d", auto())
        HEARTS = ("h", auto())
        SPADES = ("s", auto())

        def __init__(self, char: str, _):
            self.char = char

    class Rank(Enum):
        DEUCE = ("2", auto())
        TREY = ("3", auto())
        FOUR = ("4", auto())
        FIVE = ("5", auto())
        SIX = ("6", auto())
        SEVEN = ("7", auto())
        EIGHT = ("8", auto())
        NINE = ("9", auto())
        TEN = ("T", auto())
        JACK = ("J", auto())
        QUEEN = ("Q", auto())
        KING = ("K", auto())
        ACE = ("A", auto())

        def __init__(self, char: str, _):
            self.char = char

    class Card:

        def __init__(self, rank: "Cards.Rank", suit: "Cards.Suit"):
            self.rank = rank
            self.suit = suit

        def __repr__(self):
            return f"Card(rank=Cards.Rank.{self.rank.name}, suit=Cards.Suit.{self.suit.name})"

        def __str__(self):
            return f"{self.rank.char}{self.suit.char}"

    class Deck:
        def __init__(self):
            self.cards = []
            for suit in Cards.Suit:
                for rank in Cards.Rank:
                    self.cards.append(Cards.Card(rank, suit))
