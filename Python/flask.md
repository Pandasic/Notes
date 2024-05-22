# Flask

> 参考教程：https://www.w3cschool.cn/flask/flask_environment.html
>
> 文档：https://dormousehole.readthedocs.io/en/latest/

## 虚拟环境 virtualenv

安装

```
sudo pip install virtualenv
```

创建

```
mkdir aim_dir
cd aim_dir
virtualenv venv
```

激活

```
venv/bin/activate
```

## hello world

### 安装

```
pip install Flask
```

### hello world

```python
# main.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
```

* 必须导入 Flask,  Flask类的一个对象是我们的**WSGI**应用程序。

* Flask构造函数使用**当前模块（__name __）**的名称作为参数。

* **route()**函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。

  * ```python
    app.route(rule, options)
    ```

    *  **rule** 参数表示与该函数的URL绑定。        
    *  **options** 是要转发给基础Rule对象的参数列表。

* **run()**方法在本地开发服务器上运行应用程序。

  * ```
    app.run(host, port, debug, options)
    ```

  * host: 要监听的主机名。  默认为127.0.0.1（localhost）。

    * 设置为“0.0.0.0”以使服务器在外部可用     

  * port : 默认为5000

  * debug ：是否提供调试信息

  * options： 要转发到底层的Werkzeug服务器。 

### 运行

```
python main.py
```

## 路由

Flask中的**route()**装饰器用于将URL绑定到函数  

```python
@app.route('/hello')
def hello_world():
   return 'hello world'                                               
```

如果用户访问 **http://localhost:5000/hello** (默认)

hello_world()函数的输出将在浏览器中呈现

也可以由后续函数绑定

```python
app.add_url_rule('/', 'hello', hello_world)
```

### 动态url

参考 https://blog.csdn.net/CoderPai/article/details/80520955

通过向规则参数添加变量部分，可以动态构建URL。

此变量部分标记为**<variable-name>** 它作为关键字参数传递给与规则相关联的函数。

```python
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
```

此时 url中的name 将会 作为参数传递给函数

变量标记除了默认的字符串还支持转换规则

| eg             | 说明                     |
| -------------- | ------------------------ |
| \<int:postID>  | 整数                     |
| \<float:revNo> | float 浮点               |
| \<path:path>   | 接受用作目录分隔符的斜杠 |

Flask的URL规则基于**Werkzeug**的路由模块。这确保形成的URL是唯一的，

eg：

```
#一个规范的URL。因此，使用 /python 或 /python/返回相同的输出
@app.route('/python/') 

# /flask 可以访问 /flask/ 产生“404 Not Found”
@app.route('/flask')
```

### URL构建

`url_for` 函数接受 **函数的名称** 作为第一个参数，以及一个或多个关键字参数，每个参数对应于URL的变量部分。

```
url_for('hello_guest', guest = name)

@app.route('/success/<guest>')
```

## HTTP 方法

| 序号   | 方法与描述                                                   |
| ------ | ------------------------------------------------------------ |
| GET    | 以未加密的形式将数据发送到服务器。最常见的方法。             |
| HEAD   |  和GET方法相同，但没有响应体。 |
| POST   | 用于将HTML表单数据发送到服务器。POST方法接收的数据不由服务器缓存。 |
| PUT    | 用上传的内容替换目标资源的所有当前表示。 |
| DELETE |删除由URL给出的目标资源的所有当前表示。 |

默认情况下，Flask路由响应**GET**请求。但是，可以通过为**route()**装饰器提供方法参数来更改此首选项。

```
@app.route('/login',methods = ['POST', 'GET'])
```

## 模板

### 简介

- 模板其实是一个包含响应文本的文件,其中用占位符(变量)表示动态部分,告诉模板引擎其具体的值需要从使用的数据中获取
- 使用真实值替换变量,再返回最终得到的字符串,这个过程称为`渲染`
- Flask 是使用 Jinja2 这个模板引擎来渲染模板

### 优势

