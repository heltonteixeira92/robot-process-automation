"""
Doc: https://scrapy.org/
- run:
scrapy runspider main.py

- export:
scrapy runspider main.py -O olx.json

"""

import json
import scrapy


user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0'}
url = 'https://www.olx.com.br/imoveis/aluguel/estado-sp'
selector = '//script[@id="__NEXT_DATA__"]/text()'


class OlxHouse(scrapy.Spider):
    name = 'olx'

    custom_settings = {
        'USER_AGENT': user_agent,
        'AUTOTHROTTLE_ENABLED': True,
        # 'AUTOTHROTTLE_START_DELAY': 10
    }

    def start_requests(self):
        for page in range(1, 5):
            yield scrapy.Request(f'https://www.olx.com.br/imoveis/aluguel/estado-sp?o={page}')

    def parse(self, response, **kwargs):
        html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
        houses = html.get('props').get('pageProps')
        if houses is not None:
            houses = houses.get('ads')
            if houses is not None:
                for house in houses:
                    yield {
                        'title': house.get('title'),
                        'price': house.get('price'),
                        'location': house.get('location'),
                    }
