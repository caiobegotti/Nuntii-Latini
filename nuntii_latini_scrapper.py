#!/usr/bin/env python
# corpora of public posts from nuntii latini, rights reserved
# this shell scrapper is under public domain, go wild
# caio begotti <caio1982@gmail.com>

from lxml import etree
from lxml.html import tostring

def get_news_urls():
    urls = []
    url = 'http://yle.fi/radio1/tiede/nuntii_latini/'
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div[@class='block-module clearfix']/h2/a/@href")
    for p in path:
        urls.append('http://yle.fi' + p)
    urls = urls[:-1]
    return urls[:3]

def get_news_titles(urls):
    titles = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div/h1//text()")
        for p in path:
            titles.append(p)
    return titles

def get_news_dates(urls):
    dates = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div[@class='block-module clearfix']/p[@class='published']//text()")
        for p in path:
            dates.append(p)
    return dates

urls = get_news_urls()
dates = get_news_dates(urls)
titles = get_news_titles(urls)
data = zip(titles, dates, urls)
for d in data:
    print d
