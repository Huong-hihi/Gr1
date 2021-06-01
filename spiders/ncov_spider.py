import scrapy
import datetime

class QuoteSpider(scrapy.Spider):
    
    name="ncov"
    start_urls = [
         'https://ncov.moh.gov.vn/web/guest/dong-thoi-gian?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_nf7Qy5mlPXqs&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_nf7Qy5mlPXqs_delta=10&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_nf7Qy5mlPXqs_cur=1',
    ]
  
    def parse(self, response):
        for quote in response.xpath('//div[@class="timeline-detail"]'):
            format_date = '%d/%m/%Y'
            content = ""
            for page in quote.xpath('.//div[@class="timeline-content"]/p/text()').extract():
                content = content + page
            datetime_obj = datetime.datetime.strptime(quote.xpath('.//div[@class="timeline-head"]/h3/text()').extract_first().split(" ")[-1], format_date)
            yield {
                #'time' : quote.xpath('.//div[@class="timeline-head"]/h3/text()').extract_first().split(" ")[0],
                #'date' : datetime_obj.date(),
                'content' : content
            }
        
        if(len(response.xpath('//ul[@class="lfr-pagination-buttons pager"]/li[@class=""]/a/@href').extract())==1):
            next_page_url = response.xpath('//ul[@class="lfr-pagination-buttons pager"]/li[@class=""]/a/@href').extract_first()
        else:
            next_page_url = response.xpath('//ul[@class="lfr-pagination-buttons pager"]/li[@class=""]/a/@href').extract()[1]
        if next_page_url is not None:
            yield scrapy.Request(next_page_url)