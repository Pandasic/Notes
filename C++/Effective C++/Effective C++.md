---
title: Effective C++
tag: [计算机课程学习,C++,Effective C++,]
---
#	Effective C++

## 导读

本书目的时告诉你**有效**运用C++,使你的软件易于理解、易于维护、可移植、可扩充、高效、并有着你所预期的行为。

忠告分为两类：一般性的设计策略 和 带有具体细节的特定语言特性。

## 术语

* **声明式** 告诉编译器某个东西的名称和类型、但忽略细节。

    ```C++
    extern int x;						//对象(object)声明式
    std::size_t numDigits(int number);	  //函数(function)声明式
    class Weight;						//类(class)声明式
    template<typename T>				//模板<template>声明式
    class GraphNode;
    ```

    > size_t  是个typedef 计算个数时用的unsigned类型，也是stl中operator[]函数接收的参数类型

* **定义式** 提供编译器一些声明式所遗漏的细节。对象内存分配、函数定义、类的成员的列出

* **初始化** 赋予对象初值的过程。初始化由构造函数执行

    * 默认构造函数：可以被调用但不带任何实参的构造函数
    * explicit 关键字 声明 阻止隐式转换
    * copy构造函数，一同型对象自我初始化
    * copy assignment (operator=)操作符从另一个同类型对象中拷贝其值到自我对象

## 条款1：视C++为一个语言联邦

### C++是多重范型语言。 

同时支持 过程形式(procedural)、面向对象形式(object-oriented)、函数形式(functional)、泛型形式(generic) 、元编程形式(metaprogramming)

### C++四种次语言

* C C++以C为基础。C++对问题的解法就是高级的C的解法，范式以C的成分工作时凸显C的局限

    区块（blocks）、语句（statements）、预处理器（preprocessor）、内置数据类型（built-in data types）、数组（arrays）、指针（pointers）。

* Object-Oriented C++, C with Classes的诉求的

    classes（包括构造函数和析构函数），封装（encapsulation）、继承（inheritance）、多态（polymorphism）、virtual 函数（动态绑定）

* Template C++。 C++ 泛型编程(generic programming)部分。同时带来了 template metaprogramming(TMP 模板元编程)

* STL。STL是个template程序库 .它对容器（containers）、迭代器（iterators）、算法（algorithms）以及函数对象（function objects）

## 条款2：以const enum inline 替换 #define

**编译器替换预处理器**

编译器无法获得符号，因为使用名称为进入记号表(symbol)

```C++
#define ASPECT_RATIO 1.653			//预编译
const double AspectRatio = 1.653 	//常量声明
```

### 特殊情况

* 定义常量指针

    同城被放在头文件中，所以由必要将指针声明为const。

    ```C++
    cosnt char* const authorName = "Jerry";//头文件呢定义常量的char*-based 字符串
    const std::string authorName("Jerry")
    ```

    string通常比 char* based 字符串

* 类内常量

    为保证常量在类内只有一个实体 需要声明为static成员。同时C++要求所使用的任何动议均要提供定义式。但是class专属常量为整数类型需要特殊处理。只要不取地址 则无需提供定义式。

    若编译器坚持要看到定义式则必须提供定义式

    ```C++
    //.h
    class GamePlayer{
    private:
    	static const int NumTurn = 5;//声明
        int scores[NumTurns];		//使用
    }
    //.cpp
    const int GamePlayer::NumTurns //NumTurns的定义
    ```

    并将其放在实现文件中。由于class 常量已经在声明时获得初始值。则定义式不可再设置初值。

    * 无法使用#define 来创建一个class 的专属常量，#define 不重视作用域

    如果编译器不支持类内初始这顶 则将初值放在定义式中

    #### enum hark

    如果不允许完成in class 初始谁那个 可以改成**enum hark**补偿法 [一个属于枚举类型的数可以充当int 使用]

    ```c++
    class GamePlayer{
        private:
        	enum {NumTurns = 5}
    }
    ```

    * enum hark 比较像#define 二位 const 无法对enum取地址
    * 如果不想让别人获得pointer/reference 指向某个整数对象 可以使用设个时间
    * 优秀的编译器不会为整数型const对象设定另外的存储空间[除非创建一个pointer或refrrence指向该对象]，enums 和#define 不会导致非必要的内存分配

### 宏和 inline

必须为宏中所有实参加上小括号 否则表达式调用时回产生麻烦

