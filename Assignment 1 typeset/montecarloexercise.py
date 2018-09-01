#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:32:43 2018

@author: cpmcintyre
"""
import numpy as np
from numpy.random import choice
from numpy import sort
samplechoice=list(range(1,11))
Results = []
for i in range(100000):
    k=sort(choice(samplechoice,5, replace=False))
    Results.append(k[3])

counts=[0,0,0]
for i in Results:
    if i<8:
        counts[0]+=1.0
    elif i>8:
        counts[2]+=1.0
    else:
        counts[1]+=1.0
        
print((counts[0]/100000, counts[1]/100000, counts[2]/100000))
        