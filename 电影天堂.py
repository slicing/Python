# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:55:57 2017

@author: Sun Yongjiao
"""
#电影天堂
import requests
import re,time

for ii in range(1,10):
    print('正在打印第%d页:' % ii)
    a_url='http://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(ii)+'.html'
    a_html= requests.get(a_url)
    a_html.encoding='gb2312'
    detil=re.findall('<a href="(.*?)" class="ulink">',a_html.text)
    for j in detil:
        time.sleep(2)
        b_url='http://www.ygdy8.net'+j
        b_html=requests.get(b_url)
        b_html.encoding='gb2312'
        b_detil=re.findall('<a href="(.*?)">.*?</a></td>',b_html.text)
        
        try:
            with open(r'C:\Users\Sun Yongjiao\Desktop\ddtt\dt.txt','a',encoding='utf-8') as f:
                print(b_detil[0])
                f.write(b_detil[0]+'\n')
                f.close
        except:
            print('这一页没有匹配到')
        
