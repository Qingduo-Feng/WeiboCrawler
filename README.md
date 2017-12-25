# WeiboCrawler
新浪微博爬虫
主体使用Scrapy框架完成

2017年12月25日更新
初版
实现了简单的微博爬取，分别爬取个人信息与个人微博内容
为了绕开验证以及简化爬取方式，爬取了网页端的微博(m.weibo.cn)

程序使用：（macOS环境）
1. 修改配置
settings.py文件中有关于数据库的配置，本机使用的是MySQL

2. 运行
进入根目录
爬取内容：scrapy crawl weibo_content_spider
爬取个人信息：scrapy crawl weibo_fans_spider

