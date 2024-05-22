---
title: Nginx 安装配置
tag: [计算机课程学习,软工,]
---
# Nginx 安装配置

## ubuntu

> 参考：https://kalasearch.cn/community/tutorials/how-to-install-nginx-on-ubuntu-20-04/

### 安装

```sh
sudo apt update
sudo apt install nginx
```

### 防火墙配置

Nginx `ufw` 在安装时会把他自身注册成为服务。

使用

```sh
sudo ufw app list
```

查看防火墙应用

Nginx 提供三种配置文件

| Nginx Full  | 开端口80 正常，未加密的网络流量,端口443 TLS / SSL加密的流量 |
| ----------- | ----------------------------------------------------------- |
| Nginx HTTP  | 仅打开端口80 正常，未加密                                   |
| Nginx HTTPS | 仅打开端口443 TLS / SSL加密                                 |

```SH
sudo ufw allow 'Nginx xxx'
sudo ufw status #查看更改
```

### 检查测试

检查init系统状态

```sh
systemctl status nginx
```

测试工作是否正常

```sh
ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
```

外网ip

```sh
curl -4 icanhazip.com
```

### 管理 Nginx

现在，您已启动并运行了Web服务器，让我们回顾一些基本的管理命令。

要停止Web服务器，输入：

```bash
sudo systemctl stop nginx
```

要在停止时，启动Web服务器，键入：

```bash
sudo systemctl start nginx
```

要停止，然后再次启动该服务，键入：

```bash
sudo systemctl restart nginx
```

如果我们只是修改配置，Nginx 可以在不终端的情况下热加载。我们可以键入：

```bash
sudo systemctl reload nginx
```

默认情况下，Nginx 会在服务器启动时，跟随系统启动，如果我们不想这样，我们可以用这个命令来禁止：

```bash
sudo systemctl disable nginx
```

要重新让系统启动时引导 Nginx 启动，那么我们可以输入：

```bash
sudo systemctl enable nginx
```

### 设置服务器块

使用Nginx Web服务器时，*服务器块*（类似于Apache中的虚拟主机）可用于封装配置详细信息，并在一台服务器中托管多个域。我们将建立一个名为 **example.com** 的域，但我们可以**用自己的域名替换它**。

在 Ubuntu 上的 Nginx 默认情况下启用了一个服务器块（server block），服务器块的配置是为给服务器的目录提供地址 `/var/www/html`。尽管这对于单个站点非常有效，但是如果我们在服务器上托管多个站点，则可能变很臃肿。让我们给`/var/www/html`目录添加上分站点目录。

比如我们的网站是 example.com ，那我们创建一个对应的目录 example.com 目录：

```bash
sudo mkdir -p /var/www/example.com/html
```

接下来，使用`$USER`环境变量分配目录的所有权：

```bash
sudo chown -R $USER:$USER /var/www/example.com/html
```

如果我们没有修改自己的`umask`值，那么 Web 根目录的权限应该正确，我们可以通过输入以下命令来确认：

```bash
sudo chmod -R 755 /var/www/example.com
```

接下来，让我们来编辑`index.html` 可以使用 nano 编辑器或其他你用这顺手的编辑器：

```bash
nano /var/www/example.com/html/index.html
```

在其中，添加以下示例HTML：

/var/www/example.com/html/index.html

```html
<html>
    <head>
        <title>Welcome to Example.com!</title>
    </head>
    <body>
        <h1>Success!  The example.com server block is working!</h1>
    </body>
</html>
```

完成后保存并关闭文件。

接下来我们为 Nginx 来创建一个服务器块。与直接修改默认配置文件不同，我们在以下位置创建一个新文件：`/etc/nginx/sites-available/example.com`

```bash
sudo nano /etc/nginx/sites-available/example.com
```

粘贴到以下内容添加到文件中，这个块的配置与默认块的配置相似，但针对我们的新目录和域名进行了更新：

/etc/nginx/sites-available/example.com

```html
server {
        listen 80;
        listen [::]:80;
        root /var/www/example.com/html;
        index index.html index.htm index.nginx-debian.html;
        server_name example.com www.example.com;
        location / {
                try_files $uri $uri/ =404;
        }
}
```

接下来，让我们通过在`sites-enabled`目录新建一个链接，好让 Nginx 在启动过程中会读取这个目录：

```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

现在已启用并配置了两个服务器块，以及基于它们的`listen`和`server_name`指令响应请求：

- `example.com`: 将会响应`example.com` 和 `www.example.com`的请求
- `default`: 将会响应 80 端口的请求，以及不能匹配到两个服务器块上的请求

为避免可能由于添加其他服务器名称而引起的哈希存储区内存问题，有必要调整`/etc/nginx/nginx.conf`文件中的单个值。

打开文件：

```bash
sudo nano /etc/nginx/nginx.conf
```

找到`server_names_hash_bucket_size`指令并删除`#`符号：

```bash
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
```

完成后保存并关闭文件。

接下来，测试以确保我们在 Nginx 文件中的改动，没有任何问题：

```bash
sudo nginx -t
```

如果没有任何问题，请重新启动 Nginx：

```bash
sudo systemctl restart nginx
```

Nginx 现在已经可以按照刚刚我们配置的方式来工作啦。当用户通过`http://example.com`域名访问我们的服务器时，Nginx 会将它指向我们刚刚创建的 Html 页面。

### Nginx 文件及目录结构

到这一步，我们已经学会了如何在 Ubuntu 上安装和配置 Nginx 服务。接下来，我们来学习 Nginx 的文件及目录结构。

#### 内容

- `/var/www/html` 默认的 Web 页面。默认打开可以看到 Nginx 页面。
- `/var/www/html` 实际的 Web 内容。默认请看下只有 Nginx 自己的原生页面。我们可以通过更改 Nginx 配置来更改文件。

#### 服务器配置

- `/etc/nginx` Nginx 配置目录。所有 Nginx 的配置文件都在这里。
- `/etc/nginx/nginx.conf` Nginx 的配置文件。大多数全局配置可以通过这个文件来修改。
- `/etc/nginx/sites-available/sites-enabled` 用来存储服务器下每个站点服务器块的目录。 默认情况下 Nginx 不会直接使用目录下的配置文件，需要我们更改配置来告诉 Nginx 来去读。
- `/etc/nginx/sites-enabled/sites-available` 这里是存储已经启用站点服务器块的目录。
- `/etc/nginx/snippets` 这个目录包含一些 Nginx 的配置文件。可打开详细查看这些配置文件到文档进行学习。

#### 服务器日志

- `/var/log/nginx/access.log` 这里是 Nginx 到日志文件，对 Web 服务器的每个请求都会记录在这个日志中。
- `/var/log/nginx/error.log` 记录 Nginx 运行过程中发生的错误日志。