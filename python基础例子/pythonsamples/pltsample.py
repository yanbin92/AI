import matplotlib.pyplot as plt
import numpy as np

x=np.linspace (-3,3,50)
y1=x*2+1
y2=x**2

plt.figure()
l1=plt.plot(x,y1,label='linear line')
l2=plt.plot(x, y2, label='squre line',color='red', linewidth=1.0, linestyle='--')
plt.xlim((-4,4))
plt.ylim((-6,6))
plt.xlabel('i am x')
plt.ylabel('i am y')

# legend将要显示的信息来自于上面代码中的 label. 所以我们只需要简单写下一下代码, plt 就能自动的为我们添加图例.
plt.legend(loc="best")
# 如果我们想单独修改之前的 label 信息, 给不同类型的线条设置图例信息
# plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
# 其中’loc’参数有多种，’best’表示自动分配最佳位置，其余的如下：

#  'best' : 0,          
#  'upper right'  : 1,
#  'upper left'   : 2,
#  'lower left'   : 3,
#  'lower right'  : 4,
#  'right'        : 5,
#  'center left'  : 6,
#  'center right' : 7,
#  'lower center' : 8,
#  'upper center' : 9,
#  'center'       : 10,

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
# plt.yticks(
# 	[-2, -1.8, -1, 1.22, 3],
# 	[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：bottom.
# 使用.spines设置边框 使用.set_position设置边框位置：x=0的位置
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#添加图例

#标注出点(x0, y0)的位置信息

x0=1
y0=2*x0+1
#用plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5) 画出一条垂直于x轴的虚线
plt.scatter([x0,],[y0,],s=50,color='b')

plt.plot([x0, x0], [y0,0], 'k--', linewidth=2.5)
# 添加注释 annotate
# plt.annotate(r'$2x+1=%s$' % y0,
#  xy=(x0, y0), xycoords='data',
 # xytext=(+30, -30),

plt.annotate(r'$2x+1=3$',
	xy=(x0,y0),xycoords='data',
	textcoords='offset point',
	xytext=(+30,-30))

plt.show()

# plt.figure(num=3, figsize=(8, 5),)
# plt.plot(x, y2)
# plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# plt.show()