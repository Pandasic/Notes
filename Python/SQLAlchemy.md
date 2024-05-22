
# SQLAlchemy 数据库ORM

> 参考自： 
>
> https://www.sqlalchemy.org/ (官方文档)
>
> https://zhuanlan.zhihu.com/p/27400862
>
> https://www.cnblogs.com/ExMan/p/9856492.html
>
> https://en.wikipedia.org/wiki/SQLAlchemy
>
> https://greyli.com/generate-flask-sqlalchemy-model-class-for-exist-database/
>
> https://zhuanlan.zhihu.com/p/64450987

[toc]

# SQLAlchemy 简介

SQLAlchemy 是一个功能强大的Python ORM 工具包，口碑不错，社区活跃也较为开放
connect.py :底层的数据库连接
orm.py :模型定义的样例
example_test.py :单元测试，实质上可以对应业务的具体使用
python3_test.py :展示Python3 asyncio下的SQLAlchemy

分别建立python2/3的虚拟环境，然后安装对应的requirements.txt即可

无论什么语言，无论什么库，做一个ORM实现，至少应当实现完全**语义化**的数据库操作，使得操作数据库表就像在操作对象。
完整的ORM应当可以完全避免SQL拼接

## 为什么需要ORM

当时分享完毕之后，也确实很多同事表示还是喜欢裸SQL，我后来也又在工作中看到了很多遗留代码的问题。我也正好趁浴室迷思 想了一下，为什么我需要ORM呢？

第一条来自一个定理：

**一切由人直接来保证安全性的系统，就一定会出错**

拼接SQL、把SQL做成模板、开始使用ORM、封装出DAO层，几乎是每个项目的共识吧？
过往的项目中，由我第一手写的，都会第一时间加入ORM，毕竟也只是两三个小文件，一百行以内的事情（后续由于封装的增多，可能会到达数百行）

这段时间在写旧系统的小规模重构（**定理2：一个好程序猿应当友好地帮前人擦好屁股，而不是靠重新制造一个新屁股实现**），拼接字符串并没有带来任何优点，反而引入了非常简单的注入漏洞，简单的设想这样一个列表API的场景：

1. 根据请求参数控制对应的：过滤条件、排序方法、翻页
2. 根据需要预取关联的表，JOIN并把对一对多的关系化为一个list

第一条，刚一上手，就发现满地的string format，翻页用了：

```python
order_sql = "ORDER BY {} {}".format(order_by,direction)
```

毫无疑问的order_by=id%3Bselect+1%3B-- 就直接注入了

要解决这些在SQL拼接的问题，除了表单验证，毫无疑问需要做一个SQL字符转义，另外在能用SQL参数的地方，需要用参数（然后也得注意拼接时候参数的个数，是的，这里我们的接口有另一个BUG，参数数量没数对）

第二个功能点，想象一下在需要的地方额外加一句LEFT JOIN，然后对结果再做额外的解析

还有一些附属功能：单元测试如何建表？代码里遍地的硬编码表名如何解决？


自己不是不能实现，但自己来实现这些，就走上了发明ORM的老路，用一个成熟的、文档丰富的ORM，岂不美哉？

# 核心概念与入门

