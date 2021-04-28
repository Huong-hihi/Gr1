#-*- coding: utf8 -*-
import scrapy
import datetime
class QuotesSpider(scrapy.Spider):
    name = "covida" #định danh cho spider
    start_urls = [
             'https://dantri.com.vn/suc-khoe/dai-dich-covid-19/trang-1.htm',
            # 'https://baomoi.com/phong-chong-dich-covid-19/top/328.epi',
    ]
    def parse(self, response):
        for linkbao in response.xpath('//div[@class="news-item news-item--timeline news-item--left2right"]/a/@href').extract():
            linkbao = 'https://dantri.com.vn'+ linkbao
            yield scrapy.Request(linkbao, callback=self.saveFile)
        next_page_url = response.xpath('//li/a[@class="text-primary btn btn-light btn-block btn-lg"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
    def saveFile(self, response):
        content = ""
        for a in response.xpath('//div[@class="dt-news__content"]/p/text()').extract():
            content = content + a
        date = response.xpath('//div[@class="dt-news__meta"]/span[@class="dt-news__time"]/text()').extract_first().split()
        format_date = '%d/%m/%Y'
        date_object= datetime.datetime.strptime(date[2],format_date)
        dateTime = str(date_object.date())+" "+date[4]
        yield {
            'title': response.xpath('//h1[@class="dt-news__title"]/text()').extract_first().replace('\r', '').replace('\n', '').replace('\t', '').lstrip(' ').rstrip(' '),
            'content' : content, 
            'time': dateTime
        }