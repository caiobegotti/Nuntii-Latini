GitHub Markup
=============

Nuntii Latini is a news broadcast in Latin brought to you by some crazy Finnish. Although active for over 20 years they have no public archives with all their texts, you have to buy two or three ridiculously old books with limited news content instead. These are scrapped corpora of news between mid-2010 to 2012, which you can easily analyze with tools such as NLTK.


Markups
-------

The following "tags" are used throughout the corpora, so you will need to ignore them when doing your natural language processing magic:

* TITLE: the title of broadcast of the day
* PUBLISHED: metadata about its publishing date and time
* HEADER: title of secondary news of the day
* PARAGRAPH: the first without a header are from the main article, others appear after a header only
* AUTHOR: the name of the person who published the article

Contributing
------------

I'd really love to convert this scrapper into one in Python using Scrapy.org (which I actually used in the very beginning but in shell it was way faster). Wanna help me to do it? :-)
