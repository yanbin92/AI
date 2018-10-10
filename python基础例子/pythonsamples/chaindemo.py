#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
    	if(isinstance(attr,str)):
        	return Chain('%s/%s' % (self._path, attr))
		# if(isinstance(attr ,):

    def __str__(self):
        return self._path
    #任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

    def __call__(self,params):
        return Chain('%s/%s' % (self._path, params))

    __repr__ = __str__
s = Chain('Michael')
# s()#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

#如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。


print(Chain().status.user.timeline.list)
print(Chain('haha'))
print(Chain().users('michael').repos)#Chain('/users')('michael')michael').repos)#Chain().users 
# print(Chain().users('michael'))


# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：

# >>> callable(Student())
# True
# >>> callable(max)
# True
# >>> callable([1, 2, 3])
# False
# >>> callable(None)
# False
# >>> callable('str')
# False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

#
from enum import Enum,unique

month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
#value属性则是自动赋给成员的int常量，默认从1开始计数。

for name, member in month.__members__.items():
    print(name, '=>', member, ',', member.value)
@unique
class Weekday(Enum):
	Sun=0
	Mon=1
#@unique装饰器可以帮助我们检查保证没有重复值。
day1 = Weekday.Mon
print(day1)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if(isinstance(gender,Gender)):
        	self.gender = gender
        else:
        	raise ValueError('只允许接收Gender类型的参数')

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('test success')
else:
    print('测试失败!')


###########------type(). 元编程。动态创建类
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)



def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

print(type(Hello))
h = Hello()
h.hello()
print(type(h))
#动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

#metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
#metaclass，直译为元类，简单的解释就是：

# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
#定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
#有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：

class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此
# ，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

#__new__()方法接收到的参数依次是：

# 当前准备创建的类的对象；

# 类的名字；

# 类继承的父类集合；

# 类的方法集合。
vlist=[]
print(dir(vlist))
vlist=vlist.__add__([2,3])
print(vlist)


L = MyList()
L.add(1)
print(L)

#动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

#ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

#要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

# 让我们来尝试编写一个ORM框架。

# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：



# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

#首先来定义Field类，它负责保存数据库表的字段名和字段类型：

class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if(name=='Model'):
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict,metaclass=ModelMetaclass):

    def __init__(self,**kw):#**kw 指定参数必须是dict
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key]=value

    def save(self):
        fields=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql='insert into %s (%s) values (%s)' %(self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

#可以看到，save()方法已经打印出了可执行的SQL语句，以及参数列表，只需要真正连接到数据库，执行该SQL语句，就可以完成真正的功能。

# 不到100行代码，我们就通过metaclass实现了一个精简的ORM框架，是不是非常简单？

#metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。

###############-----------错误处理
#try: exception ZeroDivisionError e: finally:
# try...
# except: division by zero
# finally...
# END


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

#只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。

# try:
#     10 / 1
# except ZeroDivisionError:
#     raise ValueError('input error!')

# from functools import reduce

# def str2num(s):
#     try:
#         int(round(s))
#     except Exception as e:
#         print(e)
#     else:
#         pass
#     return 

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()

#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#如果断言失败，assert语句本身就会抛出AssertionError：
#程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

#python -O err.py 关闭后，你可以把所有的assert语句当成pass来看。

# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
#第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# python -m pdb err.py

