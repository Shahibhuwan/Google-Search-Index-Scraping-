import scrapy
from ..items import ScrapytutorialItem
class TravelNepal(scrapy.Spider):
    name ='travelnepal'
    page_number= 1
    start_urls=['https://www.google.com/search?q=Nepal+Travel&sxsrf=ALeKk03svxmI8vLIWsMJGgFCCAUnm4YVpg:1628828037882&ei=hfEVYeypNdXC3LUPh7uGmAM&start=0&sa=N&ved=2ahUKEwisgOSkka3yAhVVIbcAHYedATM4HhDy0wN6BAgBEDM&biw=795&bih=625']
#response have all the source code, extract gives only data and remove selector, extract_first gives us string

    def parse(self, response):
        items =ScrapytutorialItem()
         #all_row=response.xpath("//div[@class='g']/div/div/div/a/@href")
     
        all_row=response.xpath("//div[@class='g']")
        #title =response.xpath("//input/@value").extract()
        for row in all_row:
            url=row.xpath("div/div/div/a/@href").extract_first()
            title =row.xpath("div/div/div/a/h3/text()").extract_first()
            description =row.xpath("//div[@class='IsZvec']/div/span[last()]").extract_first()
            items['url']=url
            items['title']=title
            items['description']=description
            yield items
        # key should same as field name
        #next_page = response.xpath('//td[@class="d6cvqb"][last()]/a/@href').get()
        # next_page= 'https://www.google.com/search?q=Nepal+Travel&sxsrf=ALeKk03svxmI8vLIWsMJGgFCCAUnm4YVpg:1628828037882&ei=hfEVYeypNdXC3LUPh7uGmAM&start='+str(TravelNepal.page_number)+'0&sa=N&ved=2ahUKEwisgOSkka3yAhVVIbcAHYedATM4HhDy0wN6BAgBEDM&biw=795&bih=625'
        
        # if TravelNepal.page_number<=100 :
        #     TravelNepal.page_number=TravelNepal.page_number+1
        #     print(TravelNepal.page_number)
        #     yield response.follow(next_page, callback=self.parse)
#obey robots.txt false, user_agent middleware 