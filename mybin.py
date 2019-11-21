import html.parser
import urllib.request
import urllib.parse
import json

agent = {'User-Agent':
         "Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


def getWord(to_translate):
    base_link = "https://bin.arnastofnun.is/api/beygingarmynd/%s"
    to_translate = urllib.parse.quote(to_translate.lower())
    link = base_link % (to_translate)
    request = urllib.request.Request(link, headers=agent)
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode('utf-8'))
    return data[0]['ord'] if type(data) == 'list' else to_translate
