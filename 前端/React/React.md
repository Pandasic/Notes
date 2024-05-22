# React

> 官方文档：https://zh-hans.reactjs.org

## 简介

**React** 是一个用于构建用户界面的 JavaScript 库

## 创建

[Create React App](https://github.com/facebookincubator/create-react-app) 是一个用于**学习 React** 的舒适环境，也是用 React 创建**新的单页应用**的最佳方式

```sh
# Node >= 14.0.0 和 npm >= 5.6
npx create-react-app my-app
cd my-app
npm start
```

### CDN 链接

* 开发环境

```html
<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
```

* 压缩优化后 生产环境的React

```html
<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
```

> 其中 @18 为对应的版本，如须其他版本 更改所需版本

> crossorigin 用于处理跨域请求

## JSX

JSX，是一个 JavaScript 的语法扩展。JSX 可以生成 React “元素”。

### 嵌入表达式

在 JSX 语法中，你可以在大括号内放置任何有效的

```jsx
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;
```

### JSX 也是表达式

在编译之后，JSX 表达式会被转为普通 JavaScript 函数调用，并且对其取值后得到 JavaScript 对象。

也就是说，你可以在 `if` 语句和 `for` 循环的代码块中使用 JSX，将 JSX 赋值给变量，把 JSX 当作参数传入，以及从函数中返回 JSX

```jsx
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;  }
  return <h1>Hello, Stranger.</h1>;}
```

### JSX 中指定属性 

你可以通过使用引号，来将属性值指定为字符串字面量：

```jsx
const element = <a href="https://www.reactjs.org"> link </a>;
```

也可以使用大括号，来在属性值中插入一个 JavaScript 表达式：

```jsx
const element = <img src={user.avatarUrl}></img>;
```

在属性中嵌入 JavaScript 表达式时，不要在大括号外面加上引号。你应该仅使用引号（对于字符串值）或大括号（对于表达式）中的一个，对于同一属性不能同时使用这两种符号。

> 因为 JSX 语法上更接近 JavaScript 而不是 HTML，所以 React DOM 使用 `camelCase`（小驼峰命名）来定义属性的名称

### 使用 JSX 指定子元素 

假如一个标签里面没有内容，你可以使用 `/>` 来闭合标签，就像 XML 语法一样：

```jsx
const element = <img src={user.avatarUrl} />;
```

JSX 标签里能够包含很多子元素:

```jsx
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

### JSX 防止注入攻击 

你可以安全地在 JSX 当中插入用户输入内容：

```jsx
const title = response.potentiallyMaliciousInput;
// 直接使用是安全的：
const element = <h1>{title}</h1>;
```

React DOM 在渲染所有输入内容之前，默认会进行[转义](https://stackoverflow.com/questions/7381974/which-characters-need-to-be-escaped-on-html)。它可以确保在你的应用中，永远不会注入那些并非自己明确编写的内容。所有的内容在渲染之前都被转换成了字符串。这样可以有效地防止 [XSS（cross-site-scripting, 跨站脚本）](https://en.wikipedia.org/wiki/Cross-site_scripting)攻击。

### JSX 表示对象 

Babel 会把 JSX 转译成一个名为 `React.createElement()` 函数调用。

以下两种示例代码完全等效：

```jsx
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

`React.createElement()` 会预先执行一些检查，以帮助你编写无错代码，但实际上它创建了一个这样的对象：

```jsx
// 注意：这是简化过的结构
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world!'
  }
};
```

这些对象被称为 “React 元素”。它们描述了你希望在屏幕上看到的内容。React 通过读取这些对象，然后使用它们来构建 DOM 以及保持随时更新。

> **提示：**
>
> 我们推荐在你使用的编辑器中，使用 [“Babel” 提供的语言定义](https://babeljs.io/docs/en/next/editors)，来正确地高亮显示 ES6 和 JSX 代码。

## 元素渲染

React 元素是创建开销极小的普通对象。React DOM 会负责更新 DOM 来与 React 元素保持一致。

### 将一个元素渲染为 DOM 

仅使用 React 构建的应用通常只有单一的根 DOM 节点。如果你在将 React 集成进一个已有应用，那么你可以在应用中包含任意多的独立根 DOM 节点。

想要将一个 React 元素渲染到根 DOM 节点中，只需把它们一起传入 [`ReactDOM.createRoot()`](https://zh-hans.reactjs.org/docs/react-dom-client.html#createroot)：

```jsx
const root = ReactDOM.createRoot(
  document.getElementById('root')
);
const element = <h1>Hello, world</h1>;
root.render(element);
```

### 更新已渲染的元素 

React 元素是[不可变对象](https://en.wikipedia.org/wiki/Immutable_object)。一旦被创建，你就无法更改它的子元素或者属性。

更新 UI 唯一的方式是创建一个全新的元素，并将其传入 `root.render()`

> React DOM 会将元素和它的子元素与它们之前的状态进行比较，并只会进行必要的更新来使 DOM 达到预期的状态。

## 组件 & Props

组件允许你将 UI 拆分为独立可复用的代码片段，并对每个片段进行独立构思。

组件，从概念上类似于 JavaScript 函数。它接受任意的入参（即 “props”），并返回用于描述页面展示内容的 React 元素。

### 函数组件与class 组件

* 函数组件 , 本质上就是 JavaScript 函数

  ```react
  function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
  }
  ```

  * 接收唯一带有数据的 “props”（代表属性）对象

  * 返回一个 React 元素

* class 组件 为 [ES6 的 class](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes) 来定义组件

  ```react
  class Welcome extends React.Component {
    render() {
      return <h1>Hello, {this.props.name}</h1>;
    }
  }
  ```

### 将函数组件转换成 class 组件 

通过以下五步将 `Clock` 的函数组件转成 class 组件：

1. 创建一个同名的 [ES6 class](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes)，并且继承于 `React.Component`。
2. 添加一个空的 `render()` 方法。
3. 将函数体移动到 `render()` 方法之中。
4. 在 `render()` 方法中使用 `this.props` 替换 `props`。
5. 删除剩余的空函数声明。

### 渲染组件

React 元素 可以是DOM 标签，也可以是用户自定义的组件

```react
const element = <div />;
const element = <Welcome name="Sara" />;
```

当 React 元素为用户自定义组件时，它会将 JSX 所接收的属性（attributes）以及子组件（children）转换为单个对象传递给组件，这个对象被称之为 “props”。

eg:

```react
function Welcome(props) {  return <h1>Hello, {props.name}</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
const element = <Welcome name="Sara" />;root.render(element);

// Output Hello, Sara
```

1. 我们调用 `root.render()` 函数，并传入 `<Welcome name="Sara" />` 作为参数。
2. React 调用 `Welcome` 组件，并将 `{name: 'Sara'}` 作为 props 传入。
3. `Welcome` 组件将 `<h1>Hello, Sara</h1>` 元素作为返回值。
4. React DOM 将 DOM 高效地更新为 `<h1>Hello, Sara</h1>`。

### 组合组件

组件可以在其输出中引用其他组件。这就可以让我们用同一组件来抽象出任意层次的细节。按钮，表单，对话框，甚至整个屏幕的内容：在 React 应用程序中，这些通常都会以组件的形式表示。通过提取提取组件 实现代码解耦。

eg: 可以多次渲染 `Welcome` 组件的 `App` 组件：

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />      <Welcome name="Cahal" />      <Welcome name="Edite" />    </div>
  );
}
```

### props 只读性

组件无论是使用[函数声明还是通过 class 声明](https://zh-hans.reactjs.org/docs/components-and-props.html#function-and-class-components)，都绝不能修改自身的 props。来看下这个 `sum` 函数：

```react
function sum(a, b) {
  return a + b;
}
```

这样的函数被称为[“纯函数”](https://en.wikipedia.org/wiki/Pure_function)，因为该函数不会尝试更改入参，且多次调用下相同的入参始终返回相同的结果。

相反，下面这个函数则不是纯函数，因为它更改了自己的入参：

```react
function withdraw(account, amount) {
  account.total -= amount;
}
```

React 非常灵活，但它也有一个严格的规则：

**所有 React 组件都必须像纯函数一样保护它们的 props 不被更改。**

## State & 生命周期

### 生命周期

当组件第一次被渲染到 DOM 中的时候，这在 React 中被称为“挂载（mount）”。

同时，当 DOM 中组件被删除的时候，这在 React 中被称为“卸载（unmount）”。

class 组件声明一些特殊的方法，当组件挂载或卸载时就会去执行这些方法, 这些方法叫做“生命周期方法”。：

```react
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }
	
  // 挂载时触发
  componentDidMount() {  }
  // 卸载时触发
  componentWillUnmount() {  }
}
```

### 

[react 生命周期如下](https://www.jianshu.com/p/b331d0e4b398)

![img](img/React/webp)

### 局部state

每次组件更新时class 组件中的 `render` 方法都会被调用，但只要在相同的 DOM 节点中渲染 `<Clock />` ，就仅有一个 `Clock` 组件的 class 实例被创建使用。这就使得我们可以使用如 state 或生命周期方法等很多其他特性。

state 在 class 的构造函数中初始化

```react
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};  }
}
```

> Class 组件应该始终使用 `props` 参数来调用父类的构造函数。

访问 this.state 来获取对应值

```react
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>      					</div>
    );
  }
