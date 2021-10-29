# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:26:47 2020

@author: Iris
"""


num = int(input('请输入一个正整数：'))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

    

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x  # Python中可以用这样的方式来交换两个变量的值
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')  #// 除法，向下取整
        break