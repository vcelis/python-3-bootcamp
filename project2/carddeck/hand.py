# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from card import Card


class Hand:
    """Class to represent a hand of playing cards
    """

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = list()
        self.value = 0
        self.soft_value = 0
        self.blackjack = False

    def __str__(self):
        result = ''
        for card in self.cards:
            result += f'{str(card)}\n'
        return result

    def __len__(self):
        return self.value

    def add_card(self, card):
        # Add card to self.cards
        self.cards.append(card)
        # Add value of card to self.value
        self.value += card.get_value()
        # Calculate soft_value if ace in hand
        if card.get_value() == 1:
            self.soft_value += 11
        else:
            self.soft_value += card.get_value()
        # Check for blackjack and toggle self.blackjack
        self.blackjack = self.value == 21 or self.soft_value == 21

    def clear(self):
        self.cards.clear()


if __name__ == '__main__':
    my_hand = Hand()
    print(my_hand)
    my_hand.add_card(Card(Card.rank_values[1], Card.suit_values[1]))
    my_hand.add_card(Card(Card.rank_values[5], Card.suit_values[3]))
    my_hand.add_card(Card(Card.rank_values[5], Card.suit_values[3]))
    print(my_hand)
    print(len(my_hand))
    print(my_hand.dealer)
    print(my_hand.value)
    print(my_hand.soft_value)
    print(my_hand.blackjack)

