# JS快速入门

> https://www.w3school.com.cn/js/index.asp

## 使用

### 内部使用

在HTML<script></script> 之间使用

JavaScript 例子也许会使用 type 属性：<script type="text/javascript">

type 属性不是必需的。JavaScript 是 HTML 中的默认脚本语言

### 外部使用

在外部创建文件 后缀为.js

```js
//__hellow world function
function myFunction(){
 document.getElementById("demo").innerHTML = "段落被更改。";
}
```

调用

```js
<script src="myScript.js"></script>
```

或者使用完整的url 引用外部

```html
<script src="https://www.w3school.com.cn/js/myScript1.js"></script>
```

## 输出

JavaScript 能够以不同方式“显示”数据：

- 使用 window.alert() 写入警告框
- 使用 document.write() 写入 HTML 输出
- 使用 innerHTML 写入 HTML 元素
- 使用 console.log() 写入浏览器控制台

### innerHTML

如需访问 HTML 元素，JavaScript 可使用 document.getElementById(id) 方法。

id 属性定义 HTML 元素。innerHTML 属性定义 HTML 内容

```js
//__ 改变元素内容
document.getElementById("body").innerHTML = 5;
```

### document.write()

```js
//__ 仅用于测试
document.write(5);
```

### window.alert()

```js
//__ 
window.alert(5);
```

### console.log()

在浏览器中，您可使用 console.log() 方法来显示数据。

```js
console.log(5 + 6);
```

## 语句

JavaScript 语句是由 web 浏览器“执行”的“指令”。

通过分号分隔 JavaScript 语句。 如下是一个空语句

> 以分号结束语句不是必需的，但我们仍然强烈建议您这么做。

```js
// empty
;
```

JavaScript 会忽略多个空格。您可以向脚本添加空格，以增强可读性。

### 折行

为了达到最佳的可读性，程序员们常常喜欢把代码行控制在 80 个字符以内。

JavaScript 语句太长，对其进行折行的最佳位置是某个运算符：

```js
// break line
document.getElementById("demo").innerHTML =
 "Hello Kitty.";
```

### 代码块

​	用花括号（{...}）组合在代码块中。代码块的作用是定义一同执行的语句。

```
// code block
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello Kitty.";
    document.getElementById("demo2").innerHTML = "How are you?";
}
```

## 关键字

## JavaScript 关键词

JavaScript 语句常常通过某个关键词来标识需要执行的 JavaScript 动作。

下面的表格列出了一部分将在教程中学到的关键词：

| 关键词        | 描述                                              |
| ------------- | ------------------------------------------------- |
| break         | 终止 switch 或循环。                              |
| continue      | 跳出循环并在顶端开始。                            |
| debugger      | 停止执行 JavaScript，并调用调试函数（如果可用）。 |
| do ... while  | 执行语句块，并在条件为真时重复代码块。            |
| for           | 标记需被执行的语句块，只要条件为真。              |
| function      | 声明函数。                                        |
| if ... else   | 标记需被执行的语句块，根据某个条件。              |
| return        | 退出函数。                                        |
| switch        | 标记需被执行的语句块，根据不同的情况。            |
| try ... catch | 对语句块实现错误处理。                            |
| var           | 声明变量。                                        |

注释：JavaScript 关键词指的是保留的单词。保留词无法用作变量名。

## 语法

JavaScript 语句定义两种类型的值：混合值和变量值。混合值被称为*字面量（literal）*。变量值被称为*变量*。

### 字面量

```js
// number
15.90
10011
```

```js
// string
""
"Bill Gates"
'Bill Gates'
```

### 变量

*变量*用于*存储*数据值。

JavaScript 使用 var 关键词来*声明*变量。

= 号用于为变量*赋值*。

```js
// var
var x;
x = 7;
```

### 运算符

JavaScript 使用*算数运算符*（+ - * /）来*计算值*：

```js
// operator
(7 + 8) * 10
```

JavaScript 使用*赋值运算符*（=）向变量*赋值*：

```js
//__ equal
var x, y;
var x = 7;
var y = 8;
```

### 表达式

表达式是值、变量和运算符的组合，计算结果是值。

```js
// expression
6 * 10
```

### 注释

```js
//__ 
xx = 123 // 会执行
// xx = 123 // 不会执行
```

## 标识符

首字符必须是字母、下划线（-）或美元符号（$）.且大小写敏感。

## 变量

```js
// var test
var x = 7;
var y = 8;
var z = x + y;

document.write(x);
document.write(y);
document.write(z);
```

 JavaScript *变量*必须以*唯一的名称*的*标识*。

```js
// same var test
var x = 7;
document.write(x);
var x = 8;
document.write(x);
var x = x + x;
document.write(x);
```

赋值运算符

```js
// evaluate test
var x = 5;
x = x + 5;
document.write(x);
```

JavaScript 变量可存放数值，比如 100，以及文本值，比如 "Bill Gates"。

JavaScript 可处理多种数据类型，但是现在，我们只关注数值和字符串值。

字符串被包围在双引号或单引号中。数值不用引号。

如果把数值放在引号中，会被视作文本字符串。

### 变量声明

```js
// var define
var test;
document.write(test);
```

```js
// evaluate var
var test;
test = "1";
document.write(test);
```

```js
// evaluate var in declation
var test = "1";
document.write(test);
```

```js
// var multi declation in one condition
var person = "Bill Gates", carName = "porsche", price = 15000;

document.write(person);
document.write(carName);
document.write(price);
```

重复声明 js 变量 值不会被覆盖

```js
// differnt type dynamic define
var pi = 3.14;
var person = "Bill Gates";
var answer = 'How are you!';

document.write(pi);
document.write(person);
document.write(answer);
```

```js
// var declation two time
var car = "por";
var car;
```

### 算术

```js
// number var add multi
var x = 3 + 5 + 8;
document.write(x);
```

```js
// string var 
var x = "Bill" + " " + "Gates";
document.write(x);
```

```js
// multi type var add
var x = "8" + 3 + 5;
document.write(x);
var y = 3 + 5 + "8";
document.write(y);
```

## 作用域

### let/ const

ES2015 引入了两个重要的 JavaScript 新关键词：let 和 const。

这两个关键字在 JavaScript 中提供了块作用域（*Block Scope*）变量（和常量）

在 ES2015 之前，JavaScript 只有两种类型的作用域：*全局作用域*和*函数作用域*

### 全局作用域

*全局*（在函数之外）声明的变量拥有*全局作用域*。

```js
// __
var carName = "porsche";

// 此处的代码可以使用 carName

function myFunction() {
  // 此处的代码也可以使用 carName
}
```

