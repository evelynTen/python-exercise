# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:01:36 2020

@author: Iris
"""


'''
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)


a = 1
b = 2
c = 3
d = 4
d,c,b,a = a,b,c,d
print(a,b,c,d)
'''

def find_max_and_min(items):
    """找出列表中最大和最小的元素
    :param items: 列表
    :return: 最大和最小元素构成的二元组
    """
    max_one, min_one = items[0], items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one, min_one
print(find_max_and_min([1,2,3,4,5,6,7]))