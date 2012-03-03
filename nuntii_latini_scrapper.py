#!/usr/bin/env python
# -*- coding: utf-8 -*-
# corpora of public posts from nuntii latini, rights reserved
# this shell scrapper is under public domain, go wild
# caio begotti <caio1982@gmail.com>

import re

from elementtree.SimpleXMLWriter import XMLWriter

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
    return urls[:5]

def get_articles_dates(u):
    page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div[@class='block-module clearfix']/p[@class='published']//text()")
    return path[0]

def get_articles_title(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div/h1//text()")
    return path[0]

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
        return authors
    else:
        return authors

urls = get_news_urls()

for u in urls:
    title = get_articles_title(u)
    article_content = get_articles_content(u)
    authors = get_subnews_author(u)
    subnews = get_subnews_titles(u)
    subnews_content = get_subnews_content(u)
    date = get_articles_dates(u)

    filename = 'nl_' + title.replace(' ','_').lower() + '.xml'
    w = XMLWriter(filename, encoding='utf-8')
    html = w.start("broadcast")

    content = ' '.join(article_content)
    if len(authors) > 1:
        authorship = ','.join(set(authors))
    else:
        authorship = authors[0]

    w.element("title", title)
    w.element("meta", name="author", value=authorship)
    w.element("meta", name="published", value=date)
    w.element("meta", name="corpus", value=filename)
    w.element("meta", name="source", value=u)
    w.element("meta", name="generator", value="https://github.com/caio1982/Nuntii-Latini")
    
    w.start("headline")
    w.element("title", title)
    w.element("content", content)
    w.end("headline")

    data = zip(subnews, subnews_content)
    for d in data:
        subnews = d[0]
        subnews_content = d[1]
        w.start("news")
        w.element("title", subnews)
        w.element("content", subnews_content)
        w.end("news")
    
    w.close(html)
