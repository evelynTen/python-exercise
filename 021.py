import random
import time

from functools import wraps


# 定义装饰器函数，它的参数是被装饰的函数或类
def record_time(func):
    # 嵌套定义函数

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间：{end - start:.3f}秒')
        return result

    return wrapper


# 装饰器语法糖
@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器
download.__wrapped__('MySQL必知必会.pdf')
upload = upload.__wrapped__
upload('Python从新手到大师.pdf')


'''另一种方法'''


class RecordTime:

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'{func.__name__}执行时间: {end - start:.3f}秒')
            return result

        return wrapper


# 使用装饰器语法糖添加装饰器
@RecordTime()
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


# 直接创建对象并调用对象传入被装饰的函数
upload = RecordTime()(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')