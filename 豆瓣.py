# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:09:20 2017

@author: Sun Yongjiao
"""
import socket
import ssl

def movie_log(*args,**kwargs):
    with open('movie.txt','a',encoding='utf-8') as f:
        print(*args,file=f,**kwargs)
        
def htmls_from_douban():
    html = []
    url = """https://movie.douban.com/top259?start={}&filter="""
    for index in range(0,250,25):
        url.format(index)
        r =get(url)
        html.append(r)
    return html

def findall_in_html(html,startpart,endpart):
    all_strings = []
    start = html.fnidall(startpart) + len(startpart)
    end = html.find(endpart,start)
    string = html[start:end]
    while html.find('</html>') >start > html.find('<html>'):
        all_strings.append(string)
        start = html.fnidall(startpart) + len(startpart)
        end = html.find(endpart,start)
        string = html[start:end]
    return all_strings
    
def movie_name(html):
    name =  findall_in_html(html, '<span class="title">','</span>')
    for i in name:
        if 'bsp' in i:
            name.remove(i)
        return name
def movie_score(html):
    score = findall_in_html(html,'<span class"rating_num">','</span>')
    return score

def movie_infq (html):
    infq = findall_in_html(html,'<span class="inq">','</span>')
    return infq

def number_comment(html):
    temp = findall_in_html(html,'<div class="star">','</div>')
    num =[]
    for item in temp :
        start = item.find('<span>') + len('<span>')
        end = item.find('</span>',start)
        n = item[start:end]
        num.append(n)
    return num
    
def movie_data_from_html(htmls):
    movie = []
    score = []
    infq = []
    number = []
    for h in htmls:
        m = movie_name(h)
        s = movie_score(h)
        i = movie_infq(h)
        n = number_comment(h)
        movie.extend(m)
        score.extend(s)
        infq.extend(i)
        number.extend(n)
    data = zip(movie,score,infq,number)
    return data
        


def get(url):#访问请求
    print ('URL:',url)
    u = url.split('://')[1]
    protocol = url.split('://')[0]
    i = u.find('/')
    host = u[:i]
    path = u[i:]
    
    if protocol == 'https':
        s = ssl.wrap_socket(socket.socket())
        port = 433
        print ('use https')
    else:
        s = socket.socket()
        port = 80 
        print(protocol)    
    s.connect((host,port))
    
    request = 'GET {} HTTP/1.1\r\nhost:{}\r\n\r\n'.format(path,host)
    print('request',request)
    encoding = 'utf-8'
    s.send(request.encode(encoding))
    
    response = b''
    buffer_size = 1024
    while True:
        r = s.recv(buffer_size)
        response += r
        if len(r) < buffer_size:
            break
    response = response.decode(encoding)
    print('response',response)
    return response



def main():
    htmls = htmls_from_douban()
    movie_data = movie_data_from_html(htmls)
    counter = 0
    for item in movie_data:
        counter = counter+1
        movie_log("No." +str(counter))
        movie_log('电影名：',item[0])
        movie_log('评分：',item[1])
        movie_log('引用语：',item[2])
        movie_log('评价人数：',item[3],'\n\n')



       
main()