```

使用 `this.setState()` 来更新组件 state

```react
this.setState({      
  date: new Date()    
});
```

### 正确地使用 State 

* 不要直接修改 State

  * 例如，此代码不会重新渲染组件：

    ```
    // Wrong
    this.state.comment = 'Hello';
    ```

* State 的更新可能是异步的 

  * 出于性能考虑，React 可能会把多个 `setState()` 调用合并成一个调用。

    因为 `this.props` 和 `this.state` 可能会异步更新，所以你不要依赖他们的值来更新下一个状态。

  * 例如，此代码可能会无法更新计数器：

    ```react
    // Wrong
    this.setState({
      counter: this.state.counter + this.props.increment,
    });
    ```

  * 要解决这个问题，可以让 `setState()` 接收一个函数而不是一个对象。这个函数用上一个 state 作为第一个参数，将此次更新被应用时的 props 做为第二个参数：

    ```react
    // Correct
    this.setState((state, props) => ({
      counter: state.counter + props.increment
    }));
    ```

    > 上面使用了[箭头函数](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)，不过使用普通的函数也同样可以：

* State 的更新会被合并 
  * 当你调用 `setState()` 的时候，React 会把你提供的对象合并到当前的 state。
  * 这里的合并是浅合并

### 数据是向下流动的

这通常会被叫做“自上而下”或是“单向”的数据流。任何的 state 总是所属于特定的组件，而且从该 state 派生的任何数据或 UI 只能影响树中“低于”它们的组件。

如果你把一个以组件构成的树想象成一个 props 的数据瀑布的话，那么每一个组件的 state 就像是在任意一点上给瀑布增加额外的水源，但是它只能向下流动。

## 事件处理

React 事件与原生 HTML/JS 事件区别

- React 事件的命名采用小驼峰式（camelCase），而不是纯小写。
- 使用 JSX 语法时你需要传入一个函数作为事件处理函数，而不是一个字符串。

例如，传统的 HTML：

```
<button onclick="activateLasers()">
  Activate Lasers
