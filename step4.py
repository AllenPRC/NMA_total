# 生成反式的索引
import numpy as np

a = np.load('Params.npy')
n = 0
indi = []
for i, x in enumerate(a):
    if (abs(x[16]) > 170) :
        indi.append(i)
        n += 1
print(n)
np.save('indi.npy',indi)

#进行数据清新

import numpy as np
from sys import argv

script, old_data, new_data = argv

ind = np.load('indi.npy')
o_data = np.load(old_data)

n_data = []

for i in ind:
    n_data.append(o_data[i])

np.save(new_data,n_data)

