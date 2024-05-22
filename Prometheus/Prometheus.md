# Prometheus

> 官网：https://prometheus.io/
>
> 官方教程：https://prometheus.io/docs/prometheus/latest/getting_started/

## 简介

普罗米修斯(Prometheus)是一个SoundCloud公司开源的监控系统，适合监控Docker容器。

* Prometheus的主要特征

  - 多维度数据模型

  - 灵活的查询语言

  - 不依赖分布式存储，单个服务器节点是自主的

  - 以HTTP方式，通过Pull模型拉取时间序列数据

  - 也可以通过中间网关支持Push模型

  - 通过服务发现或者静态配，来发现目标服务对象

  - 支持多种多样的图标和界面展示

![img](https://upload-images.jianshu.io/upload_images/23394767-9b969ab66c5c049e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1120/format/webp)

- Prometheus Server: 用数据的采集和存储，PromQL查询，报警配置。
- Pushgateway: 用于批量，短期的监控数据的汇报总节点。
- Exporters: 各种汇报数据的exporter，例如汇报机器数据的node_exporter，汇报MondogDB信息的 MongoDB_exporter 等等。
- Alertmanager: 用于高级通知管理。

## 安装/配置

* DOWNLOAD：https://prometheus.io/download

* 解压下载文件并切换到目录

  ```
  tar xvfz prometheus-*.tar.gz
  ```

* 配置监控服务，如Prometheus本身，配置为prometheus.yml文件

  具体配置文件说明如下https://prometheus.io/docs/prometheus/latest/configuration/configuration/

  ```
  global:
    scrape_interval:     15s # By default, scrape targets every 15 seconds.
  
    # Attach these labels to any time series or alerts when communicating with
    # external systems (federation, remote storage, Alertmanager).
    external_labels:
      monitor: 'codelab-monitor'
  
  # A scrape configuration containing exactly one endpoint to scrape:
  # Here it's Prometheus itself.
  scrape_configs:
    # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
    - job_name: 'prometheus'
  
      # Override the global default and scrape targets from this job every 5 seconds.
      scrape_interval: 5s
  
      static_configs:
        - targets: ['localhost:9090']
  ```

* 启动

  ```
  ./prometheus --config.file=prometheus.yml
  ```

  查看采集到的数据：[localhost:9090/metrics](http://localhost:9090/metrics) 

  查看图表：http://localhost:9090/graph 



这两周主要推进Orcale 中间件的提测，完成功能与性能测试，本周四晚间上线到与BPIT的连调环境

* 共计106条测试用例，其中读取82条,写入12条,复杂语句9条,其他校验类case3条。共计发现2个BUG
* 完成构建orcale 中间件的框架自动化，
* 完成性能与压力测试，简短语句可达800qps(20字符),复杂语句可达150qps(350)字符
* 稳定性测试进行中
* 部分问题在压力测试阶段暴露，后续需要额外关注复杂语句与上线情况。
