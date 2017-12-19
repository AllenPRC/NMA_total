# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:18:07 2017

@author: Administrator
"""

import numpy as np

Fre = np.load('Fre.npy')
ver_CO = np.load('ver_CO.npy')

data_CO = []

for f, co in zip(Fre,ver_CO):
    ind_co = np.argsort(-co)
    data_CO.append((co[ind_co[:1]],f[ind_co[:1]]))
    
np.save('CO_sorted.npy',data_CO)
    
