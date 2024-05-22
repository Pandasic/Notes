---
title: linux_time
tag: [计算机课程学习,Linux,]
---
# Linux time() 

## time() 

所需头文件	#include <time.h>
函数原型	time_t time(time_t * timer)
参数说明	timer=NULL时得到机器日历时间；
timer=时间数值时，用于设置日历时间；
函数返回值	机器日历时间
      功能: 获取当前的系统时间，返回的结果是一个time_t类型，其实就是一个大整数，其值表示从CUT（Coordinated Universal Time）时间1970年1月1日00:00:00（称为UNIX系统的Epoch时间）到当前时刻的秒数。然后调用localtime将time_t所表示的CUT时间转换为本地时间（我们是+8区，比CUT多8个小时）并转成struct tm类型。

    struct  tm
    {
           int tm_sec;
           int tm_min;
           int tm_hour;
           int tm_mday;
           int tm_mon;
           int tm_year;
           int tm_wday;
           int tm_yday;
           int tm_isdst;
    }; 

补充说明：time函数的原型也可以理解为 long time(long *tloc)，即返回一个long型整数。因为在time.h这个头文件中time_t 实际上就是：


　　
```C++
#ifndef _TIME_T_DEFINED
#define _TIME_T_DEFINED /* avoid multiple defines of time_t */

typedef long time_t; /* time value */

#endif
```




函数应用举例
程序例1
time函数获得日历时间。日历时间，是用“从一个标准时间点到此时的时间经过的秒数”来表示的时间。这个标准时间点对不同的编译器来说会有所不同，但对一个编译系统来说，这个标准时间点是不变的，该编译系统中的时间对应的日历时间都通过该标准时间点来衡量，所以可以说日历时间是“相对时间”，但是无论你在哪一个时区，在同一时刻对同一个标准时间点来说，日历时间都是一样的。
```
#include <time.h>
#include <stdio.h>

int main(void)
{
	time_t t; 
<span style="white-space:pre">	</span>t = time(NULL);

　　	printf("The number of seconds since January 1, 1970 is %ld",t);

	return 0;
}
```
执行结果如下：
fs@ubuntu:~/qiang/time$ ./time1 
The number of seconds since January 1, 1970 is 1452345470
fs@ubuntu:~/qiang/time$ 

程序例2：
time函数也常用于随机数的生成，用日历时间作为种子。
```c++
#include <stdio.h>
#include <time.h>
#include<stdlib.h>

int main(void)
{
	int i;
	srand((unsigned) time(NULL));
	printf("ten random numbers from 0 to 99:\n");

	for(i = 0;i < 10;i++)
	{
		printf("%d\n",rand()%100);
	}
	 
	return 0;
}
```
执行结果如下：

fs@ubuntu:~/qiang/time$ ./time2
ten random numbers from 0 to 99:
22
0
58
7
29
90
74
7
95
55
fs@ubuntu:~/qiang/time$ 

程序例3：
用time() 函数结合其他函数（如：localtime、gmtime、asctime、ctime）可以获得当前系统时间或是标准时间。
1）localtime() 函数

函数功能：返回一个以tm结构表达的机器时间信息；

所需头文件	#include <time.h>
函数原型	struct tm *localtime(const time_t *timep)
参数说明	timerp为time(NULL)获得的日历时间；
函数返回值	 以tm结构表达的时间；
使用示例：
```c++
#include <time.h> 
#include <stdio.h> 

int main()
{
	time_t timer;
	struct tm *tblock;
	timer = time(NULL);
	tblock = localtime(&timer);

	printf("Local time is: %s",asctime(tblock));
	
	return 0; 
} 
```
执行结果如下：

fs@ubuntu:~/qiang/time$ ./localtime 
Local time is: Sat Jan  9 21:37:13 2016
fs@ubuntu:~/qiang/time$ 

2）asctime() 函数
函数功能：asctime()将参数timeptr所指的tm结构中的信息转换成真实世界所使用的时间日期表示方法，然后将结果以字符串形态返回。此函数已经由时区转换成当地时间，字符串格式为: "Wed Jun 30 21:49:08 1993/n" 

所需头文件	#include <time.h>
函数原型	 char *asctime(struct tm  *ptr)
参数说明	ptr 为 struct tm 类型的时间结构体
函数返回值	返回的时间字符串格式为：星期,月,日,小时：分：秒,年

示例如下：
```c++
#include <stdio.h> 
#include <string.h> 
#include <time.h>

int main() 
{
	struct tm t;
	char str[80];
	t.tm_sec = 1;
	t.tm_min = 3;
	t.tm_hour = 7;
	t.tm_mday = 22;
	t.tm_mon = 11;
	t.tm_year = 56;
	t.tm_wday = 4;
	t.tm_yday = 0;
	t.tm_isdst = 0;
	strcpy(str,asctime(&t));
	
	printf("%s",str);
	 
	return 0; 
} 
```

执行结果如下：

fs@ubuntu:~/qiang/time$ ./asctime 
Thu Dec 22 07:03:01 1956
fs@ubuntu:~/qiang/time$ 

3）ctime() 函数
函数功能：ctime () 将参数timep所指的time_t结构中的信息转换成真实世界所使用的时间日期表示方法，然后将结果以字符串形态返回。此函数已经由时区转换成当地时间，字符串格式为"Wed Jun 30 21 :49 :08 1993/n"。若再调用相关的时间日期函数，此字符串可能会被破坏。

所需头文件	#include <time.h>
函数原型	char *ctime(const time_t *timep);
参数说明	timep 是由 time(NULL) 得到的日历时间；
函数返回值	返回字符串格式：星期,月,日,小时:分:秒,年
示例如下：
```c++
#include <stdio.h> 
#include <time.h> 
int main() 
{
	time_t t;
	time(&t);
	
	printf("Today's date and time: %s",ctime(&t));
	return 0; 
}
```
执行结果如下：

fs@ubuntu:~/qiang/time$ ./ctime 
Today's date and time: Sat Jan  9 21:53:51 2016
fs@ubuntu:~/qiang/time$ 