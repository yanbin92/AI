#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
#第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# python -m pdb err.py
#输入命令n可以单步执行代码：

#任何时候都可以输入命令p 变量名来查看变量：

# 输入命令q结束调试，退出程序：


#import pdb
#pdb.set_trace()
#这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# err.py
# import pdb

# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)