- 视图函数只负责业务逻辑和数据处理(业务逻辑方面)
- 而模板则取到视图函数的数据结果进行展示(视图展示方面)
- 代码结构清晰,耦合度低

### 模板变量

在项目下创建 templates 文件夹，用于存放所有模板文件。

在模板中使用 `{{ var_name }}` 进行模板变量声明

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
  我的模板html内容
  <br />{{ my_str }}
  <br />{{ my_int }}
  <br />{{ my_array }}
  <br />{{ my_dict }}
</body>
</html>
```

### 流程控制

使用 `{% cond %}`流程控制

#### if

```
{% if messages %}
		func/codes/texts
{% endif %}
```

#### for

```
{% for message in messages %}
    func/codes/texts
{% endfor %}
```

#### with

```
{% with var = resources %}
   use_resourcess
{% endwith %}
```

### 渲染

```python
render_template(render_name， render_var = real_val,...)

    # 参数1: 模板名称  参数n: 传到模板里的数据
  return render_template('hello.html',my_int=my_int, my_str=my_str)
```

## 静态文件

开发过程中，您的包或模块旁边的*static*文件夹中提供，它将在应用程序的**/static**中提供

```html
<!-index.html-->
<html>

   <head>
      <script type = "text/javascript" 
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>
```

```js
// hello.js
function sayHello() {
   alert("Hello World")
}
```

## 表单处理

通过 `request`来接受请求

```
from flask import request
```

### request 对象

request对象的重要属性如下所列： 

- form  - 它是一个字典对象，包含表单参数及其值的键和值对。
- args   - 解析查询字符串的内容，它是问号（？）之后的URL的一部分。
- cookies  - 保存Cookie名称和值的字典对象。
- files  - 与上传文件有关的数据。
- method  - 当前请求方法。

```
wd = request.args.get('wd')
```

## Cookies

* 设置cookie：

 设置cookie,默认有效期是临时cookie,浏览器关闭就失效

 可以通过 max_age 设置有效期， 单位是秒

```
 resp = make_response("success")   # 设置响应体
 resp.set_cookie("key", "val", max_age=3600)
```

* 获取cookie

  获取cookie，通过request.cookies的方式， 返回的是一个字典，可以获取字典里的相应的值

```
cookie_1 = request.cookies.get("key")
```

* 删除cookie

> 这里的删除只是让cookie过期，并不是直接删除cookie

删除cookie，通过delete_cookie()的方式， 里面是cookie的名字

```
resp = make_response("del success")  # 设置响应体
resp.delete_cookie("key")
```

## 会话 Session

**Session（会话）**数据存储在服务器上。

会话是客户端登录到服务器并注销服务器的时间间隔。

需要在该会话中保存的数据会存储在服务器上的临时目录中。

为每个客户端的会话分配**会话ID**。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。对于此加密，Flask应用程序需要一个定义的**SECRET_KEY**。

```python
app.secret_key = 'SECRET_KEY'
```

session对象也是一个字典对象，包含会话变量和关联值的键值对。

例如，要设置一个**'username'**会话变量，请使用以下语句：

```
session['key'] = 'val'
```

要释放会话变量，请使用**pop()**方法。

```
session.pop('key', val)
```

## 重定向

Flask类有一个**redirect()**函数。调用时，它返回一个响应对象，并将用户重定向到具有指定状态代码的另一个目标位置。

 **redirect()**函数的原型如下： 

```
flask.redirect(location, statuscode, response)
```

-  **location**参数是应该重定向响应的URL。
-  **statuscode**发送到浏览器标头，默认为302。
-  **response**参数用于实例化响应。

## 错误码

```
flask.abort(code)
```

-  **400**   - 用于错误请求
-  **401**   - 用于未身份验证的
-  **403**   -  Forbidden
-  **404**   - 未找到
-  **406**   - 表示不接受
-  **415**   - 用于不支持的媒体类型
-  **429**   - 请求过多

## 消息闪现

非常简单的方法来使用闪现系统向用户反馈信息

闪现系统使得在一个请求结束的时候记录一个信息，`然后在且仅仅在下一个请求中访问这个数据`

flask闪现是基于`flask`内置的`session`的，利用浏览器的`session`缓存闪现信息。所以必须设置`secret_key`

### 使用

 **flash()** 方法。它将消息传递给下一个请求，该请求通常是一个模板。

```
flash(message, category)
```

-  **message** 参数是要闪现的实际消息。
-  **category** 参数是可选的。它可以是“error”，“info”或“warning”

获取闪现消息**get_flashed_messages()**。

```
get_flashed_messages(with_categories, category_filter)
```

两个参数都是可选的。如果接收到的消息具有类别，则第一个参数是元组。第二个参数仅用于显示特定消息。

## 上传

它需要一个 HTML 表单，其 `enctype` 属性设置为“`multipart/form-data”`，将文件发布到 URL。

```html
<form action="http://localhost:5000/uploader" method="POST" enctype="multipart/form-data">
	<input type="file" name="file"/>
	<input type="submit" value="提交" />
