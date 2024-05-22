# 虚拟环境

> virtualenv: https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480
>
> 官方文档： https://virtualenv.pypa.io/
>
> pipenv: https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html

## virtualenv

virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

### 安装

```sh
pip install virtualenv
```

### 使用

* 创建环境

```
virtualenv venv
```

`--system-site-package` 参数 使系统Python环境中的所有第三方包都复制过来

使用 `-p PYTHON_EXE` 指定python 版本



* 使用 `source`进入当前环境呢

```
source venv/bin/activate
```

* 退出当前环境

```
deactivate 
```

* 删除环境

```
rmvirtualenv venv
```

## pipenv

### 安装

```
pip install --user pipenv
```

> 这进行了 用户安装，以防止破坏任何系统范围的包。
>
> 如果安装后, shell 中没有 `pipenv`，则需要将 用户基础目录 的 二进制文件目录添加到 `PATH` 中。

### 使用

Pipenv 将在您的项目目录中安装超赞的 Requests 库并为您创建一个 Pipfile。`Pipfile` 用于跟踪您的项目中需要重新安装的依赖

```
pipenv install requests
```

运行

```
 pipenv run python main.py
```

` pipenv run` 可确保您的安装包可用于您的脚本。我们还可以生成一个新的 shell， 确保所有命令都可以使用 `$ pipenv shell` 访问已安装的包。