[官方文档](https://link.zhihu.com/?target=https%3A//www.sqlalchemy.org/)

| 概念    | 对应数据库 | 说明                                   |
| ------- | ---------- | -------------------------------------- |
| Engine  | 连接       |                                        |
| Session | 连接池     | 由此开始查询                           |
| Model   | 表         | 类定义和表定义蕾丝，类本质上是其中一行 |
| Column  | 列         | 各地方支持运算符操作                   |
| Query   | 若干行     | 链式操作 展开为 SELECT/DELETE/UPDATE   |

## 模型定义

我们来看看他如何完成模型定义：

```python
# coding=utf-8
from __future__ import unicode_literals, absolute_import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
ModelBase = declarative_base() #<-元类

class User(ModelBase):
    __tablename__ = "auth_user" # 表名

    id = Column(Integer, primary_key=True)
    date_joined = Column(DateTime)
    username = Column(String(length=30))
    password = Column(String(length=128))
```

> 从这里可以看到，模型定义甚至与数据库是无关的，所以允许不同的数据库后端，不同类型拥有不同的表现形式和建表语句
>
> 这里我们可以看到它实现了 ORM与数据库连接的解耦，一些数据库后端不支持的数据类型，例如Numeric类型，在sqlite中不支持，不过SQLAlchemy也能做一些兼容使用普通浮点
>
> **Model** 等同于数据库的一张表
> **Column** 显然就是这张表的一列

### 字段属性

```python
name = Column(String(32), 		# 字段类型
              index=True, 		# 是否为索引
              nullable=False, # 是否可为NULL
             	unique=True,		# 唯一字段
             	default=18,			# 默认值
              autoincrement=True, # 自增
              ForeignKey("hobby.id") # 外键
              primary_key=True） # 是否为主键
```

| arg1          | 字段类型                       |
| ------------- | ------------------------------ |
| index         | 是否为索引                     |
| nullable      | 是否可为NULL                   |
| unique        | 唯一字段                       |
| default       | 默认值                         |
| autoincrement | 自增                           |
| ForeignKey    | 外键，内部的值为\_\_tablename\_\_ 的值 |
| primary_key   | 主键 |

### 时间字段

```python
ctime = Column(DateTime, default=datetime.datetime.now)
```

> 设置默认值时不能加括号

### 联合唯一，联合索引

```python
__table_args__ = (
        # 联合唯一
        UniqueConstraint('id', 'name', name='uix_id_name'),
        
        # 联合索引
        Index('ix_id_name', 'name', 'email'),
 )
```

## 创建引擎

```python
engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/t1?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    echo = True    # echo参数为True时，会显示每条执行的SQL语句，可以关闭   
)
```
"数据库+第三方模块：//用户名：密码@数据库服务端IP：端口号/数据库名？编码"

## 创建、删除表

```python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

# 创建 Base
Base = declarative_base()

# 模型定义
class User(Base):
    __tablename__ = 'users'
    ...
# 利用Base的create_all创建表
Base.metadata.create_all(engine)

# 利用Base的create_all删除表
Base.metadata.drop_all(engine)
```

## 创建Session

```python
def get_session():
  Session = sessionmaker(bind=engine)
  session = Session()
```

## 增

```python
with get_session() as session:
    session.add(User(username="asd", password="asd"))
    session.add(User(username="qwe", password="qwe"))
    session.commit()
```

**session**(会话)的概念，可以看成一个管理数据库持久连接的对象,在此下面是完全透明的连接池和事务等东西

> get_session底下configure可以控制auto_commit参数，= False时写操作默认都不放在事务里,SQLAlchemy默认为True

session.add函数将会把Model加入当前的持久空间(可以从session.dirty看到)，直到commit时更新

## 查

```python
with get_session() as session:
    # <class 'sqlalchemy.orm.query.Query'>
    session.query(User)
```

最简单的这个查询返回了一个Query对象
需要注意的是，这里只构造Query，事实上并没有发送至数据库进行查询，只会在Query.get()、Query.all()、Query.one()以及Query.__iter__等具有“执行”语义的函数，才会真的去获取

**Query** ：本质上是数据表的若干行

1. 在查询情况的下，等同于SQL 中的 SELECT Syntax
2. 在update函数的操作时，可以根据参数选择等同于直接UPDATE users SET xxx WHERE name=xxx或者先用SELECT 选出ID，再循环用UPDATE xxx WHERE id=xxx
3. delete同上

以SQLAlchemy为代表的ORM基本都支持链式操作。
形如：

```python
with get_session() as session:
    # <class 'sqlalchemy.orm.query.Query'>
    query = (session
             .query(User)
             .filter(User.username == "asd")
             .filter_by(username="asd")
             #上面两个都是添加where
             .join(Addreess)#使用ForeignKey
             .join(Addreess,Addreess.user_id==User.id)#使用显式声明
             .limit(10)
             .offset(0)
             )
```

所有Query支持的详情见[Query API文档](https://link.zhihu.com/?target=http%3A//docs.sqlalchemy.org/en/rel_1_1/orm/query.html%23sqlalchemy.orm.query.Query.__init__)

上面也涉及到一个特别有意思的filter函数：User.username == "asd" ,实际上是SQLAlchemy重载了Column上的各种运算符  __eq__、__ge__，返回了一个BinaryExpression对象，看起来就更加符合直觉上的语义

## 复杂查询

基于Query的subquery

```python
with get_session() as session:
    # <class 'sqlalchemy.orm.query.Query'>
    query = (session
            .query(User.id)
            .filter(User.username == "asd")
            .filter_by(username="asd")
            .limit(10)
            )
    subquery = query.subquery()
    query2 = session.query(User).filter(
        User.id.in_(subquery)
    )
    print query2#<-打印展开成的SQL，此处没有SQL查询
```

理解了Query、Column的概念，也很容易自行构造出这样的SQL

所有在Column级别上的使用 详见[Column API文档](https://link.zhihu.com/?target=http%3A//docs.sqlalchemy.org/en/rel_1_1/core/metadata.html%23sqlalchemy.schema.Column.__eq__)

## 删 

上面我们提到了直接对Query进行的删除：

```python
with get_session() as session:
    query = (session
             .query(User)
             .filter(User.username == "asd")
             .filter_by(username="asd")
             .join(Addreess)
             .join(Addreess,Addreess.user_id=User.id)
             .limit(10)
             .delete()#<-这里
             )
```

另外，因为Model也可以被放进session里，然后删除的，和插入是个反向操作：

```python
with get_session() as session:
    instance = session.query(User).get(1)
    session.delete(instance)
    #下一句执行：DELETE FROM auth_user WHERE auth_user.id = ?
    session.commit()
```

## 改

改首先是上述Query中所说的update方法：

```python
with get_session() as session:
            # get by id
    query = (session
             .query(User)
             .filter_by(id=1)
             .update({"username": 
                     User.username + "a"},
                     synchronize_session=False)
                     )
```

然后是在Model级别的方法：

```python
with get_session() as session:
            # get by id
    user = (session
            .query(User)
            .get(1)
            )
    user.password = "zxcv"
    # UPDATE auth_user SET password=?
    # WHERE auth_user.id = ?
    session.commit()
```

在对Model的属性进行修改的时候，session会得到修改对应的内容,下次commit即会提交SQL
这里留个思考题：如果对1、同一对象的同一属性进行修改，2、同一对象的不同属性进行修改 ，最终会有几个SQL被发出？ 如果你来实现这样的功能，你会从哪里下手？

## 基础性能

[SQLAlchemy性能](https://link.zhihu.com/?target=http%3A//docs.sqlalchemy.org/en/rel_1_1/faq/performance.html%23faq-performance)

比较了十万条记录插入的性能



![img](https://pic1.zhimg.com/80/v2-3fd46c431fe919246a1c66484dfdec18_1440w.png)

另外不要觉得比sqlite 裸SQL慢三倍很慢，注意这个量级，实际项目中会发现慢查询、不规范操作（例如for循环里放查询）的危害比引入ORM的这点开销打多了

## 总结

到这再贴上面那个概念表，应该就能比较好的理解了

![img](https://pic3.zhimg.com/80/v2-d1f3913d109b3a70f9caddaa9e686ff6_1440w.png)

在用裸SQL可以解决的场景下，上述的SQLAlchemy入门部分就足以掌控场景，完成所有的增删查改API需求（甚至自动生成代码的需求），自动生成真是偷懒无止境。。不过发明新的DSL嘛，能不做就不做。。

# 从已有的表中生成代码

 SQLAlchemy 基于模型类对数据库表进行操作，所以，如果你想对已存在的数据库表进行操作，就要先为它编写对应的模型类。 

 对于简单的数据库，比如只有几张表，没有复杂的关系，表字段也很少，你可以直接对照表模式手写模型类。 

 其他情况下，使用自动化工具 [SQLAcodegen](https://pypi.python.org/pypi/sqlacodegen) / [Flask-SQLAcodegen](https://github.com/ksindi/flask-sqlacodegen) 自动生成模型类定义会更加方便，根据单独使用 SQALchemy 还是使用扩展 Flask-SQLAlchemy，你可以选择阅读对应的章节。 

##  单独使用 SQLAlchemy

 首先使用 pip 安装： 

```
$ pip install sqlacodegen
```

 执行下面的命令将模型类输出到 models.py 文件里（将覆盖目标文件原内容）： 

```
$ sqlacodegen --outfile models.py sqlite:///database.db
```

 这个命令的格式如下： 

```
$ sqlacodegen --outfile <输出的文件名e> <数据库连接 URI>
```

 –outfile / -o 选项设置输出的目标文件，不给出这个选项将直接在命令行输出生成的模型类定义，比如： 

```python
$ sqlacodegen sqlite:///data.db
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    body = Column(String(200))
    timestamp = Column(DateTime, index=True)
```

 *提示 如上所示，生成的模型类定义会包含 Base 和 metadata 对象定义和相关导入语句，你或许需要进行细微的调整。* 

 你可以使用下面的命令查看更多可用的设置选项： 

```
$ sqlacodegen --help
```

 *提示 除了使用 SQLAcodegen，你也可以直接使用内置的 [Automap](https://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html) 扩展生成模型类。* 

##  使用 Flask-SQLAlchemy  

 首先使用 pip 安装 Flask-SQLAcodegen： 

```
$ pip install flask-sqlacodegen
```

 执行下面的命令将模型类输出到 models.py 文件里（将覆盖目标文件原内容）： 

```
$ flask-sqlacodegen --flask --outfile models.py sqlite:///database.db
```

 这个命令的格式如下： 

```
$ flask-sqlacodegen --flask --outfile <输出的文件名> <数据库连接 URI>
```

 –flask 选项设置输出 Flask-SQLAlchemy 模型类，不给出这个选项将直接输出 SQLAlchemy 原生模型类定义；–outfile 选项设置输出的目标文件，不给出这个选项将直接在命令行输出生成的模型类定义，比如： 

```
$ flask-sqlacodegen --flask sqlite:///data.db
# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True)
```

 *提示 如上所示，生成的模型类定义会包含一个 db 对象定义和相关导入语句，你或许需要进行细微的调整。* 

 你可以使用下面的命令查看更多可用的设置选项： 

```
$ flask-sqlacodegen --help
```



# 扩展与进阶

从过往的经验来看，SQLAlchemy以优雅的直觉实现了诸多接口，并保留了良好的可扩展性，这里抛砖引玉一些有趣的特性

## 事件

应用层的触发器(trigger),支持：

1. ConnectionEvents 包括Connection和Engine(连接后进行一些自检操作)
2. DDLEvents 模型增删查改事件
3. DialectEvents 不同种类的数据库的事件
4. PoolEvents 连接池事件，连接的检出和回收等

上面的性能测试里就使用了两种事件

```python
from sqlalchemy import event
from sqlalchemy.engine import Engine
import time
import logging

logging.basicConfig()
logger = logging.getLogger("myapp.sqltime")
logger.setLevel(logging.DEBUG)

@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    logger.debug("Start Query: %s", statement)

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    logger.debug("Query Complete!")
    logger.debug("Total Time: %f", total)
```

## 反射

现有项目或者别人的代码里如果已经用其他的方式写好了表定义，不想再定义Model了，想用SQLAlchemy直接使用对应的数据库表
查文档关键字：[Automap](https://link.zhihu.com/?target=http%3A//docs.sqlalchemy.org/en/rel_1_1/orm/extensions/automap.html%23)

```python
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("sqlite:///mydatabase.db")

# reflect the tables
Base.prepare(engine, reflect=True)
tables = Base.classes#<-load tables

User = Base.classes.user
Address = Base.classes.address
# rudimentary relationships are produced
session.add(Address(email_address="foo@bar.com", user=User(name="foo")))
session.commit()

# collection-based relationships are by default named
# "<classname>_collection"
print (u1.address_collection)
```

扩展阅读：[DeferredReflection](https://link.zhihu.com/?target=http%3A//docs.sqlalchemy.org/en/rel_1_1/orm/extensions/declarative/api.html%23sqlalchemy.ext.declarative.DeferredReflection)

我之前在一些OLAP应用 用来做数据分析时用到过。。

## Python3.x asyncio扩展

16年12月 Python3.6进入稳定期，同时也标志着Python3.4和3.5中的asyncio模块进入稳定期

SQLAlchemy对asyncio的支持在于，它实质上可以在engine层进行扩展,同时扩展Engine、Connection、Transaction、Context 代码量约400行

> Strategies for creating new instances of Engine types. These are semi-private  implementation classes which provide the underlying behavior for the  "strategy" keyword argument available on  :func:~sqlalchemy.engine.create_engine. Current available options are  plain, threadlocal, and mock. New strategies can be added via new  EngineStrategy classes. """

形如：

```python
from sqlalchemy.engine.strategies import DefaultEngineStrategy
from .engine import AsyncioEngine
ASYNCIO_STRATEGY = '_asyncio'

class AsyncioEngineStrategy(DefaultEngineStrategy):
    name = ASYNCIO_STRATEGY
    engine_cls = AsyncioEngine
AsyncioEngineStrategy()  


async def main():
    engine = create_engine(
        # In-memory sqlite database cannot be accessed from different
        # threads, use file.
        'sqlite:///test.db', strategy=ASYNCIO_STRATEGY
    )

    metadata = MetaData()
    users = Table(
        'users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', Text),
    )

    # Create the table
    await engine.execute(CreateTable(users))

    conn = await engine.connect()  
```

另外提一嘴的是：asyncio不是银弹，会导致应用层压力直接传给DB，会掩盖应用的SQL写的烂的问题

## 分片Session

读写分离是当数据库压力到达一定阶段时，由应用层进行的拆分数据库压力的措施
实现一种主从分离的Session:

1. 最简单的方案是直接扩展Session类get_bind方法

> get_bind(mapper=None, clause=None)
> Return a “bind” to which this Session is bound. Note that the “mapper”  argument is usually present when Session.get_bind() is called via an ORM operation such as a Session.query(), each individual  INSERT/UPDATE/DELETE operation within a Session.flush(), call, etc.

1. 也可以使用sqlalchemy.ext.horizontal_shard模块中已经实现好的ShardedSession

> Parameters:

- shard_chooser – A callable which, passed a Mapper, a mapped instance, and possibly a  SQL clause, returns a shard ID. This id may be based off of the  attributes present within the object, or on some round-robin scheme.
- id_chooser – A callable, passed a query and a tuple of identity values, which  should return a list of shard ids where the ID might reside.
- query_chooser – For a given Query, returns the list of shard_ids where the query should be issued.
- shards – A dictionary of string shard names to Engine objects.

允许根据model或者SQL条件、ID选择具体的数据库连接。一个未经验证的脑洞：因为shards是Engine的dict，那么是否允许在异构数据库之间使用Shard？这样会带来什么样的优缺点？

## 自定义的列类型

很久很久以前做的功能了，想象一个这样的场景：

- Postgresql支持IP/CIDR的存储，本质上是使用4*8bit=32bit的int存储
- Mysql此时并没有这样简单的IP存储 如何对其进行扩展？

自定义实现的列类型实质上需要：

1. 指定在某种数据库方言下的存储类型，例如Mysql下使用int
2. 实现两个方法：从数据库中取出来一个python对象和把Python对象放入数据库
3. 按需需要实现：支持一些操作符(例如==,in_)

```python
from sqlalchemy import types
class MyIPType(types.TypeDecorator):
    impl = types.Integer


    def process_bind_param(self, value, dialect):
        #from python to database
        if dialect=="mysql":
            pass
        return #....

    def process_result_value(self, value, dialect):
        #from database to python object
        return #...
```

我们也可以在awesome-sqlalchemy中找到一些有趣的类型扩展

## 混合(hybrid)属性

我们常见使用Python的property修饰器来构造一个复杂属性，SQLAlchemy中，这个混合属性的作用也类似，不仅可以用于获得对应的值，也可以用于Query时的链式操作

定义一个Model后，可以在各类增删查改中用到这个混合属性。混合属性 混合在：既是一个Python属性，也是一个可以放入数据库查询的属性

```python
class Interval(Base):
    __tablename__ = 'interval'

    id = Column(Integer, primary_key=True)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @hybrid_property
    def length(self):
        return self.end - self.start
    #下面这个写着玩的。。
    @length.setter
    def length(self, value):
        self._value = value

>>> i1 = Interval(5, 10)
>>> i1.length
5

>>> print Session().query(Interval).filter_by(length=5)
SELECT interval.id AS interval_id, interval.start AS interval_start,
interval."end" AS interval_end
FROM interval
WHERE interval."end" - interval.start = :param_1
```

上述还有一个写着玩儿的setter，hybrid_property支持：

1. comparator 扩展Interval.length在各种比较符(><=)的行为
2. deleter/setter 顾名思义
3. expression 可以扩展最后展开的SQL表达式，例如展开成SUM(xxx):

```python
from sqlalchemy.orm import func
    #下面这个写着玩的。。
    @length.expression
    def length(self, expr):
        return func.sum(self.end, expr)
```

## 序列化Query

提供一个接口，以序列化和反序列化Query，用于跨系统、微服务的场景

```python
from sqlalchemy.ext.serializer import loads, dumps
metadata = MetaData(bind=some_engine)
Session = scoped_session(sessionmaker())

# ... define mappers

query = Session.query(User).
    filter(User.somedata=='foo').order_by(User.sortkey)

# pickle the query
serialized = dumps(query)

# unpickle.  Pass in metadata + scoped_session 
# 上面提到过的 query和Session实际上是密不可分的
query2 = loads(serialized, metadata, Session)

print query2.all()
```

这个做起来其实就非常带感了，微服务之间的必要条件就是各种dump，结合一下celery，实现一个去中心的HTTP服务也是不在话下

## Baked Query

缓存从Query生成的SQL，以减少生成时间，实际上是个应用层面的存储过程、View

```python
from sqlalchemy.ext import baked
bakery = baked.bakery()#<-创建了一个LRU

from sqlalchemy import bindparam

def search_for_user(session, username, email=None):

    baked_query = bakery(lambda session: session.query(User))
    baked_query += lambda q: q.filter(User.name == bindparam('username'))

    baked_query += lambda q: q.order_by(User.id)

    if email:
        baked_query += lambda q: q.filter(User.email == bindparam('email'))

    result = baked_query(session).params(username=username, email=email).all()

    return result
```

上面说到了SQLAlchemy展开成SQL的性能问题，真的特别担忧的话，再来一个缓存绑定参数如何？

## 多态和关系

使用多个模型，但实际上只是操作一张数据库表 此处基本略，之前写过一篇文章了：[这儿](https://zhuanlan.zhihu.com/p/26056479)

```python
class Employee(Base):  
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'employee',
        'polymorphic_on':type
    }
```

这里定义了雇员Employee 模型，指定type字段为多态所在字段，并且对于这个模型，当type字段为'employee'时，即为一个雇员

一对一、一对多、多对多的关系和自动收集成collection。

## 自动生成sqlalchemy modle

1. 安装SQLAcodegen  

   ```
   pip install sqlacodegen
   ```

2. 执行

   ```
   sqlacodegen mysql://root:123456@127.0.0.1:3306/test > models.py
   ```

   会在当前目录下生成models.py

3. 如果是python3  会报错

   No module named 'MySQLdb'

   这个时候安装pymysql。 然后在sqlacodegen 的\_\_init\_\_.py文件里加上

   ```python
   import pymysql
   
   pymysql.install_as_MySQLdb()
   ```
