# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:54:57 2020

@author: Iris
"""


#生成指定长度验证码的函数--方法一

import random

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_code(code_len = 4):
    code = ''
    for _ in range(code_len):
        index = random.randrange(0, len(ALL_CHARS))
        #在指定范围内产生一个随机整数
        code += ALL_CHARS[index]
    return code

for _ in range(10):
    print(generate_code()) 
    
    
#生成指定长度验证码的函数--方法2


import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(code_len = 4):
    return ''.join(random.choices(ALL_CHARS, k = code_len))
#random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样；choices实现有放回抽样。
#这两个函数的第一个参数代表抽样的总体，而参数k代表抽样的数量。



#滚动文字

import os
import time

content = '北 京 欢 迎 你 为 你 开 天 辟 地           '
while True:
    os.system('cls')
    print(content)
    time.sleep(0.2)
    content = content[1:] + content[0]














