#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
        
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

        
        
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, n):
      a,b=1,1
  		for x in range(n):
  			a, b = b, a + b
    	return a

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
	print (n)
# print(f[1])