</form>
```

URL 处理程序从 `request.files[]` 对象中提取文件，并将其保存到所需的位置。

每个上传的文件首先会保存在服务器上的临时位置，然后将其实际保存到它的最终位置。

目标文件的名称可以是硬编码的，也可以从 `request.files[file] `对象的` filename `属性中获取。

建议使用 `secure_filename()` 函数获取它的安全版本。

 Flask 对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小。

* app.config['UPLOAD_FOLDER']  定义上传文件夹的路径 
* app.config['MAX_CONTENT_LENGTH']   指定要上传的文件的最大大小（以字节为单位）

```python
@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')
```

> 注意：app.config['UPLOAD_FOLDER'] = 'upload/'

## 扩展

Flask扩展是一个Python模块，它向Flask应用程序添加了特定类型的支持。

Flask Extension Registry（Flask扩展注册表）是一个可用的扩展目录。

> Flask 的扩展通常命名为 Flask-Foo ”或者“ Foo-Flask

eg:

- Flask-SQLalchemy：操作数据库；
- Flask-script：插入脚本；
- Flask-migrate：管理迁移数据库；
- Flask-Session：Session存储方式指定；
- Flask-WTF：表单；
- Flask-Mail：邮件；
- Flask-Bable：提供国际化和本地化支持，翻译；
- Flask-Login：认证用户状态；
- Flask-OpenID：认证；
- Flask-RESTful：开发REST API的工具；
- Flask-Bootstrap：集成前端Twitter Bootstrap框架；
- Flask-Moment：本地化日期和时间；
- Flask-Admin：简单而可扩展的管理接口的框架

### 使用扩展

 app.config 获取其自身的配置并在初始化时传递给 应用实例

```python
from flask_foo import Foo

foo = Foo()
app = Flask(__name__)
app.config.update(
    FOO_BAR='baz',
    FOO_SPAM='eggs',
)
foo.init_app(app)
```

## 邮件

### 安装

Flask-Mail扩展

```
pip install Flask-Mail
```

### 配置

| 序号 | 参数与描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | **MAIL_SERVER** 电子邮件服务器的名称/IP地址                  |
| 2    | **MAIL_PORT** 使用的服务器的端口号                           |
| 3    | **MAIL_USE_TLS** 启用/禁用传输安全层加密                     |
| 4    | **MAIL_USE_SSL** 启用/禁用安全套接字层加密                   |
| 5    | **MAIL_DEBUG** 调试支持。默认值是Flask应用程序的调试状态     |
| 6    | **MAIL_USERNAME** 发件人的用户名                             |
| 7    | **MAIL_PASSWORD** 发件人的密码                               |
| 8    | **MAIL_DEFAULT_SENDER** 设置默认发件人                       |
| 9    | **MAIL_MAX_EMAILS** 设置要发送的最大邮件数                   |
| 10   | **MAIL_SUPPRESS_SEND** 如果app.testing设置为true，则发送被抑制 |
| 11   | **MAIL_ASCII_ATTACHMENTS** 如果设置为true，则附加的文件名将转换为ASCII |

### Mail类

它管理电子邮件消息传递需求。类构造函数采用以下形式： 

```
flask-mail.Mail(app = None)
```

构造函数将Flask应用程序对象作为参数。

#### Mail类的方法

| 序号 | 方法与描述                        |
| ---- | --------------------------------- |
| 1    | **send()**发送Message类对象的内容 |
| 2    | **connect()**打开与邮件主机的连接 |
| 3    | **send_message()**发送消息对象    |

#### Message类

它封装了一封电子邮件。Message类构造函数有几个参数: 

```
flask-mail.Message(subject, recipients, body, html, sender, cc, bcc, 
   reply-to, date, charset, extra_headers, mail_options, rcpt_options)
