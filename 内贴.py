# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:18:36 2017

@author: Sun Yongjiao


"""
#爬取内涵段子吧

import urllib.request
import re
class Spider:
    '''
    内涵段子吧 一个 爬虫类
    '''
    def __init__(self):
            self.enable = True
            self.page = 1
            
            
    def load_page(self,page):
        '''
        发送url,得到html原码
        '''
        
        url = "https://tieba.baidu.com/f/good?kw=%E5%86%85%E6%B6%B5%E6%AE%B5%E5%AD%90&ie=utf-8&cid=0&pn="+ str(page)*50 +".html"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"
        headers = {"User_Agent":user_agent}
        req = urllib.request.Request(url,headers = headers)
        response = urllib.request.urlopen(req)
        html = response.read()
        html = html.strip().decode('gbk')
        print(html)
        pattern = re.compile(r'<div.*?class ="f18 mb20">(.*?)(.*?)</div>',re.S)
        item_list = re.findall(pattern,html)
        print(item_list)
        return item_list
    
    
    def deal_one_page(self,item_list,text):
        '''
        处理一页数据
        '''
        print(item_list)
        print(" *************第 %d 页 的段子有 以下*******" %(text))
        print("正在存储 第%d页的段子..." %(text))
        for item in item_list:
            print(222)
            print (item.replace("<p>","").replace("</p>","").replace("<br />",""))
            self.write_to_file(item)
        print("第%d页的段子存储完毕..." %(text))
            
            
    def write_to_file(self,text):
        
        print(text)
        f = open('mystory.txt','a')
        f.write(text)
        f.write('-------------------------------')
        f.close()
        
    def do_work(self):
        '''
        提供跟用户交互的过程
        '''
        while self.enable:
            print ("按回车继续")
            print("输入quit退出")
            command = input()
            if(command == "quit"):
                self.enable = False
                break;
            item_list = self.load_page(self.page)
            self.page += 1
            self.deal_one_page(item_list,self.page)
            self.page +=1
    

if __name__ == "__main__":
    #创建一个spider对象
    mySpider = Spider()
    mySpider.do_work()
        
    