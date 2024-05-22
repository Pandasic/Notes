---
title: Windows右键添加
tag: [计算机课程学习,软工,]
---
# Windows 右键快捷方式添加

> 参考文章:
>
> https://blog.csdn.net/qq_39309348/article/details/108627989
>
> https://blog.csdn.net/u013719339/article/details/80089243

* win+r 输入 regedit 进入注册表
* 选择打开目标
    * 如果是``文件``则为``HKEY_CLASSES_ROOT\\*\shell`
    * 如果是``文件夹``则`HKEY_CLASSES_ROOT\directory\shell`
    * 如果``两者``都要则为`HKEY_CLASSES_ROOT\AllFilesystemObjects\shell`
    * 如果``文件夹空白处``都要则为``HKEY_CLASSES_ROOT\Directory\Background\shell\`
* `HKEY_CLASSES_ROOT-*-shell`下创建`对应程序`的项
* 默认值改为`你想右键显示的字符`
* 新建`字符串值`，名为`icon`，值为应用程序的位置
* 在`新建的应用程序的项`下新建项，名为`command`，默认值为`所对应的命令`\

附上对应的**reg**注册表文件



```shell
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\shell\copypath]
@="Copy folder path"

[HKEY_CLASSES_ROOT\Directory\shell\copypath\command]
@="mshta vbscript:clipboarddata.setdata(\"text\",\"%1\")(close)"

[HKEY_CLASSES_ROOT\*\shell\copypath]
@="Copy file path"

[HKEY_CLASSES_ROOT\*\shell\copypath\command]
@="mshta vbscript:clipboarddata.setdata(\"text\",\"%1\")(close)"
```

其中copypath 为对应的想要的描述