*全局*变量可以在 JavaScript 程序中的任何位置访问。

### 函数作用域

*局部*（函数内）声明的变量拥有*函数作用域*。

```js
//__
// 此处的代码不可以使用 carName

function myFunction() {
  var carName = "porsche";
  // code here CAN use carName
}

// 此处的代码不可以使用 carName
```

### 块作用域

通过 var 关键词声明的变量没有块*作用域*。

在块 *{}* 内声明的变量可以从块之外进行访问。

在 ES2015 之前，JavaScript 是没有块作用域的。

可以使用 let 关键词声明拥有块作用域的变量。

在块 *{}* 内声明的变量无法从块外访问：

```js
//__
{ 
  let x = 10;
}
// 此处不可以使用 x
```

### 重新声明变量

使用 var 关键字重新声明变量会带来问题。

在块中重新声明变量也将重新声明块外的变量：

```js
//__
var x = 10;
// 此处 x 为 10
{ 
  var x = 6;
  // 此处 x 为 6
}
// 此处 x 为 6
```

### HTML 中的全局变量

使用 JavaScript 的情况下，全局作用域是 JavaScript 环境。

在 HTML 中，全局作用域是 window 对象。

通过 var 关键词定义的全局变量属于 window 对象：

通过 let 关键词定义的全局变量不属于 window 对象：

```js
// let and var in windows
var carName = "porsche";
let carName2 = "porsche";
// 此处的代码可使用 window.carName
document.write(window.carName);
document.write(window.carName2);
```

相同的作用域，或在相同的块中，通过 let 重新声明一个 var 变量是不允许的

```js
//__ use let define var
var x = 10;       // 允许
let x = 6;       // 不允许
document.write(x);
{
  var x = 10;   // 允许
  let x = 6;   // 不允许
  document.write(x);
}
```

通过 let 重新声明变量是允许的：

```js
// use let in different space
let x = 6;       // 允许
document.write(x);
{
  let x = 7;   // 允许
  document.write(x);
}
{
  let x = 8;   // 允许
  document.write(x);
}
```

通过 var 声明的变量会*提升*到顶端。

通过 let 定义的变量不会被提升到顶端。

在声明 let 变量之前就使用它会导致 ReferenceError。

变量从块的开头一直处于“暂时死区”，直到声明为止。

## 运算符

```js
// add operator
var x = 7;
var y = 8;
var z = x + y;
document.write(z);
```

```js
// minus operator
var x = 7;
var y = 8;
var z = x - y;
document.write(z);
```

```js
// mulpt operator

var x = 7;
var y = 8;
var z = x * y; 
document.write(z);
```

```js
// div operator
var x = 7;
var y = 8;
var z = x / y;
document.write(z);
```

```js
// mod operator
var x = 7;
var y = 8;
var z = y % x ;
document.write(z);
```

```js
// add-add operator
var x = 7;
var y = x++ ;
document.write(x);
document.write(y);
var z = ++x ;
document.write(x);
document.write(z);
```

```js
// minus-minus operator
var x = 7;
var y = x-- ;
document.write(x);
document.write(y);
var z = --x ;
document.write(x);
document.write(z);
```

```js
// evaluate operator
var x = 20;
var y = 10;
y = x;
document.write(x);
document.write(y);
```

```js
// add-evaluate operator
var x = 20;
var y = 10;
y += x;
document.write(x);
document.write(y);
```
```js
// min-evaluate operator
var x = 20;
var y = 10;
y -= x;
document.write(x);
document.write(y);
```
```js
// mulpt-evaluate operator
var x = 20;
var y = 10;
y *= x;
document.write(x);
document.write(y);
```
```js
// div-evaluate operator
var x = 20;
var y = 10;
y /= x;
document.write(x);
document.write(y);
```
```js
// mod-evaluate operator
var x = 10;
var y = 21;
y %= x;
document.write(x);
document.write(y);
```

** 幂(ES2016),

```js
// add between str and number
var x = 7 + 8;
var y = "7" + 8;
var z = "Hello" + 7;
document.write(x);
document.write(y);
document.write(z);
```

```js
// equal compare 1
var a = 1;
var b = 1;
document.write(a == b);
```

```js
// equal compare 2
var a = 1;
var b = 1.0;
document.write(a == b);
```

```js
// equal compare 3
var a = 2;
var b = 1.0;
document.write(a == b);
```

```js
// full equal compare 1
var a = 2;
var b = 2;
document.write(a === b);
```

```js
// full equal compare 2
var a = 2.0;
var b = 2;
document.write(a === b);
```

```js
// full equal compare 3
var a = 1;
var b = 3;
document.write(a === b);
```

```js
// full equal compare 4
var a = 0;
var b = "0";
document.write(a === b);
```

```js
// full equal compare 5
var a = 1.0;
var b = "1.0";
document.write(a === b);
```

```js
// not equal compare 1
var a = 1;
var b = 1;
document.write(a != b);
```

```js
// not equal compare 2
var a = 2;
var b = 1;
document.write(a != b);
```

```js
// not equal compare 1
var a = 2;
var b = 2;
document.write(a === b);
```

```js
// not equal compare 2
var a = 2.0;
var b = 2;
document.write(a === b);
```

```js
// not equal compare 3
var a = 1;
var b = 3;
document.write(a === b);
```

```js
// not equal compare 4
var a = 0;
var b = "0";
document.write(a === b);
```

```js
// not equal compare 5
var a = 1.0;
var b = "1.0";
document.write(a === b);
```

```js
// gt compare 1
var a = 1;
var b = 2;
document.write(a > b);
```

```js
// gt compare 2
var a = 1;
var b = 1;
document.write(a > b);
```

```js
// gt compare 3
var a = 1;
var b = 0;
document.write(a > b);
```

```js
// gt compare str 1
var a = 1;
var b = "2";
document.write(a > b);
```

```js
// gt compare str 2
var a = 1;
var b = "1";
document.write(a > b);
```

```js
// gt compare str 3
var a = 1;
var b = "0";
document.write(a > b);
```
  >  符号 > < >= <=  ? 

逻辑运算符

&&  || ! 

### 类型运算符

| 运算符     | 描述                                  |
| ---------- | ------------------------------------- |
| typeof     | 返回变量的类型。                      |
| instanceof | 返回 true，如果对象是对象类型的实例。 |

##  位运算符

位运算符处理 32 位数。

该运算中的任何数值运算数都会被转换为 32 位的数。结果会被转换回 JavaScript 数。

