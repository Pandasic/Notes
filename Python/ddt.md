# ddt (数据驱动测试)

> 参考：https://ddt.readthedocs.io/en/latest/example.html

## 安装

```sh
pip install ddt
```

## 简介

DDT 有一个类装饰器 `ddt` [为测试用例类]和两个方法装饰器`data` [将参数作为数据给你的测试用例] , `file_data`[从JSON或YAML 文件中加载]。

## 使用

一般的来说，`data` 将 每一个数据 作为单一的参数作用于测试函数。

```python
@data([1,2,3])
def test_1(self,value):
  print(value)
```

> 将 [1,2,3] 作为一个整体 传入参数

```
output:

test_1_1__1__2__3_ (__main__.MyTesting) ... ok
test_compare_1__2__3_ (__main__.MyTesting) ... ERROR
[1, 2, 3]
```



可以使用额外的装饰器`unpack`，这个装饰器会自动地解包，将`tuple` `list`传入多个参数中，将 `dict`转化为多个带关键字的参数中

```python
@data([3,2,1],[5,3,2],[10,4,6])
@unpack
def test_minus(self,a,b,expected):
  actual = int(a) - int(b)
  expected = int(expected)
  self.assertEqual(actual, expected)
```

参数分解正确，分别传入

```
test_minus_1__3__2__1_ (__main__.MyTesting) ... ok
test_minus_2__5__3__2_ (__main__.MyTesting) ... ok
test_minus_3__10__4__6_ (__main__.MyTesting) ... ok
```

> unpack 将数据分解，再分别传入

反例

```python
@data([2,3],[4,5])
def test_compare(self,a,b):
  self.assertEqual(a,b)
```

因为这里没有添加`@unpack` 此时被理解为2组数据测试，但是`[2,3]`被整体传给了a

