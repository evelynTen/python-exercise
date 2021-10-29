# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:13:38 2020

@author: Iris
"""


def fac(num):
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))





# 用星号表达式来表示args可以接收0个或任意多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))