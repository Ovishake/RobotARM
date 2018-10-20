#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:30:06 2018

@author: avishek
"""

import numpy as np
import matplotlib.pyplot as plt

l1 = 10
l2 = 20
l3 = 30


t1 = 10
t2 = 70
t3 = 80



t1 = (t1/180.0)*np.pi
t2 = (t2/180.0)*np.pi


for t1 in np.arange(0, 6.28, 0.5):
    for t2 in np.arange(0, 6.28, 0.5):
        for t3 in np.arange(0, 6.28, 0.5):
            """ because 2*pi is 6.28"""

            r0_1 = [[np.cos(t1), -np.sin(t1),0],[np.sin(t1),np.cos(t1),0]]
            r1_2 = [[np.cos(t2), -np.sin(t2),0],[np.sin(t2),np.cos(t2),0]]
            r2_3 = [[np.cos(t3), -np.sin(t3),0],[np.sin(t3),np.cos(t3),0]]
            
            r0_2 = np.cross(r0_1, r1_2)
            r0_3 = np.cross(r0_2, r2_3)
            r0_1 = np.concatenate((r0_1,[[0,0,1]]),0)
            
            d0_1 = [[l1],[0],[1]]
            d1_2 = [[l2],[0],[1]]
            d2_3 = [[l3],[0],[1]]
            
            h0_1 = np.concatenate((r0_1,d0_1),1)
            h0_1 = np.concatenate((h0_1,[[0,0,0,1]]),0)
            r1_2 = np.concatenate((r1_2,[[0,0,1]]),0)
            h1_2 = np.concatenate((r1_2,d1_2),1)
            h1_2 = np.concatenate((h1_2,[[0,0,0,1]]),0)
            h0_2 = np.dot(h0_1, h1_2)
            r2_3 = np.concatenate((r2_3,[[0,0,1]]),0)
            h2_3 = np.concatenate((r2_3,d2_3),1)
            h2_3 = np.concatenate((h2_3,[[0,0,0,1]]),0)
            h0_3 = np.dot(h0_2,h2_3)
            plt.plot([0, h0_1[0,3],h0_2[0,3],h0_3[0,3]],[0,h0_1[1,3],h0_2[1,3],h0_3[1,3]])
            