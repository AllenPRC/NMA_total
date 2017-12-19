# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:18:07 2017

@author: Administrator
"""
#进行排序选出最大的值
import numpy as np

Fre = np.load('Fre.npy')
ver_CO = np.load('ver_CO.npy')

data_CO = []

for f, co in zip(Fre,ver_CO):
    ind_co = np.argsort(-co)
    data_CO.append((co[ind_co[:1]],f[ind_co[:1]]))
    
np.save('CO_sorted.npy',data_CO)
   
#筛选最大值占比例大于0.8的数

import numpy as np

CO = np.load('CO_sorted.npy')

CO_08 = []
index = []
for i, x in enumerate(CO):
    if x[0] > 0.8:
        index.append(i)
        CO_08.append(x)
np.save('indi.npy',np.array(index))
np.save('Pro08.npy',np.array(CO_08)[:,1])