| 运算符 | 描述         | 例子    | 等同于       | 结果 | 十进制 |
| ------ | ------------ | ------- | ------------ | ---- | ------ |
| &      | 与           | 5 & 1   | 0101 & 0001  | 0001 | 1      |
| \|     | 或           | 5 \| 1  | 0101 \| 0001 | 0101 | 5      |
| ~      | 非           | ~ 5     | ~0101        | 1010 | 10     |
| ^      | 异或         | 5 ^ 1   | 0101 ^ 0001  | 0100 | 4      |
| <<     | 零填充左位移 | 5 << 1  | 0101 << 1    | 1010 | 10     |
| >>     | 有符号右位移 | 5 >> 1  | 0101 >> 1    | 0010 | 2      |
| >>>    | 零填充右位移 | 5 >>> 1 | 0101 >>> 1   | 0010 |        |

## 数据类型

JavaScript 变量能够保存多种*数据类型*：数值、字符串值、数组、对象

```js
//__
var length = 7;                             // 数字
var lastName = "Gates";                      // 字符串
var cars = ["Porsche", "Volvo", "BMW"];         // 数组
var x = {firstName:"Bill", lastName:"Gates"}; //object
```

当数值和字符串相加时，JavaScript 将把数值视作字符串。

avaScript 从左向右计算表达式。不同的次序会产生不同的结果：

```js
// sum in different type
var x = 911 + "Porsche";
document.write(x);
var y = "911" + "Porsche";
document.write(y);
var z = "Porsche" + 911;
document.write(z);
var a = 911 + 7 + "Porsche";
document.write(a);
var b = "Porsche" + 911 + 7;
document.write(b);
```

### 整数

```js
// int range
var x = 999999999999999;   // x 将是 999999999999999
var y = 9999999999999999;  // y 将是 10000000000000000

document.write(x);
document.write(y);

var x = 0.2 + 0.1;       
document.write(x);

var x = (0.2 * 10 + 0.1 * 10) / 10;       // x 将是 0.3
document.write(x);
```

```js
// num like add
var x = 10;
var y = 20;
var z = x + y;           // z 将是 30（一个数）
document.write(z);

var x = "10";
var y = "20";
var z = x + y;           // z 将是 1020（字符串）
document.write(z);

var x = 10;
var y = "20";
var z = x + y;           // z 将是 1020（一个字符串）
document.write(z);

var x = 10;
var y = 20;
var z = "The result is: " + x + y;
document.write(z);

var x = 10;
var y = 20;
var z = "30";
var result = x + y + z;
document.write(result);
```
```js
// NAN
var x = 100 / "Apple";  // x 将是 NaN（Not a Number）
document.write(x);
document.write(isNaN(x));

var x = 100 / "10";     // x 将是 10
document.write(xs);

var x = NaN;
var y = 5;
var z = x + y;         // z 将是 NaN
document.write(z);

document.write(typeof NaN);
```

```js
// infinity
var x =  2 / 0;          // x 将是 Infinity
var y = -2 / 0;          // y 将是 -Infinity
document.write(x);
document.write(y);

var myNumber = 2;
while (myNumber != Infinity) {          // 执行直到 Infinity
    myNumber = myNumber * myNumber;
}
document.write(myNumber);
```

```js
// hexadecimal
//十六进制

var x = 0xFF;
document.write(x);
```

```js
// num obj
var x = 123;
var y = new Number(123);

// typeof x 返回 number
// typeof y 返回 object
document.write(x);
document.write(y);
document.write(typeof x);
document.write(typeof y);
document.write(x == y);
document.write(x === y);
```

### 动态类型

JavaScript 拥有动态类型。这意味着相同变量可用作不同类型

```js
// dynamaic type
var x;               // 现在 x 是 undefined
document.write(x);
var x = 7;           // 现在 x 是数值
document.write(x);
var x = "Bill";      // 现在 x 是字符串值
document.write(x);
```

### 数值

JavaScript 只有一种数值类型。写数值时用不用小数点均可：

```js
// var number type
var x1 = 34.00;     // 带小数点
document.write(x);
var x2 = 34;        // 不带小数点
document.write(x);
var y = 123e5;      // 12300000
document.write(x);
var z = 123e-5;     // 0.00123
document.write(x);
```

### bool

```js
// bool type var
var x = true;
document.write(x);
var y = false;
document.write(y);
```

### array

```js
// define array
var cars = ["Porsche", "Volvo", "BMW"];
document.write(cars);
var cars = [];
document.write(cars);
```

## object

```js
// define object
var person = {firstName:"Bill", lastName:"Gates", age:62, eyeColor:"blue"};
document.write(person);
```

### typeof

```js
// typeof key wordß
document.write(typeof "");                  // 返回 "string"
document.write(typeof "Bill");           // 返回 "string"
document.write(typeof "Bill Gates");          // 返回 "string"

document.write(typeof 0);                   // 返回 "number"
document.write(typeof 314);                 // 返回 "number"
document.write(typeof 3.14);                // 返回 "number"
document.write(typeof (7));                 // 返回 "number"
document.write(typeof (7 + 8));            // 返回 "number"

```

### undefine

```js
// undefined
var person;
document.write(person);
document.write(typeof person);
person = undefined;
document.write(person);
document.write(typeof person);
```

### 空值

```js
// empty val
var car = "";   // 值是 ""，类型是 "string"
```

### null

在 JavaScript 中，null 是 "nothing"。它被看做不存在的事物。

不幸的是，在 JavaScript 中，null 的数据类型是对象。

您可以把 null 在 JavaScript 中是对象理解为一个 bug。它本应是 null。

您可以通过设置值为 null 清空对象：

```js
// null 
var person = null;           // 值是 null，但是类型仍然是对象
document.write(person);
document.write(typeof person);
```

### compare undefined and null

```js
// compare undefined and null
document.write(typeof undefined);              // undefined
document.write(typeof null);                  // object
document.write(null === undefined);           // false
document.write(null == undefined);            // true);
```

### 原始数据

原始数据值是一种没有额外属性和方法的单一简单数据值。

typeof 运算符可返回以下原始类型之一：

- string
- number
- boolean
- undefined

typeof 运算符可返回以下两种类型之一：

- function
- object

```js
// type of complex var
document.write(typeof "Bill");             // 返回 "string"
document.write(typeof 3.14);               // 返回 "number"
document.write(typeof true);                // 返回 "boolean"
document.write(typeof false);               // 返回 "boolean"
document.write(typeof x);                   // 返回 "undefined" (假如 x 没有值)
```

### 复杂数据

typeof 运算符可返回以下两种类型之一：

- function
- object

```js
document.write(typeof {name:'Bill', age:62}); // 返回 "object");
document.write(typeof [1,2,3,4]);             // 返回 "object" (并非 "array"，参见下面的注释)
document.write(typeof null);                 // 返回 "object"
document.write(typeof function myFunc(){});   // 返回 "function"
```