```

#### Message类方法

 **attach()**  - 为邮件添加附件。此方法采用以下参数：

-  **filename**   - 要附加的文件的名称
-  **content_type**   -  MIME类型的文件
-  **data**   - 原始文件数据
- **处置**  - 内容处置（如果有的话）。

 **add_recipient()**  - 向邮件添加另一个收件人

### 实例

在下面的示例中，Google gmail服务的SMTP服务器用作Flask-Mail配置的MAIL_SERVER。

1. 在代码中从flask-mail模块导入Mail和Message类。

```
from flask_mail import Mail, Message
```

2. 然后按照以下设置配置Flask-Mail。

```
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
```

3.  创建Mail类的实例。

```
mail = Mail(app)
```

4. 在由URL规则**（‘/’）**映射的Python函数中设置Message对象。

```
@app.route("/")
def index():
   msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"
```

5. 整个代码如下。

在Python Shell中运行以下脚本并访问**http://localhost:5000/。**

```
from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
```



## WTF

**WTForms**的作用，一个灵活的表单，渲染和验证库。

Flask-WTF扩展为这个**WTForms**库提供了一个简单的接口

>  原生表单缺点
>
> 用户输入的数据以Http请求消息的形式通过GET或POST方法提交给服务器端脚本。
> 
> * 服务器端脚本必须从http请求数据重新创建表单元素。因此，实际上，表单元素必须定义两次 - 一次在HTML中，另一次在服务器端脚本中。        
>
> * 使用HTML表单的另一个缺点是很难（如果不是不可能的话）动态呈现表单元素。HTML本身无法验证用户的输入。        

**Flask-WTF**，我们可以在Python脚本中定义表单字段，并使用HTML模板进行渲染。还可以将验证应用于**WTF**字段。

### 安装

```
pip install flask-WTF
```

### 使用

已安装的软件包包含一个**Form**类，该类必须用作用户定义表单的父级。

 **WTforms**包中包含各种表单字段的定义。下面列出了一些**标准表单字段**。

| 序号 | 标准表单字段与描述 |                                            |
| ---- | ------------------ | ------------------------------------------ |
| 1    | **TextField**      | 表示\<input type ='text'> HTML表单元素      |
| 2    | **BooleanField**   | 表示\<input type ='checkbox'> HTML表单元素  |
| 3    | **DecimalField**   | 用于显示带小数的数字的文本字段             |
| 4    | **IntegerField**   | 用于显示整数的文本字段                     |
| 5    | **RadioField**     | 表示\<input type = 'radio'> HTML表单元素    |
| 6    | **SelectField**    | 表示选择表单元素                           |
| 7    | **TextAreaField**  | 表示\<textarea> HTML表单元素                |
| 8    | **PasswordField**  | 表示\<input type = 'password'> HTML表单元素 |
| 9    | **SubmitField**    | 表示\<input type = 'submit'>表单元素     ?  |

eg:

例如，包含文本字段的表单可以设计如下： 

```
from flask_wtf import Form
from wtforms import TextField

class ContactForm(Form):
   name = TextField("Name Of Student")
