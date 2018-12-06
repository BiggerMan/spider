import re
import scrapy
from yousuu.items import YousuuItem

def process_onclick(value):
    m = re.search("ys.common.jumpurl\('t','(.+?)'\)", value)
    if m:
        return m.group(1)
    else:
        return ''

class YousuuSpider(scrapy.Spider):
    """docstring for YousuuSpider"""
    name = "yousuu"
    start_urls =  [
        'http://www.yousuu.com/booklist'
    ]

    def parse(self, response):
        item = YousuuItem()
        for record in response.css("tr.list-item"):
            votes =  record.css("a.votes small::text").extract_first()
            name =  record.css("a.name::text").extract_first()
            author =  record.css("td:nth-child(3) a::text").extract_first()
            count =  record.css("td:nth-child(4) p:first-child::text").extract_first()
            follows =  record.css("td:nth-child(6) p:first-child::text").extract_first()
            if int(votes.strip()) < 3000:
                continue

            item['votes'] =  votes.encode('utf-8').strip()
            item['name'] =  name.encode('utf-8').strip()
            item['author'] =  author.encode('utf-8').strip()
            item['count'] =  count.encode('utf-8').strip()
            item['follows'] =  follows.encode('utf-8').strip()
            yield item
        onclick = response.css("div.sokk-body div.right2center.smallcenter li:nth_child(2) a::attr(onclick)").extract_first()
        link = process_onclick(onclick)
        next_page = '?t=' + link
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
