#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:26:44 2017

@author: chengch
"""

import numpy as np

xyz = np.load('Stand_xyz.npy')
Pro = np.load('Pros.npy')

Vec_sts = []
Vec_vars = []
ver_COs = []
ver_NHs = []

def st_vec(mat1,mat2):
    mat_vec = mat1 - mat2
    data = np.sqrt(sum((mat_vec) ** 2))
    data = mat_vec / data
    return(data)

def var_vec(mat1,mat2):
    data = mat1 - mat2
    return(data)

for isnp in xyz:
    Vec_sts.append((st_vec(isnp[4],isnp[5]),st_vec(isnp[6],isnp[7])))

for isn in Pro:
    Vec_var = []
    for i in isn:
        Vec_var.append((var_vec(i[4],i[5]),var_vec(i[6],i[7])))
    Vec_vars.append(Vec_var)

for st, var in zip(Vec_sts,Vec_vars):
    ver_CO = []
    ver_NH = []
    for v in var:
        data_CO = np.dot(st[0],v[0])
        data_NH = np.dot(st[1],v[1])
        ver_CO.append(data_CO)
        ver_NH.append(data_NH)
    ver_COs.append(ver_CO)
    ver_NHs.append(ver_NH)

ver_COs = np.array(ver_COs)
ver_NHs = np.array(ver_NHs)

np.save('ver_CO.npy',abs(ver_COs))
np.save('ver_NH.npy',abs(ver_NHs))
