# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#import pymysql

class LianjiaPipeline(object):


    #打开数据库
    # def open_spider(self, spider):
    #     db = spider.settings.get('MYSQL_DBNAME', 'scrapy_db') #数据库
    #     host = spider.settings.get('MYSQL_HOST', 'localhost') #主机
    #     port = spider.settings.get('MYSQL_PORT', 3306) #端口
    #     user = spider.settings.get('MYSQL_USER', 'root') #用户名
    #     passwd = spider.settings.get('MYSQL_PWD', '123456') #密码
    #
    #     self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
    #     self.db_cur = self.db_conn.cursor()
    #
    # #关闭数据库
    # def close_spider(self, spider):
    #     self.db_conn.commit()
    #     self.db_conn.close()


    #处理数据
    def process_item(self, item, spider):
        #self.insert_db(item)
        return item


    # 插入数据
    # def insert_db(self, item):
    #     values = (
    #         item['title'],
    #         item['price'],
    #         item['unitPrice'],
    #         item['community'],
    #         item['region'],
    #         item['houseType'],
    #         item['floor'],
    #         item['area'],
    #         item['towards'],
    #         item['decoration'],
    #         item['focus']
    #     )
    #
    #     sql = 'INSERT INTO books VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #     self.db_cur.execute(sql, values)

