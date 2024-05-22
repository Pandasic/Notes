# DataFaker 测试数据生成

> 知乎简介：https://zhuanlan.zhihu.com/p/94339692
>
> github ： https://github.com/gangly/datafaker

![preview](img/datafaker/v2-a4a8b9703a0e0425515c731c4b8b550b_r.jpg)

## 需求背景

- 后端开发新建表后，需要构造数据库测试数据，生成接口数据提供给前端使用--开发mock数据
- 数据库性能测试生成大量测试数据，测试数据库性能--性能mock数据
- 流数据测试针对kafka流数据，需要不断定时生成测试数据写入kafka--kafka流式数据mock

### 手工弊端

- 浪费工时  针对表的不同数据类型的字段，需要构造不同数据

- 数据量小 如果需要构造大量数据，手动造数据无能为力

- 不够准确 比如需要构造邮箱（满足一定格式），电话号码（确定的数字位数），ip地址（固定格式），年龄（不能为负数，有大小范围）等。这些测试数据有一定的限制或规律，手工构造可能不能满足数据范围或一些格式要求而导致后端程序报错

- 多表关联 手动造的数据量较小，在多个表中用主键不一定能关联上，或者关联出来没数据

- 动态随机写入 比如针对流数据，需要随机每隔几秒钟写入kafka。或者动态随机插入mysql，手工操作相对麻烦，而且不好统计写入数据条数

### datafaker 功能

一个多数据源测试数据构造工具

- 多种数据类型：包括常见数据库字段类型（整型、浮点型、字符型）、自定义类型（IP地址，邮箱，身份证号码等）
- 模拟多表关联数据：通过制定某些字段为枚举类型（从指定的数据列表里面随机选择），这样在数据量多的情况下能保证多表Join能关联上，查询到数据
-  支持批数据和流数据生成，可指定数据产生间隔时间；
-  支持多种数据输出方式，包括屏幕打印、文件和远程数据源；
-  支持多种数据源。目前支持关系型数据库、Hive、Kafka、Hbase、ES。后面将扩展到Mongo，Kudu等数据源；
-  可指定输出格式，目前支持text，json。

## 安装

```
pip install datafaker
```

## 使用

### 命令行参数

datafaker参数包含4个必选参数和一些可选参数，如下表所示

| 参数名     | 含义                       | 参数类型 | 是否必选 | 默认值 | 备注                                                         |
| ---------- | -------------------------- | -------- | -------- | ------ | ------------------------------------------------------------ |
| dbtype     | 数据源类型                 | string   | 是       | 无     | 可选值为 rdb,mysql,hive, kafka, hbase, es, file              |
| connect    | 数据源连接信息             | string   | 是       | 无     | 关系型数据库和hive为 sqlachemy的连接串 kafka为broker连接串 file为文件路径 hbase为thrift host和端口 |
| table      | 表名                       | string   | 是       | 无     | 将各种数据源操作单位都抽象为表，数据库中为表，kafka中为topic，file为文件名，hbase为表，es为索引和type，mongo为集合 |
| num        | 数据条数                   | int      | 是       | 无     |                                                              |
| auth       | 账号密码                   | string   | 否       | 无     | 数据源的账号密码，以:分隔，例如 admin:12334                  |
| meta       | 元数据文件                 | string   | 否       | 无     | 若设定该参数，则忽略从数据源连接信息中读取远数据             |
| metaj      | 元数据文件                 | string   | 否       | 无     | 自定义数据结构（一般用于json嵌套），metaj优先于meta参数      |
| interval   | 流数据产生间隔             | float    | 否       | 1      | 单位秒                                                       |
| version    | 显示版本号                 | bool     | 否       | 无     |                                                              |
| outprint   | 是否在屏幕打印             | bool     | 否       | false  | 若设置屏幕打印，则数据不会写文件或数据源                     |
| outspliter | 数据字段分割符             | string   | 否       | ,      | 屏幕打印，保存文件有效                                       |
| locale     | 语言类型                   | string   | 否       | zh_CN  | 支持多国语言，en_US， zh_CN                                  |
| format     | 数据格式                   | string   | 否       | text   | kafka 默认为json                                             |
| withheader | 打印和存储到文件是否带表头 | bool     | 否       | False  |                                                              |
| batch      | 每次批量写入数据源大小     | int      | 否       | 1000   |                                                              |
| workers    | 生成测试数据的线程数       | int      | 否       | 4      |                                                              |