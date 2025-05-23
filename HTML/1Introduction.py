# 1 HTML(hyper text markup language)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>title</title>
    <link rel="stylesheet" href="index.css">

</head>
<body>


</body>
</html>


"""
标签组成
<标签 属性名='属性值'>内容</标签>
1 成对出现标签：属于关闭型，有结束标签，例如title,body
2 非关闭型，没有结束标签，例如meta,br,hr
3 标签是否分行：
分为块级标签（独自占一行，为块状）：h1,hr,
行级标签（在行显示，可以与其他标签在同一行显示）:span
"""

"""
实体字符
&实体字符名称;
常用实体字符：
&lt;表示小于号<    &gt;表示大于号>
例如 图书<<雾都孤儿>>  应表达为 &lt;&lt;雾都孤儿&gt;&gt;

对于连续空白字符（空格，缩进，换行），在浏览器只会显示一个空格
&nbsp; 空格 space

如果只显示& 可以用&amp;

&quoa; 表示双引号

&copy; 版权符号

&reg;  注册符号

&times; 关闭符号
"""


"""
文档类型
使用<!DOCTYPE> 声明文档类型，主要用来指定HTML版本规范
"""
