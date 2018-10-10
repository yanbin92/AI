# coding=utf-8
#IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

#由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

# 第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；

# 另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO。

# 很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，
# 而通知你的方法也各不相同。
# 如果是服务员跑过来找到你，这是回调模式，
# 如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。
#总之，异步IO的复杂度远远高于同步IO。
#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。


try:
    f=open('./mydict2.py','r',-1,'utf-8')
    for line in f.readlines():
        print(line.encode('utf-8').strip()) # 把末尾的'\n'删掉
    # print(f.read().encode('utf-8'))
except Exception as e:
    raise e
finally:
    if f:
        f.close()
#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

# with open('/path/to/file', 'r') as f:
#     print(f.read())
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

# >>> f = open('/Users/michael/test.jpg', 'rb')
# >>> f.read()
# b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# f = open('/Users/michael/test.txt', 'w')
# >>> f.write('Hello, world!')
# >>> f.close()

# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险
# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!')

# 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

# with open('./mydict2.py', 'a') as f2:
#     f2.write('Hello, world!')


#数据读写不一定是文件，也可以在内存中读写 StringIO顾名思义就是在内存中读写str。

from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

import os
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print( os.name)
#注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print( os.uname())
print( os.environ)
#要获取某个环境变量的值，可以调用os.environ.get('key')：
print( os.environ.get('LOGNAME'))

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径:
print( os.path.abspath('.'))

#  然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：

# part-1\part-2
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')


# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
[x for x in os.listdir('.') if os.path.isdir(x)]
# 要列出所有的.py文件，也只需一行代码：

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

with os.scandir('..') as it:
    for entry in it:
        # if not entry.name.startswith('.') and entry.is_file():
        print(entry.name.encode('utf-8'))


with os.scandir('..') as it:
    for entry in it:
        # if not entry.name.startswith('.') and entry.is_file():
        print(entry.name.encode('utf-8'))




#序列化
#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import pickle
d=dict(name='bob')
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)
#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

###########JSON

import json
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

d=dict(name='haha')
print(json.dumps(d))

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
# {'age': 20, 'score': 88, 'name': 'Bob'}
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s))
print(json.dumps(s, default=lambda obj: obj.__dict__))


