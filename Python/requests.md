# request

## 简介

**Python实现的简单易⽤的HTTP库**

基于 python + urllib， 采用Apache2 Licensed 的 HTTP库。

## 安装

```
pip install requests
```

## 使用

### 使用基本函数 发送请求

```python
import requests
requests.get(url)
requests.post(url)
requests.put(url)
requests.delete(url)
requests.head(url)
requests.options(url)
```

### get

* 普通使用

```
response = requests.get('http://httpbin.org/get')
```

* 带参数的GET

```
response = requests.get("http://httpbin.org/get?name=germey&age=22")
```

使用param 参数

```
data = {
 'name': 'germey',
 'age': 22
}
response = requests.get("http://httpbin.org/get", params=data)
```

* 二进制

```
response.context
```

* headers 

```python
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("发现 - 知乎", headers=headers)                                        print(response.text)}
```

### post

```python
import requests
 
data = {'name': 'germey', 'age': '22'}
response = requests.post("http://httpbin.org/post", data=data)
print(response.text)
```

### response

```
import requests
 
response = requests.get('url')
# 状态码
print(type(response.status_code), response.status_code)
# 响应头
print(type(response.headers), response.headers)
# cookie
print(type(response.cookies), response.cookies)
# 响应
print(type(response.url), response.url)
print(type(response.history), response.history)
return：
```