```

除了**'name'**字段，还会自动创建CSRF令牌的隐藏字段。这是为了防止**Cross Site Request Forgery（\**跨站请求伪造\**）**攻击。

渲染时，**这将导致等效的HTML脚本**，如下所示：

```
<input id = "csrf_token" name = "csrf_token" type = "hidden" />
<label for = "name">Name Of Student</label><br>
<input id = "name" name = "name" type = "text" value = "" />
```

在Flask应用程序中使用用户定义的表单类，并使用模板呈现表单。

```
from flask import Flask, render_template
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)
```

WTForms包也包含验证器类。它对表单字段应用验证很有用。以下列表显示了常用的验证器。

| 序号 | 验证器类与描述                                               |
| ---- | ------------------------------------------------------------ |
| 1    | **DataRequired**                                 检查输入字段是否为空 |
| 2    | **Email                     **                                                                        检查字段中的文本是否遵循电子邮件ID约定 |
| 3    | **IPAddress**                                                     在输入字段中验证IP地址 |
| 4    | **Length**                                                     验证输入字段中的字符串的长度是否在给定范围内 |
| 5    | **NumberRange**                                 验证给定范围内输入字段中的数字 |
| 6    | **URL**                                验证在输入字段中输入的URL |

现在，我们将对联系表单中的**name**字段应用**'DataRequired'**验证规则。

```
name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
```

如果验证失败，表单对象的**validate()**函数将验证表单数据并抛出验证错误。**Error**消息将发送到模板。在HTML模板中，动态呈现error消息。

```
{% for message in form.name.errors %}
   {{ message }}
{% endfor %}
```

以下示例演示了上面给出的概念。**Contact表单**的设计如下**（forms.py）**。

```
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,
   SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter 
      your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C&plus;&plus;'), 
      ('py', 'Python')])
   submit = SubmitField("Send")
```

验证器应用于**Name**和**Email**字段。

### 请求前后处理

通过使用特殊的 g 对象可以使用 before_request() 和 teardown_request() 在请求开始前打开数据库连接，在请求结束后关闭连接。

```python
import sqlite3
from flask import g

DATABASE = '/path/to/database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
```

> 销毁函数是一定会被执行的。即使请求前处理器执行失败或根本没有执行， 销毁函数也会被执行。因此，我们必须保证在关闭数据库连接之前数据库连接是存在 的。

## Flask+SQLAlchemy

**SQLAlchemy** ，Python工具包是一个强大的**OR Mapper**，它为应用程序开发人员提供了SQL的全部功能和灵活性。

Flask-SQLAlchemy是Flask扩展，它将对SQLAlchemy的支持添加到Flask应用程序中。

**什么是ORM（Object Relation Mapping，对象关系映射）？**

大多数编程语言平台是面向对象的。另一方面，RDBMS服务器中的数据存储为表。

对象关系映射是将对象参数映射到底层RDBMS表结构的技术。

ORM API提供了执行CRUD操作的方法，而不必编写原始SQL语句。

### 安装

```
pip install flask-sqlalchemy
```

### 使用

```python
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class Students(db.Model):
  MODLUE DEFINE
  def __init__(self,...):
    ...

def deal_request_func():
  ....
```

## Sijax

**Sijax**代表**'Simple Ajax'**，它是一个**Python/jQuery**库，旨在帮助您轻松地将**Ajax**引入到您的应用程序。它使用**jQuery.ajax**来发出AJAX请求。

> [AJAX](https://www.liaoxuefeng.com/wiki/1022910821149312/1023022332902400)（Asynchronous JavaScript and XML）是JavaScript执行异步网络请求 在现代浏览器上写AJAX主要依靠`XMLHttpRequest`对象：

### 安装

Flask-Sijax的安装很简单。

```
pip install flask-sijax
```

### 组态

-  **SIJAX_STATIC_PATH**   - 要被镜像的Sijax javascript文件的静态路径。默认位置是**static/js/sijax**。在此文件夹中，保留**sijax.js**和**json2.js**文件。
-  **SIJAX_JSON_URI**   - 从中加载json2.js静态文件的URI

### 使用

**View**函数能够处理**Sijax**请求，请使用**@app.route（'/url'，methods = [\'GET\'** ，**\'POST\']）**或使用**@flask_sijax.route**辅助装饰器

```
@flask_sijax.route(app, '/hello')
```

每个Sijax处理函数（像这样）都会自动接收至少一个参数，就像Python将'self'传递给对象方法一样。**'obj_response'**参数是函数回复浏览器的方式。

```
def say_hi(obj_response):
   obj_response.alert('Hi there!')
