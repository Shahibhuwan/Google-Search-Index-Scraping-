# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#Scrapped data -> Item Containers -> Json/csv file
# Scrapped data -> Item Containers -> Pipeline -> SQL/Mongo database . for this activate pipelinez
import scrapy


class ScrapytutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    pass