</button>
```

在 React 中略微不同：

```
<button onClick={activateLasers}>  Activate Lasers
</button>
```

* 在 React 中另一个不同点是你不能通过返回 `false` 的方式阻止默认行为。你必须显式地使用 `preventDefault`。

HTML 中阻止表单的默认提交行为，你可以这样写：

```html
<form onsubmit="console.log('You clicked submit.'); return false">
  <button type="submit">Submit</button>
</form>
```

在 React 中，可能是这样的：

```react
function Form() {
  function handleSubmit(e) {
    e.preventDefault();    
    console.log('You clicked submit.');
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Submit</button>
    </form>
  );
}
```

> `e` 是一个合成事件。React 事件与原生事件不完全相同。如果想了解更多，请查看 [`SyntheticEvent`](https://zh-hans.reactjs.org/docs/events.html) 参考指南。

使用 React 时，你一般不需要使用 `addEventListener` 为已创建的 DOM 元素添加监听器。事实上，你只需要在该元素初始渲染的时候添加监听器即可。

```react
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // 为了在回调中使用 `this`，这个绑定是必不可少的    
    this.handleClick = this.handleClick.bind(this);  }

  handleClick() {    
    this.setState(prevState => ({      
      isToggleOn: !prevState.isToggleOn
    }));  
  }
  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}
