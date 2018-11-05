# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:54:30 2017

@author: Sun Yongjiao
"""

from bs4 import BeautifulSoup
import requests
import time,re

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
def spride(url):
    response = requests.get(url,headers = headers)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    word = soup.find_all('div',attrs={'class':'read-content j_readContent'})[0]
    words = word.find_all('p',attrs={})
    title = re.findall(r'<h3 class="j_chapterName">(.*?)</h3>',html)[0]
    time.sleep(2)
    with open (file_name,'a') as f:
        f.write('\t\t\t\t----------------------------------------------\n')
        f.write('\t\t\t\t\t\t'+title+'\n')
        f.close()
    for word in words:
        word = word.get_text()
        with open (file_name,'a') as f:
            f.write(word+'\n')
    
    next_url = soup.find_all('a',attrs={'data-eid':'qd_R109'})[0]['href']
    if next_url:
        next_url = 'https:' +next_url
        spride(next_url)
    else:
       print('下载结束')
if __name__ =='__main__':
    url = 'https://read.qidian.com/chapter/9CsFD4KyZlcmPxgcqNL9uQ2/rhaZPk2khyBp4rPq4Fd4KQ2'
    response = requests.get(url,headers = headers)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    name = re.findall(r'<h1>(.*?)</h1>',html)[0]
    autor = re.findall(r'<h2><a href=".*?">(.*?)</a>.*?</h2>',html)[0]
    print(name,autor)
    file_name = r'C:\Users\Sun Yongjiao\Desktop\小说\\'+name+'.txt'
    with open (file_name,'a') as f:
        f.write('\n\t\t\t\t\t'+name+'\t'+autor+'\n')
        f.close()
    spride(url)