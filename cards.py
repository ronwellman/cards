#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from random import randint, shuffle, sample
from itertools import product

'''
    Ths generic cards module implements a class for building cards and decks of cards.

    Caveat: Not fully tested.  Built while learning to extend class functionality with
    methods such as __len__, __iter__, etc.


    Copyright 2017 Ron Wellman

    Permission is hereby granted, free of charge, to any person obtaining a copy of this
    software and associated documentation files (the "Software"), to deal in the Software
    without restriction, including without limitation the rights to use, copy, modify,
    merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be included in all copies
    or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
    INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
    PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

class Card(object):
    '''
        a class for building a card

        usage:

            >>> c = Card(('ace','spade'))
            >>> c.value
            'ace'
            >>> c.suit
            'spade'
            >>> c.color
            'black'
    '''
    def __init__(self, card):
        '''
            input -> tuple('value','suit')
        '''
        value = card[0].lower()
        suit = card[1].lower()

        if value in ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace') and \
            suit in ('heart','diamond','spade','club'):

            self.value = value
            self.suit = suit

            if self.suit in ('heart','diamond'):
                self.color = 'red'
            else:
                self.color = 'black'



class Deck(object):

    '''
        The Deck class utilizes the Card class to implement a deck of cards.  Typical methods:

            draw_cards()
            add_card()
            empty_deck()
            shuffle_deck()
    '''
    def __init__(self, cards=[]):
        self.cards  = cards

    def build_deck(self, num_decks=1):
        '''

            build_deck - builds a deck of cards given the total number of decks to build

            usage:

                >>> d1 = Deck()
                >>> d1.build_deck()
                >>> len(d1)
                52
                >>> d2 = Deck()
                >>> d2.build_deck(2)
                >>> len(d2)
                104
        '''
        value = ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace')
        suit = ('heart','diamond','spade','club')

        #computes every combination of card value and suit for a deck and creates multiples of that deck
        self.cards = [Card(x) for x in product(value, suit)] * num_decks

    def __iter__(self):

        for card in self.cards:
            yield card

    def __repr__(self):

        output = ''
        for i,card in enumerate(self.cards):
            output = ''.join((output,'%s\tof\t%s\n' % (card.value.title(), card.suit.title())))
            if i+1 == len(self.cards):
                output = output.strip()
        return output

    def __len__(self):

        return len(self.cards)

    def draw_cards(self, num_cards=1):
        '''

            removes a card from the deck and returns a Card object

            usage:
            >>> d3 = Deck()
            >>> d3.build_deck()
            >>> len(d3.draw_cards(5))
            5

        '''
        return_cards = []
        try:
            for x in xrange(num_cards):
                return_cards.append(self.cards.pop())
        except IndexError:
            pass
        return set(return_cards)

    def add_cards(self, cards):
        '''

            add a card to the deck using Card((value,suit))

            usage:
            >>> d4 = Deck()
            >>> d4.add_cards(( Card(('ace','spade')) , ))
            >>> len(d4)
            1
            >>> d5 = Deck()
            >>> d5.build_deck()
            >>> d4.add_cards(d5.draw_cards(5))
            >>> len(d4)
            6

        '''
        for card in cards:
            if isinstance(card, Card):
                self.cards.append(card)

    def shuffle(self):
        '''

            performs an in-place shuffle of the deck a random number of times

            usage:
            >>> d6 = Deck()
            >>> d6.build_deck()
            >>> d6.shuffle()

        '''

        for x in xrange(randint(1,100)):
            shuffle(self.cards)

if __name__ == '__main__':
	import doctest
	print doctest.testmod()
