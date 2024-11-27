import scrapy
import csv

class RztkCsvSpider(scrapy.Spider):
    name = "rztk_csv"
    allowed_domains = ["rozetka.com.ua"]
    start_urls = ["https://rozetka.com.ua/umnoe-osveshchenie/c4638351/"]

    def parse(self, response):
        smart_light = response.css('div.goods-tile__content')
        with open("rztk.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Наименование товара', 'Цена товара', 'Ссылка на страницу с товаром'])
        for light in smart_light:
            row = [light.css('span.goods-tile__title::text').get(),
                   f'{light.css('span.goods-tile__price-value::text').get()} {light.css('span.currency::text').get()}',
                   light.css('a.product-link').attrib['href']]
            with open ("rztk.csv", 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(row)
            yield {'name': row[0], 'price': row[1], 'url': row[2]}