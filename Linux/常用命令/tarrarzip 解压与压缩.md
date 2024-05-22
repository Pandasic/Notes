---
title: tarrarzip 解压与压缩
tag: [计算机课程学习,Linux,常用命令,]
---
# 解压与压缩

> 参考 
>
> https://blog.csdn.net/afei__/article/details/82619843
>
> http://linux.51yip.com/search/tar
>
> http://linux.51yip.com/search/rar
>
> http://linux.51yip.com/search/zip

## tar

  ```sh
  tar [主选项 + 辅选项] 文件或目录
  ```

| -z   | 使用 gzip 来压缩和解压文件                              |
| ---- | ------------------------------------------------------- |
| -v   | --verbose 详细的列出处理的文件                          |
| -f   | --file=ARCHIVE 使用档案文件或设备，这个选项通常是必选的 |
| -c   | --create 创建一个新的归档（压缩包）                     |
| -x   | 从压缩包中解出文件                                      |

```sh
# 压缩文件 file1 和目录 dir2 到 test.tar.gz
tar -zcvf test.tar.gz file1 dir2
# 解压 test.tar.gz（将 c 换成 x 即可）
tar -zxvf test.tar.gz
# 列出压缩文件的内容
tar -ztvf test.tar.gz 
```

## rar

```sh
# 压缩文件
rar a -r test.rar file
# 解压文件
unrar x test.rar
```

a : 添加到压缩文件

-r : 递归处理

x : 以绝对路径解压文件

## zip 命令

```
#压缩文件
zip -r test.zip file
#解压文件
unzip test.zip
```

-r : 递归处理