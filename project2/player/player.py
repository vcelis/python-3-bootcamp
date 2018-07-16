# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from playerbase import PlayerBase


class Player(PlayerBase):
    """Class to represent a base for player objects
    """
    def __init__(self, balance=1000, bet=10):
        super().__init__()
        self.balance = balance
        self.bet = bet

    def __str__(self):
        result = f'Balance: ${self.balance}'
        result += f'\nBet: ${self.bet}'
        for card in self.hand:
            result += f'\n{str(card)}'
        return result


if __name__ == '__main__':
    my_player = Player()
    print(my_player)
