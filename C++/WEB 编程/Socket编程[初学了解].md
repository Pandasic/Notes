<<<<<<< HEAD
# Socket编程[初学 了解]

## Linux

### 创建 socket

socket() 函数用来创建套接字，确定套接字的各种属性

头文件<sys/socket.h>中的socket 原型为

```c++
int socket(int af, int type, int protocol);
```

* af: 为地址族(Address Family) 也是IP地址类型常用的是**AF_INET/PF_INET**(IPV4)和 **AF_INET16/PF_INET16**(IPV6)
* type: 为传输方式 常用的有 **SOCK_STREAM**[面向连接的传输] 和 **SOCK_DGRAM**[无连接的传输]
* protocol:传输协议 常用的有IPPROTO_TCP[TCP]和IPPROTO_UDP[UDP]

在使用IPV4地址情况下 即af = AF_INET时

* 使用SOCK_STREAM传输 满足条件的只有TCP 则

```C++
int tcp_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);  //IPPROTO_TCP表示TCP协议
```

* 使用SOCK_DGRAM 传输 满足条件的只有TCP 则

```C++
int udp_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);  //IPPROTO_UDP表示UDP协议
```

上面两种情况都只有一种协议满足条件，可以将 protocol 的值设为 0，系统会自动推演出应该使用什么协议，如下所示：

```c++
int tcp_socket = socket(AF_INET, SOCK_STREAM, 0);  //创建TCP套接字
int udp_socket = socket(AF_INET, SOCK_DGRAM, 0);  //创建UDP套接字
```

### bind()

服务器端使用bind()函数将桃子姐与IP地址和端口绑定

```C++
int bind(int sock, struct sockaddr *addr, socklen_t addrlen);  //Linux
```
* 例：

```CPP
//创建套接字
int serv_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

//创建sockaddr_in结构体变量
struct sockaddr_in serv_addr;
memset(&serv_addr, 0, sizeof(serv_addr));  //每个字节都用0填充
serv_addr.sin_family = AF_INET;  //使用IPv4地址
serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");  //具体的IP地址
serv_addr.sin_port = htons(1234);  //端口

//将套接字和IP、端口绑定
bind(serv_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
```
* 参数说明
    * sock: 为socket的描述符
