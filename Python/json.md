# json

json 相关库

## json dumps

将dict(字典)转化为json 文本

> 中文乱码 => json.dumps  序列化时默认使用的ascii编码
>
> 想输出真正的中文需要指定ensure_ascii=False：更深入分析，是应为dJSON object  不是单纯的unicode实现，而是包含了混合的unicode编码以及已经用utf-8编码之后的字符串