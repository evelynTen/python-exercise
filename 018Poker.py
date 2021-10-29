# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:10:35 2020

@author: Iris
"""



from enum import Enum

class Suite(Enum):
    #花色枚举
    SPADE, HEART, CLUB, DIAMOND = range(4)
    
class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
        
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
    #重写小于方法
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value
    
''' 
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)
'''

import random

class Poker:
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1,14)]
        self.current = 0
        
    def shuffle(self):
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)
        
    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card
    
    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)
'''    
poker = Poker()
poker.shuffle()
print(poker.cards)        
'''        
      
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def get_one(self, card):
        self.cards.append(card)
        
    def arrange(self):
        self.cards.sort()
        
poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)
        
        
        
        