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
