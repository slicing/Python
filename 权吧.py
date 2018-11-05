# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:34:50 2017

@author: Sun Yongjiao
"""

from bs4 import BeautifulSoup
import requests


def spride():
    for i in range(2):
        page = str(i*50)
        print(page)
        url = 'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%88%A9%E7%9A%84%E6%B8%B8%E6%88%8F&ie=utf-8&pn='+'page'
        wd_data = requests.get(url)
        soup = BeautifulSoup(wd_data.text,'lxml')
        contents = soup.select('div > div > div.threadlist_lz.clearfix > div.threadlist_title.pull_left.j_th_tit > a')
        authors = soup.select(' div > div > span > span > a')
        outtimes = soup.select('div > div > span.threadlist_reply_date.pull_right.j_reply_data')
        for content,author,outtime in zip(contents,authors,outtimes):
            data = {
                    'content' : content.get_text(),
                    'author' : author.get_text(),
                    'outtime' : outtime.get_text()
                    }
            print(data)
            file_name = '权利的游戏.txt'
            with open (file_name,'w') as f:
                    f.write(data)
                    f.close()
    
    
            


if __name__ =='__main__':
    spride()