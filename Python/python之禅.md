# Python 之禅(The Zen of Python)

> 参考
>
> https://www.python.org/dev/peps/pep-0020/
>
>  https://zhuanlan.zhihu.com/p/40950546

```python
import this
```

```text
PEP 20 -- The Zen of Python
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

**翻译**

```text
优美 > 丑陋

明确 > 隐晦 （1）

简单 > 复杂

复杂 > 繁复 （2）

扁平 > 嵌套

稀疏 > 拥挤（3）

可读性很重要（4）

固然代码的实用性比洁癖更重要，

所谓的“特例”也往往没有特殊到必须违背上述规则的程度

除非必要，否则不要无故忽视异常（5）

如果遇到模棱两可的逻辑，请不要自作聪明地瞎猜。

应该提供一种，且最好**只**提供一种，一目了然的途径

当然这是没法一蹴而就的，除非你是荷兰人（6）

固然，立刻着手 好过 永远不做。

然而，永远不做 也好过 闷头蛮干

倘若你的实现很难解释，它**一定不是**个好主意

倘若你的实现一目了然，它**可能是**个好主意（7）

命名空间大法好，同志们要多多搞！
```

**考据**

1. 该引入的包显式地一条条罗列出来，不要合并；不要用星号；不要在方法里藏意想不到的的副作用，等等等等。还一个例子，有一种著名的软件设计原则 Convention over Configuration（约定优于配置）如果做得不谨慎，比如你约定的规则并不是真的业界惯例，就会违背这条。
2. StackOverflow上针对这句话的提问: [必要的复杂总是难免的，繁复啰嗦的代码却是不可接受的](https://link.zhihu.com/?target=https%3A//stackoverflow.com/a/4568759/1471046)。你可以做很多事，很复杂的事，但是不能啰嗦，更不能难以理解。复杂不是罪，但是代码需要更有逻辑、更有机的组织。简而言之，Simple > Complex > Complicated >  Chaotic。（另外，以上内容仅限Python语境，不同语境下对Complex和Complicated的定义可能会有所不同）
3. 有人喜欢写很长的one-liner 比如：`lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]]) # 一行流快速排序`  这样固然可以炫技，但是也很难懂啊。让其他人读不懂的代码不是优雅的代码
4. 写这篇文章的动机之一就是看到有人把 Readability counts 翻译成可读性计数 
5. 实操中很多人不注意 catch 完就 log 一下就不管了，很快啊，这样好么？这样不好。软件界一般都讲 Let it fail，学名为 [Fail-fast 法则](https://link.zhihu.com/?target=https%3A//dzone.com/articles/fail-fast-principle-in-software-development)。简而言之就是整个项目周期中越早暴露的问题，其修复成本越低。等到你的项目上线了结果出来各种诡异的bug你会毫无头绪，结果只能去翻长长的日志。所以我劝各位，不要再犯这样的聪明，小聪明。
6. [本文作者 Tim Peters 解释说这里的荷兰人指的是 Python 的作者 Guido van Rossum](https://link.zhihu.com/?target=https%3A//softwareengineering.stackexchange.com/a/148794/173276) 吹捧 gvanrossum 的彩虹屁：等同于*“你个荷兰佬他娘的还真是个天才”*
7. 贯穿整个 PEP 20 的核心就是一句话“你的代码是给别人读的！”。从这个角度而言，难以理解、难以维护的代码，即便是“高性能”，也肯定不是好代码；但是反过来，一目了然的逻辑也不代表就一定是好代码。编程可太难了