import scrapy
class ArticleSpider(scrapy.Spider):
    name = 'article'
    
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Python_(programming_language)',
            'https://prathwik.fun'
        ]
        return [scrapy.Request(url=url,callback=self.parse) for url in urls]
    
    def parse(self,response):
        url = response.url
        title = response.css('h1::text').extract_first()#.css is a selctor whihc is most commonly used to access particular elements of an html file
        print('URl is: {}',format(url))
        print('Title is: {}',format(title))
        
