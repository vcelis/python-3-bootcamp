# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from player.dealer import Dealer
from player.player import Player
from carddeck.deck import Deck


class Game():
    """Class to represent the blackjack Game"""

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()

    def __str__(self):
        result = ''
        result += f'Dealer:\n{str(self.dealer)}\n\n'
        result += f'Player:\n{str(self.player)}\n\n'
        result += f'Deck:\n{str(self.deck)}'
        return result

    def deal(self):
        # clear both dealer and player`s hand
        self.dealer.hand.clear()
        self.player.hand.clear()
        # Populate and shuffle deck
        self.deck.populate()
        # Deal 2 cards to the dealer. Show 1
        self.dealer.hand.add_card(self.deck.deal_card().flip())
        self.dealer.hand.add_card(self.deck.deal_card())
        # Deal 2 cards to the player. Show both
        self.player.hand.add_card(self.deck.deal_card().flip())
        self.player.hand.add_card(self.deck.deal_card().flip())

    def hit(self):
        self.player.hand.add_card(self.deck.deal_card().flip())

    def stand(self):
        # Return value if <= 21 else return False
        return self.player.value if self.player.value <= 21 else False

    def play(self):
        # Check player bet isn`t greater than players balance
        if self.player.bet <= self.player.balance:
            # Deduct players bet from balance
            self.player.balance -= self.player.bet
            # Populate the deck
            # Deal two cards to dealer (1 hidden) and two cards to Player
            self.deal()
            # # Ask player if he wants to HIT
            # If player hand doesnt go over 21, ask to hit again or stand
            # If player stands, play dealers hand.
            # Determine the winner and if player wins, payout bet*2 to player
            # Ask if he wants to play again

    def play_dealer(self):
        # Flip dealers cards over
        self.dealer.hand.cards[1].flip()
        # Dealer will always hit untill value meets or exceeds 17
        while self.dealer.value < 17:
            self.dealer.hand.add_card(self.deck.deal_card().flip())

    def end_round(self):
        # Determine the winner and if the player wins, payout bet*2 to player
        if not self.player.bust and self.player.value >= self.dealer.value:
            if self.player.value == self.dealer.value:
                # Tie and player gets bet back
                self.player.balance += self.player.bet
            else:
                # Player wins
                self.player.balance += self.player.bet * 2
