#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import re

import requests
from bs4 import BeautifulSoup

from Joke_config import *


def gethtml():
    proxy = {
        'http':'221.182.133.232:1748'
    }
    try:
        response = requests.get(URL,HEADERS)
        response.encoding = 'gbk'
        if response.status_code == 200:
            return response.text
    except:
        print('请求失败')
def pansehtml(html):
    soup = BeautifulSoup(html, 'lxml')


    title = soup.select('body > div > div.main > ul > li.article-summary > span > a')
    source = soup.select('body > div > div.main > ul > li.article-summary > div.article-source > span')
    content = soup.select('body > div > div.main > ul > li.article-summary > div.summary-text > p')

    for i in range(len(title)):
        print(re.sub('[a-zA-Z<>/]', '', str(title[i])))
    for i in range(len(source)):
        print(str(source[i]).strip('<span></span>'))
    for i in range(len(content)):
        print(str(content[i]).strip('<p></p>'))


def main():
    html = gethtml()
    pansehtml(html)


main()