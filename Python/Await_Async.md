#  Async/Await

> 参考 https://zhuanlan.zhihu.com/p/27258289
>
> doc: https://docs.python.org/zh-cn/3/library/asyncio-task.html
>
> eg: https://blog.csdn.net/Likianta/article/details/90123678

## async/await

Python 3.5出现的async/await

async修饰将普通函数和生成器函数包装成异步函数和异步生成器

异步函数（协程）

```python
async def async_function():
    return 1
```

异步生成器

```python
async def async_generator():
    yield 1
```

直接调用异步函数不会返回结果，而是返回一个coroutine对象

```python
print(async_function())
# <coroutine object async_function at 0x102ff67d8>
```

协程需要通过其他方式来驱动，因此可以使用这个协程对象的send方法给协程发送一个值：

```python
print(async_function().send(None))
```

不幸的是，如果通过上面的调用会抛出一个异常：

```python
StopIteration: 1
```

因为生成器/协程在正常返回退出时会抛出一个StopIteration异常，而原来的返回值会存放在StopIteration对象的value属性中，通过以下捕获可以获取协程真正的返回值：

```python
try:
    async_function().send(None)
except StopIteration as e:
    print(e.value)
# 1
```

通过上面的方式来新建一个run函数来驱动协程函数：

```python
def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value
```

在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果：

```python
async def async_function():
    return 1

async def await_coroutine():
    result = await async_function()
    print(result)
    
run(await_coroutine())
# 1
```

await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误。

## 可等待对象

一个对象可以在 `await`  语句中使用，那么它就是 **可等待** 对象

*可等待* 对象有三种主要类型: **协程**, **任务** 和 **Future**.

### 协程

* 协程函数  async def 函数
* 协程对象 调用`协程函数`返回的对象

### 任务

*任务* 被用来“并行的”调度协程

协程通过 `asyncio.create_task()` 等函数被封装为一个 *任务*，该协程会被自动调度执行

### Futures

`Future` 是一种特殊的 **低层级** 可等待对象，表示一个异步操作的 **最终结果**。

当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

## 运行协程

asyncio 提供了三种主要机制

###  asyncio.run()

`asyncio.run()` 函数用来运行最高层级的入口点 "main()" 函数

`asyncio`. `run`(*coro*, \*, *debug=False*)

执行 coroutine *coro* 并返回结果。此函数会运行传入的协程，负责管理 asyncio 事件循环，*终结异步生成器*，并关闭线程池。

此函数总是会创建一个新的事件循环并在结束时关闭之。它应当被用作  asyncio 程序的主入口点，理想情况下应当只被调用一次。

3.9 版更改: 更新为使用 [`loop.shutdown_default_executor()`](

### 等待一个协程

以下代码段会在等待 1 秒后打印 "hello"，然后 *再次* 等待 2 秒后打印 "world":

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

### asyncio.create_task() 创建任务

来并发运行作为 asyncio 任务的多个协程

将 *coro* 协程 封装为一个 `Task` 并调度其执行。返回 Task 对象。

*name* 不为 `None`，它将使用 `Task.set_name()` 来设为任务的名称。

该任务会在 `get_running_loop()` 返回的循环中执行，如果当前线程没有在运行的循环则会引发 `RuntimeError`。

此函数 **在 Python 3.7 中被加入**。

在 Python 3.7 之前，可以改用低层级的 `asyncio.ensure_future()` 函数。

```python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```

## 休眠

*coroutine* `asyncio.sleep`(*delay*, *result=None*)

阻塞 *delay* 指定的秒数。

如果指定了 *result*，则当协程完成时将其返回给调用者。

## 并发运行任务

`asyncio.gather(**aws*, *return_exceptions=False*)`

*并发* 运行 *aws* 序列中的 可等待对象。

- 如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 *aws* 中可等待对象的顺序一致。
- 如果 *return_exceptions* 为 `False` (默认)，所引发的首个异常会立即传播给等待 `gather()` 的任务。*aws* 序列中的其他可等待对象 **不会被取消** 并将继续运行。
- 如果 *return_exceptions* 为 `True`，异常会和成功的结果一样处理，并聚合至结果列表。
- 如果 `gather()` *被取消*，所有被提交 (尚未完成) 的可等待对象也会 *被取消*。
- 如果 *aws* 序列中的任一 Task 或 Future 对象 *被取消*，它将被当作引发了 `CancelledError` 一样处理 -- 在此情况下 `gather()` 调用 **不会** 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2), currently i=2...
#     Task B: Compute factorial(3), currently i=2...
#     Task C: Compute factorial(4), currently i=2...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3), currently i=3...
#     Task C: Compute factorial(4), currently i=3...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4), currently i=4...
#     Task C: factorial(4) = 24
#     [2, 6, 24]
```

## 屏蔽取消操作

*awaitable* `asyncio.shield`(*aw*)

保护一个 [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables) 防止其被 [`取消`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.Task.cancel)。

如果 *aw* 是一个协程，它将自动被作为任务调度。

以下语句:

```
res = await shield(something())
```

相当于:

```
res = await something()
```

*不同之处* 在于如果包含它的协程被取消，在 `something()` 中运行的任务不会被取消。

## 超时

*coroutine* `asyncio.wait_for`(*aw*, *timeout*)

等待 *aw* 可等待对象 完成，指定 timeout 秒数后超时。

如果 *aw* 是一个协程，它将自动被作为任务调度。

如果发生超时，任务将取消并引发 `asyncio.TimeoutError`.

## 简单等待

*coroutine* `asyncio.wait`(*aws*, ***, *timeout=None*, *return_when=ALL_COMPLETED*)

并发地运行 *aws* 可迭代对象中的 可等待对象 并进入阻塞状态直到满足 *return_when* 所指定的条件。 *aws* 可迭代对象必须不为空

```
done, pending = await asyncio.wait(aws)
```