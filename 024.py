import json

my_dict = {
    'name': 'Evelyn',
    'age': 40,
    'friends': ['Ten', 'Lucas'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
print('字典已经保存到data.json文件中')

with open('data.json', 'r') as file:
    my_dict2 = json.load(file)
    print(type(my_dict2))
    print(my_dict2)

'''使用网络API获取数据'''
import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)
