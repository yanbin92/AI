import re
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from html.entities import name2codepoint

from lxml import html

#让我们的爬虫从 “网络爬虫” 这一页开始爬, 然后在页面中寻找其他页面的信息, 然后爬去其他页面, 然后循环这么做, 看看最后我们的爬虫到底爬去了哪.

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'}
html = requests.get(base_url+his[-1],headers=headers)
#<a target="_blank" href="/item/%E8%9C%98%E8%9B%9B/8135707" data-lemmaid="8135707">蜘蛛</a>
#https://baike.baidu.com/item/%E8%9A%82%E8%9A%81/9770178
soup = BeautifulSoup(html.text, features='lxml')


print(soup.find('h1').get_text(),
 '    url: ', his[-1])
# 网络爬虫     url:  /item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711

sub_urls = soup.find_all("a",
 {"target": "_blank",        #%E8
  "href": re.compile("/item/(%.{2})+$")})
import random
# print(sub_urls)
# if len(sub_urls) != 0:
#   #从指定序列中随机获取k个元素作为一个片段返回，sample函数不会修改原有序列。
#     his.append(random.sample(sub_urls, 1)[0]['href'])
# else:
#     # no valid sub link found
#     his.pop()

#有了这套体系, 我们就能把它放在一个 for loop 中, 让它在各种不同的网页中跳来跳去.

for i in range(20):
    url = base_url + his[-1]
    
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'}
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text, features='lxml')

    print(i, soup.find('h1').get_text().encode('utf-8'), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()