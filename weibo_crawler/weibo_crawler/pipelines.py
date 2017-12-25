# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors

from twisted.internet import defer
from twisted.enterprise import adbapi
from scrapy.exceptions import NotConfigured

from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy import log
from .items import BasicInfoItem, WeiboContentItem
import time
import datetime

class WeiboCrawlerPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item, spider)
        query.addErrback(self.handle_error)
        return query

    def _conditional_insert(self, conn, item, spider):
	    if spider.name == "weibo_fans_spider":
	        conn.execute(
	            """insert into user (id, nickname, gender, location, signup_date, brief_intro, credit) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s");"""%
	            (item["ID"],
	             item["nickname"],
	             item["gender"],
	             item["location"],
	             item["signup_date"],
	             item["brief_intro"],
	             item["credit"]
	            ))
	        if "verify" in item:
	        	conn.execute("update user set verify = '%s' where id = '%s';"%(item["verify"], item["ID"]))
	        if "tags" in item:
	        	conn.execute("update user set tags = '%s' where id = '%s';"%(item["tags"], item["ID"]))
	        if "level" in item:
	        	conn.execute("update user set level = '%s' where id = '%s';"%(item["level"], item["ID"]))
	        if "company" in item:
	        	conn.execute("update user set company = '%s' where id = '%s';"%(item["company"], item["ID"]))
	        if "school" in item:
	        	conn.execute("update user set school = '%s' where id = '%s';"%(item["school"], item["ID"]))
	        if "blog" in item:
	        	conn.execute("update user set blog = '%s' where id = '%s';"%(item["blog"], item["ID"]))
	    elif spider.name == "weibo_content_spider":
	        conn.execute(
	        """insert into weibo_content (userid, id, pub_date, text) values ('%s', '%s', '%s', '%s');"""%
	            (item["userid"],
	             item["id"],
	             item["pub_date"],
	             item["text"]
	            ))
	        if "pic" in item:
	        	conn.execute('update weibo_content set pic = "%s" where id = "%s";'%(item["pic"], item["id"]))
    def handle_error(self, e):
        log.err(e)