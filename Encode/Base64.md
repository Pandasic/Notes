# Base64

> https://zhuanlan.zhihu.com/p/339477329

base64不是加密算法，他只是一种编码方式

## 字符集

Base64 是A-Z、a-z、数字0-9、符号"+"、"/"一共64个字符的字符集。

| 数值  | 字符 |
| ----- | ---- |
| 0-25  | A-Z  |
| 26-50 | a-z  |
| 52-61 | 0-9  |
| 62-63 | + /  |



## 转换

初始值 -> 二进制序列 6位一组(不足6位 低位补0) ->每6位组成一个新的字节，高位补00 组成二进制序列 -> 依据对应表进行映射

eg:

abc --ascii-> 

01100001 01100010 01100011 --6位编码--> 

00 011000 00 010110 00 001001 00 100011 -- 64 位置索引 -> 

24 22 9 35 --映射-> YWJj

 因为高位补0，所以base64会比原字符串更长。

若最后结果不是4的倍数，在末尾补充=



