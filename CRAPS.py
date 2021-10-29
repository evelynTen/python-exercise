# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:56:01 2020

@author: Iris
"""



from random import randint

money = 1000
while money > 0:
    print(f'你的总资产为：{money}元')
    go_on = False
    
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break   # 下注金额必须大于0小于等于玩家总资产
    
    first = randint(1,6) + randint(1,6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        go_on = True
    
    while go_on:
        go_on = False
        current = randint(1,6) + randint(1,6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜!\n')
            money -= debt
        elif current == first:
            print('玩家胜!\n')
            money += debt
        else:
            go_on = True
print('你破产了, 游戏结束!')
        

#摇色子封装成函数
from random import randint

def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
        
# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))       
        
        
        
        
        
        
        
        
        