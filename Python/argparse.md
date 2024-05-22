# argparse 命令行解析

> 参考：https://docs.python.org/zh-cn/3/howto/argparse.html
>
> https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse

## 参数解析函数

ArgumentParser 通过 parse_args() 方法解析参数。

```
parser.parse_args(:list)
```

> 在脚本中，通常 parse_args() 会被 **不带参数** 调用，而 ArgumentParser 将自动从 sys.argv 中确定命令行参数。

## 位置参数

### 添加位置参数

位置参数通过 `add_argument()`方法传入，用于指定接受的命令行选项。

```python
# 模块包含
import argparse

# 创建解析器
parser = argparse.ArgumentParser()

# 添加位置参数
parser.add_argument("echo")

# 获得解析结果
args = parser.parse_args()

# 输出调用
print(args.echo)
```

### 添加 help 说明

使用 `add_argument`的`help`参数

```python
parser.add_argument("echo", help="echo the string you use here")
```

### 指定参数类型

使用 `add_argument`的`type`参数

```python
parser.add_argument("square", help="display a square of a given number",type=int)
```

### 限制选项

使用 `add_argument`的`choice`参数，可以使参数进行参数数量的限制

```python
parser.add_argument("square", help="display a square of a given number",type=int,choices=[0, 1, 2])
```

###  指定所返回对象上的属性名

使用 `add_argument`的`dest`参数，可以重命名返回结果集的属性名称

```python
args = parser.add_argument("square", dest = 's')
print(args.s)
```

### 命令行参数应当消耗的数目

ArgumentParser 对象通常关联一个单独的命令行参数到一个单独的被执行的动作。 `nargs` 命名参数关联不同数目的命令行参数到单一动作。支持的值有：

- `N` （一个整数）。命令行中的 `N` 个参数会被聚集到一个列表中。

  注意 `nargs=1` 会产生一个单元素列表。这和默认的元素本身是不同的。

- `'?'`。如果可能的话，会从命令行中消耗一个参数，并产生一个单一项。如果当前没有命令行参数，则会产生 [default](https://docs.python.org/zh-cn/3/library/argparse.html#default) 值。

  注意，对于选项，有另外的用例 - 选项字符串出现但没有跟随命令行参数，则会产生 [const](https://docs.python.org/zh-cn/3/library/argparse.html#const) 值。一些说用用例:

  `nargs='?'` 的一个更普遍用法是允许可选的输入或输出文件:

- `'*'`。所有当前命令行参数被聚集到一个列表中。注意通过 `nargs='*'` 来实现多个位置参数通常没有意义，但是多个选项是可能的。例如:

  ```sh
  parser = argparse.ArgumentParser()
  
  parser.add_argument('--foo', nargs='*')
  parser.add_argument('--bar', nargs='*')
  parser.add_argument('baz', nargs='*')
  
  parser.parse_args('a b --foo x y --bar 1 2'.split())
  Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
  ```

- `'+'`。和 `'*'` 类似，所有当前命令行参数被聚集到一个列表中。另外，当前没有至少一个命令行参数时会产生一个错误信息

如果不提供 `nargs` 命名参数，则消耗参数的数目将被 [action](https://docs.python.org/zh-cn/3/library/argparse.html#action) 决定。通常这意味着单一项目（非列表）消耗单一命令行参数。

## 可选参数

### 添加与使用可选参数

添加 形如 `-s` 或者 `--set`的参数 视为可选参数。

使用时，`parse_args()` 返回 去掉前置`-`的值

当一个可选参数 未被使用则被赋值为None

使用 `--verbosity`时 必须指定一个值，可以是任意值

```python
parser.add_argument("--verbosity", help="increase output verbosity")

args = parser.parse_args()
print(args.verbose)
```

### 仅作为标志使用

新的关键词 `action`，并赋值为 `"store_true"`。这意味着，当这一选项存在时，为 `args.verbose` 赋值为 `True`。没有指定时则隐含地赋值为 `False`。

```python
arser.add_argument("--verbose", help="increase output verbosity", action="store_true")
```

当你为其指定一个值时，它会报错，符合作为标志的真正的精神。

### 统计选项出现次数

```python
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
```

```sh
python3 test.py -vvvv #4
python3 test.py -vvvv --verbose #5
```

当你为其指定一个值时，它会报错。如果你不添加 `-v` 标志，这一标志的值会是 `None`

### 多参数的追加列表

`'append'` - 存储一个列表，并且将每个参数值追加到列表中。在允许多次使用选项时很有用(默认为 ‘store’ 储存/覆盖)

```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')
parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['1', '2']
```

### 短选项

为可选项添加短选项

```python
parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
```

### 默认值

使用 `add_argument`的`default`参数,在参数未被指定的时候更改默认值 为指定 而非原本的 None

```python
parser.add_argument("-v", "--verbosity", action="count",
                  	default=0,help="increase output  verbosity")
```

## 互斥参数组

```python
# 原本参数
arser = argparse.ArgumentParser(description="calculate X to the power of Y")
# 互斥参数组
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
```

## --help 参数

在未指定任何选项时，argparse 也拥有`--help` 选项，也可缩写为 `-h`。这是唯一一个可以直接使用的选项。指定任何内容都会导致错误。

## 子命令

`ArgumentParser` 通过 `add_subparsers()` 方法支持创建这样的子命令。

```python
import argparse
# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
# 通过添加 dest 在最后结果中 获取子命令名称
subparsers = parser.add_subparsers(dest = "sub_cmd",help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# parse some argument lists
parser.parse_args()
```

```sh
# help 输出如下
usage: PROG [-h] [--foo] {a,b} ...

positional arguments:
  {a,b}   sub-command help
    a     a help
    b     b help

options:
  -h, --help  show this help message and exit
  --foo   foo help
```

## 传入文件输入 

`FileType` 工厂类用于创建可作为 ArgumentParser.add_argument() 的 type 参数传入的对象。 以 FileType 对象作为其类型的参数将使用命令行参数以所请求模式、缓冲区大小、编码格式和错误处理方式打开文件。可以参考open 函数