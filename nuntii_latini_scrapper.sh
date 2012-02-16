#!/bin/bash -e
# corpora of public posts from nuntii latini, rights reserved
# this shell scrapper is under public domain, go wild
# caio1982@gmail.com

tidier='tidy -i -wrap 9999 -utf8 -q'

function get_news_url() {
	temp=$(mktemp -t x)
	lynx --source ${1} | ${tidier} 2>/dev/null | sed -e '/h2.*a href.*tiede/!d' > ${temp}
	cat ${temp} | sed 's/^.*href="\(.*\)"/http:\/\/yle.fi\1/g' | cut -d'>' -f1 
}

function get_article_data() {
	temp=$(mktemp -t x)
        lynx --source ${1} | ${tidier} 2>/dev/null | sed -n '/<h1>/,/Lähetä/p' > ${temp}
	echo ${temp}
}

function clean_up_article() {
	temp=$(mktemp -t x)
	cat ${1} | sed \
			-e 's/<h1>\(.*\)<\/h1>.*/TITLE: \1/g' \
			-e 's/<p class="published">\(.*\)<\/p>/PUBLISHED: \1/g' \
			-e '/kuuntele/,/<\/div>$/d;/articleaddcomment/d' \
			-e '/h[2-6]/s/<h[2-6]>\(.*\)<\/h[2-6]>/HEADER: \1/g' \
			-e 's/<p>(\(.*\))<\/p>/AUTHOR: \1/g' \
			-e 's/<p>\(.*\)/PARAGRAPH: \1/g' \
			-e 's/(\(.*\))/AUTHOR: \1/g' \
			-e 's/<br \/>//g' \
			-e 's/^[[:blank:]]\{1,\}//g' \
			-e 's/<[^>]*>//g' \
			-e '/^$/d' \
			> ${temp}
	rename_article ${temp}
}

function rename_article() {
	title=$(cat ${1} | sed '/TITLE: /!d;s///g;s/ /_/g' | tr [[:upper:]] [[:lower:]])
	timestamp=$(cat ${1} | sed -e '/PUBLISHED: /!d;s/.*\([0-9]\{2\}\).\([0-9]\{2\}\).\([0-9]\{4\}\).*/\3\2\1/g')
	filename=nl_${timestamp}_${title}.txt
	mv ${1} ${filename}
	echo ${filename}
}

news=$(get_news_url http://yle.fi/radio1/tiede/nuntii_latini)

for url in ${news}; do
	article=$(get_article_data ${url})
	clean_up_article ${article}
done

echo "Tokens in corpora: $(cat nl_*.txt | deroff -w | egrep -v 'AUTHOR|PUBLISHED|PARAGRAPH|HEADER|TITLE' | wc -l)"
echo "Corpora size: $(du -hsc nl_*.txt | grep total)"

exit 0
