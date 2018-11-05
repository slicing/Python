# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:05:40 2017

@author: Sun Yongjiao
"""

#爬取视频（桌面版）
#语法简介 入门快 



from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
import urllib.request
import requests
import re
import threading





url_name =[]
a=1#页数
def get():
    global a
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
            }
    url = 'http://www.budejie.com/video/'+str(a)
    varl.set('已经下载到第%s页视频'% (a))
    html = requests.get(url,headers = headers).text
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)#编译为增则表达方式
    url_contents = re.findall(url_content,html)
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">'
        url_items = re.findall(url_reg,i)
        if url_items:
            name_reg = re.compile(r'<a herf="/detail-.{8}?.html">(.*?)</a>',re.S)
            name_items = re.findall(name_reg,i)
            for i,k in zip(name_items,url_items):
                url_name.append([i,k])
                print (i,k)
    return url_name()


id = 1
def write():
    global id
    while id<10:
        url_name = get()
        for i in url_name:
            urllib.urlretrieve(i[1],'video\\%s.mp4'%(i[0].decode('utf-8').encode('gbk')))#下载
            text.insert(ttk.END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')
            url_name.pop(0)#删除第一个元素
            id+=1
    varl.set('蘑菇头，视频连接和视频抓取完毕，over!')
    
def start():
    th = threading.Thread(target=write())
    th.start()
    
    
root = tk.Tk()
root.title('视频爬取')
text = scrolledtext.ScrolledText(root,font=('微软雅黑',10))
text.grid()#实现布局
button = ttk.Button(root,text = '开始爬取', command = start)
button.grid()
varl = tk.StringVar()#通过tk绑定一个变量
lable=tk.Label(root,font=('微软雅黑',10),fg='red',textvariable = varl)
lable.grid()
varl.set('熊猫已准备。。。')
root.mainloop()
    
    