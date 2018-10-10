#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，
#即把大块函数通过切割成小块函数来降低系统的复杂度。

# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

#假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

#如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。

class Student(object):


	def __init__(self,name,score):
		self.name=name
		self.score=score
		self.__private_att=score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))


	def get_grade(self):
	    if self.score >= 90:
	    	return 'A'
	    elif self.score >= 60:
	        return 'B'
	    else:
	        return 'C'

	def set_private_att(self,private_att):
		self.__private_att=private_att

	def get_private_att(self):
		return self.__private_att

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
#AttributeError: 'Student' object has no attribute '__private_att'
# bart.__private_att
#因为不同版本的Python解释器可能会把__name改成不同的变量名。
print(bart._Student__private_att)
#你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。



bart.set_private_att('haha')
print(bart.get_private_att())

print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
# 面向对象的设计思想是抽象出Class，根据Class创建Instance。


##如何定义类
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，
#就使用object类，这是所有类最终都会继承的类。
#创建实例是通过类名+()实现的. 


#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

#数据封装

#但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；


print(bart)

#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
bart.age = 8
# lisa.age


#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，
#仍然可以通过_Student__name来访问__name变量：



#########--------------------------继承和多态
#不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对扩展开放：允许新增Animal子类；

# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
	#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

	def __len__(self):
	   return 100

	def run(self):
		print('Dog is running...')


	def eat(self):
		print('Eating meat...')


class Cat(Animal):
    pass
dog = Dog()
dog.run()

cat = Cat()
cat.run()

#静态语言 vs 动态语言
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#############----------------------获取对象信息
#使用type()
print(type(123))
print(type('123'))
print(type(True))
print(type(dog))



#断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

# 
import types
# 
def fn():
# ...     
	pass
# ...
type(fn)==types.FunctionType
True
type(abs)==types.BuiltinFunctionType
True
type(lambda x: x)==types.LambdaType
True
type((x for x in range(10)))==types.GeneratorType
True


#使用isinstance()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

isinstance('a', str)

isinstance(dog, Animal)


isinstance([1, 2, 3], (list, tuple))
True

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir('ABC'))

# 有属性'y'吗？

print(hasattr(dog, 'y'))

def readImage(fp):
    if hasattr(fp, 'read'):
        return fp.read
    return None

#######################_-----------------实例属性和类属性
class Student(object):
    STATIC_ATT = 'Student'

    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
#因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
print(Student.STATIC_ATT)


##########--------------面向对象高级编程
# 定义一个函数作为实例方法
def set_age(self,age):
	self.age = age
from types import MethodType
# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：

#为了给所有实例都绑定方法，可以给class绑定方法：

Student.set_age = set_age
#给class绑定方法后，所有实例均可调用：

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student(object):
# __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
	def __init__(self, name):
		self.name = name

	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

	def __str__(self):
		return 'Student object (name: %s)' % self.name
######使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

s = Student('haha')
# OK，实际转化为s.set_score(60)
s.score = 60 
print(s.score)
# s.score = 600000 

# #在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。


# class Bat(Mammal, Flyable):
#     pass

#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己


        
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    #原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# for n in Fib():
# 	print (n)
# print(f[1])

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
         #返回函数也是完全可以的：
	    if attr=='age':
	    	return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)



 #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：

 #利用完全动态的__getattr__，我们可以写出一个链式调用：


class Chain(object):

    def __init__(self, path=''):
        self._path = path
#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

Chain().status.user.timeline.list


##############-------------枚举


