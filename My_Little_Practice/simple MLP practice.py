#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:47:59 2018

@author: kimseunghyuck
"""

#hidden layer 2개
#relu 함수 적용
import numpy as np
def relu(x):
    return(np.maximum(0,x))
x=np.array([.1, .5])
w1=np.array([[.1, .3, .5], [.2,.4,.6]])
b1=np.array([.1, .2, .3])
l1=relu(np.dot(x, w1)+b1)

w2=np.array([[.1, .4], [.2,.5],[.3,.6]])
b2=np.array([.1, .2])
l2=relu(np.dot(l1, w2)+b2)

w3=np.array([[.1, .3], [.2,.4]])
b3=np.array([.1, .2])
y=np.dot(l2, w3)+b2

#sigmoid함수 적용
def sigmoid(x):
    return 1/(1+np.exp(-x))
x=np.array([.1, .5])
w1=np.array([[.1, .3, .5], [.2,.4,.6]])
b1=np.array([.1, .2, .3])
l1=sigmoid(np.dot(x, w1)+b1)

w2=np.array([[.1, .4], [.2,.5],[.3,.6]])
b2=np.array([.1, .2])
l2=sigmoid(np.dot(l1, w2)+b2)

w3=np.array([[.1, .3], [.2,.4]])
b3=np.array([.1, .2])
y=np.dot(l2, w3)+b2