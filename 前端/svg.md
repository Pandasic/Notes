# svg

> https://www.ruanyifeng.com/blog/2018/08/svg.html

## 概述

SVG 是一种基于 XML 语法的图像格式，全称是可缩放矢量图（Scalable Vector Graphics）

* svg可以直接插入网页，成为 DOM 的一部分，然后用 JavaScript 和 CSS 进行操作。
* SVG 代码也可以写在一个独立文件中，然后用`<img>`、`<object>`、`<embed>`、`<iframe>`等标签插入网页
* CSS 也可以使用 SVG 文件。
* SVG 文件还可以转为 BASE64 编码，然后作为 Data URI 写入网页

## 语法

### svg

SVG 代码都放在顶层标签`<svg>`之中。下面是一个例子。
```html
<svg width="100" height="100" viewBox="50 50 50 50">
	<circle id="mycircle" cx="50" cy="50" r="50" />
</svg>
```
* `<svg>`的width属性和height属性，指定了 SVG 图像在 HTML 元素中所占据的宽度和高度。除了相对单位，也可以采用绝对单位（单位：像素）。

  > SVG 图像默认大小是300像素（宽） x 150像素（高）。

* `<viewBox>`属性的值有四个数字，分别是左上角的横坐标和纵坐标、视口的宽度和高度。

* 如果不指定`width`属性和`height`属性，只指定`viewBox`属性，则相当于只给定 SVG 图像的长宽比。这时，SVG 图像的默认大小将等于所在的 HTML 元素的大小。

### circle

`<circle>`标签代表圆形。

```html
<svg width="300" height="180">
  <circle cx="30"  cy="50" r="25" />
  <circle cx="90"  cy="50" r="25" class="red" />
  <circle cx="150" cy="50" r="25" class="fancy" />
</svg>
```

`<circle>`标签的

* `cx`、`cy`、`r`属性分别为横坐标、纵坐标和半径，单位为像素。坐标都是相对于`<svg>`画布的左上角原点。

* `class`属性用来指定对应的 CSS 类。
   - fill：填充色
   - stroke：描边色
   - stroke-width：边框宽度

### line

`<line>`标签用来绘制直线。

 ```html
 <svg width="300" height="180">
   <line x1="0" y1="0" x2="200" y2="0" style="stroke:rgb(0,0,0);stroke-width:5" />
 </svg>
 ```

`<line>`标签

* `x1`属性和`y1`属性，表示线段起点的横坐标和纵坐标；
* `x2`属性和`y2`属性，表示线段终点的横坐标和纵坐标
* `style`属性表示线段的样式。

### polyline

`<polyline>`标签用于绘制一根折线。

```html
<svg width="300" height="180">
  <polyline points="3,3 30,28 3,53" fill="none" stroke="black" />
</svg>
```

`<polyline>`

* points`属性指定了每个端点的坐标
  * 横坐标与纵坐标之间与逗号分隔
  * 点与点之间用空格分隔。

### rect

`<rect>`标签用于绘制矩形。

```html
<svg width="300" height="180">
  <rect x="0" y="0" height="100" width="200" style="stroke: #70d5dd; fill: #dd524b" />
</svg>
```

* `<rect>`
  * ``x`属性和`y`属性，指定了矩形左上角端点的横坐标和纵坐标
  * `width`属性和`height`属性指定了矩形的宽度和高度（单位像素）。

### ellipse

`<ellipse>`标签用于绘制椭圆。

```html
<svg width="300" height="180">
  <ellipse cx="60" cy="60" ry="40" rx="20" stroke="black" stroke-width="5" fill="silver"/>
</svg>
```

* `<ellipse>`
  * ``cx`属性和`cy`属性，指定了椭圆中心的横坐标和纵坐标（单位像素）
  * `rx`属性和`ry`属性，指定了椭圆横向轴和纵向轴的半径（单位像素）。

### polygon

`<polygon>`标签用于绘制多边形。

```html
<svg width="300" height="180">
  <polygon fill="green" stroke="orange" stroke-width="1" points="0,0 100,0 100,100 0,100 0,0"/>
</svg>
```

* `<polygon>`
  * ``points`属性指定了每个端点的坐标
  * 横坐标与纵坐标之间与逗号分隔，点与点之间用空格分隔。

### path

`<path>`标签用于制路径。

```html
<svg width="300" height="180">
<path d="
  M 18,3
  L 46,3
  L 46,40
  L 61,40
  L 32,68
  L 3,40
  L 18,40
  Z
"></path>
</svg>
```

* `<path>`的`d`属性表示绘制顺序，它的值是一个长字符串，每个字母表示一个绘制动作，后面跟着坐标。

  - M：移动到（moveto）

  - L：画直线到（lineto）

  - Z：闭合路径


### text

`<text>`标签用于绘制文本。

```html
<svg width="300" height="180">
  <text x="50" y="25">Hello World</text>
</svg>
```

* `<text>`
  * ``x`属性和`y`属性，表示文本区块基线（baseline）起点的横坐标和纵坐标
  * 文字的样式可以用`class`或`style`属性指定。

### use

`<use>`标签用于复制一个形状。

```html
<svg viewBox="0 0 30 10" xmlns="http://www.w3.org/2000/svg">
  <circle id="myCircle" cx="5" cy="5" r="4"/>

  <use href="#myCircle" x="10" y="0" fill="blue" />
  <use href="#myCircle" x="20" y="0" fill="white" stroke="blue" />
