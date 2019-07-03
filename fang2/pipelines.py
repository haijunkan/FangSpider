# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class Fang2Pipeline(object):
    def __init__(self):
        self.newhouse_fp = open('newhouse.json','wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp, ensure_ascii=False)

    def process_item(self, item, spider):
        self.newhouse_exporter.export_item(item)

    def close_fp(self):
        self.newhouse_fp.close()
