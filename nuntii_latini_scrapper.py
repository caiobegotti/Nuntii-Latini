#!/usr/bin/env python
# corpora of public posts from nuntii latini, rights reserved
# this shell scrapper is under public domain, go wild
# caio begotti <caio1982@gmail.com>

from lxml import etree
from lxml.html import tostring

def get_news_urls():
    news_urls = []
    url = 'http://yle.fi/radio1/tiede/nuntii_latini/'
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div[@class='block-module clearfix']/h2/a/@href")
    for p in path:
        news_urls.append('http://yle.fi' + p)
    news_urls = news_urls[:-1]
    return news_urls

def get_news_count():
    news = get_news_urls()
    return len(news)

def get_news_titles():
    for url in news_urls:
        page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div/h1//text()")
        for p in path:
            news_titles.append(p)
        news_titles = news_titles[:-1]

count = get_news_count()
print 'Found %d news articles' % count