</svg>
```

* `<use>`的`href`属性指定所要复制的节点
  * `x`属性和`y`属性是`<use>`左上角的坐标
  * 还可以指定`width`和`height`坐标。

### g

`<g>`标签用于将多个形状组成一个组（group），方便复用。

```html
<svg width="300" height="100">
  <g id="myCircle">
    <text x="25" y="20">圆形</text>
    <circle cx="50" cy="50" r="20"/>
  </g>

  <use href="#myCircle" x="100" y="0" fill="blue" />
  <use href="#myCircle" x="200" y="0" fill="white" stroke="blue" />
</svg>
```

### defs

`<defs>`标签用于自定义形状，它内部的代码不会显示，仅供引用。

```html
<svg width="300" height="100">
  <defs>
    <g id="myCircle">
      <text x="25" y="20">圆形</text>
      <circle cx="50" cy="50" r="20"/>
    </g>
  </defs>

  <use href="#myCircle" x="0" y="0" />
  <use href="#myCircle" x="100" y="0" fill="blue" />
  <use href="#myCircle" x="200" y="0" fill="white" stroke="blue" />
</svg>
```

### pattern

`<pattern>`标签用于自定义一个形状，该形状可以被引用来平铺一个区域。

```html
<svg width="500" height="500">
  <defs>
    <pattern id="dots" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
      <circle fill="#bee9e8" cx="50" cy="50" r="35" />
    </pattern>
  </defs>
  <rect x="0" y="0" width="100%" height="100%" fill="url(#dots)" />
</svg>
```

`<pattern>`标签将一个圆形定义为`dots`模式。`patternUnits="userSpaceOnUse"`表示`<pattern>`的宽度和长度是实际的像素值。然后，指定这个模式去填充下面的矩形。

### image

`<image>`标签用于插入图片文件。

```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <image xlink:href="path/to/image.jpg"
    width="50%" height="50%"/>
</svg>
```

`<image>`的`xlink:href`属性表示图像的来源。

### animate

`<animate>`标签用于产生动画效果。

```html
<svg width="500px" height="500px">
  <rect x="0" y="0" width="100" height="100" fill="#feac5e">
    <animate attributeName="x" from="0" to="500" dur="2s" repeatCount="indefinite" />
  </rect>
</svg>
```

上面代码中，矩形会不断移动，产生动画效果。

* `<animate>`的属性含义如下。

  - attributeName：发生动画效果的属性名。

  - from：单次动画的初始值。

  - to：单次动画的结束值。

  - dur：单次动画的持续时间。

  - repeatCount：动画的循环模式。


可以在多个属性上面定义动画。

```html
<animate attributeName="x" from="0" to="500" dur="2s" repeatCount="indefinite" />
<animate attributeName="width" to="500" dur="2s" repeatCount="indefinite" />
```

### animateTransform

`<animate>`标签对 CSS 的`transform`属性不起作用，如果需要变形，就要使用`<animateTransform>`标签。

```html
<svg width="500px" height="500px">
  <rect x="250" y="250" width="50" height="50" fill="#4bc0c8">
    <animateTransform attributeName="transform" type="rotate" begin="0s" dur="10s" from="0 200" to="360 400 400" repeatCount="indefinite" />
  </rect>
</svg>
```

上面代码中，`<animateTransform>`的效果为旋转（`rotate`），这时`from`和`to`属性值有三个数字，第一个数字是角度值，第二个值和第三个值是旋转中心的坐标。`from="0 200"`表示开始时，角度为0，围绕`(200, 200)`开始旋转；`to="360 400 400"`表示结束时，角度为360，围绕`(400, 400)`旋转。

## js 操作

### DOM 操作

```html
<svg
   id="mysvg"
   xmlns="http://www.w3.org/2000/svg"
   viewBox="0 0 800 600"
   preserveAspectRatio="xMidYMid meet"

   <circle id="mycircle" cx="400" cy="300" r="50" />
 <svg>
```

上面代码插入网页之后，就可以用 CSS 定制样式。

```css
circle {
   stroke-width: 5;
   stroke: #f00;
  fill: #ff0;
 }
 
 circle:hover {
   stroke: #090;
   fill: #fff;
 }
```

然后，可以用 JavaScript 代码操作 SVG。

```javascript
var mycircle = document.getElementById('mycircle');

mycircle.addEventListener('click', function(e) {
  console.log('circle clicked - enlarging');
  mycircle.setAttribute('r', 60);
}, false);
```

### 获取 SVG DOM

使用`<object>`、`<iframe>`、`<embed>`标签插入 SVG 文件，可以获取 SVG DOM。

```javascript
var svgObject = document.getElementById('object').contentDocument;
var svgIframe = document.getElementById('iframe').contentDocument;
var svgEmbed = document.getElementById('embed').getSVGDocument();
```

注意，如果使用`<img>`标签插入 SVG 文件，就无法获取 SVG DOM。



SVG 文件就是一段 XML 文本，因此可以通过读取 XML 代码的方式，读取 SVG 源

使用`XMLSerializer`实例的`serializeToString()`方法，获取 SVG 元素的代码。

> ```javascript
> var svgString = new XMLSerializer()
>   .serializeToString(document.querySelector('svg'))
> ```