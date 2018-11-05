# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:05:35 2017

@author: Sun Yongjiao
"""

#爬取喜马拉雅
import json 
import random
import time
import pymongo
from lxml import etree
from bs4 import BeautifulSoup
import requests

clients = pymongo.MongoClient('localhost')
db = client["XiMaLaYa"]
col1 = db["content"]
col2 = db["detail"]

UA_list = []
headers1 = {}
headers2 = {}


def get_url():
    start_urls = ['http://www.ximalaya.com/dq/all/{}'.format(num) for num in range(1,85 )]
    for start_url in start_urls:
        html = requests.get(start_url,headers = headers1).text
        soup = BeautifulSoup(html,'lxml')
        for item in soup.findall(class = "albumfaceOutter"):
            conent = {
                    'herf':item.a['herf'],
                    'title' : item.img['alt'],
                    'img_url' : item.img['src']
                    }
            col1.insert(content)
            print('写入一个频道'+ item.a['herf'])
            print(content)
            get_m4a(item.a['herf'])
        time.sleep(1)
        
        
def get_m4a(url):
    time.sleep(1)
    html = requests.get(url, headers = headers2).text
    numlist = etree.HTML.xpath('')
    
        
    

if __name__ == '__main__':
    get_url()
    #从列表页获取每一个专辑的详情页面
    #在详情页面匹配所有音频的ID
    #通过抓包能够找到mp3的请求地址
    #通过遍历id构造不同的地址  获取不同的mp3的纸质