```

当检测到Ajax请求时，Sijax会像这样处理它：

```
g.sijax.register_callback('say_hi', say_hi)
   return g.sijax.process_request()
```

## 部署

如果禁用了**debug**，则可以通过将主机名设置为**'0.0.0.0'**，使本地计算机上的开发服务器可供网络上的用户使用。

```
app.run(host = ’0.0.0.0’)
```

因此，您的操作系统将侦听所有公共IP。

小型应用程序，您可以考虑在以下任何托管平台上部署它，所有这些平台都为小型应用程序提供免费计划。

- Heroku
- dotcloud
- webfaction

### mod_wsgi

**mod_wsgi**是一个Apache模块，它提供了一个WSGI兼容接口，用于在Apache服务器上托管基于Python的Web应用程序

#### 安装mod_wsgi

要直接从PyPi安装官方发行版，你可以运行： 

```
pip install mod_wsgi
```

验证

```
mod_wsgi-express start-server
```

这将在端口8000上启动Apache/mod_wsgi

您可以通过将浏览器指向以下内容来验证安装是否有效： 

```
http://localhost:8000/
```

#### 创建.wsgi文件

应该有一个**yourapplication.wsgi**文件。此文件包含代码**mod_wsgi**，该代码在启动时执行以获取应用程序对象。

对于大多数应用程序，以下文件应该足够了： 

```
from yourapplication import app as application
```

确保**yourapplication**和所有正在使用的库都在python加载路径上。

#### 配置Apache

您需要告诉**mod_wsgi，**您的应用程序的位置：

```
<VirtualHost *>
   ServerName example.com
   WSGIScriptAlias / C:\yourdir\yourapp.wsgi
   
   <Directory C:\yourdir>
      Order deny,allow
      Allow from all
   </Directory>
   
</VirtualHost>
```

#### 静态文件处理

1. **准备静态资源**        
   python        
   在项目根目录下（blog）创建static目录        
   将图片拷贝到static下
2. **配置nginx转发**    

```
# 添加一个location
location /static{
  # root html/blog;
  # 或
  alias html/blog/static;  # 两种方式都可以
}
```

### FastCGI

FastCGI是在nginx，lighttpd和Cherokee等web服务器上的Flask应用程序的另一个部署选项。

https://www.w3cschool.cn/flask/flask_fastcgi.html

## 即插视图 

> 需要梳理

灵感来自 Django 的基于类而不是函数的通用视图。 其主要目的是让你可以对已实现的部分进行替换，并且这个方式可以定制即插视图。

### 基本原则

继承flask.views.View, 并且实现 dispatch_request(). 然后我们需要用类方法 as_view() 把这个类转换到一个实际的视图函数。 字符串是视图之后的最终名称

```python
from flask.views import View

class ShowUsers(View):

    def dispatch_request(self):
        users = User.query.all()
        return render_template('users.html', objects=users)

app.add_url_rule('/users/', ShowUsers.as_view('show_users'))
```

它工作的方式是，无论何时请 求被调度，会创建这个类的一个新实例，并且 dispatch_request() 方法会以 URL 规则为参数调用。 这个类本身会用传递到 as_view() 函数的参数来实例化 构造。

```
class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name)
```

然后你可以这样注册它:: And then you can register it like this:

```
app.add_url_rule('/about', view_func=RenderTemplateView.as_view(
    'about_page', template_name='about.html'))
```

### http 方法

```python
class MyView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            ...
        ...

app.add_url_rule('/myview', view_func=MyView.as_view('myview'))
```

对 RESTful API 非常有用。你可以通过 `flask.views.MethodView` 容易地实现。每个 HTTP 方法映射到同名函

```python
from flask.views import MethodView

