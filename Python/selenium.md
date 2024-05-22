# Selenium 网页自动化测试框架

> 中文文档： https://python-selenium-zh.readthedocs.io/zh_CN/latest/1.%E5%AE%89%E8%A3%85/

## 环境

### 安装

```
pip install selenium
```

### web driver

安装三大浏览器驱动driver

1. chromedriver 下载地址：https://code.google.com/p/chromedriver/downloads/list
   
2. Firefox的驱动geckodriver 下载地址：https://github.com/mozilla/geckodriver/releases/
   
3. IE的驱动IEdriver 下载地址：http://www.nuget.org/packages/Selenium.WebDriver.IEDriver/

## 导航

使用 `get` 函数 获取对应的链接

```python
driver.get(url)
```

WebDriver会等待页面完全加载完(就是`onload`函数被触发了),才把程序的控制权交给你的测试或者脚本。

> 是如果你的页面用了太多的AJAX，那么这个机制就没什么卵用了，因为它不知道页面到底是什么时候加载完。

如果你需要确定页面完全加载完了，你可以使用`waits`

## 定位

你可以用下列任意方法找到它：

```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```

你也可以通过文本信息来找到一个链接，但是要注意，文本必须要完全匹配。 

在使用`XPATH`的时候也要注意，如果有多个元素匹配，只会返回第一个。

如果匹配不到任何元素，会抛出一个`NoSuchElementException`异常。

## 输入

获取到一个元素之后，输入一些文本到一个文本区域

```
element.send_keys("some text")
```

你可以使用`Keys`类来模拟输入方向键:

```
element.send_keys(" and some", Keys.ARROW_DOWN)
```

我们可以使用`clear`方法来很方便的清除文本框或者文本域的内容:

```
element.clear()
```

## 执行js

```javascript
js="js_codes"
dr.execute_script(js)
```
