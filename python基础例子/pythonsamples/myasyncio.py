# asyncio.py
# 异步IO

# 在IO编程一节中，我们已经知道，CPU的速度远远快于磁盘、网络等IO。在一个线程中，CPU执行代码的速度极快，然而，一旦遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作。这种情况称为同步IO。

# 在IO操作的过程中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了。

# 因为一个IO操作就阻塞了当前线程，导致其他代码无法执行，所以我们必须使用多线程或者多进程来并发执行代码，为多个用户服务。每个用户都会分配一个线程，如果遇到IO导致线程被挂起，其他用户的线程不受影响。



# 多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程。由于系统切换线程的开销也很大，所以，一旦线程数量过多，CPU的时间就花在线程切换上了，真正运行代码的时间就少了，结果导致性能严重下降。

# 由于我们要解决的问题是CPU高速执行能力和IO设备的龟速严重不匹配，多线程和多进程只是解决这一问题的一种方法。


# 另一种解决IO问题的方法是异步IO。当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。

# do_some_code()
# f = open('/path/to/file', 'r')
# r = f.read() # <== 线程停在此处等待IO操作结果
# # IO操作完成后线程才能继续执行:
# do_some_code(r)
# 所以，同步IO模型的代码是无法实现异步IO模型的。



# 异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：

loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)

# 消息模型其实早在应用在桌面应用程序中了。一个GUI程序的主线程就负责不停地读取消息并处理消息。所有的键盘、鼠标等消息都被发送到GUI程序的消息队列中，然后由GUI程序的主线程处理。




# 由于GUI线程处理键盘、鼠标等消息的速度非常快，所以用户感觉不到延迟。某些时候，

# GUI线程在一个消息处理的过程中遇到问题导致一次消息处理时间过长，此时，用户会感觉到整个GUI程序停止响应了，敲键盘、点鼠标都没有反应。

# 这种情况说明在消息模型中，处理一个消息必须非常迅速，否则，主线程将无法及时处理消息队列中的其他消息，导致程序看上去停止响应。


# 消息模型是如何解决同步IO必须等待IO操作这一问题的呢？当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，然后直接结束本轮消息处理，

# 进入下一轮消息处理过程。当IO操作完成后，将收到一条“IO完成”的消息，处理该消息时就可以直接获取IO操作结果。


# 在“发出IO请求”到收到“IO完成”的这段时间里，同步IO模型下，主线程只能挂起，但异步IO模型下，

# 主线程并没有休息，而是在消息循环中继续处理其他消息。这样，在异步IO模型下，

# 一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。

# 在学习异步IO模型前，我们先来了解协程。

# 协程，又称微线程，纤程。英文名Coroutine。

# 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。


# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

# 注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

def A():
    print('1')
    print('2')
    print('3')

def B():
    print('x')
    print('y')
    print('z')
# 假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：
1
2
x
y
3
z

# 但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。


######！！！！！ 看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？


# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

# Python对协程的支持是通过generator实现的。

# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

# 来看例子：

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)



# 执行结果：

# [PRODUCER] Producing 1...
# [CONSUMER] Consuming 1...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 2...
# [CONSUMER] Consuming 2...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 3...
# [CONSUMER] Consuming 3...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 4...
# [CONSUMER] Consuming 4...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 5...
# [CONSUMER] Consuming 5...
# [PRODUCER] Consumer return: 200 OK
# 注意到consumer函数是一个generator，把一个consumer传入produce后：

# 首先调用c.send(None)启动生成器；

# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

# consumer通过yield拿到消息，处理，又通过yield把结果传回；

# produce拿到consumer处理的结果，继续生产下一条消息；

# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

# 最后套用Donald Knuth的一句话总结协程的特点：

# “子程序就是协程的一种特例。”

#############------------------------------###############
# Python天天美味(25) - 深入理解yield

