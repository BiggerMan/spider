# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YousuuPipeline(object):
    def process_item(self, item, spider):
        out2file = '/home/flytiger/Workspace/spider/yousuu/yousuu/yousuu.txt'
        with open(out2file, 'a+') as f:
            f.write('name: {}, author: {}, votes: {}, count:{}, followers:{}\n'.format(
                        item['name'], item['author'], item['votes'],
                        item['count'], item['follows']))
