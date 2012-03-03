#!/usr/bin/env python
# -*- coding: utf-8 -*-
# corpora of public posts from nuntii latini, rights reserved
# this shell scrapper is under public domain, go wild
# caio begotti <caio1982@gmail.com>

from re import compile, findall, sub

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
    return urls

def get_articles_dates(u):
    page = etree.parse(u, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//div[@class='block-module clearfix']/p[@class='published']//text()")
    res = path[0].replace('JULKAISTU ','').replace('KLO ','').replace('.','/', 2).replace('.',':')
   
    regex = compile("(\d{2})/(\d{2})/(\d{4})")
    fields = regex.findall(res)[0]
    iso = fields[2] + fields[1] + fields[0]

    regex = compile("\d{2}:\d{2}")
    date = regex.findall(res)[0] + ':00'

    res = '%s %s' % (iso, date)
    return res

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
    path = page.xpath("//div[@class='kuuntele-netissa']/following::p[not(preceding::h3) and not(starts-with(text(),'(')) and not(contains(text(),'Tuomo')) and not(contains(text(),'Reijo'))]//text()")
    return path

def get_subnews_content(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//h3/following-sibling::p[not(starts-with(text(),'(')) and not(contains(text(),'Tuomo')) and not(contains(text(),'Reijo'))]//text()[1]")
    return path[:-5]

def get_subnews_author(url):
    page = etree.parse(url, etree.HTMLParser(encoding='utf-8'))
    path = page.xpath("//p[starts-with(text(),'(')][1]//text()")
    if path:
        res = sub(r'[^\w ]', '', path[0])
        return res
    else:
        return 'N/A'

urls = get_news_urls()

for u in urls:
    title = get_articles_title(u)
    article_content = get_articles_content(u)
    author = get_subnews_author(u)
    subnews = get_subnews_titles(u)
    subnews_content = get_subnews_content(u)
    date = get_articles_dates(u)
    iso = date.split(' ')[0]

    filename = 'nl_' + iso + '_' +  title.replace(' ','_').lower() + '.xml'
    w = XMLWriter(filename, encoding='utf-8')
    html = w.start("broadcast")

    content = ' '.join(article_content)

    w.element("title", title)
    w.element("meta", name="author", value=author)
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
