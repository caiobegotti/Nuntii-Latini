Nuntii Latini
=============

Nuntii Latini is a news broadcast in Latin brought to you by some crazy Finnish. Although active for over 20 years they have no public archives with all their texts, you have to buy two or three ridiculously old books with limited news content instead. These are scrapped corpora of news between mid-2010 to 2012, which you can easily analyze with tools such as NLTK.

As of today the corpora contain about 32.000 tokens (300kb of text). A decent set of corpora contains at least 80.000 usable tokens, so there's plenty of room for improvement, specially trying to scrap even older news posts (pre-June 2010).

To my knowledge, Nuntii Latini only publishes news in Classical Latin. Do no try to run ecclesiastical parsers or anything like that on these files, unless you know what you're doing.

Format
------

The corpora are human-readable files in XML format. Every post is in a distinct file and they all use the following structure:

```
<broadcast>
    <title></title>
    <meta name="author" value=""/>
    <meta name="published" value=""/>
    <meta name="corpus" value=""/>
    <meta name="source" value=""/>
    <meta name="generator" value=""/>
    <headline>
        <title></title>
        <content></content>
    </headline>
    <news>
        <title></title>
        <content></content>
    </news>
</broadcast>
```

Broadcast is the post of the day, containing more than one news. Title is the title of this set of news. The meta tags contain informative data about the broadcast. Headline is the title of the main news of the day, so far the first one, and it will contain its title and the body of this main news. News is the block where subnews will appear, with their titles and content as well. However please notice we may have multiple news inside the same broadcast.

Known bugs
----------

The following broadcasts are known to have problems in their scrapped data. Some old pages have titles using `h4` for news titles, while others have no nodes at all! E.g.:

http://yle.fi/radio1/tiede/nuntii_latini/aestas_calidissima_in_finnia_24777.html

Contributing
------------

I'm really looking for a way to scrap posts older than July 2010. If you have any idea on it please get in touch!
