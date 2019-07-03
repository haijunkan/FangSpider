# -*- coding: utf-8 -*-
import scrapy
import re
from fang2.items import NewHouse,EsfHouse


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.html']
    # redis_key = 'fang:start_url'
    num=2

    def parse(self, response):
        province = None
        trs = response.xpath('//table[@id="senfe"]//tr')
        for tr in trs:
            tds = tr.xpath('./td')
            province_name = tds[-2].xpath('.//text()').get()
            province_name = re.sub(r'\s','',province_name)
            if province_name:
                province = province_name
            if province_name == '其他':
                break
            links = tds[-1].xpath('.//a')
            for link in links:
                city = link.xpath('.//text()').get()
                if  city=='北京':
                    newhouse_url = 'https://newhouse.fang.com/house/s/'
                    esf_url = 'https://esf.fang.com/'
                else:
                    link = link.xpath('./@href').get()
                    link_list = link.split('.')
                    left = link_list[0]
                    right = link_list[1]+'.'+link_list[2]
                    newhouse_url = left+'.'+'newhouse.'+right
                    esf_url = left+'.'+'esf.'+right
                # print(city)
                # print(newhouse_url)
                # print(esf_url)
                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse,meta={'info':(province,city)})
                # scrapy.Request(esf_url, callback=self.parse_esf,meta={'info':(city,province)})


    def parse_newhouse(self, response):
        province,city = response.meta.get('info')
        lis=response.xpath('//div[@id="newhouse_loupai_list"]/ul/li')
        # print(len(lis))
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]//text()').getall()
            name = ''.join(name)
            name = re.sub(r'\s','',name)
            house_type = li.xpath('.//div[@class="house_type clearfix"]//text()').getall()
            rooms=''.join(house_type[0:-2])
            rooms=re.sub(r'\s','',rooms)
            # print(house_type)
            try:
                area = house_type[-1]
                area = re.sub(r'\s|－', '', area)
            except:
                area = ''


            address_info = li.xpath('.//div[@class="address"]/a/@title').get()
            # print(address_info)
            if address_info:
                address_info = address_info.split(']')
                # print(address_info)
                district = re.sub("\[","",address_info[0])
                address = address_info[-1]
            else:
                district = ''
                address = ''
            sale = li.xpath('.//div[@class="fangyuan"]/span//text()').getall()
            price = ''.join(li.xpath('.//div[@class="nhouse_price"]//text()').getall())
            price = re.sub(r'\s','',price)
            origin_url = li.xpath('.//div[@class="nlcd_name"]/a/@href').get()
            origin_url = response.urljoin(origin_url)
            item = NewHouse(province=province, city=city, name=name, rooms=rooms, area=area, address=address, district=district, sale=sale, price=price, origin_url=origin_url)
            print(item)
            yield item
        url = response.urljoin('/house/s/b9{0}/').format(self.num)
        self.num+=1
        print(url)
        yield scrapy.Request(url=url, callback=self.parse_newhouse, meta={'info':(province,city)})





