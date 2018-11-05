# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:23:50 2017

@author: Sun Yongjiao
"""
import urllib.request

def load_page(url):
    '''
        发送URL请求
        
    '''
    user_agent="Mozilla/5.0(compatible;MSIE 9.0;Windows NT 6.1; Trident/5.0;"
    headers = {"User_Agent":user_agent}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    #new_html = html.decode("gbk").encode("utf-8")
    print(html)
    return html
def write_to_file(file_name,txt):
    '''
        将txt文本存入到file_name文件中
    '''
    #打开文件
    f = open(file_name,'wb+')
    
    #读写文件
    f.write(txt)
    print("正在储存文件" +file_name)
    #关闭文件
    f.close()
    


def tieba_spider(url,begin_page,end_page):
    '''
        贴吧爬虫小方法
    '''
    for i in range(begin_page,end_page+1):
        pn = (50*(i-1))
        my_url = url +  str(pn)
        html = load_page(my_url)
        file_name = str(i) + ".html"
        write_to_file(file_name,html)
        


if __name__ == "__main__":
    url= input("请输入贴吧地址")
    begin_page =int ( input("请输入起始页码" ))
    end_page =int ( input("请输入结束页码"))
    tieba_spider(url,begin_page,end_page)