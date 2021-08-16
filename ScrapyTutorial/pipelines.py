# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3



# when the item is yield then it goes to pipeline and look for init method(after instantiated) at first only than for every time of yield it call prosses method
class ScrapytutorialPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn =sqlite3.connect('tour.db')
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tn_tb""")
        self.curr.execute("""create table tn_tb(
                title text,
                description text,
                url text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        # print("title*************************************************************************************"+ item['title'])
        # self.curr.execute("""insert into tn_tb values (?,?,?) """,(item['title'],item['description'],item['url']))
        # self.conn.commit()
        return item
    

    def store_db(self, item):
        self.curr.execute("""insert into tn_tb values (?,?,?) """,(item['title'],item['description'],item['url']))
        self.conn.commit()

    # create connection then create table and db then while processing(scrapping data) each item the corresponding data is stored in db 