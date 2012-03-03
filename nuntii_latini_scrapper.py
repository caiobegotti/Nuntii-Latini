#!/usr/bin/env python
# corpora of public posts from nuntii latini, rights reserved
# this shell scrapper is under public domain, go wild
# caio begotti <caio1982@gmail.com>

import re

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
    return urls[:1]

def get_articles_titles(urls):
    titles = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div/h1//text()")
        for p in path:
            titles.append(p)
    return titles

def get_articles_dates(urls):
    dates = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div[@class='block-module clearfix']/p[@class='published']//text()")
        for p in path:
            dates.append(p)
    return dates

def get_subnews_titles(urls):
    news = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//h3//text()")
        for p in path:
            news.append(p)
    return news[:-3]

def get_articles_content(urls):
    content = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div[@class='kuuntele-netissa']/following::p[not(preceding::h3)]//text()")
        for p in path:
            content.append(p)
    return content

def get_subnews_content(urls):
    content = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//h3/following-sibling::p//text()")
        for p in path:
            content.append(p)
    return content[:-9]

def get_subnews_authors(urls):
    authors = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//p[starts-with(text(),'(')]//text()")
        for p in path:
            res = re.sub(r'[^\w ]', '', p)
            authors.append(res)
    return authors

urls = get_news_urls()
dates = get_articles_dates(urls)
titles = get_articles_titles(urls)
subnews = get_subnews_titles(urls)
article_content = get_articles_content(urls)
subnews_content = get_subnews_content(urls)
authors = get_subnews_authors(urls)
