# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:44:42 2017

@author: Sun Yongjiao
"""
def enercy(pt,key):
    array= [""]*key
    
    for x in range(0,len(pt)):
        row=x%key
        array[row]+=pt[x]
        print(array)
    cp = ""
    for x in array:
        cp+=x
    return cp
def decode(pt):
    array = ""
    t=(len(pt)+1)/2
    
    t = int(t)
    print(t)
    if(len(pt)%2==0):
        for x in range(0,t):
            array+=pt[x]
            array+=pt[t+x]
            print(array)
    else:
        for x in range(0,t-1):
            array+=pt[x]
            array+=pt[t+x]
            print(array)
        array+=pt[t-1]
        
    return array
if __name__ == "__main__":
    pt = input("plaintxt:")
    key = 2
    ciphertxt = enercy(pt,key)
    plaintxt = decode(ciphertxt)
    print(ciphertxt)
    print(plaintxt)