```C++
#define CALL_WITH_MAX(a,b) f((a)>(b)?(a):(b))
int a = 5, b = 0;
CALL_WITH_MAX(++a,b); //a被累加两次
CALL_WITH_MAX(++a,b+10); //a被累加一次
//掉用f之前a的递增次数取决于和谁比较
```

所以使用inline 来代替宏

```C++
template<typename T>
inline void callWithMax(const T& a, const T& b)
{
	f(a>b?a:b);
}
```

## 条款3: 尽可能使用 const

const classes外部修饰 global或namespace作用域中的**常量**

修饰文件、函数、或区块作用域（block scope）中被声明为**static的对象**

你也可以用它修饰classes内部的static和non-static**成员变量**

面对**指针**你也可以指出指针自身、指针所指物，或两者都（或都不）是const

const 出现在\*左边 被指物是常量

​					 右边 指针本身是常量

​					 两边 指针与被指的都是常量

```C++
void f1(const Widget* pw); 	//f1获得一个指针，指向一个常量的Weiget 对象
void f2(Weight const* pw); 	//f2也是
```

STL 迭代器根据指针塑膜出来，即迭代及作用相当于T*，声明迭代器为const就像声明const指针一样。

令函数返回常量值 可以降低客户错误而造成的以外 由不致于一放弃安全性和高效性。

### const 成员函数

改善C++程序效率的根本方法是以 **pass by reference to const**  传递对象

两个成员函数如果只是常量性(constness)不同则可以被重载。

```c++
class TextBlock{
public:
    const char& operator[](size_t position){return text[position];}//const对象
    const char& operator[](size_t position){text[position];}//non-const对象
private:
	string text;    
}

TextBlock tb("Hello");
std::cout << tb[]; //调用non-const TextBlock::operator[]

const TextBlock ctb("Hello");
std::cout << ctb[0]; //调用const TextBlock::operator[]

//大多数程序调用
void print(const TextBlock& ctb){...}

tb[0] = 'x'		//正确
ctb[0] = 'x'; 	//错误 尝试写一个const TextBlock
```

bitwise const  陈艳函数只有在不更变对象任何成员变量时(static 除外) 才是 const

logical constness 主张 一个const 可以修改所处理对象的某些bits，但只有在客户端侦测不出的情况下才得如此。

**mutable** 表明成员变量总是可能被修改 即使在const 成员函数内

对于 const 与 non-const 的操作 回导致重复代码

```C++
class TextBlock{
    public:
    const char& operator[](std::size_t position) const {
        ... ... ...; //大量操作
        return text[posotion];
    }
    char& operator[](std::size_t position) const {
        ... ... ...; //大量操作
        return text[posotion];
    }
    //改进 non-const方法
    char& operator[](std::size_t position) const {
        return const<char&>(static_cast<const TextBlock&>(*this))[position])l
            //将返回值移除const 并为*this加上const
    }
    //两次转型是为了防止递归调用
    //反向的做法是不好的
}
```

### 总结

* 某些东西声明称const有助于编译器侦测出错误。
* 便提起强制实施bitwise constness，但是编写程序时应该使用概念上的常量性。
* const 和 non-const 陈艳函数有着实质性等价实现时 用 non-const 调用 const版本避免重复

## 条款4: 确定对象使用前已经被初始化

对于某些无法决定的状态，最佳的处理方式时在使用对象之前将它初始化。

* 内置类型 必须手工初始化。

* 非内置类型，则由构造函数将每一个成员初始化。

 不要混淆赋值与初始化，C++规定成员变量初始化发生在构造之前。所以构造函数之前是使用member initialization list(成员构造函数列)

```C++
ABEntry::ABEntry(const string& name,const string& address,list<PhoneNumber>& phones):theName(name),theAddress(address),thePhones(phones),numTimesConsulted(0){}
```

效率更高，因为避免了先默认构造再赋值的情况。

C++由十分固定的成员初始化次序。base classes 更早高于其derived classes 被初始化。而class 成员变量总是以其声明次序被初始化。

static 成员寿命从构造出来直到程序结束为止，程序结束时static对象会被自动销毁 析构函数会在mian()结束时被自动调用。

对于定义在不同编译单元内的non-local static对象的初始化无明确定义。将初始化迁移到专属函数内，该函数返回一个reference指向所含对象。即non-local对象模式被local 对象替换了。单例模式的常用方式。

### 总结

* 为内置型对象进行手工初始化，因为C++不保证初始化它们。

* 构造函数最好使用成员初值列（member initialization list），而不要在构造函数本体内使用赋值操作（assignment）。初值列列出的成员变量，其排列次序应该和它们在class中的声明次序相同。
* 为免除“跨编译单元之初始化次序”问题，请以local static 对象替换non-local static 对象。

