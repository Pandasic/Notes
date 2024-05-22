# jquery

>  https://www.runoob.com/jquery/jquery-intro.html

## 安装/引入

- 从 [jquery.com](http://jquery.com/download/) 下载 jQuery 库

  - ```
    <script src="jquery-1.10.2.min.js"></script>
    ```

- 从 CDN 中载入 jQuery

  * \<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"/>

  * \<script src="https://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.2.min.js"/>

  * \<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"/>

  * \<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.min.js"/\>


* $.fn.jquery 命令查看当前 jQuery 使用的版本

## jQuery 功能

jQuery 是一个 JavaScript 函数库。jQuery 是一个轻量级的"写的少，做的多"的 JavaScript 库。Query 库包含以下功能：

- HTML 元素选取
- HTML 元素操作
- CSS 操作
- HTML 事件函数
- JavaScript 特效和动画
- HTML DOM 遍历和修改
- AJAX
- Utilities

## 语法

jQuery 语法是通过选取 HTML 元素，并对选取的元素执行某些操作。

- 美元符号定义 jQuery
- 选择符（selector）"查询"和"查找" HTML 元素
- jQuery 的 action() 执行对元素的操作

eg:

- $(this).hide() - 隐藏当前元素
- $("p").hide() - 隐藏所有 <p> 元素
- $("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素
- $("#test").hide() - 隐藏 id="test" 的元素

> jQuery 使用的语法是 XPath 与 CSS 选择器语法的组合。

所有 jQuery 函数位于一个 document ready 函数中,这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码，即在 DOM 加载完成后才可以对 DOM 进行操作

如果在文档没有完全加载之前就运行函数，操作可能失败。下面是两个具体的例子

- 试图隐藏一个不存在的元素
- 获得未完全加载的图像的大小

## 选择器

| 语法                     | 描述                                                    |
| ------------------------ | ------------------------------------------------------- |
| $("*")                   | 选取所有元素                                            |
| $(this)                  | 选取当前 HTML 元素                                      |
| $("p")                   | 选择器基于元素名选取元素。                              |
| $("#test")               | #id 选择器 选取所有id为test 的元素                      |
| $(".test")               | .class 选择器 选取所有类为test的元素                    |
| $("p.intro")             | 选取 class 为 intro 的 <p> 元素                         |
| $("p:first")             | 选取第一个 <p> 元素                                     |
| $("ul li:first")         | 选取第一个 <ul> 元素的第一个 <li> 元素                  |
| $("ul li:first-child")   | 选取每个 <ul> 元素的第一个 <li> 元素                    |
| $("[href]")              | 选取带有 href 属性的元素                                |
| $("a[target='_blank']")  | 选取所有 target 属性值等于 "_blank" 的 <a> 元素         |
| $("a[target!='_blank']") | 选取所有 target 属性值不等于 "_blank" 的 <a> 元素       |
| $(":button")             | 选取所有 type="button" 的 <input> 元素 和 <button> 元素 |
| $("tr:even")             | 选取偶数位置的 <tr> 元素                                |
| $("tr:odd")              | 选取奇数位置的 <tr> 元素                                |

## 事件

常见 DOM 事件：

| 鼠标事件   | 键盘事件 | 表单事件 | 文档/窗口事件 |
| ---------- | -------- | -------- | ------------- |
| click      | keypress | submit   | load          |
| dblclick   | keydown  | change   | resize        |
| mouseenter | keyup    | focus    | scroll        |
| mouseleave |          | blur     | unload        |
| hover      |          |          | ready()       |

eg:
```js
$("p").click(function(){
  $(this).hide();
});
```

## 效果

### 隐藏/显示

```js
$(*selector*).hide(*speed,callback*);
$(*selector*).show(*speed,callback*);
$(selector).toggle(speed,callback);  //切换 hide() 和 show() 方法。
```

* 可选的 speed 参数规定隐藏/显示的速度，可以取以下值："slow"、"fast" 或毫秒。

* 可选的 callback 参数是隐藏或显示完成后所执行的函数名称。

```
$("#hide").click(function(){
  $("p").hide();
});
 
$("#show").click(function(){
  $("p").show();
});
```

### 淡入淡出

```js
$(selector).fadeIn(speed,callback); // 淡入
$(selector).fadeOut(speed,callback); // 淡出
$(selector).fadeToggle(speed,callback);// 淡入/淡出 切换
$(selector).fadeTo(speed,opacity,callback); // 渐变为给定的不透明度（值介于0与1之间）。
```

* 可选的 speed 参数规定效果的时长。它可以取以下值："slow"、"fast" 或毫秒。.
* 可选的 callback 参数是 fading 完成后所执行的函数名称。

### 滑动

```js
$(selector).slideDown(speed,callback); // 下滑
$(selector).slideUp(speed,callback); //上滑
$(selector).slideToggle(speed,callback); // 上滑/下滑 切换
```

可选的 speed 参数规定效果的时长。它可以取以下值："slow"、"fast" 或毫秒。

可选的 callback 参数是滑动完成后所执行的函数名称

### 动画

```
$(selector).animate({params},speed,callback);
```

* 必需的 params 参数定义形成动画的 CSS 属性。
* 可选的 speed 参数规定效果的时长。它可以取以下值："slow"、"fast" 或毫秒。
* 可选的 callback 参数是动画完成后所执行的函数名称。

eg：

例子演示 animate() 方法的简单应用。它把 <div> 元素往右边移动了 250 像素

```
$("button").click(function(){  $("div").animate({left:'250px'}); });
```

> 当使用 animate() 时，必须使用 Camel 标记法书写所有的属性名，比如，必须使用 paddingLeft 而不是 padding-left，使用 marginRight 而不是 margin-right，

> 色彩动画并不包含在核心 jQuery 库中。 如果需要生成颜色动画，您需要从 jquery.com 下载  [颜色动画](http://plugins.jquery.com/color/) 插件。

#### 相对值

也可以定义相对值（该值相对于元素的当前值）。需要在值的前面加上 += 或 -=

```js
$("button").click(function(){
  $("div").animate({
    left:'250px',
    height:'+=150px',
    width:'+=150px'
  });
});
```

#### 预定义的值

动画值设置为 "show"、"hide" 或 "toggle"：

```js
$("button").click(function(){
  $("div").animate({
    height:'toggle'
  });
});
```

#### 动画队列

Query 提供针对动画的队列功能。

这意味着如果您在彼此之后编写多个 animate() 调用，jQuery 会创建包含这些方法调用的"内部"队列。然后逐一运行这些 animate 调用。

```js
div.animate({height:'300px',opacity:'0.4'},"slow");
div.animate({width:'300px',opacity:'0.8'},"slow");
div.animate({height:'100px',opacity:'0.4'},"slow");
div.animate({width:'100px',opacity:'0.8'},"slow");
```

#### 停止

```js
(selector).stop(stopAll,goToEnd);
```

 stopAll 参数规定是否应该清除动画队列。默认是 false，即仅停止活动的动画，允许任何排入队列的动画向后执行。

 goToEnd 参数规定是否立即完成当前动画。默认是 false。

#### callback

Callback 函数在当前动画 100% 完成之后执行。

#### 链(Chaining)

有一种名为链接（chaining）的技术，允许我们在相同的元素上运行多条 jQuery 命令，一条接着另一条

如需链接一个动作，您只需简单地把该动作追加到之前的动作上。

eg:

```js
$("#p1").css("color","red").slideUp(2000).slideDown(2000);
```

## html

### 捕获/设置

```
$("#test1").text();
$("#test1").text(value, callback(index, originVal));
```

- text() - 设置或返回所选元素的文本内容
- html() - 设置或返回所选元素的内容（包括 HTML 标记）
- val() - 设置或返回表单字段的值
- attr() 方法用于获取属性值。
  - `alert($("#runoob").attr("href"));`
  - 如果有相应的属性，返回指定属性值。
  - 如果没有相应的属性，返回值是 undefined。
  - 对于 HTML 元素我们自己自定义的 DOM 属性，在处理时，使用 **attr** 方法。
- prop
  - 如果有相应的属性，返回指定属性值。
  - 如果没有相应的属性，返回值是空字符串
  - 对于 HTML 元素本身就带有的固有属性，在处理时，使用 **prop** 方法。

### 添加元素

- append() - 在被选元素的结尾插入内容 ，所选元素作为父容器
- prepend() - 在被选元素的开头插入内容 ，所选元素作为父容器
- after() - 在被选元素之后插入内容 ，所选元素作为父容器
- before() - 在被选元素之前插入内容 ，所选元素作为父容器

### 删除

- remove() - 删除被选元素（及其子元素）
  - remove() 方法也可接受一个参数，允许您对被删元素进行过滤
  - `$("p").remove(".italic");`
- empty() - 从被选元素中删除子元素

## CSS

- addClass() - 向被选元素添加一个或多个类
  - $("h1,h2,p").addClass("blue");
  - ("body div:first").addClass("important blue");
- removeClass() - 从被选元素删除一个或多个类
- toggleClass() - 对被选元素进行添加/删除类的切换操作
  - toggleClass() 方法。该方法对被选元素进行添加/删除类的切换操作
- css() - 设置或返回样式属性
  - 返回 $("p").css("background-color");
  - 设置 css("background-color","yellow");

## 尺寸

- width() 
  - width() 方法设置或返回元素的宽度（不包括内边距、边框或外边距）
- height()
  - height() 方法设置或返回元素的高度（不包括内边距、边框或外边距）
- innerWidth()
  - innerWidth() 方法返回元素的宽度（包括内边距）
- innerHeight()
  - innerHeight() 方法返回元素的高度（包括内边距）
- outerWidth()
  - outerWidth() 方法返回元素的宽度（包括内边距和边框）
- outerHeight()
  - outerHeight() 方法返回元素的高度（包括内边距和边框）

## 遍历Dom

### 祖先

* parent() 方法返回被选元素的直接父元素
* parents() 方法返回被选元素的所有祖先元素，它一路向上直到文档的根元素 (\<html>)。通过可选参数过滤元素

* parentsUntil() 方法返回介于两个给定元素之间的所有祖先元素。

### 后代

* children() 方法返回被选元素的所有直接子元素。该方法只会向下一级对 DOM 树进行遍历。可以使用可选参数来过滤对子元素的搜索
* ind() 方法返回被选元素的后代元素，一路向下直到最后一个后代

### 同胞

同胞拥有相同的父元素。

- siblings()方法返回被选元素的所有同胞元素。可选参数来过滤对同胞元素的搜索。
- next()，被选元素的下一个同胞元素。
- nextAll()，方法返回被选元素的所有跟随的同胞元素
- nextUntil()， 返回介于两个给定参数之间的所有跟随的同胞元素。
- prev()，prevAll()，prevUntil()，与上面的方法类似，只不过方向相反而已

### 过滤

* first() 方法返回被选元素的首个元素
  * $("div p").first(); 
  * 选取首个 <div> 元素内部的第一个 <p> 元素：

* last() 方法返回被选元素的最后一个元素。
  * 下面的例子选择最后一个 <div> 元素中的最后一个 <p> 元素：
  * $("div p").last();
* eq() 方法返回被选元素中带有指定索引号的元素。
  * 索引号从 0 开始，因此首个元素的索引号是 0 而不是 1。下面的例子选取第二个 <p> 元素（索引号 1）
  * $("p").eq(1);
* filter() 方法允许您规定一个标准。不匹配这个标准的元素会被从集合中删除，匹配的元素会被返回。
* not() 方法返回不匹配标准的所有元素。not() 方法与 filter() 相反。

## AJAX

AJAX = 异步 JavaScript 和 XML（Asynchronous JavaScript and XML）。

简短地说，在不重载整个网页的情况下，AJAX 通过后台加载数据，并在网页上进行显示

### load

load() 方法从服务器加载数据，并把返回的数据放入被选元素中。

```
$(selector).load(URL,data,callback);
```

* url

也可以把 jQuery 选择器添加到 URL 参数。
下面的例子把  "demo_test.txt" 文件中 id="p1" 的元素的内容，加载到指定的 <div> 元素中

```html
<h2>jQuery AJAX 是个非常棒的功能！</h2>
<p id="p1">这是段落的一些文本。</p>
```

```js
$("#div1").load("demo_test.txt #p1");
```

* callback, 参数规定当 load() 方法完成后所要允许的回调函数。回调函数可以设置不同的参数
  - *responseTxt* - 包含调用成功时的结果内容
  - *statusTXT* - 包含调用的状态
  - *xhr* - 包含 XMLHttpRequest 对象

### get

$.get() 方法通过 HTTP GET 请求从服务器上请求数据。

```
$.get( URL [, data ] [, callback ] [, dataType ] )
```

- **URL**：发送请求的 URL字符串。
- **data**：可选的，发送给服务器的字符串或 key/value 键值对。
- **callback**：可选的，请求成功后执行的回调函数。
- **dataType**：可选的，从服务器返回的数据类型。默认：智能猜测（可以是xml, json, script, 或 html）

### post

$.post() 方法通过 HTTP POST 请求向服务器提交数据。

```
$.post( URL [, data ] [, callback ] [, dataType ] )
```

- **URL**：发送请求的 URL字符串。
- **data**：可选的，发送给服务器的字符串或 key/value 键值对。
- **callback**：可选的，请求成功后执行的回调函数。
- **dataType**：可选的，从服务器返回的数据类型。默认：智能猜测（可以是xml, json, script, 或 html）

## noConflict()

noConflict() 方法会释放对 $ 标识符的控制,防止不同框架间的冲突

## JSONP

https://zhuanlan.zhihu.com/p/24390509

https://www.cnblogs.com/soyxiaobi/p/9616011.html

Jsonp(JSON with Padding) 是 json 的一种"使用模式"，可以让网页从别的域名（网站）那获取资料，即跨域读取数据，它允许在服务器端集成Script tags返回至客户端，通过javascript callback的形式实现跨域访问（这仅仅是JSONP简单的实现形式）

为什么我们从不同的域（网站）访问数据需要一个特殊的技术( JSONP )呢？这是因为同源策略。

用 JSONP 抓到的资料并不是 JSON，而是任意的JavaScript，用 JavaScript 直译器执行而不是用 JSON 解析器解析。

同源策略，它是由 Netscape 提出的一个著名的安全策略，现在所有支持 JavaScript 的浏览器都会使用这个策略