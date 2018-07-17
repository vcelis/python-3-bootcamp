# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""


class Hand:
    """Class to represent a hand of playing cards"""

    def __init__(self):
        self.cards = list()
        self.value = 0
        self.soft_value = 0
        self.blackjack = False
        self.bust = False

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
        # Check for bust and toggle self.bust
        self.bust = self.value > 21 and self.soft_value > 21

    def clear(self):
        self.cards.clear()
