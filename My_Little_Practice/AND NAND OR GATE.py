#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:51:35 2018

@author: kimseunghyuck
"""

def AND(a,b):
    theta=1.5
    w1=1;w2=1
    res=w1*a+w2*b>theta
    return(int(res))

def NAND(a,b):
    theta=-1.5
    w1=-1;w2=-1
    res=w1*a+w2*b>theta
    return(int(res))

def OR(a,b):
    theta=.5
    w1=1;w2=1
    res=w1*a+w2*b>theta
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
