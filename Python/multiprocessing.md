# multiprocessing 基于进程的并行

> 参考：
>
> 官方文档  https://docs.python.org/zh-cn/3/library/multiprocessing.html
>
> https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming

## 简介

`multiprocessing` 是一个支持使用与 [`threading`](https://docs.python.org/zh-cn/3/library/threading.html#module-threading) 模块类似的 API 来产生进程的包。 `multiprocessing` 包同时提供了本地和远程并发操作，通过使用子进程而非线程有效地绕过了 [全局解释器锁](https://docs.python.org/zh-cn/3/glossary.html#term-global-interpreter-lock)。 因此，`multiprocessing` 模块允许程序员充分利用给定机器上的多个处理器。 它在 Unix 和 Windows 上均可运行。

`multiprocessing` 模块还引入了在 `threading` 模块中没有的API。

一个主要的例子就是 `Pool` 对象，它提供了一种快捷的方法，赋予函数并行化处理一系列输入值的能力，可以将输入数据分配给不同进程处理（数据并行）。

ex:

```python
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

## Process

`Process` 和 `threading.Thread` 相同，通过`start()`生成进程。

```python
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

通过 `os`模块的函数 可以获得进程的信息

```python
print('module name:', __name__)
print('parent process:', os.getppid())	# 父进程 pid
print('process id:', os.getpid())				# 本进程 pid
```

模块中 `if __name__ == "__main__"` 是必须的

## 启动进程的方式

* spawn
  * 父进程会启动一个全新的 `python 解释器`进程。 子进程将只继承那些运行进程对象的 `run()` 方法所必需的资源。
  * 来自父进程的非必需文件描述符和句柄将不会被继承
  * 启动进程相比使用 *fork* 或 *forkserver* 要慢上许多
  * 可在Unix和Windows上使用。 Windows, macOS上的默认设置，windows无fork，macOS可能导致subprocrss崩溃。
* fork
  * 父进程使用 [`os.fork()`](https://docs.python.org/zh-cn/3/library/os.html#os.fork) 来产生 Python 解释器分叉。子进程在开始时实际上与父进程相同。父进程的所有资源都由子进程继承
  * 安全分叉多线程进程是 **棘手** 的
  * 只存在于Unix。Unix中的默认值
* forkserver
  * 启动服务器进程，每当需要一个新进程时，父进程就会连接到服务器并请求它分叉一个新进程
  * 分叉服务器进程是单线程的，因此使用 `os.fork()`  是安全的。没有不必要的资源被继承
  * 可在Unix平台上使用，支持通过Unix管道传递文件描述符。

> 在 Unix 上通过 *spawn* 和 *forkserver* 方式启动多进程会同时启动一个 *资源追踪* 进程，负责追踪当前程序的进程产生的、并且不再被使用的命名系统资源(如命名信号量以及 [`SharedMemory`](https://docs.python.org/zh-cn/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory)   对象)。
>
> 当所有进程退出后，资源追踪会负责释放这些仍被追踪的的对象。
>
> 通常情况下是不会有这种对象的，但是假如一个子进程被某个信号杀死，就可能存在这一类资源的“泄露”情况。（泄露的信号量以及共享内存不会被释放，直到下一次系统重启，对于这两类资源来说，这是一个比较大的问题，因为操作系统允许的命名信号量的数量是有限的，而共享内存也会占据主内存的一片空间）

### join

join()方法可以在当前位置阻塞主进程，带执行join()的进程结束后再继续执行主进程的代码逻辑。

## 进程间的通信

### Queue 队列

`Queue` 类是一个近似 `queue.Queue` 的克隆。

队列是线程和进程安全的。

```python
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
```

### 管道

`Pipe()` 函数返回一个由管道连接的连接对象，默认情况下是双工（双向）。例如:

```python
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
```

返回的两个连接对象 [`Pipe()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Pipe) 表示管道的两端。每个连接对象都有 `send()` 和 `recv()` 方法（相互之间的）。

请注意，如果两个进程（或线程）同时尝试读取或写入管道的 *同一* 端，则管道中的数据可能会损坏。

在不同进程中同时使用管道的不同端的情况下不存在损坏的风险。

## 进程间同步

### 使用Lock

`multiprocessing` 包含来自 `threading` 的所有同步原语的等价物`Lock`。

```python
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
```

## 共享状态

在进行并发编程时，通常最好尽量避免使用共享状态。使用多个进程时尤其如此

### 共享内存

可以使用 `Value` 或 `Array` 将数据存储在共享内存映射中。例如，以下代码:

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

为了更灵活地使用共享内存，可以使用 [`multiprocessing.sharedctypes`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#module-multiprocessing.sharedctypes) 模块，该模块支持创建从共享内存分配的任意ctypes对象。

### 服务进程

由 `Manager()` 返回的管理器对象控制一个服务进程，该进程保存Python对象并允许其他进程使用代理操作它们。

`Manager()` 返回的管理器支持类型： [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) 、 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 、 [`Namespace`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.managers.Namespace) 、 [`Lock`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Lock) 、 [`RLock`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.RLock) 、 [`Semaphore`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Semaphore) 、 [`BoundedSemaphore`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.BoundedSemaphore) 、 [`Condition`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Condition) 、 [`Event`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Event) 、 [`Barrier`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Barrier) 、 [`Queue`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Queue) 、 [`Value`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Value) 和 [`Array`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Array) 

```python
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
```

## 工作进程

[`Pool`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool) 类表示一个工作进程池。它具有允许以几种不同方式将任务分配到工作进程的方法。

```python
from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # 启动四个工作进程的进程池
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
    
```

* `apply(func[, args[, kwds]])`
  *  使用 *args* 参数以及 *kwds* 命名参数调用 *func* , 它会返回结果前阻塞。
* `apply_async(func[, args[, kwds[, callback[, error_callback]]]])`
  * `apply()` 方法的一个变种，返回一个 [`AsyncResult`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult) 对象。
  * 如果指定了 *callback* , 它必须是一个接受单个参数的可调用对象。当执行成功时， *callback* 会被用于处理执行后的返回结果.
  * 如果指定了 *error_callback* , 它必须是一个接受单个参数的可调用对象。当目标函数执行失败时， 会将抛出的异常对象作为参数传递给 *error_callback* 执行。
  * 回调函数应该立即执行完成，否则会阻塞负责处理结果的线程。

* `map(func, iterable[, chunksize])`

  * 内置 `map()` 函数的并行版本 (但它只支持一个 *iterable* 参数)

  * 这个方法会将可迭代对象分割为许多块，然后提交给进程池

* `map_async(*func*, *iterable*[, *chunksize*[, *callback*[, *error_callback*]]])`

  * `map()` 方法的一个变种，返回一个 `AsyncResult` 对象。

* `imap(*func*, *iterable*[, *chunksize*])`

  * `map()` 的延迟执行版本。*chunksize* 参数的作用和 [`map()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.map) 方法的一样。对于很长的迭代器，给 *chunksize* 设置一个很大的值会比默认值 `1` **极大** 地加快执行速度。

* `imap_unordered(*func*, *iterable*[, *chunksize*])`

  和 [`imap()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap) 相同，只不过通过迭代器返回的结果是任意的。（当进程池中只有一个工作进程的时候，返回结果的顺序才能认为是"有序"的）

* `starmap(*func*, *iterable*[, *chunksize*])`

  和 [`map()`](https://docs.python.org/zh-cn/3/library/functions.html#map) 类似，不过 *iterable* 中的每一项会被解包再作为函数参数。

  比如可迭代对象 `[(1,2), (3, 4)]` 会转化为等价于 `[func(1,2), func(3,4)]` 的调用。

* `starmap_async(*func*, *iterable*[, *chunksize*[, *callback*[, *error_callback*]]])`

  相当于 [`starmap()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap) 与 [`map_async()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.map_async) 的结合，迭代 *iterable* 的每一项，解包作为 *func* 的参数并执行，返回用于获取结果的对象。

* `close()`

  阻止后续任务提交到进程池，当所有任务执行完成后，工作进程会退出。

* `terminate()`

  不必等待未完成的任务，立即停止工作进程。当进程池对象被垃圾回收时，会立即调用 [`terminate()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate)。

* `join()`

  等待工作进程结束。调用 [`join()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.join) 前必须先调用 [`close()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.close) 或者 [`terminate()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate) 。

* `get([*timeout*])`

  用于获取执行结果。如果 *timeout* 不是 `None` 并且在 *timeout* 秒内仍然没有执行完得到结果，则抛出 [`multiprocessing.TimeoutError`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.TimeoutError) 异常。如果远程调用发生异常，这个异常会通过 [`get()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult.get) 重新抛出。

## 多进程注意事项

### 启动时需要注意

* 避免共享状态

  * 应该尽可能避免在进程间传递大量数据，越少越好。

  * 最好坚持使用队列或者管道进行进程间通信，而不是底层的同步原语。

* 可序列化
  * 保证所代理的方法的参数是可以序列化的。
* 代理的线程安全性
  * 不要在多线程中同时使用一个代理对象，除非你用锁保护它。
  * （而在不同进程中使用 *相同* 的代理对象却没有问题。）
* 使用 Join 避免僵尸进程
  * 在 Unix 上，如果一个进程执行完成但是没有被 join，就会变成僵尸进程。一般来说，僵尸进程不会很多，因为每次新启动进程（或者 [`active_children()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.active_children) 被调用）时，所有已执行完成且没有被 join 的进程都会自动被 join，而且对一个执行完的进程调用 [`Process.is_alive`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Process.is_alive) 也会 join 这个进程。尽管如此，对自己启动的进程显式调用 join 依然是最佳实践。
* 继承优于序列化、反序列化
  * 当使用 *spawn* 或者 *forkserver* 的启动方式时，[`multiprocessing`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#module-multiprocessing)  中的许多类型都必须是可序列化的，这样子进程才能使用它们。但是通常我们都应该避免使用管道和队列发送共享对象到另外一个进程，而是重新组织代码，对于其他进程创建出来的共享对象，让那些需要访问这些对象的子进程可以直接将这些对象从父进程继承过来。
* 避免杀死进程
  * 听过 [`Process.terminate`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Process.terminate) 停止一个进程很容易导致这个进程正在使用的共享资源（如锁、信号量、管道和队列）损坏或者变得不可用，无法在其他进程中继续使用。
  * 所以，最好只对那些从来不使用共享资源的进程调用 [`Process.terminate`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Process.terminate) 。
* Join 使用队列的进程
  * 记住，往队列放入数据的进程会一直等待直到队列中所有项被"feeder" 线程传给底层管道。（子进程可以调用队列的 [`Queue.cancel_join_thread`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Queue.cancel_join_thread) 方法禁止这种行为）
  * 这意味着，任何使用队列的时候，你都要确保在进程join之前，所有存放到队列中的项将会被其他进程、线程完全消费。否则不能保证这个写过队列的进程可以正常终止。记住非精灵进程会自动 join 。
  * 下面是一个会导致死锁的例子:

> ```
> from multiprocessing import Process, Queue
> 
> def f(q):
>     q.put('X' * 1000000)
> 
> if __name__ == '__main__':
>     queue = Queue()
>     p = Process(target=f, args=(queue,))
>     p.start()
>     p.join()                    # this deadlocks
>     obj = queue.get()
> ```
>
> 交换最后两行可以修复这个问题（或者直接删掉 `p.join()`）。

* 显式传递资源给子进程
  * 在Unix上，使用 *fork* 方式启动的子进程可以使用父进程中全局创建的共享资源。不过，最好是显式将资源对象通过参数的形式传递给子进程。
  * 除了（部分原因）让代码兼容 Windows 以及其他的进程启动方式外，这种形式还保证了在子进程生命期这个对象是不会被父进程垃圾回收的。如果父进程中的某些对象被垃圾回收会导致资源释放，这就变得很重要。

> 所以对于实例：
>
> ```
> from multiprocessing import Process, Lock
> 
> def f():
>     ... do something using "lock" ...
> 
> if __name__ == '__main__':
>     lock = Lock()
>     for i in range(10):
>         Process(target=f).start()
> ```
>
> 应当重写成这样：
>
> ```
> from multiprocessing import Process, Lock
> 
> def f(l):
>     ... do something using "l" ...
> 
> if __name__ == '__main__':
>     lock = Lock()
>     for i in range(10):
>         Process(target=f, args=(lock,)).start()
> ```

* 谨防将 [`sys.stdin`](https://docs.python.org/zh-cn/3/library/sys.html#sys.stdin) 数据替换为 “类似文件的对象”

> [`multiprocessing`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#module-multiprocessing) 原本会无条件地这样调用:
>
> ```
> os.close(sys.stdin.fileno())
> ```
>
> 在  `multiprocessing.Process._bootstrap()` 方法中 —— 这会导致与"进程中的进程"相关的一些问题。这已经被修改成了:
>
> ```
> sys.stdin.close()
> sys.stdin = open(os.open(os.devnull, os.O_RDONLY), closefd=False)
> ```
>
> 它解决了进程相互冲突导致文件描述符错误的根本问题，但是对使用带缓冲的“文件类对象”替换 [`sys.stdin()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.stdin) 作为输出的应用程序造成了潜在的危险。如果多个进程调用了此文件类对象的 [`close()`](https://docs.python.org/zh-cn/3/library/io.html#io.IOBase.close) 方法，会导致相同的数据多次刷写到此对象，损坏数据。
>
> 如果你写入文件类对象并实现了自己的缓存，可以在每次追加缓存数据时记录当前进程id，从而将其变成 fork 安全的，当发现进程id变化后舍弃之前的缓存，例如:
>
> ```
> @property
> def cache(self):
>     pid = os.getpid()
>     if pid != self._pid:
>         self._pid = pid
>         self._cache = []
>     return self._cache
> ```