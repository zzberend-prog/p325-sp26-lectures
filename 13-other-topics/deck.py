import numpy as np
import random

class Deck:
    '''Describes deck of cards'''

    deck = np.zeros(52)

    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = [r+s for r in ranks for s in suits]
        random.shuffle(self.deck)

    def hand(self, n=5):
        '''Deals n cards from the deck'''
        deal = self.deck[:n]
        del self.deck[:n]
        return deal

#way of testing module but wont print when imported into other programs
if __name__ == '__main__':
    deck = Deck()
    print(deck.deck)
    print(deck.hand())
    print(len(deck.deck))
