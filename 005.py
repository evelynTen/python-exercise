# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:14:55 2020

@author: Iris
"""


username = input('请输入用户名：')
password = input('请输入口令：')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

    
    
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('y = %.1f' % y)
print(f'f({x}) = {y}')



x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f'f({x}) = {y}')
    

    