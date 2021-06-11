import time
import requests
import json
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import re
import numpy as np
from PIL import Image

url = "https://money.udn.com/search/result/1001/缺水%20缺電/"
title_arr = []
href_arr = []
content = []
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
for pg_nu in range(1,10):
    url = "https://money.udn.com/search/result/1001/缺水%20缺電/"+str(pg_nu)
    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    page = soup.find_all(name='dt')
    for i in page[73:93]:
        news_title = i.find(name='h3')
        if news_title:
            title_arr.append(news_title)
            link = i.find(name='a')
            href = link.get('href')
            href_arr.append(href)
            print("news_title:",news_title.text)
            print("href:",href)
for i in href_arr:
    response = requests.get(i,headers=headers)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    page = soup.find(id='article_body')
    p = page.select('p')
    for i in p:
        if type(i.string)!=type(None):
            content.append(i.string.strip())
            print('content:',i.string)
