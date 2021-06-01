# # -*- coding: utf8 -*-
# import scrapy
# import datetime
# class QuotesSpider(scrapy.Spider):
#     name = "thethao" #định danh cho spider
#     start_urls = [
#         'https://thuvienphapluat.vn/tintuc/tag?keyword=Covid-19&p=1',
#         ]
#     def parse(self, response):
#     # if (response.url.split("=")[0] == 'https://thuvienphapluat.vn/tintuc/tag?keyword=Covid-19&p'):
#     #for linkbao in response.xpath('//article[@class="article media"]/figure[@class="media-left"]/a/@href').extract():
#         for linkbao in response.xpath('//ul[@class="ulTinList"]/li[@class="tt"]/a/@href').extract():
#             linkbao = 'https://thuvienphapluat.vn/'+ linkbao
#             yield scrapy.Request(linkbao, callback=self.saveFile)
#         next_page_url = response.xpath('//nav[@class="pagi-center"]/ul[@class="pagination pagination-sm"]/li/a/@href').extract()[7]
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))
#     def saveFile(self, response):
#         content = ""
#         for a in response.xpath('//div[@class="newcontent"]/p/text()').extract():
#             content = content + a
#         date = response.xpath('//div[@class="divCate"]/span/text()').extract_first().split()
#         format_date = '%d/%m/%Y'
#         date_object= datetime.datetime.strptime(date[0],format_date)
#         dateTime = str(date_object.date())+" "+date[1]
#         yield {
#             'title': response.xpath('//h1/text()').extract_first(),
#             'content' : content,
#             'time': dateTime
#         }
# -*- coding: utf8 -*-
# import scrapy
# import datetime
# class QuotesSpider(scrapy.Spider):
#     name = "thethao" #định danh cho spider
#     start_urls = [
#              'https://dantri.com.vn/suc-khoe/dai-dich-covid-19/trang-1.htm',
#             # 'https://baomoi.com/phong-chong-dich-covid-19/top/328.epi',
#     ]
#     def parse(self, response):
#         for linkbao in response.xpath('//div[@class="news-item news-item--timeline news-item--left2right"]/a/@href').extract():
#             linkbao = 'https://dantri.com.vn'+ linkbao
#             yield scrapy.Request(linkbao, callback=self.saveFile)
#         next_page_url = response.xpath('//li/a[@class="text-primary btn btn-light btn-block btn-lg"]/@href').extract_first()
#         if next_page_url is not None:
#             yield scrapy.Request(response.urljoin(next_page_url))
#     def saveFile(self, response):
#         content = ""
#         for a in response.xpath('//div[@class="dt-news__content"]/p/text()').extract():
#             content = content + a
#         date = response.xpath('//div[@class="dt-news__meta"]/span[@class="dt-news__time"]/text()').extract_first().split()
#         format_date = '%d/%m/%Y'
#         date_object= datetime.datetime.strptime(date[2],format_date)
#         dateTime = str(date_object.date())+" "+date[4]
#         yield {
#             'title': response.xpath('//h1[@class="dt-news__title"]/text()').extract_first().replace('\r', '').replace('\n', '').replace('\t', '').lstrip(' ').rstrip(' '),
#             'content' : content, 
#             'time': dateTime
#         }
# import scrapy
# import datetime
# class QuotesSpider(scrapy.Spider):
#     name = "thethao" #định danh cho spider
#     start_urls = [
#              'https://www.vietnamplus.vn/chude/dich-viem-duong-ho-hap-cap-covid19/1070/trang1.vnp',
#             # 'https://baomoi.com/phong-chong-dich-covid-19/top/328.epi',
#     ]
#     def parse(self, response):
#         finalPage = 'https://www.vietnamplus.vn'+ response.xpath('//nav[@class="pag"]/span[@id="mainContent_ContentList1_pager"]/ul/li/a/@href')[-1].extract()
#         buff = finalPage.split("/")[-1].split(".")[-2].split("g")[-1]
#         totalPage = int(buff)
#         for page in range(totalPage):
#             link = finalPage.replace(str(totalPage), str(page + 1))
#             yield scrapy.Request(link, callback=self.crawlLyric)
#     def crawlLyric(self, response):
#         for linkbao in response.xpath('//article[@class="story"]/a/@href').extract():
#             linkbao = 'https://www.vietnamplus.vn'+ linkbao
#             yield scrapy.Request(linkbao, callback=self.saveFile)
#     def saveFile(self, response):
#         content = ""
#         for a in response.xpath('//div[@class="content article-body cms-body AdAsia"]/p/text()').extract():
#             content = content + a
#         date = response.xpath('//div[@class="source"]/time/text()').extract_first().split()
#         format_date = '%d/%m/%Y'
#         date_object= datetime.datetime.strptime(date[0],format_date)
#         dateTime = str(date_object.date())+" "+date[1]
#         yield {
#             'title': response.xpath('//h1[@class="details__headline cms-title"]/text()').extract_first(),
#             'content' : content, 
#             'time': dateTime
#         }
import scrapy
import datetime
class QuotesSpider(scrapy.Spider):
    name = "covid1" #định danh cho spider
    start_urls = [
            'https://www.vietnamplus.vn/chude/dich-viem-duong-ho-hap-cap-covid19/1070/trang1.vnp',
            'https://thuvienphapluat.vn/tintuc/tag?keyword=Covid-19&p=1',
    ]
    def parse(self, response):
        if (response.url.split("=")[0] == 'https://thuvienphapluat.vn/tintuc/tag?keyword'):
            for linkbao in response.xpath('//ul[@class="ulTinList"]/li[@class="tt"]/a/@href').extract():
                linkbao = 'https://thuvienphapluat.vn'+ linkbao
                yield scrapy.Request(linkbao, callback=self.saveFile1)
            next_page_url = response.xpath('//nav[@class="pagi-center"]/ul[@class="pagination pagination-sm"]/li/a/@href').extract()[7]
            
            if next_page_url is not None:
                next_page_url = "https://thuvienphapluat.vn" + next_page_url
                yield scrapy.Request(next_page_url)
        else :
            finalPage = 'https://www.vietnamplus.vn'+ response.xpath('//nav[@class="pag"]/span[@id="mainContent_ContentList1_pager"]/ul/li/a/@href')[-1].extract()
            buff = finalPage.split("/")[-1].split(".")[-2].split("g")[-1]
            totalPage = int(buff)
            for page in range(totalPage):
                link = finalPage.replace(str(totalPage), str(page + 1))
                yield scrapy.Request(link, callback=self.crawlContent2)
    def crawlContent2(self, response):
        for linkbao in response.xpath('//article[@class="story"]/a/@href').extract():
            linkbao = 'https://www.vietnamplus.vn'+ linkbao
            yield scrapy.Request(linkbao, callback=self.saveFile2)
    def saveFile1(self, response):
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
    def saveFile2(self, response):
        content = ""
        for a in response.xpath('//div[@class="content article-body cms-body AdAsia"]/p/text()').extract():
            content = content + a
        date = response.xpath('//div[@class="source"]/time/text()').extract_first().split()
        format_date = '%d/%m/%Y'
        date_object= datetime.datetime.strptime(date[0],format_date)
        dateTime = str(date_object.date())+" "+date[1]
        yield {
            'title': response.xpath('//h1[@class="details__headline cms-title"]/text()').extract_first(),
            'content' : content, 
            'time': dateTime
        }
