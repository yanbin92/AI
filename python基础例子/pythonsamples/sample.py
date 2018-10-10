# coding=utf-8
maps={'key':'value'}
maps

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
	print(key,d[key])

print list(range(1,10))
l=[x*x for x in range(1,10)]
print l

for k,v in d.items():
	print (k,v)
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

n1=255
print((hex(n1)))
 
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
power(5)

def nop():
	pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#但其实这只是一种假象，Python函数返回的仍然是单一值： 原来返回值是一个tuple
# 面试官老师考leetcode也不觉得无聊吗。我给大家推荐一个有效甄别一个程序员是不是有经验的方法：
# 出一道复杂的带一点算法的数据结构得题目，你把算法都告诉他，就让他照着文字写，而不是让他去想算法。
# 譬如说二叉平衡树，你把旋转的四个细节都画成图，然后要求他写出代码来。他不需要记住什么是二叉平衡树，
# 他只需要对写代码本身有了解就行。写完了，要求他出test case出完，
# 让他说一下为什么跑完这个test case会让他对他的代码有信心最后，
# 挑一个test case人肉运行一遍代码能力各方面就都考到了。


def face(n):
	if n==1:
		return 1
	return n*face(n-1)
print face(3)

def trim(s):
	start=0
	end=-1
	print('测试值：',s)
	for i in range(len(s)):
		if s[i]!=" ":
			start=i
			break
	for i in range(len(s)):
		if s[len(s)-i-1]!=" ":
			end=len(s)-i
			break
	print '',start,end
	if start<=end:
		return s[start:end]
	else:
		return ''
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

print [m + n for m in 'ABC' for n in 'XYZ']
print [s.lower() for s in L]
isinstance(x, str)
import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] 

g=(x for x in range(10))
#print g
for n in g:
	print n
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	#return 'done'
f=fib(5)
print next(f)
# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#闭包问题
def count():
    fs = []
    def f(j):
		def g():
			return j*j
		return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()

#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

print f1(),f2(),f3()




def createCounter():
	def iter_absinteger():
		n=1
		while True:
			yield n
			n=n+1
	x=iter_absinteger()
	def counter():
		return next(x)
	return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
f=lambda x:x*x
print(f)
print(f.__name__)
print(f(3))

L = list(filter(lambda x:x%2==1, range(1, 20)))
print(L)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-9-7')
now()
### 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)

#这个3层嵌套的decorator用法如下：

#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：


import functools


def log(text):
    def decorator(func):
    	@functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now2():
    print('2015-3-25')
now2()

print(now2.__name__)


import time, functools


def metric(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (func.__name__, func(*args, **kw)))
		return func(*args, **kw)
	return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def Log(test=''):
	def log(func):
	    def inner(*args,**kw):
	        print('begin call %s' %test)
	        c = func(*args,**kw)
	        print('end call')
	        return c
	    return inner
	return log
@Log('hahah')
def now3():
    print('20180905')

@Log()
def now4():
    print('20180905')
now3()
now4()


#偏函数


print(int('12345', base=8))

def int2(x, base=2):
    return int(x, base)
int2('1000000')
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。




 #注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

max2=functools.partial(max,10)

print(max2(2,3,4))
kw = { 'base': 2 }
# int2 = functools.partial(int, base=2)
int2=int('10010', **kw)
print(int2)

