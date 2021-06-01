# -*- coding: utf8 -*-
import scrapy
import datetime
class QuotesSpider(scrapy.Spider):
    name = "covidc" #định danh cho spider
    start_urls = [
        'https://thuvienphapluat.vn/tintuc/tag?keyword=Covid-19&p=1',
        ]
    def parse(self, response):
    # if (response.url.split("=")[0] == 'https://thuvienphapluat.vn/tintuc/tag?keyword=Covid-19&p'):
    #for linkbao in response.xpath('//article[@class="article media"]/figure[@class="media-left"]/a/@href').extract():
        for linkbao in response.xpath('//ul[@class="ulTinList"]/li[@class="tt"]/a/@href').extract():
            linkbao = 'https://thuvienphapluat.vn/'+ linkbao
            yield scrapy.Request(linkbao, callback=self.saveFile)
        next_page_url = response.xpath('//nav[@class="pagi-center"]/ul[@class="pagination pagination-sm"]/li/a/@href').extract()[7]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
    def saveFile(self, response):
        content = ""
        for a in response.xpath('//div[@class="newcontent"]/p/text()').extract():
            content = content + a
        date = response.xpath('//div[@class="divCate"]/span/text()').extract_first().split()
        format_date = '%d/%m/%Y'
        date_object= datetime.datetime.strptime(date[0],format_date)
        dateTime = str(date_object.date())+" "+date[1]
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'content' : content,
            'time': dateTime
        }