# Gazebo安装

> 参考自：
>
> https://blog.csdn.net/weixin_41045354/article/details/84881498

## 安装
原则上Gazebo是跟ros一起使用的，但是这个系列并不是在教ros的使用，所以还是把Gazebo单独拿出来说

1. 添加源

```sh
sudo sh -c 'echo "deb  http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
```



2. 安装Gazebo

```sh
sudo apt-get update
sudo apt-get install gazebo9 
sudo apt-get install libgazebo9-dev
```

3. 运行

```sh
sudo gazebo
```

> 出现 symbol look up error 的错误

执行

```sh
sudo apt upgrade libignition-matg2
```

