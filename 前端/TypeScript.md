# TypeScript

> 参考：https://juejin.cn/post/7092415149809598500#heading-0

## 安装

```
npm i -g typescript
yarn global add  typescript
```

查看版本

```
tsc -v
```

## 类型

### 变量声明

```typescript
let 变量名: 类型 = 初始值
let age: number = 18
```

### 类型类别

ts 的常用基础类型分为两种

* js 已有类型
  * 原始类型：`number/string/boolean/null/undefined/symbol`
  * 对象类型：`object`（包括，数组、对象、函数等对象）
* ts 新增
  - 联合类型
  - 自定义类型(类型别名)
  - 接口
  - 元组
  - 字面量类型
  - 枚举
  - void
  - any

类型推论在某些没有明确指定类型的情况下，**TS 的类型推论机制会自动提供类型**。

由于类型推论的存在，有些情况下的类型注解可以省略不写 有如下两种场景：

1. 声明变量并初始化时
2. 决定函数返回值时

### 联合类型

```typescript
let 变量: 类型1 | 类型2 | 类型3 .... = 初始值
let arr1 :number | string = 1 // 可以写两个类型
```

### 类型别名

```typescript
type 别名 = 类型
type s = string // 定义
const str1:s = 'abc'
const str2:string = 'abc'
```

### 数组类型

```typescript
// 写法1：
let 变量: 类型[] = [值1，...]:
let numbers: number[] = [1, 3, 5] 
//  numbers必须是数组，每个元素都必须是数字
// 写法2：
let 变量: Array<类型> = [值1，...]
let strings: Array<string> = ['a', 'b', 'c'] 
//  strings必须是数组，每个元素都必须是字符串
```

### 元组

**元组**是一种特殊的**数组**。有两点特殊之处

1. 它约定了的元素个数
2. 它约定了特定索引对应的数据类型

```typescript
function useState(n: number): [number, (number)=>void] {
        const setN = (n1) => {
            n = n1
        }
        return [n, setN]
    }

const [num ,setNum] = useState(10)
```

### 字面量

字面量类型一般是配合联合类型一起使用的， 用来表示一组明确的可选值列表。

```typescript
let str1 = 'hello TS'
const str2 = 'hello TS'
```

1. str1 是一个变量(let)，它的值可以是任意字符串，所以类型为:string
2. str2 是一个常量(const)，它的**值不能变化**只能是 'hello TS'，所以，它的类型为:'hello TS'

```typescript
type Gender = 'girl' | 'boy'
// 声明一个类型，他的值 是 'girl' 或者是 'boy'
let g1: Gender = 'girl' // 正确
let g2: Gender = 'boy' // 正确
let g3: Gender = 'man' // 错误
```

### 枚举

```typescript
enum 枚举名 { 可取值1, 可取值2,.. }

枚举名.可取值
```

1. 一般枚举名称以大写字母开头
2. 枚举中的多个值之间通过 `,`（逗号）分隔
3. 定义好枚举后，直接使用枚举名称作为类型注解

#### 数值枚举 和 字符串枚举

从 0 开始自增的数值 当然，也可以给枚举中的成员初始化值

```typescript
enum Direction { Up = 10, Down, Left, Right }
// Down -> 11、Left -> 12、Right -> 13

enum Direction { Up = 2, Down = 3, Left = 8, Right = 16 }
复制代码
```

字符串枚举：

```typescript
enum Direction {
  Up = 'UP',
  Down = 'DOWN',
  Left = 'LEFT',
  Right = 'RIGHT'
}
复制代码
```

注意：字符串枚举没有自增长行为，因此，**字符串枚举的每个成员必须有初始值**

### any

any: 任意的。当类型设置为 any 时，就取消了类型的限制

- 数就是不挑类型。 例如，`console.log()` ； 定义一个函数，输入任意类型的数据，返回该数据类型
- **临时使用** any 来“避免”书写很长、很复杂的类型

还有一种隐式 any，有下面两种情况会触发

1. 声明变量不提供类型也不提供默认值
2. 定义函数时，参数不给类型

## 函数

```typescript
// 普通函数
function 函数名(形参1： 类型=默认值， 形参2：类型=默认值,...): 返回值类型 { }
// 声明式实际写法:
function add(num1: number, num2: number): number {
  return num1 + num2
}

// 箭头函数
const 函数名（形参1： 类型=默认值， 形参2：类型=默认值, ...):返回值类型 => { }
const add2 = (a: number =100, b: number = 100): number =>{
   return a + b
 }
 // 注意： 箭头函数的返回值类型要写在参数小括号的后面
add（1,'1') // 报错
```

### 统一定义函数格式

当函数的类型一致时，写多个就会显得代码冗余，所以需要统一定义函数的格式 如下所示：

```typescript
const add2 = (a: number =100, b: number = 100): number => {
    return a + b
  }

function add1 (a:number = 100 , b: number = 200): number {
    return a + b
}

// 这里的 add1 和 add2 的参数类型和返回值一致，
// 那么就可以统一定义一个函数类型
type Fn = (n1:number,n2:number) => number 
const add3 : Fn = (a,b)=>{return a+b }
// 这样书写起来就简单多啦
复制代码
```

### 函数返回值类型void

在 ts 中，如果一个函数没有返回值，应该使用 `void` 类型

```typescript
function greet(name: string): void {  console.log('Hello', name)  //}
```

### 可选参数

可选参数：在可选参数名的后面添加 ?（问号）

```typescript
function slice (a?: number, b?: number) {
    // ? 跟在参数名字的后面，表示可选的参数
    // 注意：可选参数只能在 必须参数的后面
    // 如果可选参数在必选参数的前面，会报错
    console.log(111);
    
  }
  slice()
  slice(1)
  slice(1,2)
}
```

可选和默认值的区别

设置了默认值之后，就是可选的了，不写就会使用默认值； 可选的参数一定有值。

默认值和可选参数不能同时使用，优先使用默认值

## 类型别名

```typescript
// 创建类型别名
type Person = {
  name: string，
  age: number
  sayHi(): void
}

// 使用类型别名作为对象的类型：
let person: Person = {
  name: '小花',
  age: 18
  sayHi() {}
}
```

## 接口

当一个对象类型被多次使用时，有如下两种方式来来**描述对象**的类型，以达到复用的目的：

1. 类型别名，type
2. 接口，interface

### 语法

```typescript
interface 接口名  {属性1: 类型1, 属性2: 类型2}
```

```typescript
interface IGoodItem  {
	// 接口名称(比如，此处的 IPerson)，可以是任意合法的变量名称，推荐以 `I` 开头
   name: string, price: number, func: ()=>string
}
```

接口和类型 的区别 `interface`（接口）和` type`（类型别名）的对比：

- 相同点：都可以给对象指定类型
- 不同点:
  - 接口，只能为对象指定类型。**它可以继承。**
  - 类型别名，不仅可以为对象指定类型，实际上可以为**任意类型**指定别名

### 继承

如果两个接口之间有相同的属性或方法，可以将**公共的属性或方法抽离出来，通过继承来实现复用** 语法

```typescript
interface 接口2 extends 接口1 {
 属性1： 类型1， // 接口2中特有的类型 
 }
```

```typescript
interface a { x: number; y: number }
// 继承 a
// 使用 extends(继承)关键字实现了接口
interface b extends a {
  z: number
}
// 继承后，b 就有了 a 的所有属性和方法(此时，b 同时有 x、y、z 三个属性)
复制代码
```