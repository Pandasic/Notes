---
title: 第3章 使用MySQL
tag: [计算机课程学习,数据库,MySQL 应知应会,]
---
# 第三章 使用MySQL

 

> **连接**

-   需要如下信息

    -   主机名称 本地位localhost

    -   端口 默认为330

    -   用户名 和 用户口令

> **选择数据库**

-   打开数据库 : **USE**+ databasename;必须先打开数据库

-   显示所有数据库 : **SHOW DATABASES**;

-   返回当前数据库内可用表的列表 : **SHOW TABLES**;

-   返回表中相关列的信息:**SHOW COLUMS FROM tablename**;

    -   包含字段名，数据类型，是否允许为NULL，键信息，默认值，其他信息

-   **DESCRIBE / DESC** 作为 **SHOW COLUMNS FROM** 的快捷方式

-   **SHOW STATUS** 显示广泛的服务器状态信息

-   **SHOW CREATE DATABAE**,**SHOW CREATE TABLE** 显示特定数据库/表

-   **SHOW GRANTS** 显示授予用户的安全权限

-   **SHOW ERRORS**,**SHOW WARNINGS** 显示服务器错误和警告