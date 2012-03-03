#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    return urls[:2]

def get_articles_dates(urls):
    dates = []
    for u in urls:
        page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
        path = page.xpath("//div[@class='block-module clearfix']/p[@class='published']//text()")
        for p in path:
            dates.append(p)
    return dates[:-1]

def get_articles_title(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div/h1//text()")
    return path

def get_subnews_titles(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//h3//text()")
    return path[:-3]

def get_articles_content(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div[@class='kuuntele-netissa']/following::p[not(preceding::h3) and not(starts-with(text(),'('))]//text()")
    return path

def get_subnews_content(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//h3/following-sibling::p[not(starts-with(text(),'('))]//text()")
    return path[:-8]

def get_subnews_author(url):
    authors = []
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//p[starts-with(text(),'(')]//text()")
    for p in path:
        res = re.sub(r'[^\w ]', '', p)
        authors.append(res)
    if len(authors) > 1:
        return authors[1:]
    else:
        return authors

urls = get_news_urls()
dates = get_articles_dates(urls)

for u in urls:
    title = get_articles_title(u)
    article_content = get_articles_content(u)
    
    print u
    print title
    print article_content
    
    subnews = get_subnews_titles(u)
    subnews_content = get_subnews_content(u)
    author = get_subnews_author(u)

    data = zip(subnews, subnews_content, author)
    for d in data:
        print d
