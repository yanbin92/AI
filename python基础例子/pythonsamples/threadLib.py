#coding=utf-8
#第三方模块
from PIL import Image
im= Image.open('/Users/hitomac_001/Downloads/test.png')

w,h=im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'png')



# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

# 比如，模糊效果也只需几行代码：https://pillow.readthedocs.org/ 要详细了解PIL的强大功能，请请参考Pillow官方文档：



from PIL import Image, ImageFilter

# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('test.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')



# 我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。

# 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

# import requests
# >>> r = requests.get('https://www.douban.com/') # 豆瓣首页
# >>> r.status_code
# 200
# >>> r.text

# 对于带参数的URL，传入一个dict作为params参数：

# >>> r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# >>> r.url # 实际请求的URL
# 'https://www.douban.com/search?q=python&cat=1001'

# requests自动检测编码，可以使用encoding属性查看：

# >>> r.encoding
# 'utf-8'


# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。

# 当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

import chardet
chardet.detect(b'hello world') 
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
data = '离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)			

# 我们再试试对日文进行检测：##

data = '最新の主要ニュース'.encode('euc-jp')
# >>> chardet.detect(data)


# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。

# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

import psutil
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False)) # CPU物理核心. # 2说明是双核超线程, 4则是4核非超线程



# 获取进程信息
# 通过psutil可以获取到所有进程的详细信息：

# >>> psutil.pids() # 所有进程ID
# [3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
# >>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
# >>> p.name() # 进程名称
# 'python3.6'
# >>> p.exe() # 进程exe路径
# '/Users/michael/anaconda3/bin/python3.6'
# >>> p.cwd() # 进程工作目录
# '/Users/michael'
# >>> p.cmdline() # 进程启动的命令行
# ['python3']
# >>> p.ppid() # 父进程ID
# 3765
# >>> p.parent() # 父进程
# <psutil.Process(pid=3765, name='bash') at 4503144040>
# >>> p.children() # 子进程列表
# []
# >>> p.status() # 进程状态
# 'running'
# >>> p.username() # 进程用户名
# 'michael'
# >>> p.create_time() # 进程创建时间
# 1511052731.120333
# >>> p.terminal() # 进程终端
# '/dev/ttys002'
# >>> p.cpu_times() # 进程使用的CPU时间
# pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
# >>> p.memory_info() # 进程使用的内存
# pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
# >>> p.open_files() # 进程打开的文件
# []
# >>> p.connections() # 进程相关网络连接
# []
# >>> p.num_threads() # 进程的线程数量
# 1
# >>> p.threads() # 所有线程信息
# [pthread(id=1, user_time=0.090318, system_time=0.062736)]
# >>> p.environ() # 进程环境变量
# {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
# >>> p.terminate() # 结束进程
# Terminated: 15 <-- 自己把自己结束了




# 首先，我们用pip安装virtualenv：

# $ pip3 install virtualenv
# 然后，假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：

# 第一步，创建目录：

# Mac:~ michael$ mkdir myproject
# Mac:~ michael$ cd myproject/
# Mac:myproject michael$
# 第二步，创建一个独立的Python运行环境，命名为venv：

# Mac:myproject michael$ virtualenv --no-site-packages venv
# Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
# New python executable in venv/bin/python3.4
# Also creating executable in venv/bin/python
# Installing setuptools, pip, wheel...done.

# 命令virtualenv就可以创建一个独立的Python运行环境，我们还加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。

# 新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境：

# Mac:myproject michael$ source venv/bin/activate
# (venv)Mac:myproject michael$


# 下面正常安装各种第三方包，并运行python命令：

# (venv)Mac:myproject michael$ pip install jinja2
# ...
# Successfully installed jinja2-2.7.3 markupsafe-0.23
# (venv)Mac:myproject michael$ python myapp.py
# ...
# 在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。

# 退出当前的venv环境，使用deactivate命令：

# (venv)Mac:myproject michael$ deactivate 
# Mac:myproject michael$
# 此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。
# 完全可以针对每个应用创建独立的Python运行环境，这样就可以对每个应用的Python环境进行隔离。

# virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，
#virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。

# virtualenv为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题。


