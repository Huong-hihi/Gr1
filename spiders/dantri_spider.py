#-*- coding: utf8 -*-
import scrapy
import datetime
class QuotesSpider(scrapy.Spider):
    name = "erro" #định danh cho spider
    start_urls = [
             'https://baomoi.com/phong-chong-dich-covid-19/top/328.epi',
    ]
    def parse(self, response):
    # if (response.url.split("=")[0] == 'https://thuvienphapluat.vn/tintuc/tag?keyword=Covid-19&p'):
    #for linkbao in response.xpath('//article[@class="article media"]/figure[@class="media-left"]/a/@href').extract():
        for linkbao in response.xpath('//h4[@class="story__heading"]//a/@href').extract():
            yield scrapy.Request(linkbao, callback=self.saveFile)
        next_page_url = response.xpath('//a[@class="btn btn-sm btn-primary"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
    def saveFile(self, response):
        content = ""
        for a in response.xpath('//div[@class="article__body cms-body"]/p/text()').extract():
            content = content + a
        date = response.xpath('//div[@class="divCate"]/span[@class="time"]/time/text()').extract_first().split()
        format_date = '%d/%m/%Y'
        date_object= datetime.datetime.strptime(date[0],format_date)
        dateTime = str(date_object.date())+" "+date[1]
        yield {
            'title': response.xpath('//h1[@class="article__title cms-title"]/text()').extract_first(),
            'content' : content,
            'time': dateTime
        }