# http://www.cnblogs.com/coderzh/articles/1202040.html
# #yield的英文单词意思是生产，刚接触Python的时候感到非常困惑，一直没弄明白yield的用法。只是粗略的知道yield可以用来为一个函数返回值塞数据，比如下面的例子：
# def addlist(alist):
#     for i in alist:
#         yield i + 1
# 取出alist的每一项，然后把i + 1塞进去。然后通过调用取出每一项：
# alist = [1, 2, 3, 4]
# for x in addlist(alist):
#     print x,
# 这的确是yield应用的一个例子，但是，看过limodou的文章《2.5版yield之学习心得》，并自己反复体验后，对yield有了一个全新的理解。
# 1. 包含yield的函数
# 假如你看到某个函数包含了yield，这意味着这个函数已经是一个Generator，它的执行会和其他普通的函数有很多不同。比如下面的简单的函数：
# def h():
#     print 'To be brave'
#     yield 5

# h()
# 可以看到，调用h()之后，print 语句并没有执行！这就是yield，那么，如何让print 语句执行呢？这就是后面要讨论的问题，通过后面的讨论和学习，就会明白yield的工作原理了。
# 2. yield是一个表达式
# Python2.5以前，yield是一个语句，但现在2.5中，yield是一个表达式(Expression)，比如：
# m = yield 5
# 表达式(yield 5)的返回值将赋值给m，所以，认为 m = 5 是错误的。那么如何获取(yield 5)的返回值呢？需要用到后面要介绍的send(msg)方法。
# 3. 透过next()语句看原理
# 现在，我们来揭晓yield的工作原理。我们知道，我们上面的h()被调用后并没有执行，因为它有yield表达式，因此，我们通过next()语句让它执行。next()语句将恢复Generator执行，并直到下一个yield表达式处。比如：
# def h():
#     print 'Wen Chuan'
#     yield 5
#     print 'Fighting!'

# c = h()
# c.next()
# c.next()调用后，h()开始执行，直到遇到yield 5，因此输出结果：
# Wen Chuan
# 当我们再次调用c.next()时，会继续执行，直到找到下一个yield表达式。由于后面没有yield了，因此会拋出异常：
# Wen Chuan
# Fighting!
# Traceback (most recent call last):
#   File "/home/evergreen/Codes/yidld.py", line 11, in <module>
#     c.next()
# StopIteration
# 4. send(msg) 与 next()
# 了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做
# c.next() 和 c.send(None) 作用是一样的。
# 来看这个例子：
# def h():
#     print 'Wen Chuan',
#     m = yield 5  # Fighting!
#     print m
#     d = yield 12
#     print 'We are together!'

# c = h()
# c.next()  #相当于c.send(None)
# c.send('Fighting!')  #(yield 5)表达式被赋予了'Fighting!'
# 输出的结果为：
# Wen Chuan Fighting!
# 需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。
# 5. send(msg) 与 next()的返回值
# send(msg) 和 next()是有返回值的，它们的返回值很特殊，返回的是下一个yield表达式的参数。比如yield 5，则返回 5 。到这里，是不是明白了一些什么东西？本文第一个例子中，通过for i in alist 遍历 Generator，其实是每次都调用了alist.Next()，而每次alist.Next()的返回值正是yield的参数，即我们开始认为被压进去的东东。我们再延续上面的例子：
# def h():
#     print 'Wen Chuan',
#     m = yield 5  # Fighting!
#     print m
#     d = yield 12
#     print 'We are together!'

# c = h()
# m = c.next()  #m 获取了yield 5 的参数值 5
# d = c.send('Fighting!')  #d 获取了yield 12 的参数值12
# print 'We will never forget the date', m, '.', d
# 输出结果：
# Wen Chuan Fighting!
# We will never forget the date 5 . 12
# 6. throw() 与 close()中断 Generator
# 中断Generator是一个非常灵活的技巧，可以通过throw抛出一个GeneratorExit异常来终止Generator。Close()方法作用是一样的，其实内部它是调用了throw(GeneratorExit)的。我们看：
# def close(self):
#     try:
#         self.throw(GeneratorExit)
#     except (GeneratorExit, StopIteration):
#         pass
#     else:
#         raise RuntimeError("generator ignored GeneratorExit")
# # Other exceptions are not caught
# 因此，当我们调用了close()方法后，再调用next()或是send(msg)的话会抛出一个异常：
# Traceback (most recent call last):
#   File "/home/evergreen/Codes/yidld.py", line 14, in <module>
#     d = c.send('Fighting!')  #d 获取了yield 12 的参数值12
# StopIteration

