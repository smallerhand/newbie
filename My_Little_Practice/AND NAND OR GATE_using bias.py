#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:51:35 2018

@author: kimseunghyuck
"""

def AND(a,b):
    bias=-1.5
    w1=1;w2=1
    res=bias+w1*a+w2*b>0
    return(int(res))

def NAND(a,b):
    bias=1.5
    w1=-1;w2=-1
    res=bias+w1*a+w2*b>0
    return(int(res))

def OR(a,b):
    bias=-.5
    w1=1;w2=1
    res=bias+w1*a+w2*b>0
    return(int(res))

lst=[[0,0], [1,0], [0,1], [1,1]]

print("AND")
for i in lst:
    print(AND(i[0], i[1]))
print("NAND")    
for i in lst:
    print(NAND(i[0], i[1]))
print("OR")
for i in lst:
    print(OR(i[0], i[1]))