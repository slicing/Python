#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib2 import request
#目的：下载盗墓笔记
first_url = "http://www.quanshuwang.com/book/9/9055/"
#访问小说首页面
html = request.urlopen(first_url).read().decode('jdk')
print html

import re   #re模块
string = 'llabcaafabcfa'
res = re.seach('abc',string)
res = re.findall('abc',string)

print res