## 条款5：了解C++默默编写并调用了那些函数

C++在你未声明的情况下回默认声明 copy构造函数copy assignment操作符和一个析构函数，一个default 构造函数 ，所有函数都是public 而且是inline的

```C++
class Empty{};
//相当于
class Empty{
public:
	Empty(){}	//default 构造函数
    Empty(const Empty& rhs){} 	//copy构造函数
    ~Empty(){}					//析构函数 非虚函数
    
    Empty& operator=(const Empty& rhs){ } //copy assignment 操作符
}
```

default构造函数与析构函数主要是编译调用base classes 和 non-static 变量的构造与析构函数。

编译器版本的opy构造函数copy assignment操作符 将来源对象的每个non-static函数与成员变量拷贝到目标对象 并允许将名称与T 的对象产生关联。

## 条款6：若不想使用编译器自动生成的函数，就该明确拒绝

将对象声明未private 并且只声明而不实现

C++11后 使用=delete 来删除

## 条款7：为多态基类声明virtual析构函数

为了防止派生类由基类指针释放而产生的内存泄露，析构函数应该被声明为virtual。通过虚表覆盖来删除整个对象。

析构函数调用顺序：最深层派生类的析构回被调用，然后其每一个base class 的析构函数被调用。

### 总结

polymorphic（带多态性质的）base classes应该声明一个virtual析构函数。如果class 带有任何virtual函数，它就应该拥有一个virtual析构函数。

Classes的设计目的如果不是作为base classes使用，或不是为了具备多态性（polymorphically），就不该声明virtual析构函数。

## 条款8：别让异常逃离析构函数

如果析构函数发生异常，有两种方法解决问题

* 通过std::abort 强迫结束程序
* 吞掉异常

通过接口将异常交由用户处理

## 条款9:不要在构造与析构过程中调用 virtual函数

构造函数调用时，如果内部使用的时virtual 函数，则会在构造时调用的是基类的版本。

```C++
class Transaction{//所有交易的base class 
    public：Transaction():
    virtual void logTransaction() const=0；//做出一份因类型不同而不同的日志记录（log entry)
};

Transaction::Transaction(){
    ...;
	logTransaction();
}

class BuyTransaction::public Transaction{
public:
    virtual void logTransaction() const;
    ...
}

class SellTransaction::public Transaction{
public:
    virtual void logTransaction() const;
    ...
}

BuyTransaction b;
```

为解决这个问题，使用non-virtual 函数并在构造时候额外传参。

在构造和析构期间不要调用virtual 函数，因为类调用从不下降至derived class(比起当前执行构造与析构函数的那层)

## 条款10:  令 operator= 返回一个 reference to \*this

赋值连锁形式

```c++
int x,y,z;
x = y = z = 15; 	//赋值连锁形式
=> x = (y = (z = 15));
```

为了实现 连锁赋值。赋值操作必须返回一个reference 指向操作符的左侧实参。

只是协议并不是强制性。

## 条款11:在operator= 中处理自我赋值

自我赋值

```C++
Weight w;
w = w; 		//赋值给自己
a[i] = a[j]; //潜在自我赋值
*px = *py 	//潜在自我赋值
```

如果自我管理资源，可能回调入停止使用资源之前以外释放它的陷阱。例如**浅拷贝指针**。

欲组织和错误 传统做法是借由证同测试 达到自我赋值的检验目的

```C++
if (this == &rhs) return *this;
```

但operator= 具备异常安全性 往往自动获得 自我赋值安全的回报

在operator= 函数内手工排列语句(确保代码不但**异常安全**而且**自我赋值安全**)使用**copy and swap**技术。

```C++
class Widget{
	void swap(Widget& rhs);
}

Widget& Widget::operator=(const Widget& rhs){
    Widget temp(rhs); 	//为rhs 数据制作一个副本
    swap(temp);			//将*this数据和上述副本数据交换
    return *this;
}
```

* 某class 的copy assignment 可能被声明为 by value 方式接受实参
* 以by value 方式传递回造成一份复件/副本

## 条款12: 赋值的对象时勿忘每一个成分

如果新增成员，注意修改其copying 函数

对于继承的子类 应该在拷贝函数内调用子类的copying函数，否则只是复制的其声明

copying 函数应该确保复制对象内所有成员变量，以及所有base class 成分

不要尝试以某个copying 函数实现另一个copying 函数。应该将共同技能放进第三个函数中，并由两个copying 函数共同调用。