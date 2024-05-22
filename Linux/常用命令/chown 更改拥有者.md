---
title: chown 更改拥有者
tag: [计算机课程学习,Linux,常用命令,]
---
# Linux chown

**命令 :**

```SH
chown [-cfhvR] [--help] [--version] user[:group] file...
```


**功能 :** 更改文件或者文件夹的拥有者
**参数格式 :**
 　    user : 新的档案拥有者的使用者 IDgroup : 新的档案拥有者的使用者群体(group)
 　       -c : 若该档案拥有者确实已经更改，才显示其更改动作
 　       -f : 若该档案拥有者无法被更改也不要显示错误讯息
 　       -h : 只对于连结(link)进行变更，而非该 link 真正指向的档案
 　       -v : 显示拥有者变更的详细资料
        　-R : 对目前目录下的所有档案与子目录进行相同的拥有者变更(即以递回的方式逐个变更)
 **例如：** chown -R oracle:oinstall /oracle/u01/app/oracle
 更改目录拥有者为oracle
链接：https://www.jianshu.com/p/49908a4c6fd0

