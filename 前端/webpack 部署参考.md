# nodejs + webpack 部署服务

> 官方文档(webpack5)
>
> https://webpack.docschina.org/concepts
>
> https://webpack.docschina.org/guides/getting-started/
>
> 文档
> https://www.webpackjs.com/api/node/
> https://webpack.js.org/
> 教程
> http://xxpromise.gitee.io/webpack5-docs/base/#%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%E6%89%93%E5%8C%85%E5%B7%A5%E5%85%B7
> 安装 
> https://blog.csdn.net/h675107964/article/details/91954591
> 多页面
> https://blog.csdn.net/huangbiao86/article/details/123164062?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0-123164062-blog-79852857.pc_relevant_paycolumn_v3&spm=1001.2101.3001.4242.1&utm_relevant_index=3
> https://zhuanlan.zhihu.com/p/109527475
## webpack 安装

### 本地安装
若webpack版本>4+，需要先安装webpack-cli
```nodejs
npm install -save-dev webpack-cli
npm install -save-dev webpack
npm install -save-dev webpack@<version>
```

### 全局安装
将webpack安装在nodejs的node_modules文件夹中
```
npm install -g webpack
npm install -g webpack@<version> 
```

## 依赖模块

html-webpack-plugin

## 目录与文件

|说明|目录|
|---|---|
|服务配置 |webpack.config.js|
|代码文件放置于 | /src 目录下|
|放置静态资源|/public|

## webpack.config.js

|节点|说明|详细说明|
|---|---|---|
|entry|入口|指示 Webpack 从哪个文件开始打包|
|output|输出|指示 Webpack 打包完的文件输出到哪里去，如何命名等|
|loader|加载器|webpack 本身只能处理 js、json 等资源，其他资源需要借助 loader，|
|plugins|插件|扩展 Webpack 的功能|
|mode|模式|主要由两种模式：开发模式：development生产模式：production|

# 输出/部署
输出 npx webpack
部署 npx webpack serve