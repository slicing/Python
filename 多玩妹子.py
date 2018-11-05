# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 00:35:43 2017

@author: Sun Yongjiao
"""

import requests
import re
import time
import json
import os

def strip(path):
    path = re.sub(r'[?\\*|"<>:/]','',str(path))
    return path


class Spider:
    def __init__(self):
        self.session = requests.Session()
        
    def download(self,url):
        response = self.session.get(url)
        try:
            return response
        except Exception as e:
            print(e)
            
    def run(self,start_url):
        img_ids = self.get_img_item_ids(start_url)
        for img_id in img_ids:
            img_item_info = self.get_img_item_nfo(img_id)
            self.save_img(img_item_info)
    
    
    def get_img_item_ids(self,start_url):
        response = self.download(start_url)
        if response:
            html = response.text
            ids = re.findall(r'http://tu.duowan.com/gallery/(\d+).html',html)
            return set(ids)
    
    
    def get_img_item_nfo(self,img_id):
        img_item_url = "http://tu.duowan.com/index.php?r=show/getByGallery/&gid=%s&_=%s"%(img_id,time)
        response = self.download(img_item_url)
        if response:
            return json.loads(response.text)
        
    #根据套图的信息持久化
    def save_img(self,img_item_info):
        dir_name = strip(img_item_info['gallery_title'].strip())
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        for img_info in img_item_info['picInfo']:
            img_name = strip(img_info['title'].strip())
            img_url = img_info['url']
            pix = (img_url.split('/')[-1]).split('.')[-1]
            img_path = os.path.join(dir_name,"%s,%s"% (img_name,pix))
            if not os.path.exists(img_path):
                response = self.download(img_url)
                if response:
                    img_data = response.contant
                    with open (img_path,'wb') as f:
                        f.write(img_data)
                        
                        
if __name__ == '__main__':
    spider = Spider
    #start_url = 'http://tu.duowan.com/m/meinv'
    spider.run('http://tu.duowan.com/m/meinv')