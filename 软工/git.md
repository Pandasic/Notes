---
title: git
tag: [计算机课程学习,软工,]
---
# git
## 工作区域
### 工作区（Working Directory）

指的当前目录所有的文件

### 版本库（Repository）

### 暂存区 

对于文件的修改与提交，先保存至暂存区

git commit 命令就是一次性将暂存区内的修改提交到分枝
## 基础命令
### 常用命令
#### git init 创建git仓库

```shell
git init
# 默认创建.git文件 并且默认是隐藏的
```

#### git diff 查看区别

#### git add 添加文件到仓库

```shell
git add filename
```

#### git commit 提交文件到仓库

```shell
git commit -m 'xxx'
```

-m  提交的说明

#### git log 查看文件提交的记录

```shell
git log
git log --pretty=online #内容单行显示
```

#### git reset 版本回退

```shell
git reset --hard HEAD^		#HEAD^ 代表回退到上一个版本
git reset --hard HEAD^^ 	#HEAD^^代表回退到上2个版本
git reset --hard HEAD~100	#HEAD~100 代表回退到上100个版本

git reset --hard #版本号不必写全 #回退到指定版本 可以是未来的版本
```

#### git reflog显示操作的记录

```shell
git reflog
```

#### git status 查看当前的状态

#### git 撤销修改

 git checkout -- file

把文件在工作区的修改全部撤销，这里有两种情况：

一种是自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

git reset Head <file> 撤销暂存区修改 放回工作区



从暂存区恢复工作区，

git resotre --worktree readme.txt

从master恢复暂存区 

git restore --staged readme.txt

从master同时恢复工作区和暂存区

git restore --source=HEAD --staged --worktree readme.txt



#### 删除文件 

rm filename

再用 git rm 在版本库里删除文件

#### git stash

```shell
git stash #可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作：

git stash list; #查看stash 的列表
git stash apply #恢复stash
git stash drop  #删除
git pop 		#恢复并删除

####多次stash 恢复
git stash apply stash@{0}
```

#### git 标签

```shell
#切换到 需要打标签的分支上
git tag <name>  #git tag 打上标签
git tag #查看标签

git tag -a 标签名 -m 指定说明文字

git show <标签名> #查看标签信息

#默认标签是打在最新提交的commit上的
#历史标签 添加tag
git tag <tag name> <commit id>
```

### git 分支

#### 分支创建

```shell
git branch dev   #创建分支 dev 为分支名称
git checkout dev #切换分支 
git switch dev	#切换分支
#等同于
git switch -c dev
git checkout -b dev #创建并切换分支
```

```shell
git branch # 查看当前分支
git merge dev #合并分支
git branch -d #删除分支
```

#### 合并分支与冲突解决

当不同分支的 文件存在冲突时 无法执行快速合并 只能试图各自修改合并起来

Git 通过<<<<<<<`，`=======`，`>>>>>>> 标记出不同分支的内容 我们需要修改后再提交保存。

带参数的git log 可以查看分支的合并情况

### git远程

#### git clone 远程仓库克隆
git clone顾名思义就是将其他仓库克隆到本地，包括被clone仓库的版本变化
```
git clone 远程仓库地址
```
git clone的用法：
```shell
$ git clone 版本库的url
例如克隆TensorFlow：
$ git clone https://github.com/tensorflow/tensorflow.git
或者使用SSH协议：

$ git clone git@github.com:tensorflow/tensorflow.git

该目录与远程仓库不同名。

$ git clone 版本库的网址  本地目录名
```

#### git pull

git pull是拉取远程分支更新到本地仓库的操作，git pull是相当于从远程仓库获取最新版本，然后再与本地分支merge（合并）

```git pull = git fetch + git merge```

##### git pull的用法：

```
$ git pull &lt;远程主机名&gt; &lt;远程分支名&gt;:&lt;本地分支名&gt;
```

举例：将远程主机origin的master分支拉取过来，与本地的branchtest分支合并。

```sh
$ git pull origin master:branchtest
```

如果将冒号和后面的branchtest去掉，则表示将远程origin仓库的master分支拉取下来与本地**当前分支**合并。
以上的git pull操作如果用git fetch来表示：

```sh
$ git fetch origin master:brantest
$ git merge brantest
```

#### git fetch 更新远程代码到本地仓库

理解 fetch 的关键, 是理解 FETCH_HEAD，FETCH_HEAD指的是: 某个branch在服务器上的最新状态’。这个列表保存在 .Git/FETCH_HEAD 文件中, 其中每一行对应于远程服务器的一个分支。
当前分支指向的FETCH_HEAD, 就是这个文件第一行对应的那个分支.
一般来说, 存在两种情况:

- 如果没有显式的指定远程分支, 则远程分支的master将作为默认的FETCH_HEAD
- 如果指定了远程分支, 就将这个远程分支作为FETCH_HEAD

**git fetch更新本地仓库的两种用法：**

```sh
# 方法一
$ git fetch origin master                #从远程的origin仓库的master分支下载代码到本地的origin maste
$ git log -p master.. origin/master      #比较本地的仓库和远程参考的区别
$ git merge origin/master                #把远程下载下来的代码合并到本地仓库，远程的和本地的合并
# 方法二
$ git fetch origin master:temp           #从远程的origin仓库的master分支下载到本地并新建一个分支temp
$ git diff temp                          #比较master分支和temp分支的不同
$ git merge temp                         #合并temp分支到master分支
$ git branch -d temp                     #删除temp
```

### git push 向远程推送

```sh
git push <远程主机名> <本地分支名>:<远程分支名>
#远程分支与本地分支名称相同可省略
git push <远程主机名> <本地分支名>
#如果本地版本与远程版本有差异，但又要强制推送可以使用 --force 参数
git push --force origin master
#删除主机的分支 可以用--delete参数
git push origin --delete master
```

##### push 错误

* refusing to update checked out branch

  这是由于git默认拒绝了push操作，需要进行设置，修改.git/config文件后面添加如下代码：

  ```
  [receive]
  	denyCurrentBranch = ignore
  ```

* 无法查看push后的git中文件的原因与解决方法

  * 在初始化远程仓库时最好使用

  ```sh
  git --bare init
  ```

  > 如果使用了git init初始化，则远程仓库的目录下，也包含work tree，当本地仓库向远程仓库push时,  如果远程仓库正在push的分支上（如果当时不在push的分支，就没有问题）, 那么push后的结果不会反应在work tree上, 也即在远程仓库的目录下对应的文件还是之前的内容，必须得使用git reset –hard才能看到push后的内容.

  * 必须得使用命令 git reset --hard 才能看到push后的内容.

  * 登录到远程的那个文件夹，使用

    git config --bool core.bare true