## 函数

**JavaScript 函数是被设计为执行特定任务的代码块。**

*JavaScript 函数会在某代码调用它时被执行。*

JavaScript 函数通过 function 关键词进行定义，其后是*函数名*和括号 ()。

```js
// function define
function myFunction(p1, p2) {
    document.write(123);              // 该函数返回 p1 和 p2 的乘积
}
```

### 函数调用

函数中的代码将在其他代码调用该函数时执行：

- 当事件发生时（当用户点击按钮时）
- 当 JavaScript 代码调用时
- 自动的（自调用）

### 函数返回

 return 语句，函数将停止执行

```js
// function return
var x = myFunction(7, 8);        // 调用函数，返回值被赋值给 x

function myFunction(a, b) {
    return a * b;                // 函数返回 a 和 b 的乘积
}

document.getElementById("test").innerHTML += x;
```

### 函数调用

```js
// call functuons
function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
}

document.getElementById("test").innerHTML += toCelsius;
```

### 函数用来赋值

```js
// function result to var
function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
}

var x = toCelsius(77);
var text = "The temperature is " + x + " Celsius";
document.write(x);
document.write(text);
```

### 局部变量

```js
// var in function field
function myFunction() {
    var carName = "Volvo";
    document.write(carName);
    // code here CAN use carName
}

// 此处的代码可以使用 carName
document.write(carName);
```

## 对象

值以*名称:值*对的方式来书写（名称和值由冒号分隔）。

JavaScript 对象是*被命名值*的容器。

```js
//__
var car = {type:"porsche", model:"911", color:"white"};
```

### 属性

名称:值对被称为*属性*。

```js
//__
var person = {firstName:"Bill", lastName:"Gates", age:62, eyeColor:"blue"};
```

| 属性      | 属性值 |
| --------- | ------ |
| firstName | Bill   |
| lastName  | Gates  |
| age       | 62     |
| eyeColor  | blue   |

对象也可以有*方法*。方法是在对象上执行的*动作*。

方法以*函数定义*被存储在属性中。

```js
// object define with function
var person = {
  firstName: "Bill",
  lastName : "Gates",
  id       : 678,
  fullName : function() {
    return "123";
  }
};

document.write(person.fullName());
```

| 属性      | 属性值                     |
| --------- | -------------------------- |
| firstName | Bill                       |
| lastName  | Gates                      |
| age       | 62                         |
| eyeColor  | blue                       |
| fullName  | function() {return "123";} |

### 对象属性

两种方式访问属性

`objectName["propertyName"]` / `objectName.propertyName`

```js
// object get property 
var person = {
  firstName: "Bill",
  lastName : "Gates",
  id       : 678,
  fullName : function() {
    return "123";
  }
};

document.write(person.lastName);
document.write(person["firstName"]);
```

### this

在函数定义中，this 引用该函数的“拥有者”。

在上面的例子中，this 指的是“拥有” fullName 函数的 *person 对象*。

```js
// this case
var person = {
  firstName: "Bill",
  lastName : "Gates",
  id       : 678,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
document.write(person.fullName());
```

### new

如果通过关键词 "new" 来声明 JavaScript 变量，则该变量会被创建为对象：

```js
// new case
var x = new String();        // 把 x 声明为 String 对象
var y = new Number();        // 把 y 声明为 Number 对象
var z = new Boolean();       //	把 z 声明为 Boolean 对象

document.write(x);
document.write(typeof x);
document.write(y);
document.write(typeof y);
document.write(z);
document.write(typeof z);
```

## 事件

HTML 事件可以是浏览器或用户做的某些事情。

下面是 HTML 事件的一些例子：

- HTML 网页完成加载
- HTML 输入字段被修改
- HTML 按钮被点击

```html
<element event='一些 JavaScript'/>
<element event="一些 JavaScript"/>
<button onclick='document.getElementById("demo").innerHTML=Date()'>现在的时间是？</button>
  
```

下面是一些常见的 HTML 事件：

| 事件        | 描述                         |
| ----------- | ---------------------------- |
| onchange    | HTML 元素已被改变            |
| onclick     | 用户点击了 HTML 元素         |
| onmouseover | 用户把鼠标移动到 HTML 元素上 |
| onmouseout  | 用户把鼠标移开 HTML 元素     |
| onkeydown   | 用户按下键盘按键             |
| onload      | 浏览器已经完成页面加载       |

### 字符串

字符串定义 单引号或双引号 

```js
// define string 
var carname = "Porsche 911";
document.write(carname)
var carname = 'Porsche 912';
document.write(carname)
// var carname = `Porsche 913`;
// document.write(carname)
```

### 长度

```js
// str length
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var sln = txt.length;
document.write(sln);
```

### 特殊字符

反斜杠转义字符把特殊字符转换为字符串字符：

| 代码 | 结果 | 描述   |
| ---- | ---- | ------ |
| \'   | '    | 单引号 |
| \"   | "    | 双引号 |
| \\   | \    | 反斜杠 |

```js
// special char 
var y = "中国是瓷器的故乡，因此 china 与\"China（中国）\"同名。";
```

```js
// change line str
document.getElementById("test").innerHTML += "Hello \
Kitty!";

document.getElementById("test2").innerHTML += "Hello" + 
"Kitty!";
```

```js
// new str
var x = "Bill";
var y = new String("Bill");

document.write(x);
document.write(y);
document.write(typeof x);
document.write(typeof y);
document.write(x == y);
document.write(x === y);
```

JavaScript 对象无法进行对比，比较两个 JavaScript 将始终返回 false。

```js
// object str

var x = new String("Bill");
var y = new String("Bill");

document.write(x);
document.write(y);
document.write(typeof x);
document.write(typeof y);
document.write(x == y);
document.write(x === y);
```

### 字符串方法

