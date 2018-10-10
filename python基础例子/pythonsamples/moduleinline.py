#coding=utf-8
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# namedtuple('名称', [属性list]):

Circle = namedtuple('Circle', ['x', 'y', 'r'])


# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'

dd['key1'] # key1存在
'abc'
dd['key2'] # key2不存在，返回默认值
'N/A'

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：

# >>> from collections import Counter
# >>> c = Counter()
# >>> for ch in 'programming':
# ...     c[ch] = c[ch] + 1
# ...
# >>> c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次

import struct
print(struct.pack('>I', 10240099))

# pack的第一个参数是处理指令，'>I'的意思是：

# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

# unpack把bytes变成相应的数据类型

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。
# s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print( s)
# -*- coding: utf-8 -*-
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


#https://docs.python.org/3/library/struct.html#format-characters
def bmp_info(data):
    bmpArr=struct.unpack('<2c6I2h',data[:30])
    # BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

    # 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
    # 一个4字节整数：表示位图大小；
    # 一个4字节整数：保留位，始终为0；
    # 一个4字节整数：实际图像的偏移量；
    # 一个4字节整数：Header的字节数；
    # 一个4字节整数：图像宽度；
    # 一个4字节整数：图像高度；
    # 一个2字节整数：始终为1；
    # 一个2字节整数：颜色数。
    print(bmpArr)
    print(bmpArr[:2])
    # if():
    if(bmpArr[:2]==(b'B',b'M') or bmpArr[:2]==(b'B',b'A')):
        return {
            'width': bmpArr[6],
            'height': bmpArr[7],
            'color': bmpArr[9]
        }
# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

  
##########hashlib.  Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())



#经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

# ！！！！！有意思. 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

##Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools

natuals = itertools.count(1)

for n in natuals:
    if(n==100):
        break
    print(n)
# cycle()会把传入的一个序列无限重复下去：>>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种。repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数： itertools.repeat('A', 3)

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

# >>> for c in itertools.chain('ABC', 'XYZ'):
# ...     print(c)
'''
groupby()
groupby()把迭代器中相邻的重复元素挑出来放在一起：
>>> for key, group in itertools.groupby('AAABBBCCAAA'):
...     print(key, list(group))
...
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']

实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：


>>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
...     print(key, list(group))
...
A ['A', 'a', 'a']
B ['B', 'B', 'b']
C ['c', 'C']
A ['A', 'A', 'a']

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：


'''
natuals = itertools.count(1)
print(natuals)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
# testmap=map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# print(testmap)
# for n in testmap:
#     print(n)
from functools import reduce

def add(x, y):
    return x + y 
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natual = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    selectArr=[]
    i=0
    for n in natual:
        if(i>=N):
            break
        selectArr.append(n)
        i+=1
    # print(selectArr)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # anther=[]
    onebyone=itertools.cycle([1,-1])
    # i=0
    # for  c  in onebyone:
    #     if(i>N):
    #         break
    #     anther.append(c)
    #     # print (c)
    #     i+=1
    # print(anther)

    processdata=map(lambda x,y:4.0*y/x,selectArr,onebyone )
    # step 4: 求和:
    sum=reduce(add,processdata)
    return sum
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


#并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('haha') as q:
    q.query()


# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：

with create_query('Bob') as q:
    q.query()

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

#很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
with tag("h1"):
    print("hello")
    print("world")

# 代码的执行顺序是：
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理


# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：

from contextlib import closing
from urllib.request import urlopen

# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
# 它的作用就是把任意对象变为上下文对象，并支持with语句。



# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()

# @contextlib还有一些其他decorator，便于我们编写更简洁的代码。

############## urllib提供了一系列用于操作URL的功能。
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

# 例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data)# data.decode('utf-8')
# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：

from urllib import request
import json
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', f.read())


def fetch_data(url):
    with request.urlopen(url) as f:
        data=f.read()
        return json.loads(data.decode('utf-8'))
# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')