```

你必须谨慎对待 JSX 回调函数中的 `this`，在 JavaScript 中，class 的方法默认不会[绑定](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_objects/Function/bind) `this`。如果你忘记绑定 `this.handleClick` 并把它传入了 `onClick`，当你调用这个函数的时候 `this` 的值为 `undefined`。

如果觉得使用 `bind` 很麻烦，这里有两种方式可以解决。你可以使用 [public class fields 语法](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#public_instance_fields) to correctly bind callbacks

```react
class LoggingButton extends React.Component {
  // This syntax ensures `this` is bound within handleClick.  
  handleClick = () => {    console.log('this is:', this);  };  render() 	{
    return (
      <button onClick={this.handleClick}>
        Click me
      </button>
    );
  }
}
```

[Create React App](https://github.com/facebookincubator/create-react-app) 默认启用此语法。

### 向事件处理程序传递参数

在循环中，通常我们会为事件处理函数传递额外的参数。例如，若 `id` 是你要删除那一行的 ID，以下两种方式都可以向事件处理函数传递参数

```react
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

上述两种方式是等价的，分别通过[箭头函数](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)和 [`Function.prototype.bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) 来实现。

## 条件渲染

### if/条件运算符

React 中的条件渲染和 JavaScript 中的一样，使用 JavaScript 运算符 [`if`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) 或者[条件运算符](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)去创建元素来表现当前的状态，然后让 React 根据它们来更新 UI。

eg :

```react
function UserGreeting(props) {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>;
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {    
    return <UserGreeting />;  
  }  
  return <GuestGreeting />;
}

const root = ReactDOM.createRoot(document.getElementById('root')); 
// Try changing to isLoggedIn={true}:
root.render(<Greeting isLoggedIn={false} />);
```

### 逻辑运算符

JavaScript 中的逻辑与 (&&) 运算符。它可以很方便地进行元素的条件渲染

`true && expression` 总是会返回 `expression`,

而 `false && expression` 总是会返回 `false`。

```react
{unreadMessages.length > 0 &&
  <h2>          
   You have {unreadMessages.length} unread messages.
 </h2>      
}
```

### 三目运算符

另一种内联条件渲染的方法是使用 JavaScript 中的三目运算符 [`condition ? true : false`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)。

### 阻止组件渲染 

在极少数情况下，你可能希望能隐藏组件，即使它已经被其他组件渲染。若要完成此操作，你可以让 `render` 方法直接返回 `null`，而不进行任何渲染。

## 列表 & KEY

你可以通过使用 `{}` 在 JSX 内构建一个[元素集合](https://zh-hans.reactjs.org/docs/introducing-jsx.html#embedding-expressions-in-jsx)。

下面，我们使用 Javascript 中的 [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) 方法来遍历 `numbers` 数组。将数组中的每个元素变成 `<li>` 标签，最后我们将得到的数组赋值给 `listItems`：

```react
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>  <li>{number}</li>);
```

然后，我们可以将整个 `listItems` 插入到 `<ul>` 元素中：

```react
<ul>{listItems}</ul>
```

### 列表组件

我们可以把前面的例子重构成一个组件，这个组件接收 `numbers` 数组作为参数并输出一个元素列表。

```react
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>    
		<li key={number.toString()}>
			{number}
 		</li>  );  
  return (
    <ul >{listItems}</ul>  
  );
}

