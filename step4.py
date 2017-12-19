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