```js
// str functions


// length
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var sln = txt.length;
document.write(txt);

//indexof/lastIndexOf
var str = "The full name of China is the People's Republic of China.";
var pos = str.indexOf("China");
document.write(pos);
var pos = str.indexOf("XXX");
document.write(pos);
var pos = str.lastIndexOf("China");
document.write(pos);
var pos = str.lastIndexOf("XXX");
document.write(pos);

//search() 返回匹配的位置：
var str = "The full name of China is the People's Republic of China.";
var pos = str.search("locate");
document.write(pos);

// 提取部分字符串
var str = "Apple, Banana, Mango";
var res = str.slice(7,13);
document.write(res);
var res = str.slice(-13,-7);
document.write(res);
var res = str.slice(7);
document.write(res);
var res = str.slice(-13);
document.write(res);

var res = str.substring(7,13);
document.write(res);

// substr 第二个参数为长度
var str = "Apple, Banana, Mango";
var res = str.substr(7,6);
document.write(res);
var str = "Apple, Banana, Mango";
var res = str.substr(7);
document.write(res);

// replace
var str = "Please visit Microsoft and Microsoft!";
var n = str.replace("Microsoft", "W3School");
document.write(str);
document.write(n);
// replace ignore strcase 
var str = "Please visit Microsoft!";
var n = str.replace("/MICROSOFT/i", "W3School");

var text1 = "Hello World!";       // 字符串
var text2 = text1.toUpperCase();  // text2 是被转换为大写的 text1
document.write(text1);
document.write(text2);
var text2 = text1.toLowerCase();  // text2 是被转换为小写的 text1
document.write(text2);

// concat
var text1 = "Hello";
var text2 = "World";
var text3 = text1.concat(" ",text2);
document.write(text3);

// trim
var str = "       Hello World!        ";
document.write(str.trim());

// charAt
var str = "HELLO WORLD";
document.write(str.charAt(0));            // 返回 H
document.write(str[0]);            // 返回 H

// split
var txt = "a,b,c,d,e"; // 字符串
document.write(txt.split(","));          // 用逗号分隔

```

属性访问字符串

使用属性访问有点不太靠谱：

- 不适用 Internet Explorer 7 或更早的版本
- 它让字符串看起来像是数组（其实并不是）
- 如果找不到字符，[ ] 返回 undefined，而 charAt() 返回空字符串。
- 它是只读的。str[0] = "A" 不会产生错误（但也不会工作！）
- 如果找不到字符，[ ] 返回 undefined，而 charAt() 返回空字符串

```js
var str = "HELLO WORLD";
str[0] = "A";             // 不产生错误，但不会工作
document.write(str[0]);                   // 返回 H
```

### 字符串模板

```js
// templaet str
let text = `Hello World!`;
document.write(text);  

let text =
`The quick
brown fox
jumps over
the lazy dog`;
document.write(text);  

let firstName = "John";
let lastName = "Doe";
let text = `Welcome ${firstName}, ${lastName}!`;
document.write(text); 

let price = 10;
let VAT = 0.25;
let total = `Total: ${(price * (1 + VAT)).toFixed(2)}`;
document.write(total); 
```

### 数字方法

```js
// number funcs
var x = 123;
document.write(x.toString());            // 从变量 x 返回 123
document.write((123).toString());        // 从文本 123 返回 123
document.write((100 + 23).toString());   // 从表达式 100 + 23 返回 123

var x = Number.MAX_VALUE;
document.write(x);
var x = Number.MIN_VALUE;
document.write(x);
var x = Number.POSITIVE_INFINITY;
document.write(x);

var x = 6;
var y = x.MAX_VALUE;    // y 成为 undefined
document.write(y);
```

## 数组

```js
// array define
var cars = ["Saab", "Volvo", "BMW"];
document.write(cars);
var cars = new Array("Saab", "Volvo", "BMW");
document.write(cars);
```

添加元素

```js
// add ele to array
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[fruits.length] = "Lemon";     // 向 fruits 添加一个新元素 (Lemon)
document.write(fruits);
```

### 数组和对象的区别

在 JavaScript 中，*数组*使用*数字索引*。

在 JavaScript 中，*对象*使用*命名索引*。

数组方法

```js
// array func
var fruits = ["Banana", "Orange", "Apple", "Mango"];
document.write(fruits.pop());              // 从 fruits 删除最后一个元素（"Mango"）
fruits.push("Kiwi");       //  向 fruits 添加一个新元素
document.write(fruits);  
fruits.shift();
document.write(fruits);
fruits.unshift("Lemon");    // 向 fruits 添加新元素 "Lemon"
document.write(fruits);
fruits[0] = "Kiwi";        // 把 fruits 的第一个元素改为 "Kiwi"
document.write(fruits);
delete fruits[0];           // 把 fruits 中的首个元素改为 undefined
document.write(fruits);
fruits.splice(2, 0, "Lemon", "Kiwi");
document.write(fruits);
fruits.sort();           
document.write(fruits);
fruits.reverse();         // 反转元素顺序
document.write(fruits);


function myFunction(value, index, array) {
  	document.write(value); 
}
numbers.forEach(myFunction);
```



用 const 声明的数组不能重新赋值：

它不定义常量数组。它定义的是对数组的常量引用。

因此，我们仍然可以更改常量数组的元素。



```js
// const array\
const cars = ["Saab", "Volvo", "BMW"];
// 您可以更改元素：
cars[0] = "Toyota";
document.write(cars); 
// 您可以添加元素：
cars.push("Audi");
document.write(cars); 
```

## 逻辑/bool

JavaScript 布尔（逻辑）代表两个值之一：true 或 false

所有具有“真实”值的即为 True

```js
document.write(Boolean(100));
document.write(Boolean(3.14));
document.write(Boolean(-15));
document.write(Boolean("Hello");
document.write(Boolean("false"));
document.write(Boolean(7 + 1 + 3.14));
document.write(Boolean(5 < 6 );
```

所有不具有“真实”值的即为 True

```js
document.write(Boolean(0));
document.write(Boolean(-0));
document.write(Boolean(""));
document.write(Boolean(undefined));
document.write(Boolean(false));
document.write(Boolean(NaN));
```

## comapre

三元运算法

```js
// three operator
var age = 10;
var voteable = (age < 18) ? "yang":"old";
document.write(Boolean(voteable));
document.write(voteable);
```

## 流程控制

请使用 if 语句来规定假如条件为 true

```js
// if case
if(true){
  document.write("true");
}
```

```js
// if else
if(false){
  document.write("true");
}else{
  document.write("false");
}

if(true){
  document.write("true");
}else{
  document.write("false");
}
```

```js
// if else if
var age = 18;
if (age < 18){
 	document.write("yang");
}else if( age > 60){
  document.write("old");
}else{
  document.write("alive");
}

var age = 8;
if (age < 18){
 	document.write("yang");
}else if( age > 60){
  document.write("old");
}else{
  document.write("alive");
}

var age = 70;
if (age < 18){
 	document.write("yang");
}else if( age > 60){
  document.write("old");
}else{
  document.write("alive");
}
```

## switch

```js
// switch without break
// switch case
var day;
switch (new Date().getDay()) {
  case 0:
    day = "周日";
  case 1:
    day = "周一";
  case 2:
    day = "周二";
  case 3:
    day = "周三";
  case 4:
    day = "周四";
  case 5:
    day = "周五";
  case  6:
    day = "周六";
}
document.getElementById("test").innerHTML = "今天是" + day; 
```