class UserAPI(MethodView):

    def get(self):
        users = User.query.all()
        ...

    def post(self):
        user = User.from_form_data(request.form)
        ...

app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))

# 显式地 指出 HTTP 方法
user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<int:user_id>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])
```

### 装饰视图

装饰视图类并没有多大意义。 相反的，你可以手动装饰 `as_view()` 的返回值:

```python
def user_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator

view = user_required(UserAPI.as_view('users'))
app.add_url_rule('/users/', view_func=view)
```

从 Flask 0.8 开始，你也有一种在类声明中设定一个装饰器列表的方法:

```
class UserAPI(MethodView):
    decorators = [user_required]
```

因为从调用者的视角来看 self 是不明确的，所以你不能在单独的视图方法上使用 常规的视图装饰器，请记住这些。

## 请求上下文

### 上下文作用域

比如说你有一个应用函数返回用户应该跳转到的 URL 。想象它总是会跳转到 URL 的 `next` 参数，或 HTTP referrer ，或索引页:

我们当前并没有可以访问的请求。所以我们需要制造一个 请求并且绑定到当前的上下文。 `test_request_context` 方 法为我们创建一个 `RequestContext`:

可以通过两种方式利用这个上下文：使用 with 声明或是调用 `push()` 和 `pop()` 方法:

```
ctx.push()
```

从这点开始，你可以使用请求对象:

```
>>> redirect_url()
u'http://example.com/'
```

直到你调用 pop:

```
>>> ctx.pop()
```

因为请求上下文在内部作为一个栈来维护，所以你可以多次压栈出栈。这在实现 内部重定向之类的东西时很方便。



## 应用上下文

应用上下文存在的主要原因是，在过去，请求上下文被附加了一堆函数，但是又没 有什么好的解决方案。

因为 Flask 设计的支柱之一是你可以在一个 Python 进程中 拥有多个应用。

那么代码如何找到“正确的”应用？

在过去，我们推荐显式地到处传递应用，但是这 会让我们在使用不是以这种理念设计的库时遇到问题。

解决上述问题的常用方法是使用后面将会提到的 `current_app` 代 理对象，它被绑定到当前请求的应用的引用。

既然无论如何在没有请求时创建一个 这样的请求上下文是一个没有必要的昂贵操作，应用上下文就被引入了。

### 创建

* 第一种是隐式的：无论何时当一个请求上下文被压栈时， 如果有必要的话一个应用上下文会被一起创建。

​		由于这个原因，你可以忽略应用 上下文的存在，除非你需要它。

* 第二种是显式地调用 `app_context()` 方法:

```
from flask import Flask, current_app

app = Flask(__name__)
with app.app_context():
    # within this block, current_app points to app.
    print current_app.name
