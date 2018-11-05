# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:27:18 2017

@author: Sun Yongjiao
"""

from bs4 import BeautifulSoup
import requests

  #url = 'http://bj.xiaozhu.com/fangzi/4637053514.html'  

def get_sex(class_name):
    if class_name == 'member_ico':
        return '男'
    if class_name == 'member_ico1':
        return '女'
def zufang(url):
    wb_data = requests.get(url)#发起requests请求
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select(' div.pho_info > h4 > em')[0].text
    add = soup.select(' div.pho_info > p > span')[0].text
    picer = soup.select(' div.day_l > span')[0].text
    img = soup.select('#curBigImage')[0].get('src')
    people = soup.select(' div.w_240 > h6 > a')[0].text
    pimg = soup.select(' div.member_pic > a > img')[0].get('src')
    psex = soup.select(' div.member_pic > div')[0].get('class')
    print(add)
    data = {
            'title' : title,
            'add' : add,
            'picer' :picer,
            'img' : img,
            'people' : people,
            'pimg' : pimg,
            'psex' : get_sex(psex),
            }
    print (data)
    write_to_file(data)
    
def write_to_file(self,text):
    f = open('./zufang.text','a')
    f.write(text)
    f.write('------------------------')
    f.close()

page_link = [] # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~

def get_page_link(page_number):
    for each_number in range(1,page_number): # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        links = soup.select('.resule_img_a').fiand_all('herf')
        #page_list > ul > li:nth-child(1) > a
        print(links)
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为resule_img_a 的 a 标签即可

            #page_list > ul > li:nth-child(1) > a
            #page_list > ul > li:nth-child(2) > a
            page_link.append(link)
    for url in page_link:
        #url = soup.select('page_list > ul > li:nth-child(1) > a')
        zufang(url)

if __name__ == "__main__":
    page_number = input("请输入页码:")
    get_page_link(int(page_number))
    