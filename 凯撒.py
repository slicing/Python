# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:28:49 2017

@author: Sun Yongjiao
"""

mstr = 'abcdefghijklmnopqrstuvwxz'
lengthM = len(mstr)

def crease(strs,shift):
    newstrs = ''
    for x in strs:
        newX = mstr.index(x)
        newX = (newX+shift)%lengthM
        newstrs = newstrs+mstr[newX]
    return newstrs
if __name__ == '__main__':
    strs = input("输入明文：")
    shift = input("移动位数:")
    shift = int(shift)
    C = crease(strs,shift)
    print("加密后：",C)
    print("解密",crease(C,int(shift)*(-1)))
    