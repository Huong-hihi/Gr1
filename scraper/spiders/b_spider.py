import scrapy
import datetime
class QuotesSpider(scrapy.Spider):
    name = "covidb" #định danh cho spider
    start_urls = [
             'https://www.vietnamplus.vn/chude/dich-viem-duong-ho-hap-cap-covid19/1070/trang1.vnp',
            # 'https://baomoi.com/phong-chong-dich-covid-19/top/328.epi',
    ]
    def parse(self, response):
        finalPage = 'https://www.vietnamplus.vn'+ response.xpath('//nav[@class="pag"]/span[@id="mainContent_ContentList1_pager"]/ul/li/a/@href')[-1].extract()
        buff = finalPage.split("/")[-1].split(".")[-2].split("g")[-1]
        totalPage = int(buff)
        for page in range(totalPage):
            link = finalPage.replace(str(totalPage), str(page + 1))
            yield scrapy.Request(link, callback=self.crawlLyric)
    def crawlLyric(self, response):
        for linkbao in response.xpath('//article[@class="story"]/a/@href').extract():
            linkbao = 'https://www.vietnamplus.vn'+ linkbao
            yield scrapy.Request(linkbao, callback=self.saveFile)
    def saveFile(self, response):
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