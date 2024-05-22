---
title: gdb 的使用
tag: [计算机课程学习,C++,]
---
# gdb

##  启动调试

```sh
gdb [参数][文件]
```

| 参数 | 说明                               |
| :--- | ---------------------------------- |
| -cd  | 设置工作目录                       |
| -q   | 安静模式，不打印介绍信息和版本信息 |
| -d   | 添加文件查找路径                   |
| -x   | 从指定文件中执行GDB指令            |
| -s   | 设置读取的符号表文件               |

## 常用命令

| file <文件名> | 加载被调试的可执行程序文件                 |
| ------------- | ------------------------------------------ |
| run/r         | 重新开始运行文件                           |
| start/s       | 单步执行，运行程序，停在第一执行语句       |
| [list](#list) | 查看原代码                         |
| set           | 设置变量的值                               |
| next/n        | 单步调试（逐过程，函数直接执行）           |
| step/s        | 单步调试（逐语句：跳入自定义函数内部执行） |
| backtrace/bt  | 查看函数的调用的栈帧和层级关系     |
| frame/f       | 切换函数的栈帧                      |
| info/i        | 查看函数内部局部变量的数值          |
| finish        | 结束当前函数，返回到函数调用点             |
| continue/c    | 继续运行                            |
| print/p       | 打印值及地址,                      |
| quit/q        | 退出gdb                              |
|  whatis|打印类型|
|  ptype|打印类型详细信息|
| return |强制返回当前函数|
| [Enter]直接回车 |执行上一次命令|
| jump <n> |跳转到第n行，然后继续执行|
| call/print  <expr> |强制调用函数函数 ，print 会打印返回值|
| break/b |文件中设置某一行为断点|
| watch <expr> |检测表达式为真则停住|
| info break/info breakpoints |显示断电信息|
| delete N |删除N号断点|
| delete |删除所有断点|
| backtrace                   | 显示调用函数堆栈中的函数                   |
| show language |当前调试程序的语言(默认为C)|
| info frame |当前函数的语言|
| info source |当前调试的源程序|
| set language <language> |设置当前程序的语言|
| kill |中止调试|
| ||
| ||
| ||
| ||
| ||
| ||
| ||
| ||
| ||
| ||

## 命令细节

### list

```sh
(gdb) list n1 n2 
```

list可以简写为l,将会显示n1行和n2行之间的代码，如果使用-tui启动gdb，将会在相应的位置显示。

如果没有n1和n2参数，那么就会默认显示当前行和之后的10行，再执行又下滚10行。

另外，list还可以接函数名。 
一般来说在list后面可以跟以下这们的参数：

| 参数                | 说明                             |
| ------------------- | -------------------------------- |
| linenum           | 行号                             |
| +offset           | 当前行号的正偏移量               |
| -offset           | 当前行号的负偏移量               |
| filename:linenum  | 哪个文件的哪一行                 |
| function          | 函数名。                         |
| filename:function | 哪个文件中的哪个函数             |
| *address            | 程序运行时的语句在内存中的地址。 |

 ## break

```sh
(gdb)break n #设置第六行断点
(gdb)break n if expr #条件断点
(gdb)break func #函数断点
(gdb)break filename:func #文件函数设置断点
(gdb)delete N #删除N号断点
```

## print

```sh
print var #显示变量的值
```

```sh
print /x var #十六进制显示
```

* x 按十六进制格式显示变量。 
  d 按十进制格式显示变量。 
  u 按十六进制格式显示无符号整型。 
  o 按八进制格式显示变量。 
  t 按二进制格式显示变量。 
  a 按十六进制格式显示变量。 
  c 按字符格式显示变量。 
  f 按浮点数格式显示变量。 

```sh
print *a@10 #显示10个元素
```

```sh
print var = value #更改变量的值
```

