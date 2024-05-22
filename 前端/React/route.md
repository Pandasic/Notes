# React Router

> 参考文档
>
> https://juejin.cn/post/7033313711947251743#heading-8
>
> https://zhuanlan.zhihu.com/p/191419879

## 安装(V6)

```
 npm install react-router-dom@6
```

React Router库包含三个不同的npm包，以下每个包都有不同的用途

- react-router 核心库，用作上面列出的他两个程序包的对等依赖项
- react-router-dom  是React应用中用于路由的软件包
- react-router-native 有用于开发React Native应用的绑定

## 全局路由

全局路由有常用两种路由模式可选：HashRouter 和 BrowserRouter

HashRouter：URL中采用的是hash(#)部分去创建路由，类似www.example.com/#/

BrowserRouter：URL采用真实的URL资源

```jsx
import { BrowserRouter } from 'react-router-dom';

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```

| 组件名      | 作用           | 说明                                                         |
| ----------- | -------------- | ------------------------------------------------------------ |
| `<Routers>` | 一组路由       | 代替原有`<Switch>`，所有子路由都用基础的Router children来表示 |
| `<Router>`  | 基础路由       | Router是可以嵌套的，解决原有V5中严格模式，后面与V5区别会详细介绍 |
| `<Link>`    | 导航组件       | 为了避免刷新网页，在实际页面中跳转使用                       |
| `<Outlet/>` | 自适应渲染组件 | 根据实际路由url自动选择组件                                  |

```jsx
import './App.css';
import { Routes, Route, Link } from "react-router-dom"
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <!-- 路由组, 路由渲染处-->
        <Routes>
          <!-- 路由 与 组件绑定 -->
          <Route path="/" element={<Home />}></Route>
          <Route path="/about" element={<About />}></Route>
        </Routes>
      </header>
    </div>
  );
}

function Home() {
  return <div>
    <main>
      <h2>Welcome to the homepage</h2>
    </main>
    <nav>
      <!-- 页面提阿战使用 -->
      <Link to="/about">about</Link>
    </nav>
  </div>
}
function About() {
  return <div>
    <main>
      <h2>Welcome to the about page</h2>
    </main>
    <nav>
      <ol>
        <Link to="/">home</Link>
        <Link to="/about">about</Link>
      </ol>
    </nav>
  </div>
}
export default App;
```

| hooks名           | 作用                                  | 说明                      |
| ----------------- | ------------------------------------- | ------------------------- |
| `useParams`       | 返回当前参数                          | 根据路径读取参数          |
| `useNavigate`     | 返回当前路由                          | 代替原有V5中的 useHistory |
| `useOutlet`       | 返回根据路由生成的element             |                           |
| `useLocation`     | 返回当前的location 对象               |                           |
| `useRoutes`       | 同Routers组件一样，只不过是在js中使用 |                           |
| `useSearchParams` | 用来匹配URL中?后面的搜索参数          |                           |

## 嵌套路由

一般认为网页的某一部分保持不变，只有网页的子部分发生变化。

从React Router库中挑选了一个名为 `Outlet` 的最佳元素，为特定路由呈现任何匹配的子元素。

嵌套路由是V6版本对之前版本一个较大的升级，采用嵌套路由会智能的识别

```js
function App() {
  return (
    <Routes>
      <Route path="user" element={<Users />}>
        <Route path=":id" element={<UserDetail />} />
        <Route path="create" element={<NewUser />} />
      </Route>
    </Routes>
  );
}
```

当访问 /user/123 的时候，组件树将会变成这样

```js
<App>
    <Users>
        <UserDetail/>
    </Users>
</App>
```

当访问/user/create的时候，组件树将变成这样

```js
<App>
   <Users>
       <NewUser/>
   </Users>
</App>
复制代码
```

如果只是内部组件修改，也可以采用`<Outlet/>`  指定渲染子元素位置来直接实现，如下所示

```js
function App() {
  return (
    <Routes>
      <Route path="user" element={<Users />}>
        <Route path=":id" element={<UserDetail />} />
        <Route path="create" element={<NewUser />} />
      </Route>
    </Routes>
  );
}
function Users() {
  return (
    <div>
      <h1>Users</h1>
      <Outlet/>
    </div>
  );
}
```

## index 路由

index属性解决当嵌套路由有多个子路由但本身无法确认默认渲染哪个子路由的时候，可以增加index属性来指定默认路由

```jsx
function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<About />} />
        <Route path="user" element={<User />} />
        <Route path="about" element={<About />} />
      </Route>
    </Routes>
  );
```

这样当访问/的时候`<Outlet/>`会默认渲染About组件

## 路由通配符

支持

```js
/groups
/groups/admin
/users/:id
/users/:id/messages
/files/*
/files/:id/*
```

不支持

```bash
/users/:id?
/tweets/:id(\d+)
/files/*/cat.jpg
/files-*
```

关于NotFound类路由，可以用`*`来代替

```js
function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="dashboard" element={<Dashboard />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}
```

## 参数获取

假设现有App路由

```js
function App() {
 return (
   <Routes>
     <Route path="user" element={<Users />}>
       <Route path=":id" element={<UserDetail />} />
       <Route path="create" element={<NewUser />} />
     </Route>
   </Routes>
 );
}
复制代码
```

那么在UserDetail内部需要用useParams来获取对应的参数

```js
import { useParams } from "react-router-dom";

export default function UserDetail() {
  let params = useParams();
  return <h2>User: {params.id}</h2>;
}
复制代码
```

useSearchParams相对复杂，他返回的是一个当前值和set方法

```
let [searchParams, setSearchParams] = useSearchParams();
```

使用时可以用`searchParams.get("id")`来获取参数，同时页面内也可以setSearchParams({"id":2})

## 导航

useNavigate是替代原有V5中的useHistory的新hooks，其用法和useHistory类似，整体使用起来更轻量

他的声明方式如下：

```ts
declare function useNavigate(): NavigateFunction;

interface NavigateFunction {
  (
    to: To,
    options?: { replace?: boolean; state?: State }
  ): void;
  (delta: number): void;
}
```
```js
  //js写法
  let navigate = useNavigate();
  function handleClick() {
    navigate("/home");
  }
  //组件写法
  function App() {
     return <Navigate to="/home" replace state={state} />;
  }
  //替代原有的go goBack和goForward
 <button onClick={() => navigate(-2)}>
    Go 2 pages back
  </button>
  <button onClick={() => navigate(-1)}>Go back</button>
  <button onClick={() => navigate(1)}>
    Go forward
  </button>
  <button onClick={() => navigate(2)}>
    Go 2 pages forward
  </button>
```

