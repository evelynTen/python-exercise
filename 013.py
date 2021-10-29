# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:22:12 2020

@author: Iris
"""



names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']

scores = [[0] * len(courses) for _ in range(len(names))]

for i, name in enumerate(names):
    print(f'请输入{name}的成绩 ===>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}: '))
print()
print('-' * 5, '学生平均成绩', '-' * 5)

for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为：{avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)

for index, courses in enumerate(courses):
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')



#设计一个函数返回指定日期是这一年的第几天
    
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date
    
print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2016, 3, 1))
    
  


#实现双色球随机选号

from random import randint, sample

def random_select():
    red_balls = [x for x in range(1,34)]
    # 通过无放回随机抽样的方式选中6个红色球
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')
    print()          #数字补零
    
n = int(input('机选几注：'))
for _ in range(n):
    display(random_select())
    
  
    
    
#幸运的女人
    
persons = [True] * 30

counter, index, number = 0,0,0
while counter < 15:
    if persons[index]:
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    index %= 30  #到30回到0
for person in persons:
    print('女' if person else '男', end='')


















    
    
    
    
    
    
    