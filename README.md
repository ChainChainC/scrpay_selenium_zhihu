# scrpay_selenium_zhihu
利用知乎网站为测试，学习使用scrapy框架嵌入selenium


#主要的嵌入方式在middleware中
在middleware中继承process——response/request等（注意在setting中开启中间件）

#其中cookie获取没有嵌入到爬虫中去，学习项目，代码分散简单更好理解
cookie.py能够从网页中抓取到你登录的cookie，但需要我们自己去进行登录操作，登录使用第三方登录（如QQ），之后需要将抓取到的cookie放到middleware的下载中间件中。
