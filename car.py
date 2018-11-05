# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:20:20 2017

@author: Sun Yongjiao
"""

#汽车之家
import requests
import re,time
first_url = "https://car.autohome.com.cn/photo/series/31067/1/3963415.html"
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
def save_img(first_url):
    response =  requests.get(first_url,headers=headers)
    html = response.text
    img_ele = re.findall(r'<img id="img"..*?>',html)[0]
    img_url = re.findall(r'src="(.*?)"',img_ele)[0]
    print(img_url)
    time.sleep(2)
    #img_res = requests.get('http:'+img_url)
    #img_file_name = img_url.split('/')[-1]  
    '''with open(img_file_name,'wb') as f:
        f.write(img_res.content)
    next_url = re.findall(r"nexturl = '(.*?)'",html)
    if next_url:
        next_url = "https://car.autohome.com.cn"+next_url[0]
        save_img(next_url)
        
    else:
        print('结束了！')
    '''
    
save_img(first_url)