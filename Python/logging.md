# logging 日志模块

> 参考：https://www.cnblogs.com/yyds/p/6901864.html

## 日志简介

### 日志作用

* 程序调试

- 了解软件程序运行情况，是否正常
- 软件程序运行故障分析与问题定位
- 用户行为分析

### 一般日志等级

- DEBUG
- INFO
- NOTICE
- WARNING
- ERROR
- CRITICAL
- ALERT
- EMERGENCY

### 信息与格式

一条日志信息对应的是一个事件的发生，而一个事件通常需要包括以下几个内容：

- 事件发生时间
- 事件发生位置
- 事件的严重程度--日志级别
- 事件内容

还可以包括一些其他信息

* 进程ID
* 进程名称
* 线程ID
* 线程名称

## logging

### 日志级别

`logging`模块默认定义了以下几个日志等级

| 日志等级（level） | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| DEBUG             | 最详细的日志信息，典型应用场景是 问题诊断                    |
| INFO              | 信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作 |
| WARNING           | 当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的 |
| ERROR             | 由于一个更严重的问题导致某些功能不能正常运行时记录的信息     |
| CRITICAL          | 当发生严重错误，导致应用程序不能继续运行时记录的信息         |

> `logging`允许开发人员自定义其他日志级别,但是这是不被推荐的，尤其是在开发供别人使用的库时，因为这会导致日志级别的混乱。

上面列表中的日志等级是从上到下依次升高的

`DEBUG < INFO < WARNING < ERROR < CRITICAL`

当为某个应用程序指定一个日志级别后，应用程序会记录所有日志级别大于或等于指定日志级别的日志信息。

### 使用方式

`logging`模块提供了两种记录日志的方式

- 第一种方式是使用logging提供的模块级别的函数
- 第二种方式是使用Logging日志系统的四大组件

#### logging模块定义的模块级别的常用函数

| 函数                                   | 说明                                 |
| -------------------------------------- | ------------------------------------ |
| logging.debug(msg, *args, **kwargs)    | 创建一条严重级别为DEBUG的日志记录    |
| logging.info(msg, *args, **kwargs)     | 创建一条严重级别为INFO的日志记录     |
| logging.warning(msg, *args, **kwargs)  | 创建一条严重级别为WARNING的日志记录  |
| logging.error(msg, *args, **kwargs)    | 创建一条严重级别为ERROR的日志记录    |
| logging.critical(msg, *args, **kwargs) | 创建一条严重级别为CRITICAL的日志记录 |
| logging.log(level, *args, **kwargs)    | 创建一条严重级别为level的日志记录    |
| logging.basicConfig(**kwargs)          | 对root logger进行一次性配置          |

其中`basicConfig`函数用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信。

其他几个都是用于记录各个级别日志的函数。

#### logging模块的四大组件

| 组件       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| loggers    | 提供应用程序代码直接使用的接口                               |
| handlers   | 用于将日志记录发送到指定的目的位置                           |
| filters    | 提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略） |
| formatters | 用于控制日志信息的最终输出格式                               |

> logging模块提供的模块级别的那些函数实际上也是通过这几个组件的相关实现类来记录日志的，只是在创建这些类的实例时设置了一些默认值。

## 使用

分别输出一条不同日志级别的日志记录

```python
import logging

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
```

也可以这样写：

```python
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
```

输出

```sh
WARNING:root:This is a warning log.
ERROR:root:This is a error log.
CRITICAL:root:This is a critical log.
```

### 输出分析

#### 日志级别

logging模块提供的日志记录函数所使用的日志器设置的日志级别是`WARNING`

因此只有`WARNING`级别的日志记录以及大于它的`ERROR`和`CRITICAL`级别的日志记录被输出了，而小于它的`DEBUG`和`INFO`级别的日志记录被丢弃了。

#### 输出格式

```sh
# 日志级别:日志器名称:日志内容
WARNING:root:This is a warning log.
# 默认的 格式字符串为 BASIC_FORMAT
"%(levelname)s:%(name)s:%(message)s"
```

#### 输出目标

logging模块提供的日志记录函数所使用的日志器设置的处理器所指定的日志输出位置默认为: `sys.stderr`。

### 格式化输出

#### *arg

如果要记录的日志中包含变量数据，可使用一个格式字符串作为这个事件的描述消息，然后将变量数据作为第二个参数`*args`的值进行传递，如:

```python
logging.warning('%s is %d years old.', 'Tom', 10)
# output WARNING:root:Tom is 10 years old.
```

#### **kwarg

它们支持3个关键字参数: `exc_info, stack_info, extra`

- ***exc_info：*** 其值为布尔值，如果该参数的值设置为True，则会将异常异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中。
- ***stack_info：*** 其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中。
- ***extra：*** 这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突。

### 配置

当我们没有提供任何配置信息的时候，函数都会去调用`logging.basicConfig(**kwargs)`方法，且不会向该方法传递任何参数。

更改配置 需要手动调用 `basicConfig()`方法

> `logging.basicConfig()`函数是一个 **一次性** 的简单配置工具使
>
> 也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。

 `basicConfig()` 参数说明

| 参数名称 | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| filename | 指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了 |
| filemode | 指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效 |
| format   | 指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。 |
| datefmt  | 指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效 |
| level    | 指定日志器的日志级别                                         |
| stream   | 指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 `ValueError`异常 |
| style    | Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%' |
| handlers | Python  3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root  logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。 |

其中format 中定义好的可用字符串：

