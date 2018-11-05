# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:29:15 2017

@author: Sun Yongjiao
"""
#图书排名
from atexit import register
from  re import compile
from threading import  Thread#线程python3 没有
from time import ctime
from urllib import urlopen as uopen

REGEX = compile('#([\d,]+) in Books') 
AMZN = 'http://amazon.com/dp/'
ISBNs = {
        '0132269937' : 'Core python programming',
        '0132356139' : 'python web development with Django',
        '0137143419' : 'python fundamentals',
        }
def getranking(isbn):
    page = uopen('%s%s' %(AMZN,isbn)) 
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print('-%r ranked %s' %(ISBNs[isbn]),getranking(isbn))
    
def _main():
    print('At',ctime(), 'on Amazon...')
    for isbn in  ISBNs:
        _showRanking(isbn)
@register
def _atexit():
    print('all DONE at:',ctime())
    
if __name__ == '__main__':
    _main()