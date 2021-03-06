# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ImdbcrawlingPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = sqlite3.connect("actor.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS imdb_tb""")
        self.curr.execute("""create table imdb_tb(
                            actor_name text,
                            actor_photo text,
                            actor_traits text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        for i in range(75):

            self.curr.execute("""insert into imdb_tb values (?,?,?)""",(
                item['actor_name'][i],
                item['actor_photo'][i],
                item['actor_traits'][i]
            ))
        self.conn.commit()