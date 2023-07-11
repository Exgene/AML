import scrapy

class SearchSpider(scrapy.Spider):
    name = "goodmorning"
    start_urls = ["https://www.google.com"]
    base_urls = ["www.google.com"]
    
    def parse(self,response):
        images = response.css('img::attr(src)').get()
        paragraphs = response.css('p::text').getall()
        
        with open('images.txt','w') as file:
            for image in images:
                file.write(image+'\n')
        
        with open('para.txt','w') as file:
            for para in paragraphs:
                file.write(para + '\n')
    