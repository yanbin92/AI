#!/usr/bin/python
# -*- coding: utf-8 -*-
#filter
#序列
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n
#过滤
def _not_disvisible(n):
	return lambda x:x%n>0 # x 指代序列中的值 

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#最后，定义一个生成器，不断返回下一个素数：
def primes():
	yield 2
	#初始序列
	it=_odd_iter()
	while True:
		#返回序列的第一个数
		n=next(it)
		yield n
		#n=3 it=[1,3 ...]
		it=filter(_not_disvisible(n),it)

for n in primes():
	if n < 1000:
		print n
	else:
		break