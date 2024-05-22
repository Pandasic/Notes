# unittest 单元测试框架

> 参考文章：https://docs.python.org/zh-cn/3.7/library/unittest.html

## 简介

* 测试脚手架

  test fixture 表示为了开展一项或多项测试做的准备

* 测试用例

  独立的测试单元，检查输入特定数据时的相应。unittest 提供基类 `TestCase` 用于新建测试用例

* 测试套件

  test suite 时一系列测试用例，或测试套件。用于归档要一起执行的测试

* 测试运行器

  执行和输出测试结果的组件。这个运行器可能使用图形接口、文本接口，或返回一个特定的值表示运行测试的结果。

## 基础用例

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

* 首先 继承 `unittest.TestCase` 就创建了一个测试样例.
* 三个独立的测试时三个类的方法，均以`test`开头。命名约定告诉测试运行者那些方法表示测试
*  `assertEqual()`检测预期输出
*  `assertTrue()`和`assertFalse()`验证条件
* `assertRaise()` 验证是否抛出异常
* 使用函数而不是 `assert`时为了聚合测试结果来产生报告。

通过 `setUp()`和 `tearDown()` 方法，可以设置测试开始前与完成后需要执行的指令。

最后 使用 `unittest.main()`运行该脚本，完成格式的输出。

## 命令行

通过命令行运行模块、类和独立测试方法的测试:

```sh
# 模块
python -m unittest test_module1 test_module2
# 类
python -m unittest test_module.TestClass
# 函数
python -m unittest test_module.TestClass.test_method
```

### 参数

* 使用`-v` 来输出详细信息。

* 不包含参数 开始探索性测试

  ```sh
  python -m unittest
  ```

* `-h` 获取选项列表

- `-b`, `--buffer`

  在测试运行时，标准输出流与标准错误流会被放入缓冲区。成功的测试的运行时输出会被丢弃；测试不通过时，测试运行中的输出会正常显示，错误会被加入到测试失败信息。

- `-c` `--catch`

  当测试正在运行时， Control-C 会等待当前测试完成，并在完成后报告已执行的测试的结果。当再次按下 Control-C 时，引发平常的 [`KeyboardInterrupt`](https://docs.python.org/zh-cn/3.7/library/exceptions.html#KeyboardInterrupt) 异常。 See [Signal Handling](https://docs.python.org/zh-cn/3.7/library/unittest.html#signal-handling) for the functions that provide this functionality.

- `-f`, `--failfast`

  当出现第一个错误或者失败时，停止运行测试。

- `-k`
  只运行匹配模式或子串的测试方法和类。可以多次使用这个选项，以便包含匹配子串的所有测试用例。 
  包含通配符（*）的模式使用`fnmatch.fnmatchcase()` 对测试名称进行匹配。大小写敏感的。
  模式对测试加载器导入的测试方法全名进行匹配。 

- 例如，`-k foo` 可以匹配到 
  
  `foo_tests.SomeTest.test_something`  和 `bar_tests.SomeTest.test_foo` 
  
  但是不能匹配到 `bar_tests.FooTest.test_something` 。
  
- `--locals`

  在回溯中显示局部变量。

## 探索性测试

`unittest`支持简单搜索。所有测试必须是`module` 或者 `packages` 包括 namespace packags 并从根目录导入

在 TestLoader.discover() ,也可以是命令行

```sh
cd project_directory
python -m unittest discover
```

- `-v`, ``--verbose`

  更详细地输出结果。

- `-s`, ``--start-directory` directory

  开始进行搜索的目录(默认值为当前目录 `.` )。

- `-p`, ``--pattern`` pattern

  用于匹配测试文件的模式（默认为 `test*.py` ）。

- `-t`, ``--top-level-directory`` directory

  指定项目的最上层目录（通常为开始时所在目录）。

> `-s` `-p`和 `-t` 选项可以按顺序作为位置参数传入

## 组织测试代码

### setUp tearDown 和 \_\_init\_\_

构建单位是 test case： 独立的 包含执行条件与正确性的执行条件。

我们可以把测试的前置操作从测试代码中拆解出来，并实现测试前置方法 `setUp()` 。在运行测试时，测试框架会自动地为每个单独测试调用前置方法。相似的，我们提供了一个 `tearDown()` 方法在测试方法运行后进行清理工作

若 `setUp()` 成功运行，无论测试方法是否成功，都会运行 `tearDown()` 

在测试运行时，若 `setUp()` 方法引发异常，测试框架会认为测试发生了错误，因此测试方法不会被运行。

运行每个测试时，`setUp()` 、`tearDown()` 和 `__init__()` 会被调用一次。

> \_\_init\_\_ 函数会在所有setUp 之前调用 该类里测试用例数量的次数

### 自定义测试套件

实现测试用的 `TestCase `实现集合起来。可以自定义套件来组织测试

```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

### 复用代码

unittest 提供 FunctionTestCase 类，用于打包已有函数，支持设置前置和后置函数。

如下两个方法是等价的

```python
def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...
```

```python
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)
```

### 跳过预计的失败

使用 `skip()`,`skipIf()`,`skipUnles()`装饰器来跳过函数，或者在 setUp 函数或测试模块中 使用 `skipTest`函数跳过， 或者直接引发 `SkipTest` 异常来跳过

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
```

跳过类的测试

```python
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

使用 `expectedFailure()` 装饰器表明这个测试预计失败。:

```
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```



- @unittest.skip(*reason*)

  跳过被此装饰器装饰的测试。 *reason*  为测试被跳过的原因。

- @unittest.skipIf(*condition*, *reason*)

  当 *condition* 为真时，跳过被装饰的测试。

- @unittest.skipUnless(*condition*, *reason*)

  跳过被装饰的测试，除非 *condition* 为真。

- @unittest.expectedFailure

  把测试标记为预计失败。如果测试不通过，会被认为测试成功；如果测试通过了，则被认为是测试失败。

- *exception* unittest.SkipTest(*reason*)

  引发此异常以跳过一个测试。
