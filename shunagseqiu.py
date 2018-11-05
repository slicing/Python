# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:56:52 2017

@author: Sun Yongjiao
"""
#双色球信息
from bs4 import BeautifulSoup
import requests
import re

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
def spride():
    for i in range(1,10):
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' +str(i)+'.html'
        data = requests.get(url,headers = headers)
        soup = BeautifulSoup(data.text,'lxml')
        tags = soup.find_all('tr',attrs={})
        for tag in tags:
            if(tag.find('em')):
                tagtd = tag.find_all('td')
                data = tagtd[0].get_text()
                order = tagtd[1].get_text()
                tagem = tag.find_all('em')
                red1 = tagem[0].get_text()
                red2 = tagem[1].get_text()
                red3 = tagem[2].get_text()
                red4 = tagem[3].get_text()
                red5 = tagem[4].get_text()
                red6 = tagem[5].get_text()
                blue = tagem[6].get_text()
                money = tagtd[3].find('strong').get_text()
                firstprize = tagtd[4].find('strong').get_text()
                secondprize = tagtd[5].find('strong').get_text()
                with open(r'C:\Users\Sun Yongjiao\Desktop\ssq\ss.txt','a') as f:
                    f.write('%s %s \t %s %s %s %s %s %s %s \t %s \t %s %s \n' % (data,order,red1,red2,red3,red4,red5,red6,blue,money,firstprize,secondprize))
                    f.close()
            

spride()

