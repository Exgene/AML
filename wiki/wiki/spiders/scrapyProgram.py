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
        
#Simplified code

import scrapy

class Program(scrapy.Spider):
    name = 'Program'
    
    def requests(self):
        url = 'https://google.com'
        return scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print(f"Url:{url}\nTitle:{title}")
        
#Write a program to fetch paragraphs from any two urls

import scrapy

class Paragrpah(scrapy.Spider):
    name = "paragraph"
    
    def requests(self):
        urls = [
            'https://www.google.com/',
            'https://www.github.com/'
        ]
        return [scrapy.Request(url=url,callback = self.parse)for url in urls]
    
    def parse(self,response):
        url = response.url
        paragraph = response.css('p::text').getall()
        print(f"URL:{url}\n")
        for para in paragraph:
            print(f"Paragraph : {para}")
        