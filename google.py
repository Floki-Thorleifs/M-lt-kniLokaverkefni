import sys
import html.parser
import urllib.request
import urllib.parse
import re

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

# Þýðingar fall: Tekur inn orðið sem á að þýða, upprunalegt tungumál og
# tungumál sem á að þýða yfir í.


def translate(to_translate, to_language, from_language):
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    to_translate = urllib.parse.quote(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    request = urllib.request.Request(link, headers=agent)
    raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    parser = html.parser.HTMLParser()
    return (parser.unescape(re_result)[0])
