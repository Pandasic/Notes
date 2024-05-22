---
title: ssh 远程登陆
tag: [计算机课程学习,Linux,常用命令,]
---
# SSH 远程登陆与配置

> 参考 https://www.jianshu.com/p/1e793e386beb

ssh 是一种网络协议，用于计算机之间的加密登陆。

## 基本用法

使用用户登陆远程主机

```sh
ssh user@host
```

如果本地与远程用户名一直 则省略用户名

```
ssh host
```

ssh端口默认是22 使用-p 参数修改端口

```sh
ssh -p port user@host
```

## 公钥登陆

1. 在本地使用`ssh-keygen` 生成公钥id_rsa.pub和私钥id_rsa

2. 将生成的id_rsa.pub添加到服务器的.ssh文件夹下的authorized_key 中

3. 使用私钥登陆

    ```sh
    ssh usrname@ip -p port -i id_rsa
    ```

4. 配置本地文件

    ```
    Host 连接的主机的名称，可自定
        Hostname 远程主机的IP地址
        User 用于登录远程主机的用户名
        Port 用于登录远程主机的端口
        IdentityFile 本地的id_rsa的路径
    ```

    