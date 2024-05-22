---
title: PlantUML
tag: [计算机课程学习,软工,]
---
# PlantUML
> 参考教程 https://plantuml.com/zh/starting
> 不再频繁更新 感觉就是在抄官网的 = =
## 简介

**PlantUML**是一个开源项目，支持快速绘制：

- [时序图](https://plantuml.com/zh/sequence-diagram)
- [用例图](https://plantuml.com/zh/use-case-diagram)
- [类图](https://plantuml.com/zh/class-diagram)
- [对象图](https://plantuml.com/zh/object-diagram)
- [活动图](https://plantuml.com/zh/activity-diagram-beta) ([旧版语法](https://plantuml.com/zh/activity-diagram-legacy)在此处)
- [组件图](https://plantuml.com/zh/component-diagram)
- [部署图](https://plantuml.com/zh/deployment-diagram)
- [状态图](https://plantuml.com/zh/state-diagram)
- [定时图](https://plantuml.com/zh/timing-diagram)

同时还支持以下非UML图：

- [JSON 数据](https://plantuml.com/zh/json)
- [YAML 数据](https://plantuml.com/zh/yaml)
- [网络图 (nwdiag)](https://plantuml.com/zh/nwdiag)
- [线框图形界面](https://plantuml.com/zh/salt)
- [架构图](https://plantuml.com/zh/archimate-diagram)
- [规范和描述语言 (SDL)](https://plantuml.com/zh/activity-diagram-beta#sdl)
- [Ditaa 图](https://plantuml.com/zh/ditaa)
- [甘特图](https://plantuml.com/zh/gantt-diagram)
- [思维导图](https://plantuml.com/zh/mindmap-diagram)
- [WBS 工作分解图](https://plantuml.com/zh/wbs-diagram)
- [以 AsciiMath 或 JLaTeXMath 符号的数学公式](https://plantuml.com/zh/ascii-math)
- [实体关系图](https://plantuml.com/zh/ie-diagram)

## 时序图

### 语法

`->`绘制参与者之间传递的信息

`-->`绘制虚线箭头

可以自己给自己发消息

> `<-`,`<--`也是可行的

#### 参与者声明

使用 `participant` 关键字来声明一个参与者可以使你对参与者做出更多控制。

关键字 `participant` 用于改变参与者的先后顺序。

你也可以使用下面这些关键字来声明参与者，这会**改变参与者的外观**：

- `actor`（角色）
- `boundary`（边界）
- `control`（控制）
- `entity`（实体）
- `database`（数据库）
- `collections`（集合）
- `queue`（队列）

#### 参与者重命名

participant L  as "longlonglongName"

participant "longlonglongName" as L

### 打印顺序

order 自定义顺序打印参与者

### 文本对齐

`skinparam responseMessageBelowArrow true`命令，让响应信息显示在箭头下面

### 修改箭头样式

修改箭头样式的方式有以下几种:

- 表示一条丢失的消息：末尾加 `x`

- 让箭头只有上半部分或者下半部分：将`<`和`>`替换成`\`或者 `/`

- 细箭头：将箭头标记写两次 (如 `>>` 或 `//`)

- 虚线箭头：用 `--` 替代 `-`

- 箭头末尾加圈：`->o`

- 双向箭头：`<->`

  ```uml
  @startuml
  Bob ->x Alice
  Bob -> Alice
  Bob ->> Alice
  Bob -\ Alice
  Bob \\- Alice
  Bob //-- Alice
  
  Bob ->o Alice
  Bob o\\-- Alice
  
  Bob <-> Alice
  Bob <->o Alice
  @enduml
  ```

  ![img](https://s.plantuml.com/imgw/img-39e8d62171fb94d07f26e6e0f9aa1605.webp)

### 箭头颜色

```
-[#red]>
-[#0000FF]->
```

### 消息序列编号

`autonumber` 用于自动消息编号

`automember start increment ` 设置编号初始值和每次增加的值

`automember <b>`指定编号的格式

`autonumber stop` 和 `autonumber resume increment format` 来表示暂停或继续使用自动编号。

```
@startuml
autonumber 10 10 "<b>[000]"
Bob -> Alice : Authentication Request
Bob <- Alice : Authentication Response

autonumber stop
Bob -> Alice : dummy

autonumber resume "<font color=red><b>Message 0  "
Bob -> Alice : Yet another authentication Request
Bob <- Alice : Yet another authentication Response

autonumber stop
Bob -> Alice : dummy

autonumber resume 1 "<font color=blue><b>Message 0  "
Bob -> Alice : Yet another authentication Request
Bob <- Alice : Yet another authentication Response
@enduml
```

![img](https://s.plantuml.com/imgw/img-239a7f79a3bdaf2a3884c5b34070d157.webp)

### 页面标题,页眉,页脚

使用`title`关键词增加标题
使用`header`关键词增加页眉
使用`footer`关键词增加页脚

###  分割示意图

`newpage`将一张图分割成多张

### 消息分组

我们可以通过以下关键词来组合消息，在标头(header )添加需要显示的文字 用end来结束分组，可以嵌套使用

- `alt/else`
- `opt`
- `loop`
- `par`
- `break`
- `critical`
- `group`, 后面紧跟着消息内容 在表头处的[和]显示刺激文本

```
@startuml 
Alice -> Bob: 认证请求 
alt 成功情况     
	Bob -> Alice: 认证接受 
else 某种失败情况     
	Bob -> Alice: 认证失败    
group 我自己的标签    
	Alice -> Log : 开始记录攻击日志        
	loop 1000次            
		Alice -> Bob: DNS 攻击        
    end    
    Alice -> Log : 结束记录攻击日志    
    end 
else 另一种失败    
	Bob -> Alice: 请重复 
end 
@enduml 
```

![img](https://s.plantuml.com/imgw/img-7fb7ee2943a57639d0df6dec787c6c01.webp)

### 注释

消息后添加 note left 或者 note right 添加注释 使用 end note 添加多行注释

可以使用`note left of`，`note right of`或`note over`在节点(participant)的相对位置放置注释。

还可以通过修改背景色来高亮显示注释

以及使用关键字`end note`来添加多行注释。

![img](https://s.plantuml.com/imgw/img-b4364b99e1e95b5f9f457c38d9501a67.webp)

### 分割符

使用==关键字来将图标分割成多个逻辑步骤

### 引用

使用 ref over 来实现引用,使用...来表示延迟。

### 延时

使用`...`表示延时,还可以给延时添加注释

### 文本换行

使用`\n`

### 空间

使用`|||`增加空间

生命线的激活与撤销

关键字`activate`和`deactivate`用来表示参与者的生命活动。

一旦参与者被激活，它的生命线就会显示出来。

`activate`和`deactivate`适用于以上情形。

`destroy`表示一个参与者的生命线的终结。

```sh
@startuml
participant User

User -> A: DoWork
activate A

A -> B: << createRequest >>
activate B

B -> C: DoWork
activate C
C --> B: WorkDone
destroy C

B --> A: RequestCreated
deactivate B

A -> User: Done
deactivate A

@enduml
# 
@startuml
participant User

User -> A: DoWork
activate A #FFBBBB

A -> A: Internal call
activate A #DarkSalmon

A -> B: << createRequest >>
activate B

B --> A: RequestCreated
deactivate B
deactivate A
A -> User: Done
deactivate A

@enduml

#也可以使用自动激活关键字（autoactivate），这需要与return关键字配合
@startuml
autoactivate on
alice -> bob : hello
bob -> bob : self call
bill -> bob #005500 : hello from thread 2
bob -> george ** : create
return done in thread 2
return rc
bob -> george !! : delete
return success

@enduml
```

### 返回

新命令`return`可以用于生成一个带有可选文本标签的返回信息。返回的点是导致最近一次激活生命线的点。语法是简单的返回标签，其中标签（如果提供）可以是传统信息中可以接受的任何字符串。

### 创建参与者

你可以把关键字`create`放在第一次接收到消息之前，以强调本次消息实际上是在*创建*新的对象。

### 进入与发出消息

使用 `[` 和`]`表示图示的左右两侧

```
@startuml
participant Alice
participant Bob #lightblue
Alice -> Bob
Bob -> Carol
...
[-> Bob
[o-> Bob
[o->o Bob
[x-> Bob
...
[<- Bob
[x<- Bob
...
Bob ->]
Bob ->o]
Bob o->o]
Bob ->x]
...
Bob <-]
Bob x<-]

@enduml
```

![img](https://s.plantuml.com/imgw/img-85eb1ac81d8a2f5064d87a2417dede48.webp)

## 用例图

 用例用圆括号括起来也可以使用usecase来定义  用关键字as 定义别名

```
@startuml

(First usecase)
(Another usecase) as (UC2)
usecase UC3
usecase (Last\nusecase) as UC4

@enduml
```

### 角色

角色用两个冒号括起来 也可以使用`actor` 来定义角色 使用`as` 来定义别名

### 角色样式

```
用户头像样式：skinparam actorStyle awesome
透明人样式：skinparam actorStyle hollow
```

### 用例描述

如果想定义跨越多行的用例描述，可以用双引号将其裹起来。

还可以使用这些分隔符：

- `--`（横线）
- `..`（虚线）
- `==`（双横线）
- `__`（下划线）

并且还可以在分隔符中间放置标题。

### 包

使用`package`对角色或用例进行分组

基础示例

使用`-->`横杠-越多 箭头越长在后面添加`:`的方式添加标签

### 继承

如果一个角色或用例继承于另一个 则用 <|-- 符号表示

### 构造类型

用 `<<` 和 `>>` 来定义角色或者用例的构造类型。

### 箭头方向

箭头默认方向是述职方向 用 `-`(一个)或者点表示水平链接

添加 left.right,up,down 改变方向

### 分割图示

使用newpage  将图示分解为多个页面

### 从左往右构建

默认为从上往下构建

left to right direction



## 类图

### 元素声明

```
@startuml
abstract        abstract
abstract class  "abstract class"
annotation      annotation
circle          circle
()              circle_short_form
class           class
diamond         diamond
<>              diamond_short_form
entity          entity
enum            enum
interface       interface
@enduml
```

### 类之间的关系

| Type        | Symbol | Drawung                                          |
| ----------- | ------ | ------------------------------------------------ |
| Extension   | <\|--  | ![img](https://s.plantuml.com/img/extends01.png) |
| Composition | *--    | ![img](https://s.plantuml.com/img/sym03.png)     |
| Aggregation | o--    | ![img](https://s.plantuml.com/img/sym01.png)     |

使用`..`代替`--`可以得到点划线

###  关系上的标签

```
@startuml
Class01 <|-- Class02
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 -- Class10
@enduml
```

![img](https://s.plantuml.com/imgw/img-540ce2f28c41a078e2cb947691250f66.webp)

```
@startuml
Class11 <|.. Class12
Class13 --> Class14
Class15 ..> Class16
Class17 ..|> Class18
Class19 <--* Class20
@enduml
```

![img](https://s.plantuml.com/imgw/img-2fba156f1b18d7baf59ebbea662bdf0d.webp)

```
@startuml
Class21 #-- Class22
Class23 x-- Class24
Class25 }-- Class26
Class27 +-- Class28
Class29 ^-- Class30
@enduml
```

![img](https://s.plantuml.com/imgw/img-12ec8ec15e5567f40029b4061344768a.webp)

### 关系上的标签

在关系之间使用标签来说明时, 使用 `:`后接 标签文字。

对元素的说明，你可以在每一边使用 `""` 来说明.

```
@startuml
Class01 "1" *-- "many" Class02 : contains
Class03 o-- Class04 : aggregation
Class05 --> "1" Class06
@enduml
```

![img](https://s.plantuml.com/imgw/img-7b350be2f50ccfc0d3023346aa8a7edc.webp)

在标签的开始或结束位置添加`<` 或 `>`以表明是哪个对象作用到哪个对象上

```
@startuml
class Car

Driver - Car : drives >
Car *- Wheel : have 4 >
Car -- Person : < owns

@enduml
```

![img](https://s.plantuml.com/imgw/img-a5c87f68dfd214735c4bda862440f718.webp)