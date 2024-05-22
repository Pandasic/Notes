---
title: hexo 个人博客框架
tag: [计算机课程学习,软工,]
---
# 博客搭建

## Hexo

### 安装Node.js

```sh
sudo apt install nodejs npm
# 这个方法安装的是 8.10.x 的过时了

#安装15.x
curl -sL https://deb.nodesource.com/setup_15.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 安装hexo

```sh
npm install -g cnpm
# 淘宝源
npm install -g cnpm --registry=https://registry.npm.taobao.org
#  安装hexo
cnpm install -g hexo-cli
```

### 启动

```sh
hexo s
```

### 其他操作

Create a new post

```
hexo new "My New Post"
```

Run server

```
hexo server
```

 Generate static files

```
hexo generate
```

Deploy to remote sites

```
hexo deploy
```

