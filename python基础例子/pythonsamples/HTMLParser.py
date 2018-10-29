#coding=utf-8
#HTMLParser
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：


from html.parser import HTMLParser
from html.entities import name2codepoint

##lxml 是一个优美的扩展库，用来快速解析XML以及HTML文档 即使所处理的标签非常混乱。
#我们也将使用 Requests 模块取代内建的urllib2模块，因为其速度更快而且可读性更好。您可以通过使用 pip install lxml 与 pip install requests 命令来安装这两个模块。
import requests
from lxml import html

class MyHTMLParser(HTMLParser):
    def __init__(self):
        mySelectValue=[{"会议时间":"","名称":"","地点":""}]
 
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data.encode('utf-8'))

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

# 小结
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。

#tree 现在包含了整个HTML文件到一个优雅的树结构中，我们可以使用两种 方法访问：XPath以及CSS选择器。在这个例子中，我们将选择前者。

# <li>
#                         <h3 class="event-title"><a href="/events/python-events/763/">PyCode Conference 2018</a></h3>
#                         <p>
                            
                            
# <time datetime="2018-10-01T00:00:00+00:00">01 Oct. – 03 Oct. <span class="say-no-more"> 2018</span></time>

                            

                            
#                             <span class="event-location">Warsaw, Poland</span>
                            
#                         </p>
#                     </li>
import requests
from lxml import html
def fetchWebData(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    # print(tree)
    titles=tree.xpath('//h3[@class="event-title"]/a/text()')
    times=tree.xpath('//h3/../p/time/@datetime')
    locations=tree.xpath('//span[@class="event-location"]/text()')
    processdata=map(lambda x,y,z:{'event-title':x,'event-time':y,'event-location':z} ,titles,times,locations)
    for n in processdata:
        print (n)

fetchWebData('https://www.python.org/events/python-events/')

# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
# request.urlopen('http://www.python.org/')

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<head>
    ...
    <style>
    .jan {
        background-color: yellow;
    }
    ...
    .month {
        color: red;
    }
    </style>
</head>

<body>
...
<ul>
    <li class="month">一月</li>
    <ul class="jan">
        <li>一月一号</li>
        <li>一月二号</li>
        <li>一月三号</li>
    </ul>
    ...
</ul>
</body>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, features='lxml')
# print(soup.prettify())
print(soup.p)
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)


jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')              # use jan as a parent
for d in d_jan:
    print(d.get_text())

"""
一月一号
一月二号
一月三号
"""
import re


html = requests.get("https://morvanzhou.github.io/static/scraping/table.html")
soup = BeautifulSoup(html.text, features='lxml')
print(soup.prettify())
img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])