```js
// switch break case
var day;
switch (new Date().getDay()) {
  case 0:
    day = "周日";
    break;
  case 1:
    day = "周一";
    break;
  case 2:
    day = "周二";
    break;
  case 3:
    day = "周三";
    break;
  case 4:
    day = "周四";
    break;
  case 5:
    day = "周五";
    break;
  case  6:
    day = "周六";
    break;
}
document.getElementById("test").innerHTML = "今天是" + day; 
```

- 计算一次 switch 表达式
- 把表达式的值与每个 case 的值进行对比
- 如果存在匹配，则执行关联代码

```js
// switch with default
switch (new Date().getDay()) {
    case 6:
        text = "今天是周六";
        break; 
    case 0:
        text = "今天是周日";
        break; 
    default: 
        text = "期待周末~";
} 
document.getElementById("test").innerHTML = text; 
```

```js
// switch with default
switch (new Date().getDay()) {
 case 4:
    case 5:
        text = "周末快到了：）";
        break; 
    case 0:
    case 6:
        text = "今天是周末~";
         break;
    default: 
        text = "期待周末！";
} 
document.getElementById("test").innerHTML = text; 
```

Switch case 使用严格比较（===）

```js
// switch with same value but different type
var x = "0";
switch (x) {
  case 0:
    text = "Off";
    break;
  case 1:
    text = "On";
    break;
  default:
    text = "No value found";
}
```

## for 循环

```js
// for 
for (i = 0; i < 5; i++) {
     text += "数字是 " + i + "<br>";
}
document.write(text);
```

``` js
// for with multi init
var cars = ["BMW", "Volvo", "porsche", "Ford"];
var i, len, text;
for (i = 0, len = cars.length, text = ""; i < len; i++) {
  text += cars[i] + "<br>";
}
document.getElementById("test").innerHTML += text;
```

```js
// for without init
var i = 2;
var cars = ["BMW", "Volvo", "porsche", "Ford"];
var len = cars.length;
var text = "";
for (; i < len; i++) { 
    text += cars[i] + "<br>";
}
document.write(text);
```

```js
// for without end condition
var text = "";
for (i = 2; ; i+=i) { 
		text += i;
  	if (i > 500){
      break;
    }
}
document.write(text);
```

```js
// for without increase var
var i = 2;
var text = "";
for (i = 0; i< 500; ) { 
		i += i;
  	text += i;
}
document.write(text);
```

```js
// for without condition
var i = 2;
var text = "";
for (; ; ) { 
		i += i;
  	text += i;
  	if (i > 500){
      break;
    }
}
document.write(text);
```

```js
// for in
var person = {fname:"Bill", lname:"Gates", age:62}; 

var text = "";
var x;
for (x in person) {
    text += person[x];
}
document.write(text);
```

```js
// for init in 
var person = {fname:"Bill", lname:"Gates", age:62}; 

var text = "";
for (var x in person) {
    text += person[x];
}
document.write(text);
```

```js
// for in array
const numbers = [45, 4, 9, 16, 25];

let txt = "";
for (let x in numbers) {
  txt += numbers[x];
}
document.write(text);
```

```js
// array forEach
const numbers = [45, 4, 9, 16, 25];

let txt = "";
numbers.forEach(myFunction);

function myFunction(value, index, array) {
  txt += value;
}
document.write(txt);
```

```js
// for of

const cars = ["BMW", "Volvo", "Mini"];
let text = "";
for (let x of cars) {
  text += x;
}
document.write(txt);
```

```js
// while
var text = "";
while (i < 10) {
    text += "数字是 " + i;
    i++;
}
document.write(txt);
```

```js
// do while
var text = "";
do {
    text += "The number is " + i;
    i++;
 }
while (i < 10);
document.write(text);
```

```js
// for break
text = ""
for (i = 0; i < 10; i++) {
    if (i === 3) { break; }
    text += "数字是 " + i + "<br>";
}
document.write(text);
```

```js
// for continue
text = ""
for (i = 0; i < 10; i++) {
    if (i % 2) { continue; }
    text += "数字是 " + i + "<br>";
}
document.write(text);
```

```js
// do while break
var text = "";
do {
    text += "The number is " + i;
    i++;
  	if (i == 3) { break; }
 }
while (i < 10);
document.write(text);
```

```js
// do while continue
var text = "";
do {
    i++;
  	if (i % 2) { continue; }
  	text += "The number is " + i;
 }
while (i < 10);
document.write(text);
```

```js
// while continue
var text = "";
while (i < 10) {
    text += "数字是 " + i;
  	if (i % 2) { continue; }
    i++;
}
document.write(text);
```

```js
// while break
var text = "";
while (i < 10) {
    text += "数字是 " + i;
  	if (i == 3) { break; }
    i++;
}
document.write(text);
```

## label

```js
// label
var  cars = ["BMW", "Volvo", "Saab", "Ford", "Xiaopeng","Weilai"];
var text = "";
list: {
    text += cars[0] + "<br>"; 
    text += cars[1] + "<br>"; 
    text += cars[2] + "<br>"; 
    text += cars[3] + "<br>"; 
    text += cars[4] + "<br>"; 
    text += cars[5] + "<br>"; 
}
document.write(text);
```

```js
// label break
var  cars = ["BMW", "Volvo", "Saab", "Ford", "Xiaopeng","Weilai"];
var text = "";
list: {
    text += cars[0] + "<br>"; 
    text += cars[1] + "<br>"; 
    text += cars[2] + "<br>"; 
    break list;
    text += cars[3] + "<br>"; 
    text += cars[4] + "<br>"; 
    text += cars[5] + "<br>"; 
}
document.write(text);
```

## type

### typeof

```js
// typeof
document.write(typeof "John");                // 返回 "string"
document.write(typeof 3.14);                   // 返回 "number"
document.write(typeof NaN);                    // 返回 "number"
document.write(typeof false);                  // 返回 "boolean"
document.write(typeof [1,2,3,4]);             // 返回 "object"
document.write(typeof {name:'John', age:34});  // 返回 "object"
document.write(typeof new Date());             // 返回 "object"
document.write(typeof function () {});         // 返回 "function"
document.write(typeof myCar);                  // 返回 "undefined" *
document.write(typeof null);                   // 返回 "object"
```

### constructor

