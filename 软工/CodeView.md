---
title: CodeView
tag: [计算机课程学习,软工,]
---
# Schedule 调度逻辑文档

# 执行流程

* ScheduleCore   主函数调用 通过类的重载实现功能的差异化

  - UpdateDataStep 数据更新 

    * [StructRobotsData](#TemplateMethod::StructRobotsData) 更新机器人状态
    * [CheckAbnormal](#TemplateMethod::CheckAbnormal)检测异常的状态
    * [CheckBlockTime](#TemplateMethod::CheckBlockTime)检测阻塞时间
    * [CheckAvoidState](#TemplateMethod::Avoidance) 检测避让的状态
    * [CheckTaskChange](#TemplateMethod::CheckTaskChange)检测任务变化
    * [UpdatePathsUse](#TemplateMethod::UpdatePathsUse) 路径使用情况
    * [CheckTaskFinished](#TemplateMethod::CheckTaskFinished)检测任务是否完成
    * [CheckAvoidArrive](#TemplateMethod::CheckAvoidArrive)检测避让到达情况

- ScheduleStep 日程更新

  [BlockCheck](#TemplateMethod::BlockCheck)阻塞检查并且更新阻塞状态
  
  [StructConflictTable](#TemplateMethod::StructConflictTable)构造冲突列表
  
- this->StructConflictTable()  //冲突列表
  - [ConflictProcess]() 冲突处理 通过子类重载实现
  
- this->[SpeedControlProcess](#TemplateMethod::SpeedControlProcess) // 速度控制

# 枚举与常量

## 枚举
### ChassisType

机壳的外型

#### ChassisT1

enum 0

#### ChassisG1
enum 1

#### ChassisG2

enum 2

#### ChassisT2

enum 3

#### ChassisT5

enum 4

#### ChassisT6

enum 5

#### ChassisW1

enum 6

#### ChassisW3

enum 7

## RobotType 
####  Delivery
送餐 0 
####  OriginRobot
返回原点 1
####  GuideRobot
引导 
####  ArriveRobot
送餐即将到达
####  IdleRobot
空闲
####  ForbidRobot   
静止调度

### 任务类型
#### Deliver
送餐
#### OriginTask
原点
#### Guide
引导
#### Arrive
到达
#### Idle
空闲

## RobotStatus 

#### NoTask
无任务
#### Task
有任务
#### Avoidance
避让
#### AvoidanceWait
避让等待
#### AvoidanceArrive
避让到达
#### WaitToTask
等待任务
#### WaitToAvoidance
避让等待
#### LowSpeedTask
低速任务
#### PathAvoidArrive
路径点上避让
#### AsideTask
靠边任务
#### AsideLowSpeedTask
靠边低速任务
#### AsideWaitToTask
靠边等待任务

### VertexCapacity 
顶点类型
#### CannotMove
#### CannotAvoidance
#### CanAvoidance

### ConflictType
冲突类型
#### NoConflict
#### CanWait
#### Conflict
#### CanAside


### SpeedControlType 
速度控制类型
#### Normal
正常
#### LowSpeed
低速
#### Wait
等待

### RelativeDirection 
#### Same
相同
#### Reverse
相反
#### Other
其他

# 数据结构

## DijkstraVal

@public property cid : 当前顶点的ID

@public property length: 距离起始点的距离

@public property cost : 从起始点到当前点的cost

@public property lastId : 最短路径上上一个点的ID

@public function operator(const DijkstraValue& ) : 比较函数 返回 cost的比较

## DijkstraCompare

DijkstraVal 仿函数的比较类

@public function operator (const DijkstraValue& , const DijkstraValue& ):  返回两个DijkstraVal 的 cost 比较

## DijkstraHeap

容器类 重载实现类似于优先队列的结构 辅助建立最短路径的Map

@private property  dijMap:最短路径的集合

@private property value : 容器内元素的集合

@public function size(): 获取value 的大小

@public function empty():判断value集合是否为空

@public function hasCheck(int key):判断key是否在map内 即是否被检查过

@public function top():返回堆顶元素

@public function push():添加dijMap更新元素 并 维护堆

@public function pop():弹出堆顶的元素

@public function clear():清空value的数据

@public function begin():返回Val的end迭代器

@public function end():返回Val的end迭代器

@public function find(const int ): 获取dijMap对应点val

@public function getMap():获得map数据

## DijkstraMap

`std::map<int, DijkstraValue>`

顶点与DijkstraValue的集合


#  工具函数与行为类

## TemplateMethod

### TemplateMethod::StructRobotsData

TemplateMethod::StructRobotsData(vector<Robot>& ) 更新机器人的数据

**执行流程**

* 更新blockrecord 阻塞缓存
* 更新可用顶点
* 清除 机器的数据
* 清除 占用点 的数据
* 清除 已使用路径的数据
* 缓存原始数据(ctx->orgRobotsData[it->ID] = *it)
* 重新计算Dijkstra最短路径数据
* 去除未被激活的机器人的数据
* 依据状态与距离 取消激活
* 判断 机器是否返回了原点
* 记录历史

### TemplateMethod::CheckAbnormal

TemplateMethod::CheckAbnormal() 检查异常

* 检测状态 如果为避让到达则返回
* 如果周围没有避让点 或者离避让点过远
  * 如果没当前目标点
    * 如果有原始目标点
      * 如果是原点类型并到达原点 则启用原点避让标志位
      * 否则 设置为无任务状态 并将当前目标点作为自生的点
    * 如果没有原始目标点
      * 设置为无任务 并在当前点停留
  * 将当前标记为任务状态 并标记为任务状态 设置当前的任务

### TemplateMethod::CheckBlockTime

CheckBlockTime 检测阻塞时间

* 如果当前点与上次点位置相同 并且不是无任务状态
  * 对所有其他机器人检测 是否相邻 并判断状态 
    * 如果状态相符(已经避让) 则计算是否超时时间 并设置isTimeout 标志位
* 否则 将blockTime 更新并关闭timeout
* 更新最后的坐标

### TemplateMethod::Avoidance

检测避障状态

* 如果处于避让(Avoidance)  并且 当前坐标与目标相同 并且目标点在最近避让点的集合中 
  * 设置状态为避让等待
* 依据车辆状态处理
  * 在 避让 等待去避让 避让等待的状态
    * 初始化开始等待的时间与尝试等待的时间 为当前时间
    * 如果等待避让超时
      * 设置尝试等待与开始等待时间为 INT_MAX
      * 计算与目标点距离< minBlockRecordDistance 
        * 则将目标点加入阻塞的记录
        * 否则 LOG:不能记录目标点
      * 如果 有任务点 
        * 将其设置为任务状态
        * 对应机器的目标设置为当前任务
      * 或则 在原点并且为原点机器人
        * 将标志到达位设置为(originAvoidArrive)真
      * 否则 
        * 寻找避让点 并将目标设置避让点
    * 尝试继续超时
      * 继续尝试
      * 将尝试并将最后一次尝试状态设置为当前时间
  * 在避让到达的状态
    * 设置开始与上一次尝试时间为INT_MAX
  * 其他状态
    * 停止尝试 重置时间
    * 设置目标 并激活任务状态

### TemplateMethod::CheckTaskChange

检测任务变化

* 如果 状态标志位(hasChangeTask)被激活 且 目标点不为NAN 和0 并且状态不为避让到达
  * 设置目标
  * 将状态更新为Task
* 标志位(hasChangeTask)置否
* 如果 删除任务标志位为(true) 但是 isFinish 为假 
  * 则 将hasKillTask任务的标志位置为假
  * 判断 机器是否为 原点机器人
    * 如果是原点机器人 则 目标置为原地并且设置为无任务状态
    * 如果 处于 任务 等待任务  低速任务 等待任务 到达路径点上避让
      * 使车停留
      * 标志为无状态
      * 将Context置为送餐状态
      * 将机器置为送餐状态

### TemplateMethod::UpdatePathsUse

UpdatePathsUse() 寻找占用 的路径

* 遍历所有robot
  * 如果robot处于无任务的状态
    * 将robot的目标设为原点\
  * 计算每个点与目标之间的最短路径 并存放于pathUse数组中

### TemplateMethod::CheckTaskFinished

CheckTaskFinished 检测任务的完成情况

* 检测 isFinish标志位 如果为false 即未完成 则直接返回
* 如果已经完成 将标志位置否 将状态设置为无任务 将车定位原地
* 如果为原点机器人 则 将原点避让到达为否

### TemplateMethod::CheckAvoidArrive

CheckAvoidArrive 检测避让点到达

* 如果 避让没有到达 （isAvoidanceArrive == false） 则直接返回
* 设置标志位(isAvoidanceArrive )为false
* 如果 机器在附近的的避让点中
  * 将对应的机器设置为 AvoidanceArrive’
  * 清除该机器的占用路径
  * 如果是原点机器人 并且 到达原点且 原始任务不为NaN
    * ctx 认为原点避让到达
  * 如果 当前任务置空 为NaN
    * 原点避让到达
* 不在避让点中
  * 如果是原点机器人 并且原点到达 并且原始任务不为NaN
    * 认为原点避让到达为证
    * 置为无任务
    * 机器人停止
    * 路径为空
  * 否则
    * 对于避让 等待去避让 避让等待的机器人
      * 如果当前任务不为NaN
        * 置为路径避让机器人 并且停在原点
      * 原点避让设置为真
      * 当前任务设置为无任务
      * 路径为停留在原点
        * 更新使用的路径

### TemplateMethod::BlockCheck

* 阻塞检查并且更新阻塞状态
* 将当需要计划的Robot 置为NaN
* 当前避让点为NaN
* 清除避让点
* 检测当前机器的状态 并调用 [IsBlock](#ScheduleContext::isBlock)进行阻塞检查与阻塞的任务的更新与规划 需要规划为真 否则为假
  * 如果 上述条件为真 则更新避让状态[SetAvoidanceData](#TemplateMethod::SetAvoidanceData) 传入距离最近的机器人ID 与 Context 避让点

### TemplateMethod::SetAvoidanceData
设置避让状态 并更新避让的目标点 然后重新计算路径

### TemplateMethod::StructConflictTable

构造冲突列表

* 如果机器在无任务的情况下 [判断 是否偏离路线 (false 即未偏离) 或者在原点并未开启原点避让] 

  * 则 无需规划 并排除在冲突列表外

  * 否则 依据车辆的状态 

    * 在 等待任务 等待避免 路径点避让 的 **状态**

      * 检查所有机器的冲突状态 二重遍历+[ConflictCheck](#ScheduleContext::ConflictCheck)

      * 更新两个机器见的冲突表 

        > 被检测的两个车辆的状态并不一定一致 可能一个冲突避让 另一个是正常的状态

    * 在其他的状态

      * 对所有的机器遍历
        * 如果是本机 且当前只占用一条路径 则跳过
        * 检测机器与本机的冲突状态 并更新冲突状态

### TemplateMethod::CheckAvoidArrive

检测避让是否到达

### TemplateMethod::ConflictProcess

通过重载对应的行为类 来完成冲突的处理

[AsideMetho::ConflictProcess](#AsideMethod::ConflictProcess)
[IdleMethod::ConflictProcess](#IdleMethod::ConflictProcess)
[OriginMethod::ConflictProcess](#OriginMethod::ConflictProcess)
[TaskMethod::ConflictProcess](#TaskMethod::ConflictProcess)
[AvoidMethod::ConflictProcess](#AvoidMethod::ConflictProcess)



### TemplateMethod::SpeedControlProcess

车辆速度控制 与车辆状态转换

* 如果是无任务状态 避让等待 避让到达的状态
  * 关闭 避让到达的标志位
* 调用ctx的[SpeedControl](#ScheduleContext::SpeedControl) 获取速度的状态

* 依据状态进行状态转移
  * Task LowSpeedTask WaitToTask PathAvoidArrive:
    * 依据速度选择(speedType)
      * wait
        * 如果未 路径避让到达 则继续爆出状态
        * 否为 变为 等待任务的状态 
      * lowspeed
        * 任务状态变为低速状态
      * 其他
        * 变为任务状态
  * 在靠边 ，低速靠边，靠边等待任务的状态
    * 依据速度选择
      * wait 
        * 转台转化为靠边等待
      * lowspeed
        * 靠边低速等待
      * 其他状态
        * 转变为靠边任务
  * 避让状态
    * 当速度为等待时，转变为WaitToAvoidance等待避让状态
  * 等待避让状态
    * 当速度不为等待时转变为避让状态
  * 其他
    * 速度控制中的错误状态

# ScheduleContext
## 变量
### std::set<int> Schedule::remotePathPoints
偏僻的岔路 在避让时避免主干道
### std::set<int> Schedule::wideVertexs
宽路径的一个路径点的集合
### std::map<int, Robot> Schedule::robotsData
机器人的数据
### std::map<int, Robot> Schedule::orgRobotsData
原始机器人的数据
### std::map<int, std::vector<int>> Schedule::pathsUse
每个机器人的路径
### std::unordered_map<int, Vertex> Schedule::vertexs
地图的顶点
### std::unordered_map<int, std::vector<Edge>> Schedule::graph
地图的边 只初始化一次
### std::unordered_map<int, std::vector<ConverseEdge>> Schedule::converseGraph
反向的地图 只初始化一次
### std::unordered_map<int, Vertex> Schedule::orgVertexs
备份的顶点
### std::unordered_map<int, std::vector<Edge>> Schedule::orgGraph
备份的图
### std::unordered_map<int, std::vector<ConverseEdge>> Schedule::orgConverseGraph
备份的反向图 useless 未使用
### std::unordered_map<int, Vertex> Schedule::obstacles
建图
### std::unordered_map<int, std::vector<Wall>> Schedule::walls
虚拟墙
### std::map<int, DijkstraMap> Schedule::robotsDijMap
Dijkstra 所计算出的所有路径的地图
### bool Schedule::hasReadFile
是否读过地图
### bool Schedule::enablePathAvoid
是否开启路径点避让 开启则可到岔路上避让
### bool Schedule::enableOriginAvoid
原点机器是否需要避让
### bool Schedule::enableAvoidAside
是否开启靠边避让
### int Schedule::checkLen
调度距离
### int Schedule::timeoutLimit
超时时间
### Reduction Schedule::reduction
距离减益
### std::set<int> Schedule::narrowOrigin
狭窄原点
### std::set<int> Schedule::forks
岔路
### std::map<int, int> Schedule::originPathId
 key = path id, value = origin priority
### std::map<int, std::map<int, int>> Schedule::originPriority
原点的优先级
### std::set<int> Schedule::configOrigins
会用的原点的集合
### bool Schedule::hasOwnData
是否拥有自己的数据
### bool Schedule::isAtOrigin
是否在原点
### bool Schedule::originAvoidArrive
停在原点的机器需要出去避让从而到达避让点
### bool Schedule::isAvoidanceArrive
### bool Schedule::isFinish
当前任务是否完成
### bool Schedule::isEnable
是否允许调度
### bool Schedule::hasChangeTask
是否已经切换任务
### bool Schedule::hasKillTask
结束任务
### bool Schedule::tryContinue
避让之后是否继续
### bool Schedule::hadArriveOrigin
是否去过原点
### bool Schedule::isPathAvoidance
是否是到路径上避让
### bool Schedule::needSlowDown
需要减速
### bool Schedule::needControlSpeed
需要控制速度
### bool Schedule::arriveRightside
是否到达路边
### bool Schedule::needPullOver
是否需要靠边
### bool Schedule::needWaitAtFork
路口前方等待
### int Schedule::id
机器人ID
### int Schedule::task
目标任务点的最近的路径点的编号
### int Schedule::taskGoal
当前目标点
### int Schedule::originTask
原点任务
### int Schedule::avoidanceId
需要避让的机器ID
### int Schedule::blockTime
已经卡住的时间
### int Schedule::tryContinueWaitTime
尝试继续的时间间隔
### int Schedule::maxAvoidanceMoveTime
最大避让移动时间
### int Schedule::lastPosition
上一个位置
### int Schedule::speedGoal
速度目标
### ChassisType Schedule::chassisType
底盘类型
### RobotType Schedule::robotType
机器人类型 外部更新缓存
### TaskType Schedule::taskType
任务类型
### Robot Schedule::robot
要返回的Robot
### std::map<int, std::map<int, ConflictType>> Schedule::allCftTypeTable
所有机器人冲突的表
### std::map<ChassisType, int> Schedule::chassisTypeTable
底盘型号对应的ID
### std::map<int, std::set<int>> Schedule::wideVertexsTable
宽路线的表
### RobotStatus Schedule::preState
调度前的状态
### time_t Schedule::startAvoidanceTime
开始避让的时间
### time_t Schedule::lastTryContinueTime
上次尝试继续任务的时间点
### time_t Schedule::currentTime
当前时间 精确到秒 内部计时
### int Schedule::needScheduleRobot
需要调度的机器人 卡死状态下
### int Schedule::avoidanceVertex
卡死状态下避让的机器所需要去的点
### std::vector<int> Schedule::avoidancePath
避让路径
### std::vector<int> Schedule::blockRecord
无效避让点
### std::vector<int> Schedule::tempBlockRecord
多线程 临时变量
### std::set<int> Schedule::occupiedPoints
 其他机器已经占据的路径点
### std::map<int, int> Schedule::closetPath
 key-目标点 value-与目标点最近的路径点
### std::map<int, Vertex> Schedule::closetGoal
 路径点最近的目标点 fix-bug
### std::map<int, Vertex> Schedule::closeAvoid
 路径点附近的避让点
### std::map<int, Vertex> Schedule::goals
所有目标点 key-path

### ScheduleContext::ConflictCheck

  void ScheduleContext::ConflictCheck(int idA, int idB, ConflictType& cftType)

**param** idA,idB : 要检测的两个冲突的机器人

**param** out cftType: 输出参数 冲突类型

### ScheduleContext::isBlock

该函数依据车辆速度与状态 检测多个路径拥堵的状态 并进行整体的规划

### ScheduleContext::ConflictCheck

冲突检测模块

### ScheduleContext::IsLoop

检测冲突等待环 死锁

@param out loopScheduleRobot : 用于解锁的机器

@param out loopAvoidanceGoal : 解锁的机器的目标避让点

@return : 是否本机为需要解锁的机器

old: 

* 首先 遍历所有机器人 排除被禁用

* 更新冲突列表

* 通过广度优先遍历 检测出环与其中的依赖关系。

    > 当前机器较少 最多找出5个冲突机器 所以只找两个表的重合节点
    >
    > 如果当前机器冲突多于5个 可能出现两个多余的环 则要找出自身所在的环 。

new：

* 遍历机器人列表 排除禁用的机器
* 更新冲突列表
* 在冲突列表中 统计所有节点的 出度 与 入度
* 通过出度排序 找出出度最大的节点组
* 在节点组中寻找出度最大的节点
* 如果还有重复 则找出避让距离最短的机器

 ### ScheduleContext::DijkstraInitial

Dijkstra地图初始化 写入robotsDijMap

old:

* 清空 robotsDijMap
* 遍历所有机器数据
  * 创建[DijkstraHeap](#DijkstraHeap) `堆` `dijSet`用于维护
  * 向 `堆` 添加开始节点(机器的启动节点)
  * 当容器不为空
    * 弹出获取 `堆` 顶元素 为 `当前节点`
    *  遍历 `当前节点` 所有目标节点
      * 如果 `目标节点` 应被遍历过 则 不在更新
      * 声明 最小的代价，id，与距离
      * 如果当前节点为开始节点[成环？]
        * 更新 最短距离 为两点间的几何距离
      * 否则
        * 遍历反向地图获取所有`目标节点`的地图的`反向节点`  当反向节点非当前节点
        * 在如果反向节点FromID 在集合中 比较最短值 并且进行更新
      * 遍历所有原始机器人数据
        * 如果有机器占用当前点 增加cost(robotReduction)
      * 如果当前节点靠近目标
        * 增加靠进目标的cost 
      * 如果顶点的容量不等于 可避让的，可靠边的
        * 增加靠边的cost
      * 添加元素
    * 更新地图

### ScheduleContext::Dijkstra

获取点与点之间的最短路径

@param robotId : 对应的机器人的ID
@param start  : 起始点
@param goal  : 目标点 在
@param out pathLen : 返回值 返回路径的长度
@return : 返回目标路径

* 声明对当前robit的DijMap的引用(robotsDijMap[robotId])
* 更新PathLen
* 判断目标的正确性
* 判断目标与起点是否重合 重合则直接返回只有起点的路径
* 依次从DijMap中获取路径
* 获取从goal到0的路径
* 逆序后返回


## AsideMethod(public TemplateMethod)

靠边模式的行为类 继承于TemplateMethod

### AsideMethod::ConflictProcess

AsideMethod 下的冲突处理函数

* 依据状态进行选择
  * AsideWaitToTask 避让等待任务
    * 如果isLoop 有无等待环 并且loop的就是本机器且有循环避让的目标点
      * 打开loop标志位
      * 更新避让日志SetAvoidanceData，加入GetClosetRobotId和循环避让的目标点
      * 循环检查所有机器人 并检查所有机器人的冲突状态ConflictCheck
      * 更新自身的冲突表
  * AsideLowSpeedTask ，AsideTask：
    * 更新自生的冲突状态SetConflictType(如果可以降级则降级 不升级)
    * 依据冲突状态选择
      * 冲突
        * isConflict设置为真
        * 设置更新避让状态
      * 可等待
        * 如果不在循环状态 将状态转变为避让等待任务的状态
      * 可避让
        * 更行为冲突状态
        * 需要靠边停车
        * 将避让目标设置为迭代的目标
* 检测自生冲突状态
  * 如果莫得冲突
    * 将自生状态更新为任务状态
    * 到达右边与停车状态置否
    * 更新路径占用
* 如果maxCft为CanWait 则路口等待标志位设置为真

## AvoidMethod(public TemplateMethod)

避让模式下的行为类 继承于TemplateMethod

### AvoidMethod::ConflictProcess

避让模式下的冲突处理函数

* 根据自生状态选择
  * 避让等待
    * 如果避让已经完成[AvoidanceRecorrect](#AvoidMethod::AvoidanceRecorrect) 并且当前任务点为NaN
      * 更新任务状态 设置目标 并且更新路径
  * 避让到达
    * 避让到达的状态调用[CanContinue](#AvoidMethod::CanContinue)检测任务是否能够继续
      * 更新任务状态 设置目标 并且更新路径
  * 等待去避让
    * 检测是否有循环等待的情况 并且等待的是否为本台机器
      * 更新冲突表
      * 遍历所有机器
        * 如果为本机 或者 没有路径 则跳过
        * 否则 设置为无冲突任务并且更新冲突状态[ConflictCheck](ScheduleContext::ConflictCheck)
        * 更新冲突表
  * 正在避让
    * 如果避让已经完成[AvoidanceRecorrect](#AvoidMethod::AvoidanceRecorrect)
      * 更新任务状态 设置目标 并且更新路径 
      * 跳出
    * 遍历所有机器
      * 更新冲突等级(只增不减)
      * 如果为冲突状态
        * 有冲突为真
        * 更新冲突表
      * 为可等待的状态
        * 有冲突为真
        * 更新状态为等待去避让的状态
    * 如果没有冲突
      * 计算本机器与所有机器最短距离
      * 如果道路不足够宽并且不能进行避让等待
        * 更新冲突列表
      * 否则 继续执行任务
    * 如果尝试继续并且可以继续
      * 继续任务

### AvoidMethod::AvoidanceRecorrect

@return : 本机器是否需要避让 为真是不需要避让 假则需要

避让纠正

* 如果存在需要避让的机器并且避让点与冲突的机器的避让点相同 
  * 尝试重新寻径 如果新的路径上不再与需要避让即机器冲突则不需要避让。(return true)
* 否则 遍历所有机器人数据
  * 选择在避让等待/避让/等待避让 的机器人 两个机器人需要互相避让则依据ID判断
    * 本机Id较小则无需避让(return true) 
* 否则 本机需要继续避让

### AvoidMethod::CanContinue

@return :  任务是否能继续

*  如果无任务 或者 目标点为0 则返回不能继续

* canContinue标志为真

* 计算当前点到目标点的路径

* 创建检查过的点的合集

* 遍历所有路径点

  * 遍历所有路径点附近的避让点 
  * 这些避让点中有hasCheckded集合中的点 则已经检查过 就直接跳过下列步骤

  * 计算避让点与当前路径点的距离 小于相近距离 并且避让点未被占用且不在集合中
    * 将有避让点的标志(hasAvoidPoint)打开 并且 加入到检查过的集合中

* 遍历所有机器 

  * 计算机器与在路径上与本机的距离
  * 如果是本机 或者长度大于调度距离+额外距离 则忽略
  * 如果两台机器 有同样的占用点，或者占用点的距离在危险的距离中
    * 计算本机到本机占用点的距离
    * 计算目标机器到目标机器的占用点的距离
    * 如果已经在目标点附近[tempPathA.size() < 2] 则不继续靠近,让其他机器先走
    * 否则 再计算到路径的距离小于其他车到目标点的距离 并且速度大于50 让本机先走
    * 否则 让其他机器先走
  * 如果其他机器即将路过此目标点 则让其先走
  * 在当前路径上运行检测是否会与其他点冲突
    * 如果检测到反向的机器则不再继续
  * 检测目标点是否已经被占用 否则为否
  * 检测自生是否为原点机器人并且检测是否会发生碰撞 如果为真则不再继续

## IdleMethod(public TemplateMethod)

靠边模式的行为类 继承于TemplateMethod

### IdleMethod::ConflictProcess

冲突处理程序

* 遍历所有机器数据
  * 如果当前处于冲突状态 更新避让列表

  ### IdleMethod::StructConflictTable

构建冲突表

* 如果当前道路足够宽  。。。
* 否则 调用父类的冲突表构造函数

## OriginMethod(public TemplateMethod)

在原点模式的行为类 继承于TemplateMethod

### OriginMethod::ConflictProcess

原点模式冲突处理函数

* 遍历机器数据 如果目标机器是冲突的 则更新避让表

## TaskMethod(public TemplateMethod)

任务模式下的行为类 继承于TemplateMethod

### TaskMethod::ConflictProcess

依据状态进行选择

* PathAvoidArrive 和 WaitToTask 状态
* LowSpeedTask 和 Task 其他状态
  * 遍历所有机器数据 
    * 获得对应的冲突列表，并向上更新冲突等级
    * Conflict 等级：
    * CanWait 等级
    * CanAside 等级
    * 其他
  * 如果 没有冲突
    * 更新路径占用
  * 如果最大冲突等级为CanWait
    * 需要在路口等待





