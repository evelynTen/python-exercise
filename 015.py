# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:55:24 2020

@author: Iris
"""



sentence = input('请输入一段话')
counter = {}
for ch in sentence:
    in 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
    



stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}  
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)