| 字段/属性名称   | 使用格式            | 描述                                                         |
| --------------- | ------------------- | ------------------------------------------------------------ |
| asctime         | %(asctime)s         | 日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896 |
| created         | %(created)f         | 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值 |
| relativeCreated | %(relativeCreated)d | 日志事件发生的时间相对于logging模块加载时间的相对毫秒数      |
| msecs           | %(msecs)d           | 日志事件发生事件的毫秒部分                                   |
| levelname       | %(levelname)s       | 该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'） |
| levelno         | %(levelno)s         | 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）         |
| name            | %(name)s            | 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger |
| message         | %(message)s         | 日志记录的文本内容，通过 `msg % args`计算得到的              |
| pathname        | %(pathname)s        | 调用日志记录函数的源码文件的全路径                           |
| filename        | %(filename)s        | pathname的文件名部分，包含文件后缀                           |
| module          | %(module)s          | filename的名称部分，不包含后缀                               |
| lineno          | %(lineno)d          | 调用日志记录函数的源代码所在的行号                           |
| funcName        | %(funcName)s        | 调用日志记录函数的函数名                                     |
| process         | %(process)d         | 进程ID                                                       |
| processName     | %(processName)s     | 进程名称，Python 3.1新增                                     |
| thread          | %(thread)d          | 线程ID                                                       |
| threadName      | %(thread)s          | 线程名称                                                     |

```python
logging.basicConfig(filename="log.log", filemode='a', \
    format=r"[%(levelname)s][%(asctime)s][P:%(process)d_%(processName)s][T:%(thread)d]\n"\
    "in %(pathname)s::%(module)s:%(lineno)d, FUNC: %(funcName)s \n"\
    "\n%(message)s")
```

## 处理流程

### 四大组件

| 组件名称 | 对应类名  | 功能描述                                                     |
| -------- | --------- | ------------------------------------------------------------ |
| 日志器   | Logger    | 提供了应用程序可一直使用的接口                               |
| 处理器   | Handler   | 将logger创建的日志记录发送到合适的目的输出                   |
| 过滤器   | Filter    | 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录 |
| 格式器   | Formatter | 决定日志记录的最终输出格式                                   |

- 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
- 不同的处理器（handler）可以将日志输出到不同的位置；
- 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
- 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
- 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。

> 日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

## 模块

### Logger

- 向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息；
- 基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；
- 将日志消息传送给所有感兴趣的日志handlers。

#### 配置方法

| 方法                                          | 描述                                       |
| --------------------------------------------- | ------------------------------------------ |
| Logger.setLevel()                             | 设置日志器将会处理的日志消息的最低严重级别 |
| Logger.addHandler() 和 Logger.removeHandler() | 为该logger对象添加 和 移除一个handler对象  |
| Logger.addFilter() 和 Logger.removeFilter()   | 为该logger对象添加 和 移除一个filter对象   |

#### 创建日志记录

| 方法                                                         | 描述                                              |
| ------------------------------------------------------------ | ------------------------------------------------- |
| Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical() | 创建一个与它们的方法名对应等级的日志记录          |
| Logger.exception()                                           | 创建一个类似于Logger.error()的日志消息            |
| Logger.log()                                                 | 需要获取一个明确的日志level参数来创建一个日志记录 |

#### 实例化

* 通过Logger类的实例化方法创建一个Logger类的实例

* 通过 logging.getLogger()方法，方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为'root'。若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。

#### 层级结构与有效等级

logger的名称是一个以`.`分割的层级结构，每个`.`后面的logger都是`.`前面的logger的children，

child loggers在完成对日志消息的处理后，默认会将日志消息传递给与它们的祖先loggers相关的handlers。

### Handler

| 方法                                          | 描述                                        |
| --------------------------------------------- | ------------------------------------------- |
| Handler.setLevel()                            | 设置handler将会处理的日志消息的最低严重级别 |
| Handler.setFormatter()                        | 为handler设置一个格式器对象                 |
| Handler.addFilter() 和 Handler.removeFilter() | 为handler添加 和 删除一个过滤器对象         |

为Handler是一个基类，它只定义应有的接口。同时提供了一些子类可以直接使用或覆盖的默认行为。

下面是一些常用的Handler：

| Handler                                   | 描述                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| logging.StreamHandler                     | 将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。 |
| logging.FileHandler                       | 将日志消息发送到磁盘文件，默认情况下文件大小会无限增长       |
| logging.handlers.RotatingFileHandler      | 将日志消息发送到磁盘文件，并支持日志文件按大小切割           |
| logging.hanlders.TimedRotatingFileHandler | 将日志消息发送到磁盘文件，并支持日志文件按时间切割           |
| logging.handlers.HTTPHandler              | 将日志消息以GET或POST的方式发送给一个HTTP服务器              |
| logging.handlers.SMTPHandler              | 将日志消息发送给一个指定的email地址                          |
| logging.NullHandler                       | 该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。 |



### Formater

Formater对象用于配置日志信息的最终顺序、结构和内容。

应用代码可以直接实例化Formatter类

如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。

Formatter类的构造方法定义如下：

```
logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
```

可见，该构造方法接收3个可选参数：

- fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
- datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
- style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'

### Filter

Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤。该类定义如下：

```
class logging.Filter(name='')
    filter(record)
```

比如，一个filter实例化时传递的name参数值为'A.B'，那么该filter实例将只允许名称为类似如下规则的loggers产生的日志记录通过过滤：'A.B'，'A.B,C'，'A.B.C.D'，'A.B.D'，而名称为'A.BB', 'B.A.B'的loggers产生的日志则会被过滤掉。如果name的值为空字符串，则允许所有的日志事件通过过滤。

filter方法用于具体控制传递的record记录是否能通过过滤，如果该方法返回值为0表示不能通过过滤，返回值为非0表示可以通过过滤。

## 处理流程

![img](https://images2015.cnblogs.com/blog/1063221/201705/1063221-20170511145312144-488305597.png)