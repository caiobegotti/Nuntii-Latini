Nuntii Latini
=============

Nuntii Latini is a news broadcast in Latin brought to you by some crazy Finnish. Although active for over 20 years they have no public archives with all their texts, you have to buy two or three ridiculously old books with limited news content instead. These are scrapped corpora of news between mid-2010 to 2012, which you can easily analyze with tools such as NLTK.

As of today the corpora contain almost 27.000 tokens (300kb of text). A decent set of corpora contains at least 80.000 usable tokens, so there's plenty of room for improvement, specially trying to scrap even older news posts (pre-June 2010).

To my knowledge, Nuntii Latini only publishes news in Classical Latin. Do no try to run ecclesiastical parsers or anything like that on these files, unless you know what you're doing.

Format
------

The corpora is a set of human-readable files in XML format. Every post is in a distinct file and they all use the following structure:

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

The following "tags" are used throughout the corpora, so you will need to ignore them when doing your natural language processing magic:

Known bugs
----------

The following broadcasts are known to have problems in their scrapped data:

http://yle.fi/radio1/tiede/nuntii_latini/mario_monti_primus_minister_33069.html

http://yle.fi/radio1/tiede/nuntii_latini/emanatio_informatica_wikileaks_27325.html

http://yle.fi/radio1/tiede/nuntii_latini/destalinizatio_in_russia_suscipietur_27167.html

http://yle.fi/radio1/tiede/nuntii_latini/certamen_saunationis_fatale_24846.html

http://yle.fi/radio1/tiede/nuntii_latini/aestas_calidissima_in_finnia_24777.html

http://yle.fi/radio1/tiede/nuntii_latini/in_kirgisia_tumultus_violenti_24092.html

http://yle.fi/radio1/tiede/nuntii_latini/nuntii_latini_-_israeliani_impetum_maritimum_fecerunt_609.html

Contributing
------------

I'm really looking for a way to scrap posts older than July 2010. If you have any idea on it please get in touch!
