# setuptools

> 知乎 ：https://zhuanlan.zhihu.com/p/276461821

## 打包

打包，就是将你的源代码进一步封装，并且将所有的项目部署工作都事先安排好，这样使用者拿到后即装即用，不用再操心如何部署的问题

常用打包工具  `disutils`、 `distutils` 、`distutils2`、`setuptools`等等



## 安装

* 源码安装：在 [https://pypi.org/project/setuptools/#files](https://link.zhihu.com/?target=https%3A//pypi.org/project/setuptools/%23files) 中下载 zip 包 解压执行 `python setup.py install` 安装
* 通过引导程序安装：下载引导程序，它可以用来下载或者更新最新版本的 setuptools

```sh
wget http://peak.telecommunity.com/dist/ez_setup.py

# 安装
python ez_setup.py

# 更新，以下两种任选
python ez_setup.py –U setuptools
pip install -U setuptools
```



## 分法

两种分法方式

### 以源码包的形式发布

源码包安装的过程，是先解压，再编译，最后才安装，所以它是跨平台的



源码包的本质是一个压缩包

### 以二进制包形式发布

二进制包的安装过程省去了编译的过程，直接进行解压安装，所以安装速度较源码包来说更快。

由于不同平台的编译出来的包无法通用，所以在发布时，需事先编译好多个平台的包。常见格式为 `.egg`/`.whl`

## setup.py 编写

ex:

```python
from setuptools import setup, find_packages

setup(
    name="mytest",
    version="1.0",
    author="wangbm",
    author_email="wongbingming@163.com",
    description="Learn to Pack Python Module",

    # 项目主页
    url="http://iswbm.com/", 

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages()
)
```

### 分类信息

`classifiers` 参数说明包的分类信息。

所有支持的分类列表见：[https://pypi.org/pypi?%3Aaction=list_classifiers](https://link.zhihu.com/?target=https%3A//pypi.org/pypi%3F%3Aaction%3Dlist_classifiers)

```python
from setuptools import setup, find_packages

setup(
    classifiers = [
        # 发展时期,常见的如下
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 开发的目标用户
        'Intended Audience :: Developers',

        # 属于什么类型
        'Topic :: Software Development :: Build Tools',

        # 许可证信息
        'License :: OSI Approved :: MIT License',

        # 目标 Python 版本
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
```

### 文件的分发

```sh
from setuptools import setup, find_packages


setup(
    name="mytest",
    version="1.0",
    author="wangbm",
    author_email="wongbingming@163.com",
    description="Learn to Pack Python Module",
    url="http://iswbm.com/", 
    packages=find_packages(),

    # 安装过程中，需要安装的静态文件，如配置文件、service文件、图片等
    data_files=[
        ('', ['conf/*.conf']),
        ('/usr/lib/systemd/system/', ['bin/*.service']),
               ],

    # 希望被打包的文件
    package_data={
        '':['*.txt'],
        'bandwidth_reporter':['*.txt']
               },
    # 不打包某些文件
    exclude_package_data={
        'bandwidth_reporter':['*.txt']
               }
)
```

### MANIFEST.in

除了以上的参数配置之外，还可以使用一个叫做 `MANIFEST.in` 的文件，来控制文件的分发。

如下这是一个 `MANIFEST.in` 的样例：

```text
include *.txt
recursive-include examples *.txt *.py
prune examples/sample?/build
```

这些配置，规定了如下几点

- 所有根目录下的以 txt 为后缀名的文件，都会分发
- 根目录下的 examples 目录 和 txt、py文件都会分发
- 路径匹配上 examples/sample?/build 不会分发

`MANIFEST.in` 需要放在和 setup.py 同级的顶级目录下，setuptools 会自动读取该文件。

## **关于依赖包下载安装**

```python
from setuptools import setup, find_packages


setup(
    ...

    # 表明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    install_requires=['docutils>=0.3'],

    # setup.py 本身要依赖的包，这通常是为一些setuptools的插件准备的配置
    # 这里列出的包，不会自动安装。
    setup_requires=['pbr'],

    # 仅在测试时需要使用的依赖，在正常发布的代码中是没有用的。
    # 在执行python setup.py test时，可以自动安装这三个库，确保测试的正常运行。
    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],

    # 用于安装setup_requires或tests_require里的软件包
    # 这些信息会写入egg的 metadata 信息中
    dependency_links=[
        "http://example2.com/p/foobar-1.0.tar.gz",
    ],

    # install_requires 在安装模块时会自动安装依赖包
    # 而 extras_require 不会，这里仅表示该模块会依赖这些包
    # 但是这些包通常不会使用到，只有当你深度使用模块时，才会用到，这里需要你手动安装
    extras_require={
        'PDF':  ["ReportLab>=1.2", "RXP"],
        'reST': ["docutils>=0.3"],
    }
)
```

关于 `install_requires`， 有以下五种常用的表示方法：

1. `'argparse'`，只包含包名。 这种形式只检查包的存在性，不检查版本。 方便，但不利于控制风险。
2. `'setuptools==38.2.4'`，指定版本。 这种形式把风险降到了最低，确保了开发、测试与部署的版本一致，不会出现意外。 缺点是不利于更新，每次更新都需要改动代码。
3. `'docutils >= 0.3'`，这是比较常用的形式。 当对某个库比较信任时，这种形式可以自动保持版本为最新。
4. `'Django >= 1.11, != 1.11.1, <= 2'`，这是比较复杂的形式。 如这个例子，保证了Django的大版本在1.11和2之间，也即1.11.x；并且，排除了已知有问题的版本1.11.1（仅举例）。 对于一些大型、复杂的库，这种形式是最合适的。
5. `'requests[security, socks] >= 2.18.4'`，这是包含了额外的可选依赖的形式。 正常安装requests会自动安装它的`install_requires`中指定的依赖，而不会安装`security`和`socks`这两组依赖。 这两组依赖是定义在它的`extras_require`中。 这种形式，用在深度使用某些库时。

## 关于安装环境的限制

有些库并不是在所以的 Python 版本中都适用的，若一个库安装在一个未兼容的 Python 环境中，理论上不应该在使用时才报错，而应该在安装过程就使其失败，提示禁止安装。

这样的功能，可以使用 `python_requires` 来实现。

```text
setup(
    ...
    python_requires='>=2.7, <=3',
)
```

## 生成可执行文件的分发

```python
from setuptools import setup, find_packages


setup(
    name="mytest",
    version="1.0",
    author="wangbm",
    author_email="xxx@xxx.com",
    description="Learn to Pack Python Module",
    url="http://iswbm.com/", 
    packages=find_packages(),

    # 用来支持自动生成脚本，安装后会自动生成 /usr/bin/foo 的可执行文件
    # 该文件入口指向 foo/main.py 的main 函数
    entry_points={
        'console_scripts': [
            'foo = foo.main:main'
        ]
    },

    # 将 bin/foo.sh 和 bar.py 脚本，生成到系统 PATH中
    # 执行 python setup.py install 后
    # 会生成 如 /usr/bin/foo.sh 和 如 /usr/bin/bar.py
    scripts=['bin/foo.sh', 'bar.py']
)
```



上面的 scripts 里有的脚本中有 `sh` 和 `py` 后缀，那么安装后，setuptools 会原封不动的移动到 /usr/bin 中，并添加可执行权限。

若你想对这些文件再作一些更改，比如去掉多余的后缀，可以这样做

```python
from setuptools.command.install_scripts import install_scripts

class InstallScripts(install_scripts):

    def run(self):
        setuptools.command.install_scripts.install_scripts.run(self)

        # Rename some script files
        for script in self.get_outputs():
            if basename.endswith(".py") or basename.endswith(".sh"):
                dest = script[:-3]
            else:
                continue
            print("moving %s to %s" % (script, dest))
            shutil.move(script, dest)

setup(
    ...
    scripts=['bin/foo.sh', 'bar.py'],

    cmdclass={
        "install_scripts": InstallScripts
    }
)
```

## ext_modules

`ext_modules` 参数用于构建 C 和 C++ 扩展扩展包。其是 Extension 实例的列表，每一个 Extension 实例描述了一个独立的扩展模块，扩展模块可以设置扩展包名，头文件、源文件、链接库及其路径、宏定义和编辑参数等。如：

```text
setup(
    # other arguments here...
    ext_modules=[
        Extension('foo',
                  glob(path.join(here, 'src', '*.c')),
                  libraries = [ 'rt' ],
                  include_dirs=[numpy.get_include()])
    ]
)
```



详细了解可参考：[https://docs.python.org/3.6/distutils/setupscript.html#preprocessor-options](https://link.zhihu.com/?target=https%3A//docs.python.org/3.6/distutils/setupscript.html%23preprocessor-options)

## **指定release**

setup.py 里只能指定 version，而不能指定 release，如果你需要变更版本号，可以使用 `--release` 参数进行指定

```text
python setup.py bdist_rpm --release=20200617
```

## 参数总结

setup.py 的参数非常多，能够不借助文档写好一个setup.py好像没那么简单。为了备忘，我整理了 setup 函数常用的一些参数：

![img](https://pic3.zhimg.com/80/v2-4563e810d05ec25ce283c7f54a271e2e_1440w.jpg)

更多参数可见：[https://setuptools.readthedocs.io/en/latest/setuptools.html](https://link.zhihu.com/?target=https%3A//setuptools.readthedocs.io/en/latest/setuptools.html)

## 打包辅助神器PBR 是什么？

`pbr` 是 setuptools 的辅助工具，最初是为 OpenStack 开发

https://launchpad.net/pbr

`pbr` 会读取和过滤setup.cfg中的数据，然后将解析后的数据提供给 `setup.py` 作为参数。包含如下功能：

1. 从git中获取Version、AUTHORS and ChangeLog信息
2. Sphinx Autodoc。pbr 会扫描project，找到所有模块，生成stub files
3. Requirements。pbr会读取requirements.txt，生成setup函数需要的`install_requires/tests_require/dependency_links` 

这里需要注意，在 `requirements.txt` 文件的头部可以使用：`--index https://pypi.python.org/simple/`，这一行把一个抽象的依赖声明如 requests==1.2.0 转变为一个具体的依赖声明 requests 1.2.0 from pypi.python.org/simple/

1. long_description。从README.rst, README.txt or README file中生成`long_description`参数

使用pbr很简单：

```text
from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True,
)
```

使用pbr时，setup.cfg中有一些配置。在[files]中，有三个key：
`packages`:指定需要包含的包，行为类似于setuptools.find_packages
`namespace_packages`:指定namespace packages
`data_files`: 指定目的目录和源文件路径，一个示例：

```text
[files]
data_files =
    etc/pbr = etc/pbr/*
    etc/neutron =
        etc/api-paste.ini
        etc/dhcp-agent.ini
    etc/init.d = neutron.init
```

`[entry_points]` 段跟 setuptools 的方式相同。

到此，我讲了三种编写使用 setup.py 的方法

- 使用命令行参数指定，一个一个将参数传递进去（极不推荐）
- 在 setup.py 中的setup函数中指定（推荐使用）
- 使用 pbr ，在 setup.cfg 中指定（易于管理，更推荐）

## setup.py 构建包

1、构建源码发布包。

用于发布一个 Python 模块或项目，将源码打包成 tar.gz （用于 Linux 环境中）或者 zip 压缩包（用于 Windows 环境中）

```text
$ python setup.py sdist
```

那这种包如何安装呢`setuptools` 中提供的 `easy_install` 工具。

```text
$ easy_install xxx.tar.gz
```

使用 sdist 将根据当前平台创建默认格式的存档。在类 Unix 平台上，将创建后缀后为 `.tar.gz`  的 gzip 压缩的tar文件分发包，而在Windows上为 ZIP 文件。

当然，你也可以通过指定你要的发布包格式来打破这个默认行为

```text
$ python setup.py sdist --formats=gztar,zip
```

你可以指定的格式有哪些呢？

创建一个压缩的tarball和一个zip文件。可用格式为：

![img](https://pic2.zhimg.com/80/v2-7416d2c5ffd4fde928d7bd214ea59d39_1440w.jpg)



对以上的格式，有几点需要注意一下：

- 在版本3.5中才添加了对  `xztar` 格式的支持
- zip 格式需要你事先已安装相应的模块：zip程序或zipfile模块（已成为Python的标准库）
- ztar 格式正在弃用，请尽量不要使用

另外，如果您希望归档文件的所有文件归root拥有，可以这样指定

```text
python setup.py sdist --owner=root --group=root
```

2、构建二进制分发包。

在windows中我们习惯了双击 exe 进行软件的安装，Python 模块的安装也同样支持 打包成 exe 这样的二进制软件包。

```text
$ python setup.py bdist_wininst
```

而在 Linux 中，大家也习惯了使用 rpm 来安装包，对此你可以使用这条命令实现 rpm 包的构建

```text
$ python setup.py bdist_rpm
```

若你喜欢使用 easy_install 或者 pip 来安装离线包。你可以将其打包成 egg 包

```text
$ python setup.py bdist_egg
```



若你的项目，需要安装多个平台下，既有 Windows 也有 Linux，按照上面的方法，多种格式我们要执行多次命令，为了方便，你可以一步到位，执行如下这条命令，即可生成多个格式的进制

```text
$ python setup.py bdist
```



## 10. 如何使用 setup.py 安装包



正常情况下，我们都是通过以上构建的源码包或者二进制包进行模块的安装。

但在编写 setup.py 的过程中，可能不能一步到位，需要多次调试，这时候如何测试自己写的 setup.py 文件是可用的呢？

这时候你可以使用这条命令，它会将你的模块安装至系统全局环境中

```text
$ python setup.py install
```

如若你的项目还处于开发阶段，频繁的安装模块，也是一个麻烦事。

这时候你可以使用这条命令安装，该方法不会真正的安装包，而是在系统环境中创建一个软链接指向包实际所在目录。这边在修改包之后不用再安装就能生效，便于调试。

```text
$ python setup.py develop
```



## 如何发布包到 PyPi？

通过上面的学习，你一定已经学会了如何打包自己的项目，若你觉得自己开发的模块非常不错，想要 share 给其他人使用，你可以将其上传到 PyPi （Python Package Index）上，它是 Python  官方维护的第三方包仓库，用于统一存储和管理开发者发布的 Python 包。

如果要发布自己的包，需要先到 pypi 上注册账号。然后创建 `~/.pypirc` 文件，此文件中配置 PyPI 访问地址和账号。如的.pypirc文件内容请根据自己的账号来修改。

典型的 .pypirc 文件

```text
[distutils]
index-servers = pypi

[pypi]
username:xxx
password:xxx
```



然后使用这条命令进行信息注册，完成后，你可以在 PyPi 上看到项目信息。

```text
$ python setup.py register
```

注册完了后，你还要上传源码包，别人才使用下载安装

```text
$ python setup.py upload
```

或者也可以使用 `twine` 工具注册上传，它是一个专门用于与 pypi 进行交互的工具，详情可以参考官网：[https://www.ctolib.com/twine.html，这里不详细讲了。](https://link.zhihu.com/?target=https%3A//www.ctolib.com/twine.html%EF%BC%8C%E8%BF%99%E9%87%8C%E4%B8%8D%E8%AF%A6%E7%BB%86%E8%AE%B2%E4%BA%86%E3%80%82)