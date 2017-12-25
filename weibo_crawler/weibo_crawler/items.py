# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()

    pass

class WeiboContentItem(scrapy.Item):
	userid = scrapy.Field()
	id = scrapy.Field()
	pub_date = scrapy.Field()
	text= scrapy.Field()
	pic = scrapy.Field()


class BasicInfoItem(scrapy.Item):
	ID = scrapy.Field()	
	nickname = scrapy.Field()		#昵称
	gender = scrapy.Field()			#性别
	age = scrapy.Field()			#年龄
	tags = scrapy.Field()			#标签
	brief_intro = scrapy.Field()	#简介
	verify = scrapy.Field()			#微博认证
	location = scrapy.Field()		#所在地
	level = scrapy.Field()			#等级
	signup_date = scrapy.Field()	#注册时间
	credit = scrapy.Field()			#阳光信用
	company = scrapy.Field()		#公司
	school = scrapy.Field()			#学校
	blog = scrapy.Field() 			#博客
