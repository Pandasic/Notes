# find

Linux find 命令用来在指定目录下查找文件。任何位于参数之前的字符串都将被视为欲查找的目录名。如果使用该命令时，不设置任何参数，则 find  命令将在当前目录下查找子目录与文件。并且将查找到的子目录和文件全部进行显示。

```sh
find path -option [ -print ]   [ -exec -ok command]   {} \;
```

expression最常用的参数

- -mount, -xdev : 只检查和指定目录在同一个文件系统下的文件，避免列出其它文件系统中的文件
- -amin n : 在过去 n 分钟内被读取过
- -anewer file : 比文件 file 更晚被读取过的文件
- -atime n : 在过去n天内被读取过的文件
- -cmin n : 在过去 n 分钟内被修改过
- -cnewer file :比文件 file 更新的文件
- -ctime n : 在过去n天内被修改过的文件
- -empty : 空的文件-gid n or -group name : gid 是 n 或是 group 名称是 name
- -ipath p, -path p : 路径名称符合 p 的文件，ipath 会忽略大小写
- -name name, -iname name : 文件名称符合 name 的文件。iname 会忽略大小写
- -size n : 文件大小 是 n 单位，b 代表 512 位元组的区块，c 表示字元数，k 表示 kilo bytes，w 是二个位元组。

- -type c : 文件类型是 c 的文件。

  - d: 目录

  - c: 字型装置文件

  - b: 区块装置文件

  - p: 具名贮列

  - f: 一般文件

  - l: 符号连结

  - s: socket

- -pid n : process id 是 n 的文件

使用 ( ) 将运算式分隔，并使用下列运算。

- exp1 -and exp2
- ! expr
- -not expr
- exp1 -or exp2
- exp1, exp2