const numbers = [1, 2, 3, 4, 5];
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<NumberList numbers={numbers} />);
```

> 若删除li 的key 属性，将会看到一个警告 `a key should be provided for list items`，意思是当你创建一个元素时，必须包括一个特殊的 `key` 属性。我们将在下一节讨论这是为什么

### key 

key 帮助 React 识别哪些元素改变了，比如被添加或删除。因此你应当给数组中的每一个元素赋予一个确定的标识，一个元素的 key 最好是这个元素在列表中拥有的一个独一无二的字符串。通常，我们使用数据中的 id 来作为元素的 key

**key 值在兄弟节点之间必须唯一** 

如果列表项目的顺序可能会变化，我们不建议使用索引来用作 key 值，因为这样做会导致性能变差，还可能引起组件状态的问题。

> 要是你有兴趣了解更多的话，这里有一篇文章[深入解析为什么 key 是必须的](https://zh-hans.reactjs.org/docs/reconciliation.html#recursing-on-children)可以参考

#### 用 key 提取组件 

元素的 key 只有放在就近的数组上下文中才有意义。

比方说，如果你[提取](https://zh-hans.reactjs.org/docs/components-and-props.html#extracting-components)出一个 `ListItem` 组件，你应该把 key 保留在数组中的这个 `<ListItem />` 元素上，而不是放在 `ListItem` 组件中的 `<li>` 元素上。

**例子：不正确的使用 key 的方式**

```react
function ListItem(props) {
  const value = props.value;
  return (
    // 错误！你不需要在这里指定 key：    <li key={value.toString()}>      {value}
    </li>
  );
}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // 错误！元素的 key 应该在这里指定：    <ListItem value={number} />  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}
```

**例子：正确的使用 key 的方式**

```react
function ListItem(props) {
  // 正确！这里不需要指定 key：  return <li>{props.value}</li>;}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // 正确！key 应该在数组的上下文中被指定    <ListItem key={number.toString()} value={number} />  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}
```

key 会传递信息给 React ，但不会传递给你的组件。如果你的组件中需要使用 `key` 属性的值，请用其他属性名显式传递这个值

## 表单

### 受控组件

在 HTML 中，表单元素（如`<input>`、 `<textarea>` 和 `<select>`）通常自己维护 state，并根据用户输入进行更新。而在 React 中，可变状态（mutable state）通常保存在组件的 state 属性中，并且只能通过使用 [`setState()`](https://zh-hans.reactjs.org/docs/react-component.html#setstate)来更新。

我们可以把两者结合起来，使 React 的 state 成为“唯一数据源”。渲染表单的 React 组件还控制着用户输入过程中表单发生的操作。被 React 以这种方式控制取值的表单输入元素就叫做“受控组件”。

例如，如果我们想让前一个示例在提交时打印出名称，我们可以将表单写为受控组件：

```react
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {    
    this.setState({value: event.target.value});  
  }
  
  handleSubmit(event) {
    alert('提交的名字: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>        <label>
          名字:
          <input type="text" value={this.state.value} onChange={this.handleChange} />        </label>
        <input type="submit" value="提交" />
      </form>
    );
  }
}
```

由于在表单元素上设置了 `value` 属性，因此显示的值将始终为 `this.state.value`，这使得 React 的 state 成为唯一数据源。由于 `handlechange` 在每次按键时都会执行并更新 React 的 state，因此显示的值将随着用户输入而更新。

### textarea

在 HTML 中, `<textarea>` 元素通过其子元素定义其文本:

```
<textarea>
  你好， 这是在 text area 里的文本
