#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:31:48 2018

@author: kimseunghyuck
"""

import numpy as np
x=np.array([0,1])       #입력값
w=np.array([.5, .5])    #가중치값
b=.7
w*x
np.sum(w*x)
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([1,1])
    b=-1.5
    tmp=np.sum(w*x)+b
    return(int(tmp>0))

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-1,-1])
    b=1.5
    tmp=np.sum(w*x)+b
    return(int(tmp>0))

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([1,1])
    b=0
    tmp=np.sum(w*x)+b
    return(int(tmp>0))
     
def XOR(x1,x2):
    x=np.array([NAND(x1,x2), OR(x1,x2)])
    w=np.array([1,1])
    b=-1.5
    tmp=np.sum(w*x)+b    
    return(int(tmp>0))

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
print("XOR")
for i in lst:
    print(XOR(i[0], i[1]))