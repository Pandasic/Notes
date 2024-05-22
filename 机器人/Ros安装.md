# Ros 安装

> 参考：
>
> http://wiki.ros.org/cn/ROS/Installation
>
> http://wiki.ros.org/ROS/Installation

~~以下内容来自官方文档，所以你为啥要抄一遍 = =~~

## 配置Ubuntu软件仓库

配置你的Ubuntu软件仓库（repositories）以允许使用“restricted”“universe”和“multiverse”存储库。你可以根据[Ubuntu软件仓库](https://help.ubuntu.com/community/Repositories/Ubuntu)指南来完成这项工作。



## 设置sources.list

设置电脑以安装来自packages.ros.org的软件。

- 

    ```
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    ```

    | [ROS镜像源](http://wiki.ros.org/ROS/Installation/UbuntuMirrors) | [Deb源码站](http://wiki.ros.org/DebianPackageSources) |
    | ------------------------------------------------------------ | ----------------------------------------------------- |
    |                                                              |                                                       |

若下载速度缓慢，推荐就近选择一个镜像源替换上面的命令。例如，Tsinghua University为：

- 

    ```
    sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
    ```

如果依旧遇到连接问题，请尝试[为Ubuntu apt换源](https://developer.aliyun.com/mirror/ubuntu)（非ROS网站）。

## 设置密钥

- 

    ```
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    ```

    

若无法连接到密钥服务器，可以尝试替换上面命令中的 `hkp://keyserver.ubuntu.com:80` 为 `hkp://pgp.mit.edu:80` 。

你也可以使用curl命令替换apt-key命令，这在使用代理服务器的情况下比较有用：

- 

    ```
    curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
    ```

## 安装

首先，确保你的 Debian 包索引是最新的：

- 

    ```
    sudo apt update
    ```

在 ROS 中有很多不同的库和工具。我们提供了四种默认选项供你开始。你也可以单独安装 ROS 的软件包。

如果下面的步骤出现问题，你可以用这个源来替代上面提到的源：[ros-shadow-fixed（英文页面）](http://wiki.ros.org/ShadowRepository)

- **桌面完整版（推荐）：** : 包含 ROS、[rqt](http://wiki.ros.org/rqt)、[rviz](http://wiki.ros.org/rviz)、机器人通用库、2D/3D 模拟器、导航以及 2D/3D 感知包。

    - 

        

        ```
        sudo apt install ros-melodic-desktop-full
        ```

        或 [单击这里](apt:ros-melodic-desktop-full?refresh=yes)

    **桌面版：** 包含 ROS，[rqt](http://wiki.ros.org/rqt)，[rviz](http://wiki.ros.org/rviz) 和机器人通用库

    - 

        ```
        sudo apt install ros-melodic-desktop
        ```

        或 [单击这里](apt:ros-melodic-desktop?refresh=yes)

    **ROS-基础包：** 包含 ROS 包，构建和通信库。没有图形界面工具。

    - 

        ```
        sudo apt install ros-melodic-ros-base
        ```

        或 [单击这里](apt:ros-melodic-ros-base?refresh=yes)

    **单独的包：** 你也可以安装某个指定的ROS软件包（使用软件包名称替换掉下面的PACKAGE）：

    - 

        ```
        sudo apt install ros-melodic-PACKAGE
        ```

        如：

        ```
        sudo apt install ros-melodic-slam-gmappin
        ```

要查找可用软件包，请运行：

```
apt search ros-melodic
```

## 初始化 rosdep

在你使用 ROS 之前，需要初始化 `rosdep`。`rosdep` 让你能够轻松地安装被想要编译的源代码，或被某些 ROS 核心组件需要的系统依赖。

```
sudo rosdep init
rosdep update
```

> 如果没有rosdep 的命令 安装 python-rosdep
>
> 不要安装python-rosdep2 会卸载掉原本的ros1

init 失败。 应该是网站被墙，科学上网或者更改host

## 设置环境

将 ROS 环境变量自动添加到新 bash 会话会很方便：

```
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

*如果你不只安装了一个 ROS 发行版， `~/.bashrc` 只能使用你需要的 ROS 版本的 `setup.bash` 。*

如果你只想设置当前 bash 会话的 ROS 环境变量，只需要输入：

```
source /opt/ros/melodic/setup.bash
```

如果你使用 zsh，那么你需要将上述命令改为：

```
echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
source ~/.zshrc
```

## 构建工厂依赖

到目前为止，你已经安装了运行核心 ROS 包所需的内容。为了创建和管理自己的 ROS 工作区，有各种各样的工具和需求分别分布。例如：[rosinstall](http://wiki.ros.org/rosinstall) 是一个经常使用的命令行工具，它使你能够轻松地从一个命令下载许多 ROS 包的源树。

要安装这个工具和其他构建ROS包的依赖项，请运行:

```
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```