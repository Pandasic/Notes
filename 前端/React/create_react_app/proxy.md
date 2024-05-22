> 参考来源：[React 使用 Proxy 代理（create-react-app）](https://cloud.tencent.com/developer/article/1664425#:~:text=%E5%9C%A8create-react-app%20%E4%B8%AD%E9%85%8D%E7%BD%AEproxy%E4%BB%A3%E7%90%86%20proxy%EF%BC%8C%E9%BB%98%E8%AE%A4%E4%B8%BANULL%EF%BC%8C%E7%B1%BB%E5%9E%8B%E4%B8%BAURL%EF%BC%8C%E4%B8%80%E4%B8%AA%E4%B8%BA%E4%BA%86%E5%8F%91%E9%80%81http%E8%AF%B7%E6%B1%82%E7%9A%84%E4%BB%A3%E7%90%86%20%E5%9C%A8%E5%B9%B3%E6%97%B6%E5%BC%80%E5%8F%91%E6%97%B6%EF%BC%8C%E5%B0%A4%E5%85%B6%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E6%97%B6%EF%BC%8C%E9%9C%80%E8%A6%81%E5%81%87%E6%95%B0%E6%8D%AE%E6%9D%A5%E8%BF%9B%E8%A1%8C%E6%A8%A1%E6%8B%9F%E8%AF%B7%E6%B1%82%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%97%B6%E5%80%99%E5%B0%B1%E9%9C%80%E8%A6%81,proxy%20%E4%BB%A3%E7%90%86%E6%9D%A5%E5%A4%84%E7%90%86%20create-react-app%20%3C%202.0)

1. 安装 http-proxy-middleware

```javascript
npm install http-proxy-middleware -D
```

2. 创建 /src/setupProxy.js 并配置

```javascript
const proxy = require('http-proxy-middleware');
module.exports = function (app) {
    app.use(
        '/api/v1/', //原本路由
        proxy({
            target : 'https://localhost:8080/', // 目标
            changeOrigin : true,  // 设置跨域请求
            PathRewrite : {
                '^/api/v1' : '' // 将/api/v1 变为 '' // 路径覆盖
            }
        })
    );
};
```