
#直接生成库仑矩阵
import numpy as np

list1 = [1,6,1,1,6,8,7,1,6,1,1,1,8,1,1,8,1,1,8,1,1,8,1,1,8,1,1]

xyz_data = np.load('Stand_xyz.npy')

indicies = []
for i, x in zip(range(27),list1):
    for j, y in zip(range(27),list1):
        indicies.append(((i,j), x * y))
indicies = np.array(indicies)

MCs = []  
num = 0
for mo in xyz_data:
    num += 1
    MC = []
    for (x,y), i in indicies:
        if x == y :  
            dat = 0.5 * ((i  ** 0.5 )** 2.4)
            MC.append(dat)
        else:
            dat = (sum((mo[x] - mo[y]) ** 2)) ** 0.5        
            MC.append( i / (dat))
    print (num)
    MC = np.reshape(MC,(27,27))
    MCs.append(MC)
np.save('MCs.npy',np.array(MCs))

#进行排序
import numpy as np

CMs = np.load('CMs.npy')
CMs_sort = []
for i in CMs:
    norm = np.linalg.norm(i,axis=1)
    ind = np.argsort(norm)
    i = i[ind]
    i = i.T
    i = i[ind]
    i = i.T
    i = np.reshape(i,(27 ** 2,))
    CMs_sort.append(i)
CMs_sort = np.array(CMs_sort)
np.save('CMs_sort.npy',CMs_sort)

#生成特征谱
import numpy as np
list1 = [1,6,1,1,6,8,7,1,6,1,1,1,8,1,1,8,1,1,8,1,1,8,1,1,8,1,1]

xyz_data = np.load('../data/xyz_08.npy')

indicies = []
for i, x in zip(range(27),list1):
    for j, y in zip(range(27),list1):
        indicies.append(((i,j), x * y))
indicies = np.array(indicies)

Eig_spe = []  
num = 0
for mo in xyz_data:
    mo = np.reshape(mo,(27,3))
    num += 1
    MD = []
    for (x,y), i in indicies:
        if x == y :  
            dat = 0.5 * ((i  ** 0.5 )** 2.4)
            MD.append(dat)
        else:
            dat = (sum((mo[x] - mo[y]) ** 2)) ** 0.5        
            MD.append( i / (dat))
    print (num)
    MD = np.reshape(MD,(27,27))
    u,v = np.linalg.eig(MD)
    Eig_spe.append(u)
print (np.shape(u))
Eig_spe = np.array(Eig_spe)
np.save('Eig_CM_08.npy',Eig_spe)
