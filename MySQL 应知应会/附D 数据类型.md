**串数据类型**

  数据类型|     说明
---|---
  CHAR      |   1\~255个字符的定长串。它的长度必须在创建时指定，否则MySQL假定为CHAR（1）
  ENUM     |    接受最多64K个串组成的一个预定义集合的某个串
  LONGTEXT    | 与TEXT相同，但最大长度为4GB
  MEDIUMTEXT|   与TEXT相同，但最大长度为16K SET接受最多64个串组成的一个预定义集合的零个或多个串
  TEXT      |   最大长度为64K的变长文本
  TINYTEXT     |与TEXT相同，但最大长度为255字节
  VARCHAR |     长度可变，最多不超过255字节。如果在创建时指定为VARCHAR（n），则可存储0到n个字符的变长串（其中n≤255）

**数值数据类型**

  类型           |     说明
  ---|---
  BIT              |   位字段，1\~64位。（在MySQL5之前，BIT在功能上等价于TINYINT
  BIGINT      |        整数值，支持-9223372036854775808\~-923372036854775807（如果是UNSIGNED，为0\~18446744073709551615）的数
  BOOLEAN（或B00L）|   布尔标志，或者为0或者为1，主要用于开/关（on/off）标志
  DECIMAL（或DEC）|    精度可变的浮点值
  DOUBLE |             双精度浮点值
  FLOAT     |          单精度浮点值
  INT（或INTEGER） |   整数值，支持-2147483648\~2147483647（如果是UNSIGNED，为0\~4294967295）的数
  MEDIUMINT         |  整数值，支持-8388608\~8388607（如果是UNSIGNED，为0\~16777215）的数
  REAL      |          4字节的浮点值
  SMALLINT        |    整数值，支持-32768\~32767（如果是UNSIGNED，为0～65535）的数
  TINYINT      |       整数值，支持-128\~127（如果为UNSIGNED，为0\~255）的数

货币存储一般用DECIMAL(8,2)

**二进制存储**

  数据类型   |  说明
  ---|---
  BLOB         |Blob最大长度为64KB
  MEDIUMBLOB|   Blob最大长度为16MB
  LONGBLOB    | Blob最大长度为4GB
  TINYBLOB     |Blob最大长度为255字节