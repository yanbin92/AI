# connectsql.py
#还可以定义各种保存格式，但是问题来了：

# 存储和读取需要自己实现，JSON还是标准，自己定义的格式就各式各样了；

# 不能做快速查询，只有把数据全部读到内存中才能自己遍历，但有时候数据的大小远远超过了内存（比如蓝光电影，40GB的数据），根本无法全部读入内存。

# 为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定的数据，就出现了数据库（Database）这种专门用于集中存储和查询的软件。

# 数据库软件诞生的历史非常久远，早在1950年数据库就诞生了。经历了网状数据库，层次数据库，我们现在广泛使用的关系数据库是20世纪70年代基于关系模型的基础上诞生的。



# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# <sqlite3.Cursor object at 0x10f8aa260>
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# <sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
print(cursor.rowcount)

cursor.execute('select * from user where id=?', ('1',))

values = cursor.fetchall()

print(values)
# 1
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()






# 安装MySQL驱动
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：

# $ pip install mysql-connector-python --allow-external mysql-connector-python
# 如果上面的命令安装失败，可以试试另一个驱动：

# $ pip install mysql-connector
# 我们演示如何连接到MySQL服务器的test数据库：

# # 导入MySQL驱动:
# >>> import mysql.connector
# # 注意把password设为你的root口令:
# >>> conn = mysql.connector.connect(user='root', password='password', database='test')
# >>> cursor = conn.cursor()
# # 创建user表:
# >>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# >>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# >>> cursor.rowcount
# 1
# # 提交事务:
# >>> conn.commit()
# >>> cursor.close()
# # 运行查询:
# >>> cursor = conn.cursor()
# >>> cursor.execute('select * from user where id = %s', ('1',))
# >>> values = cursor.fetchall()
# >>> values
# [('1', 'Michael')]
# # 关闭Cursor和Connection:
# >>> cursor.close()
# True
# >>> conn.close()
# 由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。

# 小结
# 执行INSERT等操作后要调用commit()提交事务；

# MySQL的SQL占位符是%s。


# 在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。

# 先通过pip安装SQLAlchemy：

# $ pip install sqlalchemy
# 然后，利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：

# 第一步，导入SQLAlchemy，并初始化DBSession：

# # 导入:
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # 创建对象的基类:
# Base = declarative_base()

# # 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'

#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))

# # 初始化数据库连接:
# engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)


# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如School：

# class School(Base):
#     __tablename__ = 'school'
#     id = ...
#     name = ...
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# 你只需要根据需要替换掉用户名、口令等信息即可。

# 下面，我们看看如何向数据库表中添加一行记录。

# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()
# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。

# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：

# # 创建Session:
# session = DBSession()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='5').one()
# # 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
# # 关闭Session:
# session.close()
# 运行结果如下：

# type: <class '__main__.User'>
# name: Bob
# 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。

# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

# class User(Base):
#     __tablename__ = 'user'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')

# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

# 小结
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

# 正确使用ORM的前提是了解关系数据库的原理。