```

在配置了 `SERVER_NAME` 时，应用上下文也被用于 `url_for()` 函 数。这允许你在没有请求时生成 URL 。

## 回调和错误

1. 在每个请求之前，执行 `before_request()` 上绑定的函数。 如果这些函数中的某个返回了一个响应，其它的函数将不再被调用。任何情况 下，无论如何这个返回值都会替换视图的返回值。
2. 如果 `before_request()` 上绑定的函数没有返回一个响应， 常规的请求处理将会生效，匹配的视图函数有机会返回一个响应。
3. 视图的返回值之后会被转换成一个实际的响应对象，并交给 `after_request()` 上绑定的函数适当地替换或修改它。
4. 在请求的最后，会执行 `teardown_request()` 上绑定的函 数。这总会发生，即使在一个未处理的异常抛出后或是没有请求前处理器执行过 （例如在测试环境中你有时会想不执行请求前回调）。

### 销毁回调

销毁回调是是特殊的回调，因为它们在不同的点上执行。严格地说，它们不依赖实际 的请求处理，因为它们限定在 `RequestContext` 对象的生命周期。 当请求上下文出栈时， `teardown_request()` 上绑定的函数会 被调用。

### 留意代理

Flask 中提供的一些对象是其它对象的代理。背后的原因是，这些代理在线程间共享， 并且它们在必要的情景中被调度到限定在一个线程中的实际的对象。

大多数时间你不需要关心它，但是在一些例外情况中，知道一个对象实际上是代理是 有益的:

- 代理对象不会伪造它们继承的类型，所以如果你想运行真正的实例检查，你需要 在被代理的实例上这么做（见下面的 _get_current_object ）。
- 如果对象引用是重要的（例如发送 信号 ）

如果你需要访问潜在的被代理的对象，你可以使用 `_get_current_object()` 方法:

```
app = current_app._get_current_object()
my_signal.send(app)
```

## 蓝图

Flask 用 *蓝图（blueprints）* 的概念来在一个应用中或跨应用制作应用组件和支 持通用的模式。

- 把一个应用分解为一个蓝图的集合。这对大型应用是理想的。一个项目可以实例化 一个应用对象，初始化几个扩展，并注册一集合的蓝图。
- 以 URL 前缀和/或子域名，在应用上注册一个蓝图。 URL 前缀/子域名中的参数即 成为这个蓝图下的所有视图函数的共同的视图参数（默认情况下）。
- 在一个应用中用不同的 URL 规则多次注册一个蓝图。
- 通过蓝图提供模板过滤器、静态文件、模板和其它功能。一个蓝图不一定要实现应 用或者视图函数。
- 初始化一个 Flask 扩展时，在这些情况中注册一个蓝图。



这看起来像是一个非常基本的蓝图。在这个案例中，我们想要实现一个简单渲染静态 模板的蓝图:

```
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
```

 `@simple_page.route` 装饰器绑定函数时，在蓝图之后被注册时它 会记录把 show 函数注册到应用上的意图

此外，它会给函数的端点加上 由 `Blueprint` 的构造函数中给出的蓝图的名称作为前缀（在此例 中是 `simple_page` ）。

### 注册蓝图

```
app.register_blueprint(simple_page)
```

### 静态文件

一个蓝图可以通过 static_folder 关键字参数提供一个指向文件系统上文件夹的路 径，来暴露一个带有静态文件的文件夹。这可以是一个绝对路径，也可以是相对于蓝图 文件夹的路径:

```
admin = Blueprint('admin', __name__, static_folder='static')
```

默认情况下，路径最右边的部分就是它在 web 上所暴露的地址。因为这里这个文件夹 叫做 `static` ，它会在 蓝图 + `/static`。也就是说，蓝图为 `/admin` 把静态文件夹注册到 `/admin/static` 。



，蓝图被设想为包含在一个文件夹中。当多个蓝图源于同一个文件 夹时，可以不必考虑上述情况，但也这通常不是推荐的做法。

这个文件夹会从 `Blueprint` 的第二个参数中推断出来，通常是 __name__ 。  这个参数决定对应蓝图的是哪个逻辑的 Python 模块或包。如果它指向一个存在的 Python  包，这个包（通常是文件系统中的文件夹）就是资源文件夹。如果是一个模块， 模块所在的包就是资源文件夹。你可以访问 `Blueprint.root_path` 属性来查看 资源文件夹是什么:

当你想要从一个页面链接到另一个页面，你可以像通常一个样使用 `url_for()` 函数，只是你要在 URL 的末端加上蓝图的名称和一个点（ `.` ）作为前缀:

```
url_for('admin.index')
```

此外，如果你在一个蓝图的视图函数或是模板中想要从链接到同一蓝图下另一个端点， 你可以通过对端点只加上一个点作为前缀来使用相对的重定向:

```
url_for('.index')
```

这个案例中，它实际上链接到 `admin.index` ，假如请求被分派到任何其它的 admin 蓝图端点。

## 代码模式

https://www.w3cschool.cn/flask/flask-egtb3hgw.html

## 解决跨源调用问题

https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS

首先安装flask_cors 包

```
pip install pip install 
```

之后引用

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