```js
// constructor
// 属性返回所有 JavaScript 变量的构造函数。JavaScript 变量的构造函数。

document.write("Bill".constructor);              // 返回 function String()  {[native code]}
document.write((3.14).constructor);                // 返回 function Number()  {[native code]}
document.write(false.constructor);                 // 返回 function Boolean() {[native code]}
document.write([1,2,3,4].constructor);             // 返回 function Array()   {[native code]}
document.write({name:'Bill',age:19}.constructor);  // 返回 function Object()  {[native code]}
document.write(new Date().constructor);            // 返回 function Date()    {[native code]}
document.write(function () {}.constructor);        // 返回 function Function(){[native code]}
```

### type recast

```js
// to string
document.write(String(123));
document.write(String(100 + 23));
document.write(String("123"));
document.write(String(true));
document.write(String(false));
document.write(String(undefined));
document.write(String([1,2,3]));
document.write(String(Date()));
```

```js
// to Number
document.write(Number("3.14"));    // 返回 3.14
document.write(Number(" "));       // 返回 0
document.write(Number(""));        // 返回 0
document.write(Number("99 88"));   // 返回 NaN
document.write(Number(false));     // 返回 0
document.write(Number(true));      // 返回 1

var d = new Date();
document.write(parseInt(d)/100);
```
```js
// to number with add sign
var y = "5";      // y 是字符串
var x = + y;      // x 是数字
document.write(x);

var y = "Bill";   // y 是字符串
var x = + y;      // x 是数字 (NaN)
document.write(x);
```

```js
// auto parsered
document.write(5 + null);    // 返回 5         因为 null 被转换为 0
document.write("5" + null);  // 返回 "5null"   因为 null 被转换为  "null"
document.write("5" + 2);     // 返回 52        因为 2 被转换为 "2"
document.write("5" - 2);     // 返回 3         因为 "5" 被转换为 5
document.write("5" * "2");   // 返回 10        因为 "5" 和 "2" 被转换为 5 和 2
```

| 原始值           | 转换为数字 | 转换为字符串      | 转换为逻辑 |
| ---------------- | ---------- | ----------------- | ---------- |
| false            | 0          | "false"           | false      |
| true             | 1          | "true"            | true       |
| 0                | 0          | "0"               | false      |
| 1                | 1          | "1"               | true       |
| "0"              | 0          | "0"               | **true**   |
| "000"            | 0          | "000"             | **true**   |
| "1"              | 1          | "1"               | true       |
| NaN              | NaN        | "NaN"             | false      |
| Infinity         | Infinity   | "Infinity"        | true       |
| -Infinity        | -Infinity  | "-Infinity"       | true       |
| ""               | **0**      | ""                | **false**  |
| "20"             | 20         | "20"              | true       |
| "twenty"         | NaN        | "twenty"          | true       |
| [ ]              | **0**      | ""                | true       |
| [20]             | **20**     | "20"              | true       |
| [10,20]          | NaN        | "10,20"           | true       |
| ["twenty"]       | NaN        | "twenty"          | true       |
| ["ten","twenty"] | NaN        | "ten,twenty"      | true       |
| function(){}     | NaN        | "function(){}"    | true       |
| { }              | NaN        | "[object Object]" | true       |
| null             | **0**      | "null"            | false      |
| undefined        | NaN        | "undefined"       | false      |

## 位运算

| 运算符 | 名称         | 描述                                                     |
| ------ | ------------ | -------------------------------------------------------- |
| &      | AND          | 如果两位都是 1 则设置每位为 1                            |
| \|     | OR           | 如果两位之一为 1 则设置每位为 1                          |
| ^      | XOR          | 如果两位只有一位为 1 则设置每位为 1                      |
| ~      | NOT          | 反转所有位                                               |
| <<     | 零填充左位移 | 通过从右推入零向左位移，并使最左边的位脱落。             |
| >>     | 有符号右位移 | 通过从左推入最左位的拷贝来向右位移，并使最右边的位脱落。 |
| >>>    | 零填充右位移 | 通过从左推入零来向右位移，并使最右边的位脱落。           |

JavaScript 将数字存储为 **64 位浮点数**，但所有按位运算都以 32 位二进制数执行

```js
// operation and
document.write(0 & 0);
document.write(0 & 1);
document.write(1 & 0);
document.write(1 & 1);

document.write(1111 & 0000);
document.write(1111 & 0001);
document.write(1111 & 0010);
document.write(1111 & 0100);

```

````js
// operation or
document.write(0 | 0);
document.write(0 | 1);
document.write(1 | 0);
document.write(1 | 1);

document.write(1111 | 0000);
document.write(1111 | 0001);
document.write(1111 | 0010);
document.write(1111 | 0100);
````

```js
// operation xor
document.write(0 ^ 0);
document.write(0 ^ 1);
document.write(1 ^ 0);
document.write(1 ^ 1);

document.write(1111 ^ 0000);
document.write(1111 ^ 0001);
document.write(1111 ^ 0010);
document.write(1111 ^ 0100);
```

```js
// operation not
document.write(~5);
```

```js
// operation left shift
var x = 5 << 1;
document.write(x);
```

```js
// operation right shift
var x = -5 >> 1;
document.write(x);
```

```js
// operation right shift fill zero
document.write(x);
```

## 正则

正则表达式是构成*搜索模式（search pattern）*的字符序列。

```js
//__
/pattern/modifiers;
var patt = /w3school/i;
```

```js
//regex example
var patt = /w3school/i;
var str = "Visit W3School";
var n = str.search(patt); 
document.write(patt);
document.write(str);
document.write(n);
```

| 修饰符 | 描述                                                     |
| ------ | -------------------------------------------------------- |
| i      | 执行对大小写不敏感的匹配。                               |
| g      | 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。 |
| m      | 执行多行匹配。                                           |

test() 是一个正则表达式方法。

它通过模式来搜索字符串，然后根据结果返回 true 或 false。

```js
// regex test
var patt = /e/;
var res = patt.test("The best things in life are free!"); 
document.write(res);

var res = /e/.test("The best things in life are free!");
document.write(res);
```

exec() 方法是一个正则表达式方法。它通过指定的模式（pattern）搜索字符串，并返回已找到的文本。

如果未找到匹配，则返回 null。

```js
// regex exec
var context = "The best things in life are free!";
var res = /e/.exec(context);
document.write(res);

var res = /z/.exec(context);
document.write(res);
```

## 异常处理

当发生错误时，JavaScript 通常会停止并产生错误消息。

技术术语是这样描述的：*JavaScript 将抛出异常（抛出错误）*。

JavaScript 实际上会创建带有两个属性的 *Error 对象*：name 和 message

```js
// try catch
try {
    var x;
  	document.write(x.err);
  	document.write("not shown");
}
 catch(err) {
     document.write(err);
}
```

```js
// try throw catch
try {
    var x;
  	throw "I AM ERROR. XD";
  	document.write("not shown");
}catch(err) {
     document.write(err);
}
```

