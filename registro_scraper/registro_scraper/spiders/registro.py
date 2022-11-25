import pandas as pd
import scrapy
import get_list
import des_prod


class SpiderRegistro(scrapy.Spider):
    name = 'registro'
    start_urls = [
        'https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP='
    ]
    custom_settings = {
        # 'FEED_URI': 'cia.json',
        # 'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        list_links = get_list.get_links()

        for link in list_links:
            # print(link)
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        descripcion = des_prod.des_prod(link)
        print(descripcion)
