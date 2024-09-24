from libraries.cards import Cards


def test_suit_enum():
    assert Cards.Suit.CLUBS.char == "c"
    assert Cards.Suit.DIAMONDS.char == "d"
    assert Cards.Suit.HEARTS.char == "h"
    assert Cards.Suit.SPADES.char == "s"


def test_rank_enum():
    assert Cards.Rank.DEUCE.char == "2"
    assert Cards.Rank.TREY.char == "3"
    assert Cards.Rank.FOUR.char == "4"
    assert Cards.Rank.FIVE.char == "5"
    assert Cards.Rank.SIX.char == "6"
    assert Cards.Rank.SEVEN.char == "7"
    assert Cards.Rank.EIGHT.char == "8"
    assert Cards.Rank.NINE.char == "9"
    assert Cards.Rank.TEN.char == "T"
    assert Cards.Rank.JACK.char == "J"
    assert Cards.Rank.QUEEN.char == "Q"
    assert Cards.Rank.KING.char == "K"
    assert Cards.Rank.ACE.char == "A"


def test_card_initialization():
    card = Cards.Card(Cards.Rank.ACE, Cards.Suit.SPADES)
    assert card.rank == Cards.Rank.ACE
    assert card.suit == Cards.Suit.SPADES


def test_card_repr():
    card = Cards.Card(Cards.Rank.ACE, Cards.Suit.SPADES)
    assert repr(card) == "Card(rank=Cards.Rank.ACE, suit=Cards.Suit.SPADES)"


def test_card_str():
    card = Cards.Card(Cards.Rank.ACE, Cards.Suit.SPADES)
    assert str(card) == "As"


def test_deck_initialization():
    deck = Cards.Deck()
    assert len(deck.cards) == 52


def test_deck_contains_correct_cards():
    deck = Cards.Deck()
    all_cards = {
        str(Cards.Card(rank, suit)) for suit in Cards.Suit for rank in Cards.Rank
    }
    deck_cards = {str(card) for card in deck.cards}
    assert all_cards == deck_cards
