---
title: gtest
tag: [计算机课程学习,C++,]
---
# GTEST

## 安装

1. Ubuntu直接通过控制台安装

   ```shell
   sudo apt-get install libgtest-dev
   ```

2. 编译链接库
    1. 进入gtest文件夹

      ```shell
      cd /usr/src/gtest
      ```

	2. 编译

    ```shell
    #没有安装Cmake的请先安装cmake
    sudo mkdir build 
    cd build
    sudo cmake ..  #一定要以sudo的方式运行，否则没有写入权限
    sudo make      #这个也一样要以sudo的方式
    ```

3. 将生成的libgtest.a 和 libgtest_main.a 拷贝到系统的lib路径下

    ```shell
    sudo cp libgtest*.a /usr/local/lib
    ```

## 使用

### 测试函数

使用TEST() 宏测试函数

```c++
#include <gtest/gtest.h>
TEST(CaseClassName,CasePartName){//TSET宏声明测试函数
    //测试内容
}

int main(int argc,char **argv){
    testing::InitGoogleTest(&argc,argv);
    return RUN_ALL_TESTS();
}
```

### 事件机制

要实现全局事件，继承testing::Environment类，实现里面的SetUp和TearDown方法

1. SetUp()方法在所有案例执行前执行
2. TearDown()方法在所有案例执行后执行
3. 还需要告诉gtest添加这个全局事件，我们需要在main函数中通过testing::AddGlobalTestEnvironment方法将事件挂进来，也就是说，我们可以写很多个这样的类，然后将他们的事件都挂上去。

#### TestSuite事件
我们需要写一个类，继承testing::Test，然后实现两个静态方法

* SetUpTestCase() 方法在第一个TestCase之前执行

* TearDownTestCase() 方法在最后一个TestCase之后执行

在编写测试案例时，我们需要使用TEST_F这个宏，第一个参数必须是我们上面类的名字，代表一个TestSuite。

#### TestCase事件
TestCase事件是挂在每个案例执行前后的，实现方式和上面的几乎一样，不过需要实现的是SetUp方法和TearDown方法：

* SetUp()方法在每个TestCase之前执行

* TearDown()方法在每个TestCase之后执行

### 编译

```shell
g++ filename -lgtest -lpthread -std=c++11 -o output.out
```

## 断言列表

|        | ASSERT:直接中断             | EXPECT: 继续执行            | 备注                      |
| ------ | --------------------------- | --------------------------- | ------------------------- |
| BOOL   | ASSERT_TRUE(bValue)         | EXPECT_TRUE(bValue)         | bValue为true触发          |
| BOOL   | ASSERT_FALSE(bValue)        | EXPECT_TRUE(bValue)         | bValue为false触发         |
| VALUE  | ASSERT_EQ(val1，val2)       | EXPECT_EQ(val1，val2)       | val 1 ==  val2            |
| VALUE  | ASSERT_NE(val1，val2)       | EXPECT_NE(val1，val2)       | val 1 !=  val2            |
| VALUE  | ASSERT_LT(val1，val2)       | EXPECT_LT(val1，val2)       | val 1 <   val2            |
| VALUE  | ASSERT_LE(val1，val2)       | EXPECT_LE(val1，val2)       | val 1 <=  val2            |
| VALUE  | ASSERT_GT(val1，val2)       | EXPECT_GT(val1，val2)       | val 1 >   val2            |
| VALUE  | ASSERT_GE(val1，val2)       | EXPECT_GE(val1，val2)       | val 1 >=  val2            |
| STRING | ASSERT_STREQ(str1,str2)     | EXPECT_STREQ(str1,str2)     | 两字符完全相同            |
| STRING | ASSERT_STRNE(str1,str2)     | EXPECT_STRNE(str1,str2)     | 两字符不同                |
| STRING | ASSERT_STRCASEEQ(str1,str2) | EXPECT_STRCASEEQ(str1,str2) | 两字符完全相同,忽略大小写 |
| STRING | ASSERT_STRCASEEQ(str1,str2) | EXPECT_STRCASEEQ(str1,str2) | 两字符不同,忽略大小写     |

ASSERT_* 断言会产生致命失败，并结束当前函数。

EXPECT_* 产生非致命失败，不会中止当前函数。



### cmake

```cmake
cmake_minimum_required(VERSION 2.6)
# 启用测试
enable_testing()
find_package (Threads)
include_directories($ENV{GTEST_ROOT}/include)
link_directories(/usr/local/lib)
add_executable(main main.cpp)
target_link_libraries(main gtest gtest_main) #注意这里
target_link_libraries(main ${CMAKE_THREAD_LIBS_INIT})
```