</textarea>
```

而在 React 中，`<textarea>` 使用 `value` 属性代替。这样，可以使得使用 `<textarea>` 的表单和使用单行 input 的表单非常类似：

```react
class EssayForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {      value: '请撰写一篇关于你喜欢的 DOM 元素的文章.'    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {    this.setState({value: event.target.value});  }
  handleSubmit(event) {
    alert('提交的文章: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          文章:
          <textarea value={this.state.value} onChange={this.handleChange} />        </label>
        <input type="submit" value="提交" />
      </form>
    );
  }
}
```

请注意，`this.state.value` 初始化于构造函数中，因此文本区域默认有初值。

### select 标签 

在 HTML 中，`<select>` 创建下拉列表标签。例如，如下 HTML 创建了水果相关的下拉列表：

```
<select>
  <option value="grapefruit">葡萄柚</option>
  <option value="lime">酸橙</option>
  <option selected value="coconut">椰子</option>
  <option value="mango">芒果</option>
</select>
```

请注意，由于 `selected` 属性的缘故，椰子选项默认被选中。React 并不会使用 `selected` 属性，而是在根 `select` 标签上使用 `value` 属性。这在受控组件中更便捷，因为您只需要在根标签中更新它。例如：

```react
class FlavorForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: 'coconut'};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {    this.setState({value: event.target.value});  }
  handleSubmit(event) {
    alert('你喜欢的风味是: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          选择你喜欢的风味:
          <select value={this.state.value} onChange={this.handleChange}>            <option value="grapefruit">葡萄柚</option>
            <option value="lime">酸橙</option>
            <option value="coconut">椰子</option>
            <option value="mango">芒果</option>
          </select>
        </label>
        <input type="submit" value="提交" />
      </form>
    );
  }
}
```

### 文件 input 标签 

在 HTML 中，`<input type="file">` 允许用户从存储设备中选择一个或多个文件，将其上传到服务器，或通过使用 JavaScript 的 [File API](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications) 进行控制。

```
<input type="file" />
```

因为它的 value 只读，所以它是 React 中的一个**非受控**组件。将与其他非受控组件[在后续文档中](https://zh-hans.reactjs.org/docs/uncontrolled-components.html#the-file-input-tag)一起讨论。

### 处理多个输入 

当需要处理多个 `input` 元素时，我们可以给每个元素添加 `name` 属性，并让处理函数根据 `event.target.name` 的值选择要执行的操作。

例如：

```react
class Reservation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isGoing: true,
      numberOfGuests: 2
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;
    this.setState({
      [name]: value    
    });
  }

  render() {
    return (
      <form>
        <label>
          参与:
          <input
            name="isGoing"            
						type="checkbox"
            checked={this.state.isGoing}
            onChange={this.handleInputChange} />
        </label>
        <br />
        <label>
          来宾人数:
          <input
            name="numberOfGuests"            
            type="number"
            value={this.state.numberOfGuests}
            onChange={this.handleInputChange} />
        </label>
      </form>
    );
  }
}
```

这里使用了 ES6 [计算属性名称](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Object_initializer#Computed_property_names)的语法更新给定输入名称对应的 state 值：

例如：

```react
this.setState({
  [name]: value
});
```

等同 ES5:

```react
var partialState = {};
partialState[name] = value;
this.setState(partialState);
```

另外，由于 `setState()` 自动[将部分 state 合并到当前 state](https://zh-hans.reactjs.org/docs/state-and-lifecycle.html#state-updates-are-merged), 只需调用它更改部分 state 即可。

### 受控输入空值 

在[受控组件](https://zh-hans.reactjs.org/docs/forms.html#controlled-components)上指定 `value` 的 prop 会阻止用户更改输入。如果你指定了 `value`，但输入仍可编辑，则可能是你意外地将 `value` 设置为 `undefined` 或 `null`。

### 受控组件的替代品

有时使用受控组件会很麻烦，因为你需要为数据变化的每种方式都编写事件处理函数，并通过一个 React 组件传递所有的输入  state。

当你将之前的代码库转换为 React 或将 React 应用程序与非 React  库集成时，这可能会令人厌烦。

在这些情况下，你可能希望使用[非受控组件](https://zh-hans.reactjs.org/docs/uncontrolled-components.html), 这是实现输入表单的另一种方式。

## 状态提升

https://juejin.cn/post/6844903743364792334

使用 react 经常会遇到几个组件需要共用状态数据的情况。这种情况下，我们最好将这部分共享的状态提升至他们最近的父组件当中进行管理。

React状态提升主要就是用来处理父组件和子组件的数据传递的；他可以让我们的数据流动的形式是自顶向下单向流动的，所有组件的数据都是来自于他们的父辈组件，也都是由父辈组件来统一存储和修改，再传入子组件当中。

通过父组件提供事件，并绑定在子组件，子组件触发父组件。

1. 在父组件定义数据源与更新事件
2. 通过prop的方式 传递给子组件 数据与事件
3. 子组件调用事件更新数据

你应当依靠[自上而下的数据流](https://zh-hans.reactjs.org/docs/state-and-lifecycle.html#the-data-flows-down)，而不是尝试在不同组件间同步 state。

## 组合 vs 继承

### 包含关系

有些组件无法提前知晓它们子组件的具体内容。我们建议这些组件使用一个特殊的 `children` prop 来将他们的子组件传递到渲染结果中

```react
function FancyBorder(props) {
  return (
    <div className={'FancyBorder FancyBorder-' + props.color}>
      {props.children}    
    </div>
  );
}

