#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:36:01 2017

@author: chengch
"""
import os
import numpy as np

def read_xyz(fname):
    with open(fname, 'r') as fh:
        natoms = 27
        coord = np.zeros([27,3])
        fh.readline()
        for ia in range(natoms):
            coord[ia] = [float(x) for x in fh.readline().split()[1:]]
        return coord

def get_len_HB(coord):
    natoms = len(coord)
    n_water_mols = (natoms - 12 ) // 3
    coord_water = np.zeros([n_water_mols, 3, 3])
    for iw in range(n_water_mols):
        coord_water[iw] = coord[12+iw*3:15+iw*3]
    
    coord_O6 = coord[5]
    coord_H8 = coord[7]
    len_HBs = np.zeros(5)
    # first the three shortest O6-H HBs 
    dists = coord_water[:,1:,:] - coord_O6
    dists = np.sum(dists*dists, axis=-1)
    dists = np.sqrt(dists)
    dist = np.min(dists, axis=-1)
    len_HBs[:3] = np.sort(dist)[:3]

    # for H8-O HBs
    dist = coord_water[:,0,:] - coord_H8
    dist = np.sum(dist*dist, axis=-1)
    dist = np.sqrt(dist)
    len_HBs[3:] = np.sort(dist)[:2]
    return len_HBs

def get_len_CB(coord):
    # get the covalent lengths
    a1 = np.array([2,5,5,7,7]) - 1 # atomic indicies 
    a2 = np.array([5,6,7,8,9]) - 1
    coord_a1 = coord[a1]
    coord_a2 = coord[a2]
    dists = coord_a1 - coord_a2
    dists = np.sum(dists*dists, axis=-1)
    return np.sqrt(dists)

def get_angles(coord):
    # get bond angles
    a1 = np.array([2,2,6,5,5,8]) - 1
    a2 = np.array([5,5,5,7,7,7]) - 1
    a3 = np.array([6,7,7,8,9,9]) - 1
    coord_a1 = coord[a1]
    coord_a2 = coord[a2]
    coord_a3 = coord[a3]
    v21 = coord_a1 - coord_a2
    v23 = coord_a3 - coord_a2
    l21 = np.sqrt(np.sum(v21*v21, axis=-1))
    l23 = np.sqrt(np.sum(v23*v23, axis=-1))
    v21_dot_v23 = np.sum(v21*v23, axis=-1)
    cos = v21_dot_v23 / (l21 * l23)
    return np.arccos(cos) / np.pi * 180.

def dihedral2(p):
    b = p[:-1] - p[1:]
    b[0] *= -1
    v = np.array(
        [v - (v.dot(b[1])/b[1].dot(b[1])) * b[1] for v in [b[0], b[2]]]
            )
    v /= np.sqrt(np.einsum('...i,...i', v, v)).reshape(-1,1)
    b1 = b[1] / np.linalg.norm(b[1])
    x = np.dot(v[0], v[1])
    m = np.cross(v[0], b1)
    y = np.dot(m, v[1])
    return np.degrees(np.arctan2(y,x))

def get_dihedrals(coord):
    # use the atan2 version from
    #   https://stackoverflow.com/questions/20305272/dihedral-torsion-angle-from-four-points-in-cartesian-coordinates-in-python
    a1 = np.array([2,2,6,6]) - 1
    a2 = np.array([5,5,5,5]) - 1
    a3 = np.array([7,7,7,7]) - 1
    a4 = np.array([9,8,9,8]) - 1
    dihedrals = []
    for i in range(4):
        p = np.zeros([4,3])
        p[0] = coord[a1[i]]
        p[1] = coord[a2[i]]
        p[2] = coord[a3[i]]
        p[3] = coord[a4[i]]
        dihedrals.append(dihedral2(p))

    return np.array(dihedrals)

params = []

Stand_xyz = np.load('/home/chengch/Stand_xyz.npy')
for f_xyz in Stand_xyz:    
    coord = f_xyz
    HBs = get_len_HB(coord)
    CBs = get_len_CB(coord)
    angles = get_angles(coord)
    dihedrals = get_dihedrals(coord)
    params.append(np.concatenate(
        (HBs, CBs, angles, dihedrals)
        ))
np.save('Params.npy',params)