import re


username = input('请输入用户名：')
qq = input('请输入qq号：')
# match函数的第一个参数是正则表达式字符串或正则表达式对象
# match函数的第二个参数是要跟正则表达式做匹配的字符串对象
m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
if not m1:
    print('请输入有效的用户名.')
# fullmatch函数要求字符串和正则表达式完全匹配
# 所以正则表达式没有写起始符和结束符
m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
if not m2:
    print('请输入有效的QQ号.')
if m1 and m2:
    print('你输入的信息是有效的!')



'''从一段文字中提取出国内手机号码。'''

pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''

# 方法一：查找所有匹配并保存到一个列表中
tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)
print('--------华丽的分隔线--------')

# 方法二：通过迭代器取出匹配对象并获得匹配的内容
for temp in pattern.finditer(sentence):
    print(temp.group())
print('--------华丽的分隔线--------')

# 方法三：通过search函数指定搜索位置找出所有匹配
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence, m.end())


'''替换字符串中的不良内容'''

sentence2 = '你丫是傻逼吗? 我操你大爷的. Fuck you.'
purified = re.sub('[操草艹]|fuck|shit|[傻煞沙][比屄逼叉缺吊屌碉雕]',
                  '*', sentence2, flags = re.IGNORECASE)
print(purified)


'''拆分长字符串'''

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentence_list = re.split(r'[，。,.]', poem)
sentence_list = [sentence3 for sentence3 in sentence_list if sentence3]
for sentence4 in sentence_list:
    print(sentence4)