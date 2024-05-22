# Pytest python测试框架

> 参考：https://learning-pytest.readthedocs.io/zh/latest/doc/test-function/parametrize.html

## 安装

```sh
pip install -U pytest
```

检查是否安装了正确的版本

```
pytest --version
```

## 运行

```sh
pytest test/test1.py
```

pytest 使用`.`表示成功，使用`F`表示失败

## 标记函数

默认情况下 pytest 会递归查找目录下所有以`test`开头或结尾的`python`脚本 并执行所有以`test`开始或结尾的函数与方法

### 执行特定的函数

1. 使用`::`标记

```sh
pytest testxxx.py::test_fun()
```

2. 使用 `-k`标识 模糊匹配

  ```sh
  pytest -k partname testxxx.py
  ```

   

3. 使用 `pytest.mark`标记

```python
@pytest.mark.finished
def testfunc1():
	pass

@pytest.mark.unfinished
def testfunc1():
	pass
```

使用`-m`来使用标记 每个函数可以打上不同的标记

```sh
pytest -m finished testxxx.py
pytest -m "finished and not merged"
```

## 跳过测试

 使用 `pytest.mark.skip`跳过测试

 ```python
 @pytest.mark.skip()
 def testfunc():
   pass
 
 # 制定忽略条件
 @pytest.mark.skip(judge,reason='...')
 def testfunc():
   pass
 
 ```

pytest 使用 `s` 表示测试被跳过（`SKIPPED`）

### 预见的错误

Pytest 使用 `pytest.mark.xfail` 实现预见错误功能：

```python
@pytest.mark.xfail(gen.__version__ < '0.2.0',
                   reason='not supported until v0.2.0')
def test_api():
    id_1 = gen.unique_id()
    id_2 = gen.unique_id()
    assert id_1 != id_2

```

pytest 使用 `x` 表示预见的失败（`XFAIL`）。

如果预见的是失败，但实际运行测试却成功通过，pytest 使用 `X` 进行标记（`XPASS`）


## 断言

`assert` 断言用于判断表达式是否为真

```python
assert a==b
```

## 捕捉异常

使用 `pytest.raises()`  进行异常捕获,判断是否如期抛出异常
通过异常捕获，我们可以保证程所有参数完整执行

```python
def test_raises():
  with pytest.raises(TypeError) as e:
    func()
  exec_msg = e.value.args[0]
  assert exec_msg == 'port type must be int'
```

## 参数化
在 pytest 中，使用 参数化测试，即每组参数都独立执行一次测试。
`pytest.mark.parametrize(argnames, argvalues)`
eg:
这里是一个密码长度的测试函数，其中参数名为 passwd，其可选列表包含三个值：
```python

@pytest.mark.parametrize('passwd',
                      ['123456',
                       'abcdefdfs',
                       'as52345fasdf4'])
def test_passwd_length(passwd):
    assert len(passwd) >= 8

@pytest.mark.parametrize('user, passwd',
                         [('jack', 'abcdefgh'),
                          ('tom', 'a123456a')])
def test_passwd_md5(user, passwd):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
    }
    import hashlib
    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]

@pytest.mark.parametrize('user, passwd',
                         [pytest.param('jack', 'abcdefgh', id='User<Jack>'),
                          pytest.param('tom', 'a123456a', id='User<Tom>')])
def test_passwd_md5_id(user, passwd):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
    }
    import hashlib
    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]
```
使用`-v`参数进行测试


## 固件

固件（Fixture）是一些函数，pytest 会在执行测试函数之前（或之后）加载运行它们。
我们可以利用固件做任何事情，其中最常见的可能就是数据库的初始连接和最后关闭操作。

使用`@pytest.fixture()` 定义固件
```python

@pytest.fixture()
def postcode():
    return '010'

def test_postcode(postcode):
    assert postcode == '010'

```

### 预处理与后处理

pytest 使用`yield` 将关键字分为预处理与后处理

eg:
模拟数据库连接与关闭
```python 
@pytest.fixture()
def db():
    print('Connection successful')

    yield

    print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'

```

执行时使用 `-s` 阻止消息被吞
如果想更细的跟踪固件执行，可以使用 `--setup-show` 选项：

同时支持 setup 和teardown

* 模块级（setup_module/teardown_module）开始于模块始末
* 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
* 方法级（setup_method/teardown_method）开始于方法始末（在类中）
* 类里面的（setup/teardown）运行在调用方法的前后
* 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

```python
# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/2 19:41

import pytest


# 模块中的方法
def setup_module():
    print("setup_module：整个.py模块只执行一次")


def teardown_module():
    print("teardown_module：整个test_module.py模块只执行一次")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


# 测试模块中的用例1
def test_one():
    print("正在执行测试模块----test_one")
    x = "this"
    assert 'h' in x


# 测试模块中的用例2
def test_two():
    print("正在执行测试模块----test_two")
    x = "hello"
    assert hasattr(x, 'check')


# 测试类
class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup(self):
        print("setup：每个用例开始前都会执行")

    def teardown(self):
        print("teardown：每个用例结束后都会执行")

    def test_three(self):
        print("正在执行测试类----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行测试类----test_four")
        x = "hello"
        assert hasattr(x, 'check')


if __name__ == "__main__":
    pytest.main(["-s", "test_module.py"])
```

```css
test_module.py setup_module：整个.py模块只执行一次
setup_function：每个用例开始前都会执行
正在执行测试模块----test_one
.teardown_function：每个用例结束后都会执行
setup_function：每个用例开始前都会执行
正在执行测试模块----test_two
Fteardown_function：每个用例结束后都会执行
setup_class：所有用例执行之前
setup：每个用例开始前都会执行
正在执行测试类----test_three
.teardown：每个用例结束后都会执行
setup：每个用例开始前都会执行
正在执行测试类----test_four
Fteardown：每个用例结束后都会执行
teardown_class：所有用例执行之后
teardown_module：整个test_module.py模块只执行一次
```

### 作用域

通过`scope` 参数声明作用域,默认为`function`

选项如下
* function: 函数级，每个测试函数都会执行一次固件；
* class: 类级别，每个测试类执行一次，所有方法都可以使用；
* module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
* session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。

对于类使用作用域，需要使用 `pytest.mark.usefixtures` （对函数和方法也适用）：

```python
@pytest.mark.usefixtures('class_scope')
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass
```

## 报告

```bash
# 生成xml格式的报告
pytest -v test_1.py --junitxml=Path

# 生成txt格式的报告
pytest -v test_1.py --resultlog=Path

# 生成html格式的报告
# 需预先装上pytest-html
pip install pytest_html
pytest -v test_1.py --html=Path
```

## 日志

python里提供日志功能的标准模块就是logging

正常用法就是我们需要用logging模块创建logger, 然后为logger配置handler让日志output到哪里，当然你还需要定制化日志信息格式（时间，代码位置等）去创建format。

在pytest中你就无需做这些事了，只要在pytest.ini配置好logging信息就行了

```text
log_cli = 1
log_cli_level = DEBUG
log_cli_date_format = %Y-%m-%d-%H-%M-%S
log_cli_format = %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s
log_file = test.log
log_file_level = DEBUG
log_file_date_format = %Y-%m-%d-%H-%M-%S
log_file_format = %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s
```