import scrapy

class WikiSearch(scrapy.Spider):
    name = "program1"
    start_urls = ["https://nitte.edu.in/"]

    # set the user agent
    custom_settings = {
        # TO trick them into thinking this is not a bot
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    def parse(self, response):
        # Extract images
        images = response.css('img::attr(src)').getall()

        # Extract paragraphs
        paragraphs = response.css('p::text').getall()

        # Save images to a file
        with open('imagescpy.txt', 'w') as file:
            for image in images:
                file.write(image+'\n')

        # Saving paragraphs to a file
        with open('paragraphscpy.txt', 'w') as file:
            for para in paragraphs:
                file.write(para+'\n')