* addr: sockaddr 结构体变量的指针 ,[sockaddr_in](#sockaddr_in结构体)结构体，然后再强制转换为 sockaddr 类型
  
* addrlen: addr变量的大小 可以由sizeof() 计算得出

### sockaddr_in结构体

![image-20200807210059213](E:\Notes\MarkDown\计算机课程学习\imgs\Socket编程[初学了解]_1.png)

```C++
struct sockaddr_in{
    sa_family_t     sin_family;   //地址族（Address Family），也就是地址类型
    uint16_t        sin_port;     //16位的端口号
    struct in_addr  sin_addr;     //32位IP地址
    char            sin_zero[8];  //不使用，一般用0填充
};
```

* sin_family 和 socket() 的第一个参数的含义相同，取值也要保持一致。

* sin_prot 为端口号。

  uint16_t 的长度为两个字节，理论上端口号的取值范围为 0~65536。但 0~1023 的端口一般由系统分配给特定的服务程序，例如 Web 服务的端口号为 80，FTP 服务的端口号为 21，所以我们的程序要尽量在 1024~65536 之间分配端口号。端口号需要用 htons() 函数转换

* sin_addr 是 struct in_addr 结构体类型的变量

  ```C++
  struct in_addr{
    in_addr_t  s_addr;  //32位的IP地址
  };
  ```
  * in_addr_t 在头文件 <netinet/in.h> 中定义，等价于 unsigned long，长度为4个字节。也就是说，s_addr 是一个整数，而IP地址是一个字符串，所以需要 inet_addr() 函数进行转换，例如：

    ```C++
    unsigned long ip = inet_addr("127.0.0.1");
    printf("%ld\n", ip);
    //OUT:16777343
    ```

* sin_zero[8] 是多余的8个字节，没有用，一般使用 memset() 函数填充为 0。例程中，先用 memset() 将结构体的全部字节填充为 0，再给前3个成员赋值，剩下的 sin_zero 自然就是 0 了。

#### 为什么不直接用sockaddr结构体

sockaddr 结构体的定义如下：

```C++
struct sockaddr{    
    sa_family_t  sin_family;   //地址族（Address Family），也就是地址类型    
    char         sa_data[14];  //IP地址和端口号
};
```

下图是 sockaddr 与 sockaddr_in 的对比（括号中的数字表示所占用的字节数）：
![img](E:\Notes\MarkDown\计算机课程学习\imgs\Socket编程[初学了解]_2.png)

sockaddr 和 sockaddr_in 的长度相同，都是16字节，只是将IP地址和端口号合并到一起，用一个成员 sa_data 表示。

要想给 sa_data 赋值，必须同时指明IP地址和端口号，例如”127.0.0.1:80“，遗憾的是，没有相关函数将这个字符串转换成需要的形式，也就很难给 sockaddr 类型的变量赋值，所以使用 sockaddr_in 来代替。这两个结构体的长度相同，强制转换类型时不会丢失字节，也没有多余的字节。

可以认为，sockaddr 是一种通用的结构体，可以用来保存多种类型的IP地址和端口号，而 sockaddr_in 是专门用来保存 IPv4 地址的结构体。另外还有 sockaddr_in6，用来保存 IPv6 地址，它的定义如下：

```c++
struct sockaddr_in6 {     
    sa_family_t sin6_family;  //(2)地址类型，取值为AF_INET6    
    in_port_t sin6_port;  //(2)16位端口号    
    uint32_t sin6_flowinfo;  //(4)IPv6流信息    
    struct in6_addr sin6_addr;  //(4)具体的IPv6地址    
    uint32_t sin6_scope_id;  //(4)接口范围ID
};
```

正是由于通用结构体 sockaddr 使用不便，才针对不同的地址类型定义了不同的结构体。

### connect()

connect() 函数用来建立连接，它的原型为：

```C++
int connect(int sock, struct sockaddr *serv_addr, socklen_t addrlen);  //Linux
```

各个参数的说明和 bind() 相同

### listen()

对于服务器端程序，使用 bind() 绑定套接字后，还需要使用 listen() 函数让套接字进入被动监听状态，再调用 accept() 函数，就可以随时响应客户端的请求了。

```C++
int listen(int sock, int backlog);  //Linux
```

* sock 为需要进入监听状态的套接字
* backlog 为请求队列的最大长度。

#### 请求队列

当套接字正在处理客户端请求时，如果有新的请求进来，套接字是没法处理的，只能把它放进缓冲区，待当前请求处理完毕后，再从缓冲区中读取出来处理。如果不断有新的请求进来，它们就按照先后顺序在缓冲区中排队，直到缓冲区满。这个缓冲区，就称为请求队列（Request Queue）。

缓冲区的长度（能存放多少个客户端请求）可以通过 listen() 函数的 backlog 参数指定，但究竟为多少并没有什么标准，可以根据你的需求来定，并发量小的话可以是10或者20。

如果将 backlog 的值设置为 SOMAXCONN，就由系统来决定请求队列长度，这个值一般比较大，可能是几百，或者更多。

当请求队列满时，就不再接收新的请求

对于 Linux，客户端会收到 ECONNREFUSED 错误

对于 Windows，客户端会收到 WSAECONNREFUSED 错误。

### accept()

当套接字处于监听状态时，可以通过 accept() 函数来接收客户端请求。它的原型为：

```C++
int accept(int sock, struct sockaddr *addr, socklen_t *addrlen);  //Linux
```

参数与 listen() 和 connect() 是相同的

* 参数说明
  * sock 为服务器端套接字
  * addr 为 sockaddr_in 结构体变量
  * addrlen 为参数 addr 的长度，可由 sizeof() 求得。

* accept() 返回一个新的套接字来和客户端通信，addr 保存了客户端的IP地址和端口号，而 sock 是服务器端的套接字后面和客户端通信时，要使用这个新生成的套接字，而不是原来服务器端的套接字。

* accept() 会阻塞程序执行（后面代码不能被执行），直到有新的请求到来。

### 数据传输与发送

Linux 不区分套接字文件和普通文件，使用 write() 可以向套接字中写入数据，使用 read() 可以从套接字中读取数据。

#### write()

```c++
ssize_t write(int fd, const void *buf, size_t nbytes);
```

* fd 为要写入的文件的描述符

* buf 为要写入的数据的缓冲区地址

* nbytes 为要写入的数据的字节数。

> size_t 是通过 typedef 声明的 unsigned int 类型；ssize_t 在 "size_t" 前面加了一个"s"，代表 signed，即 ssize_t 是通过 typedef 声明的 signed int 类型。

#### read()

```c++
ssize_t read(int fd, void *buf, size_t nbytes);
```

* fd 为要读取的文件的描述符
* buf 为要接收数据的缓冲区地址
* nbytes 为要读取的数据的字节数。

read() 函数会从 fd 文件中读取 nbytes 个字节并保存到缓冲区 buf，成功则返回读取到的字节数（但遇到文件结尾则返回0），失败则返回 -1。 

### shutdown()

一般情况下这不会有问题，但有些特殊时刻，需要只断开一条数据传输通道，而保留另一条。

使用 shutdown() 函数可以达到这个目的，它的原型为：

```C++
int shutdown(int sock, int howto);  //Linux
```

* sock 为需要断开的套接字
* howto 为断开方式。howto 在 Linux 下有以下取值：
  * SHUT_RD：断开输入流。套接字无法接收数据（即使输入缓冲区收到数据也被抹去），无法调用输入相关函数。
  * SHUT_WR：断开输出流。套接字无法发送数据，但如果输出缓冲区中还有未传输的数据，则将传递到目标主机。
  * SHUT_RDWR：同时断开 I/O 流。相当于分两次调用 shutdown()，其中一次以 SHUT_RD 为参数，另一次以 SHUT_WR 为参数。

## Windows

### socket()

windows下的原型

```C++
SOCKET socket(int af, int type, int protocol);
```

* windows下返回的时句柄

```CPP
SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);  //创建TCP套接字
```

### bind()

```C++
int bind(SOCKET sock, const struct sockaddr *addr, int addrlen);  //Windows
```

### connect()

```C++
int connect(SOCKET sock, const struct sockaddr *serv_addr, int addrlen);  //Windows
```

### listen()

```C++
int listen(SOCKET sock, int backlog);  //Windows
```

### accept()

````C++
SOCKET accept(SOCKET sock, struct sockaddr *addr, int *addrlen);  //Windows
````

### 数据传输与发送

#### send()

发送数据

```c++
int send(SOCKET sock, const char *buf, int len, int flags);
```

* sock 为要发送数据的套接字
* buf 为要发送的数据的缓冲区地址
* len 为要发送的数据的字节数
* flags 为发送数据时的选项 一般设置为 0 或 NULL

#### recv()

接收数据

```c++
int recv(SOCKET sock, char *buf, int len, int flags);
```



### shutdown()

一般情况下这不会有问题，但有些特殊时刻，需要只断开一条数据传输通道，而保留另一条。

使用 shutdown() 函数可以达到这个目的，它的原型为：

```C++
int shutdown(int sock, int howto);  //Linux
```

* sock 为需要断开的套接字
* howto 为断开方式。howto 在 Linux 下有以下取值：
  * SD_RECEIVE：关闭接收操作，也就是断开输入流。
  * SD_SEND：关闭发送操作，也就是断开输出流。
  * SD_BOTH：同时关闭接收和发送操作。

* Linux 下一切都是文件 所有文件均有一个int类型的编号 称为文件描述符 使用文件时候 只要直到文件描述符就可以
* socket 也被认为是文件的一种 可以认为两台计算机之间的通信时socket文件之间的互相读写

### close()/closesocket()和shutdown()的区别

确切地说，close() / closesocket() 用来关闭套接字，将套接字描述符（或句柄）从内存清除，之后再也不能使用该套接字，与C语言中的 fclose() 类似。应用程序关闭套接字后，与该套接字相关的连接和缓存也失去了意义，TCP协议会自动触发关闭连接的操作。

shutdown() 用来关闭连接，而不是套接字，不管调用多少次 shutdown()，套接字依然存在，直到调用 close() / closesocket() 将套接字从内存清除。

调用 close()/closesocket() 关闭套接字时，或调用 shutdown() 关闭输出流时，都会向对方发送 FIN 包。FIN 包表示数据传输完毕，计算机收到 FIN 包就知道不会再有数据传送过来了。

=======
---
title: Socket编程[初学了解]
tag: [计算机课程学习,C++,WEB 编程,]
---
# Socket编程[初学 了解]

## Linux

创建 socket

socket() 函数用来创建套接字，确定套接字的各种属性

头文件<sys/socket.h>中的socket 原型为

```c++
int socket(int af, int type, int protocol);
```

* af: 为地址族(Address Family) 也是IP地址类型常用的是**AF_INET/PF_INET**(IPV4)和 **AF_INET16/PF_INET16**(IPV6)
* type: 为传输方式 常用的有 **SOCK_STREAM**[面向连接的传输] 和 **SOCK_DGRAM**[无连接的传输]
* protocol:传输协议 常用的有IPPROTO_TCP[TCP]和IPPROTO_UDP[UDP]

在使用IPV4地址情况下 即af = AF_INET时

* 使用SOCK_STREAM传输 满足条件的只有TCP 则

```C++
int tcp_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);  //IPPROTO_TCP表示TCP协议
```

* 使用SOCK_DGRAM 传输 满足条件的只有TCP 则

```C++
int udp_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);  //IPPROTO_UDP表示UDP协议
```

上面两种情况都只有一种协议满足条件，可以将 protocol 的值设为 0，系统会自动推演出应该使用什么协议，如下所示：

```c++
int tcp_socket = socket(AF_INET, SOCK_STREAM, 0);  //创建TCP套接字
int udp_socket = socket(AF_INET, SOCK_DGRAM, 0);  //创建UDP套接字
```

### bind()

服务器端使用bind()函数将桃子姐与IP地址和端口绑定

```C++
int bind(int sock, struct sockaddr *addr, socklen_t addrlen);  //Linux
```
* 例：

```CPP
//创建套接字
int serv_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

//创建sockaddr_in结构体变量
struct sockaddr_in serv_addr;
memset(&serv_addr, 0, sizeof(serv_addr));  //每个字节都用0填充
serv_addr.sin_family = AF_INET;  //使用IPv4地址
serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");  //具体的IP地址
serv_addr.sin_port = htons(1234);  //端口

//将套接字和IP、端口绑定
bind(serv_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
```
* 参数说明
    * sock: 为socket的描述符
* addr: sockaddr 结构体变量的指针 ,[sockaddr_in](#sockaddr_in结构体)结构体，然后再强制转换为 sockaddr 类型
  
* addrlen: addr变量的大小 可以由sizeof() 计算得出

### sockaddr_in结构体

![Socket编程[初学了解]_1.png](/images\Socket编程[初学了解]_1.png)

```C++
struct sockaddr_in{
    sa_family_t     sin_family;   //地址族（Address Family），也就是地址类型
    uint16_t        sin_port;     //16位的端口号
    struct in_addr  sin_addr;     //32位IP地址
    char            sin_zero[8];  //不使用，一般用0填充
};
```

* sin_family 和 socket() 的第一个参数的含义相同，取值也要保持一致。

* sin_prot 为端口号。

  uint16_t 的长度为两个字节，理论上端口号的取值范围为 0~65536。但 0~1023 的端口一般由系统分配给特定的服务程序，例如 Web 服务的端口号为 80，FTP 服务的端口号为 21，所以我们的程序要尽量在 1024~65536 之间分配端口号。端口号需要用 htons() 函数转换

* sin_addr 是 struct in_addr 结构体类型的变量

  ```C++
  struct in_addr{
    in_addr_t  s_addr;  //32位的IP地址
  };
  ```
  * in_addr_t 在头文件 <netinet/in.h> 中定义，等价于 unsigned long，长度为4个字节。也就是说，s_addr 是一个整数，而IP地址是一个字符串，所以需要 inet_addr() 函数进行转换，例如：

    ```C++
    unsigned long ip = inet_addr("127.0.0.1");
    printf("%ld\n", ip);
    //OUT:16777343
    ```

* sin_zero[8] 是多余的8个字节，没有用，一般使用 memset() 函数填充为 0。例程中，先用 memset() 将结构体的全部字节填充为 0，再给前3个成员赋值，剩下的 sin_zero 自然就是 0 了。

#### 为什么不直接用sockaddr结构体

sockaddr 结构体的定义如下：

```C++
struct sockaddr{    
    sa_family_t  sin_family;   //地址族（Address Family），也就是地址类型    
    char         sa_data[14];  //IP地址和端口号
};
```

下图是 sockaddr 与 sockaddr_in 的对比（括号中的数字表示所占用的字节数）：
![Socket编程[初学了解]_2.png](/images\Socket编程[初学了解]_2.png)

sockaddr 和 sockaddr_in 的长度相同，都是16字节，只是将IP地址和端口号合并到一起，用一个成员 sa_data 表示。

要想给 sa_data 赋值，必须同时指明IP地址和端口号，例如”127.0.0.1:80“，遗憾的是，没有相关函数将这个字符串转换成需要的形式，也就很难给 sockaddr 类型的变量赋值，所以使用 sockaddr_in 来代替。这两个结构体的长度相同，强制转换类型时不会丢失字节，也没有多余的字节。

可以认为，sockaddr 是一种通用的结构体，可以用来保存多种类型的IP地址和端口号，而 sockaddr_in 是专门用来保存 IPv4 地址的结构体。另外还有 sockaddr_in6，用来保存 IPv6 地址，它的定义如下：

```c++
struct sockaddr_in6 {     
    sa_family_t sin6_family;  //(2)地址类型，取值为AF_INET6    
    in_port_t sin6_port;  //(2)16位端口号    
    uint32_t sin6_flowinfo;  //(4)IPv6流信息    
    struct in6_addr sin6_addr;  //(4)具体的IPv6地址    
    uint32_t sin6_scope_id;  //(4)接口范围ID
};
```

正是由于通用结构体 sockaddr 使用不便，才针对不同的地址类型定义了不同的结构体。

### connect()

connect() 函数用来建立连接，它的原型为：

```C++
int connect(int sock, struct sockaddr *serv_addr, socklen_t addrlen);  //Linux
```

各个参数的说明和 bind() 相同

### listen()

对于服务器端程序，使用 bind() 绑定套接字后，还需要使用 listen() 函数让套接字进入被动监听状态，再调用 accept() 函数，就可以随时响应客户端的请求了。

```C++
int listen(int sock, int backlog);  //Linux
```

* sock 为需要进入监听状态的套接字
* backlog 为请求队列的最大长度。

#### 请求队列

当套接字正在处理客户端请求时，如果有新的请求进来，套接字是没法处理的，只能把它放进缓冲区，待当前请求处理完毕后，再从缓冲区中读取出来处理。如果不断有新的请求进来，它们就按照先后顺序在缓冲区中排队，直到缓冲区满。这个缓冲区，就称为请求队列（Request Queue）。

缓冲区的长度（能存放多少个客户端请求）可以通过 listen() 函数的 backlog 参数指定，但究竟为多少并没有什么标准，可以根据你的需求来定，并发量小的话可以是10或者20。

如果将 backlog 的值设置为 SOMAXCONN，就由系统来决定请求队列长度，这个值一般比较大，可能是几百，或者更多。

当请求队列满时，就不再接收新的请求

对于 Linux，客户端会收到 ECONNREFUSED 错误

对于 Windows，客户端会收到 WSAECONNREFUSED 错误。

### accept()

当套接字处于监听状态时，可以通过 accept() 函数来接收客户端请求。它的原型为：

```C++
int accept(int sock, struct sockaddr *addr, socklen_t *addrlen);  //Linux
```

参数与 listen() 和 connect() 是相同的

* 参数说明
  * sock 为服务器端套接字
  * addr 为 sockaddr_in 结构体变量
  * addrlen 为参数 addr 的长度，可由 sizeof() 求得。

* accept() 返回一个新的套接字来和客户端通信，addr 保存了客户端的IP地址和端口号，而 sock 是服务器端的套接字后面和客户端通信时，要使用这个新生成的套接字，而不是原来服务器端的套接字。

* accept() 会阻塞程序执行（后面代码不能被执行），直到有新的请求到来。

### 数据传输与发送

Linux 不区分套接字文件和普通文件，使用 write() 可以向套接字中写入数据，使用 read() 可以从套接字中读取数据。

#### write()

```c++
ssize_t write(int fd, const void *buf, size_t nbytes);
```

* fd 为要写入的文件的描述符

* buf 为要写入的数据的缓冲区地址

* nbytes 为要写入的数据的字节数。

> size_t 是通过 typedef 声明的 unsigned int 类型；ssize_t 在 "size_t" 前面加了一个"s"，代表 signed，即 ssize_t 是通过 typedef 声明的 signed int 类型。

#### read()

```c++
ssize_t read(int fd, void *buf, size_t nbytes);
```

* fd 为要读取的文件的描述符
* buf 为要接收数据的缓冲区地址
* nbytes 为要读取的数据的字节数。

read() 函数会从 fd 文件中读取 nbytes 个字节并保存到缓冲区 buf，成功则返回读取到的字节数（但遇到文件结尾则返回0），失败则返回 -1。 

### shutdown()

一般情况下这不会有问题，但有些特殊时刻，需要只断开一条数据传输通道，而保留另一条。

使用 shutdown() 函数可以达到这个目的，它的原型为：

```C++
int shutdown(int sock, int howto);  //Linux
```

* sock 为需要断开的套接字
* howto 为断开方式。howto 在 Linux 下有以下取值：
  * SHUT_RD：断开输入流。套接字无法接收数据（即使输入缓冲区收到数据也被抹去），无法调用输入相关函数。
  * SHUT_WR：断开输出流。套接字无法发送数据，但如果输出缓冲区中还有未传输的数据，则将传递到目标主机。
  * SHUT_RDWR：同时断开 I/O 流。相当于分两次调用 shutdown()，其中一次以 SHUT_RD 为参数，另一次以 SHUT_WR 为参数。

## Windows

### socket()

windows下的原型

```C++
SOCKET socket(int af, int type, int protocol);
```

* windows下返回的时句柄

```CPP
SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);  //创建TCP套接字
```

### bind()

```C++
int bind(SOCKET sock, const struct sockaddr *addr, int addrlen);  //Windows
```

### connect()

```C++
int connect(SOCKET sock, const struct sockaddr *serv_addr, int addrlen);  //Windows
```

### listen()

```C++
int listen(SOCKET sock, int backlog);  //Windows
```

### accept()

````C++
SOCKET accept(SOCKET sock, struct sockaddr *addr, int *addrlen);  //Windows
````

### 数据传输与发送

#### send()

发送数据

```c++
int send(SOCKET sock, const char *buf, int len, int flags);
```

* sock 为要发送数据的套接字
* buf 为要发送的数据的缓冲区地址
* len 为要发送的数据的字节数
* flags 为发送数据时的选项 一般设置为 0 或 NULL

#### recv()

接收数据

```c++
int recv(SOCKET sock, char *buf, int len, int flags);
```



### shutdown()

一般情况下这不会有问题，但有些特殊时刻，需要只断开一条数据传输通道，而保留另一条。

使用 shutdown() 函数可以达到这个目的，它的原型为：

```C++
int shutdown(int sock, int howto);  //Linux
```

* sock 为需要断开的套接字
* howto 为断开方式。howto 在 Linux 下有以下取值：
  * SD_RECEIVE：关闭接收操作，也就是断开输入流。
  * SD_SEND：关闭发送操作，也就是断开输出流。
  * SD_BOTH：同时关闭接收和发送操作。

* Linux 下一切都是文件 所有文件均有一个int类型的编号 称为文件描述符 使用文件时候 只要直到文件描述符就可以
* socket 也被认为是文件的一种 可以认为两台计算机之间的通信时socket文件之间的互相读写

### close()/closesocket()和shutdown()的区别

确切地说，close() / closesocket() 用来关闭套接字，将套接字描述符（或句柄）从内存清除，之后再也不能使用该套接字，与C语言中的 fclose() 类似。应用程序关闭套接字后，与该套接字相关的连接和缓存也失去了意义，TCP协议会自动触发关闭连接的操作。

shutdown() 用来关闭连接，而不是套接字，不管调用多少次 shutdown()，套接字依然存在，直到调用 close() / closesocket() 将套接字从内存清除。

调用 close()/closesocket() 关闭套接字时，或调用 shutdown() 关闭输出流时，都会向对方发送 FIN 包。FIN 包表示数据传输完毕，计算机收到 FIN 包就知道不会再有数据传送过来了。

>>>>>>> 0f26ed6 (add new notes)
默认情况下，close()/closesocket() 会立即向网络中发送FIN包，不管输出缓冲区中是否还有数据，而shutdown() 会等输出缓冲区中的数据传输完毕再发送FIN包。也就意味着，调用 close()/closesocket() 将丢失输出缓冲区中的数据，而调用 shutdown() 不会。