function WelcomeDialog() {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">        
        Welcome      
      </h1>      
      <p className="Dialog-message">
        Thank you for visiting our spacecraft!      
      </p>    
    </FancyBorder>
  );
}
```

`<FancyBorder>` JSX 标签中的所有内容都会作为一个 `children` prop 传递给 `FancyBorder` 组件。

少数情况下，你可能需要在一个组件中预留出几个“洞”(slot)。这种情况下，我们可以不使用 `children`，而是自行约定：将所需内容传入 props，并使用相应的 prop。

### 特例

有些时候，我们会把一些组件看作是其他组件的特殊实例，比如 `WelcomeDialog` 可以说是 `Dialog` 的特殊实例。

在 React 中，我们也可以通过组合来实现这一点。“特殊”组件可以通过 props 定制并渲染“一般”组件：

```react
function Dialog(props) {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        {props.title}      </h1>
      <p className="Dialog-message">
        {props.message}      </p>
    </FancyBorder>
  );
}

function WelcomeDialog() {
  return (
    <Dialog      
      title="Welcome"      
      message="Thank you for visiting our spacecraft!" 
      />  );
}
```

组合也同样适用于以 class 形式定义的组件。

## React 哲学

1. 将设计好的 UI 划分为组件层级

   * 向用户展示 JSON 数据模型，如果你的模型设计得恰当，UI（或者说组件结构）便会与数据模型一一对应，这是因为 UI 和数据模型都会倾向于遵守相同的*信息结构*。将 UI 分离为组件，其中每个组件需与数据模型的某部分匹配。

2. 用 React 创建一个静态版本 

   在构建应用的静态版本时，我们需要创建一些会重用其他组件的组件，然后通过 *props* 传入所需的数据。*props* 是父组件向子组件传递数据的方式。即使你已经熟悉了 *state* 的概念，也**完全不应该使用 state** 构建静态版本。state 代表了随时间会产生变化的数据，应当仅在实现交互时使用。所以构建应用的静态版本时，你不会用到它。

   * 你可以自上而下或者自下而上构建应用
     * **自上而下**意味着首先编写层级较高的组件，当你的应用比较简单时，使用自上而下的方式更方便；
     * **自下而上**意味着从最基本的组件开始编写。对于较为大型的项目来说，自下而上地构建，并同时为低层组件编写测试是更加简单的方式。
   * 由于我们构建的是静态版本，所以这些组件目前只需提供 `render()` 方法用于渲染。

3. 确定 UI state 的最小（且完整）表示 

   * 想要使你的 UI 具备交互功能，需要有触发基础数据模型改变的能力。React 通过实现 **state** 来完成这个任务。
   * 为了正确地构建应用，你首先需要找出应用所需的 state 的最小表示，并根据需要计算出其他所有数据。其中的关键正是 [DRY: *Don’t Repeat Yourself*](https://en.wikipedia.org/wiki/Don't_repeat_yourself)。
   * 只保留应用所需的可变 state 的最小集合，其他数据均由它们计算产生。
   * eg:比如，你要编写一个任务清单应用，你只需要保存一个包含所有事项的数组，而无需额外保存一个单独的 state 变量（用于存储任务个数）。当你需要展示任务个数时，只需要利用该数组的 length 属性即可。

   * 通过问自己以下三个问题，你可以逐个检查相应数据是否属于 state：

     1. 该数据是否是由父组件通过 props 传递而来的？如果是，那它应该不是 state。

     2. 该数据是否随时间的推移而保持不变？如果是，那它应该也不是 state。

     3. 你能否根据其他 state 或 props 计算出该数据的值？如果是，那它也不是 state。

4. 确定 state 放置的位置 

   * 我们需要确定哪个组件能够改变这些 state，或者说*拥有*这些 state。
   * React 中的数据流是单向的，并顺着组件层级从上往下传递。
   * 通过以下步骤来判断
     * 找到根据这个 state 进行渲染的所有组件。
     * 找到他们的共同所有者（common owner）组件（在组件层级上高于所有需要该 state 的组件）。
     * 该共同所有者组件或者比它层级更高的组件应该拥有该 state。
     * 如果你找不到一个合适的位置来存放该 state，就可以直接创建一个新的组件来存放该 state，并将这一新组件置于高于共同所有者组件层级的位置。

5. 添加反向数据流 

   * 我们将尝试让数据反向传递：处于较低层级的表单组件更新较高层级中的 state。

##    推荐的工具链

* 如果你是在**学习 React** 或**创建一个新的[单页](https://zh-hans.reactjs.org/docs/glossary.html#single-page-application)应用**，请使用 [Create React App](https://zh-hans.reactjs.org/docs/create-a-new-react-app.html#create-react-app)。

* 如果你是在**用 Node.js 构建服务端渲染的网站**，试试 [Next.js](https://zh-hans.reactjs.org/docs/create-a-new-react-app.html#nextjs)。

* 如果你是在构建**内容主导的静态网站**，试试 [Gatsby](https://zh-hans.reactjs.org/docs/create-a-new-react-app.html#gatsby)。

- **[Neutrino](https://neutrinojs.org/)** 把 [webpack](https://webpack.js.org/) 的强大功能和简单预设结合在一起。并且包括了 [React 应用](https://neutrinojs.org/packages/react/)和 [React 组件](https://neutrinojs.org/packages/react-components/)的预设。
- **[Nx](https://nx.dev/react)** 是针对全栈 monorepo 的开发工具包，其内置了 React，Next.js，[Express](https://expressjs.com/) 等。
- **[Parcel](https://parceljs.org/)** 是一个快速的、零配置的网页应用打包器，并且可以[搭配 React 一起工作](https://parceljs.org/recipes/react/)。
- **[Razzle](https://github.com/jaredpalmer/razzle)** 是一个无需配置的服务端渲染框架，但它提供了比 Next.js 更多的灵活性。

### 从头开始打造工具链 

一组 JavaScript 构建工具链通常由这些组成：

- 一个 **package 管理器**，比如 [Yarn](https://yarnpkg.com/) 或 [npm](https://www.npmjs.com/)。它能让你充分利用庞大的第三方 package 的生态系统，并且轻松地安装或更新它们。
- 一个**打包器**，比如 [webpack](https://webpack.js.org/) 或 [Parcel](https://parceljs.org/)。它能让你编写模块化代码，并将它们组合在一起成为小的 package，以优化加载时间。
- 一个**编译器**，例如 [Babel](https://babeljs.io/)。它能让你编写的新版本 JavaScript 代码，在旧版浏览器中依然能够工作。