```js
// try catch finally
try {
  	throw "THIS IS MY FINAL RIPPLE, ";
  	document.write("not shown");
}
catch(err) {
     document.write(err);
} 
finally {
     document.write("JOJO!!");
}
```

| 错误名         | 描述                          |
| -------------- | ----------------------------- |
| EvalError      | 已在 eval() 函数中发生的错误  |
| RangeError     | 已发生超出数字范围的错误      |
| ReferenceError | 已发生非法引用                |
| SyntaxError    | 已发生语法错误                |
| TypeError      | 已发生类型错误                |
| URIError       | 在 encodeURI() 中已发生的错误 |

```js
// err Range Error
var num = 1;
try {
    num.toPrecision(500);   // 数无法拥有 500 个有效数
 }
catch(err) {
  document.write(err.name);
} 
```

```js
// err ReferenceError
var x;
try {
  x = y + 1;   // y 无法被引用（使用）
}catch(err) {
	document.write(err.name);
}
```

```js
// err SyntaxError
try {
    eval("alert('Hello)");   // 缺少 ' 会产生错误
}
catch(err) {
   document.write(err.name);
} 
```

```js
// err typeError
var num = 1;
try {
    num.toUpperCase();   // 您无法将数字转换为大写
}
catch(err) {
  document.write(err.name);
} 
```

```js
// err URL
try {
    decodeURI("%%%");   // 您无法对这些百分号进行 URI 编码
 }
catch(err) {
   	document.write(err.name);
} 
```

## 提升

在 JavaScript 中，可以在使用变量之后对其进行声明。

换句话说，可以在声明变量之前使用它。

```js
// Hoisting
x = 5; // 把 5 赋值给 x
 
elem = document.getElementById("test"); // 查找元素
elem.innerHTML = x;                     // 在元素中显示 x
var x; // 声明 x
```

```js
// Hoisting and not init
var x = 5; // 初始化 x
 
elem = document.getElementById("demo"); // 查找元素
elem.innerHTML = x + " " + y;           // 显示 x 和 y
 
var y = 7; // 初始化 y 
```

## 严格模式

"use strict" 是 JavaScript 1.8.5 中的新指令（ECMAScript version 5）。

"use strict"; 的作用是指示 JavaScript 代码应该以“严格模式”执行。

```js
// use strict use undeclared var
"use strict";
try{
  x = 3.14;
  var x;
}catch(err){
  document.write(err.name);
}
```

```js
// use strict delete var
"use strict";
try{
  var x = 3.14;
	delete x;   
  document.write(x);
}catch(err){
  document.write(err.name);
}
```

不声明对象的情况下使用对象也是不允许的：

```js
// use strict use undeclared obj
"use strict";
try{
  x = {p1:10, p2:20};      // 这将引发错误 
  document.write(x);
}catch(err){
  document.write(err.name);
}

```

删除函数是不允许的：

```js
// use strict delete func
"use strict";
try{
  function x(p1, p2) {}; 
  delete x;                 // 这将引发错误
  document.write(x);
}catch(err){
  document.write(err.name);
}


```

重复参数名是不允许的：

```js
// use strict declare func with same param
"use strict";
try{
	function x(p1, p1) {};   // 这将引发错误  
  document.write(x);
}catch(err){
  document.write(err.name);
}
```

八进制数值文本是不允许的：

```js
// use strict declare with OCT text	
"use strict";
try{
	var x = 010;             // 这将引发错误
  document.write(x);
}catch(err){
  document.write(err.name);
}

```

转义字符是不允许的：

```js
// use strict escape chars
"use strict";
try{
	var x = \010;            // 这将引发错误
  document.write(x);
}catch(err){
  document.write(err.name);
}

```

写入只读属性是不允许的：

```js
// use strict write to readonly property
"use strict";
try{
  var obj = {};
  Object.defineProperty(obj, "x", {value:0, writable:false});
  obj.x = 3.14;            // 这将引发错误
  document.write(x);
}catch(err){
  document.write(err.name);
}

```

写入只能获取的属性是不允许的：

```js
// use strict delete
"use strict";
try{
  var obj = {get x() {return 0} };
	obj.x = 3.14;  // 这将引发错误
}catch(err){
  document.write(err.name);
}
```

删除不可删除的属性是不允许的：

```js
// use strict delete
"use strict";
try{
 	delete Object.prototype; // 这将引发错误
}catch(err){
  document.write(err.name);
}
```

字符串 "eval" 不可用作变量：

```js
// use strict delete
"use strict";
try{
	var eval = 3.14;         // 这将引发错误
  document.write(eval);
}catch(err){
  document.write(err.name);
}
```

字符串 "arguments" 不可用作变量：

```js
// use strict delete
"use strict";
try{
  var arguments = 3.14;    // 这将引发错误   
  document.write(arguments);
}catch(err){
  document.write(err.name);
}

```

with 语句是不允许的：

```js
// use strict delete
"use strict";
try{
	with (Math){document.write(cos(2))}; // 这将引发错误  
}catch(err){
  document.write(err.name);
}
```

处于安全考虑，不允许 eval() 在其被调用的作用域中创建变量：

```js
// use strict delete
"use strict";
try{
	eval ("var x = 2");
  document.write(x);
}catch(err){
  document.write(err.name);
}
```

## this

- 在方法中，this 指的是所有者对象。
- 单独的情况下，this 指的是全局对象。
- 在函数中，this 指的是全局对象。
- 在函数中，严格模式下，this 是 undefined。
- 在事件中，this 指的是接收事件的元素。

```js
// this in object
var person = {
  firstName: "Bill",
  lastName : "Gates",
  id     : 678,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

// 显示来自对象的数据：
document.write(person.fullName());
```

```js
// this in module
var x = this;
document.write(x);
```

```js
// this in module use strict 
"use strict";
var x = this;
document.write(x);
```

```js
// this in func
function myFunction() {
  return this;
}
document.write(myFunction());
```

```js
// this in func use strict
"use strict";
function myFunction() {
  return this;
}
document.write(myFunction());
```

```js
// this with call
var person1 = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
var person2 = {
  firstName:"Bill",
  lastName: "Gates",
}
var res = person1.fullName.call(person2);  // 会返回 "Bill Gates"
document.write(res);
```

## 箭头函数

```js
// arrow func
const hello = function() {
  return "Hello World!";
}
document.write(hello());
```

```js
// arrow func with param
hello = (val) => "Hello " + val;
document.write(hello("Robot"));
```

```js
// arrow with called object
// 箭头函数：
hello = () => {
  document.write += this;
}

// window 对象调用该函数：
window.addEventListener("load", hello);
```

