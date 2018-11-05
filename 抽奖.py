# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:02:13 2017

@author: Sun Yongjiao
"""

import random
from tornado import web, httpserver, ioloop


LUCK_NUM = random.randint(1,100)
#业务模块
class IndexHandler(web.RequestHandler):
    def get(self, *arg, **wags):
        #返回页面
        self.render('index.html',luck_num=LUCK_NUM)
        
        #self.write('欢迎来到网络科技协会')
        
class  LotteryHandler(web.RequestHandler):
    def post(self, *arg, **kwargs):
        #接收参数phone,qq
        phone = self.get_argument('phone')
        qq = self.get_argument('qq')
        print(phone,qq)

#配置路由（应用模块）
application = web.Application([(r"/index",IndexHandler),(r"/lottery",LotteryHandler),])

if __name__ =='__main__':
    #socket服务，处理http服务
    #创建一个http服务器
    http_server = httpserver.HTTPServer(application)
    #监听端口
    http_server.listen(8080)
    #服务启动
    ioloop.IOLoop.current().start()



    
