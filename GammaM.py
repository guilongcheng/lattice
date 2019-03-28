#!/bin/env python
import numpy as np
from scipy import sparse


row = np.array([0,1,2,3])
col = np.array([3,2,1,0])
data = np.array([-1j,-1j,1j,1j])
gamma1 = sparse.csr_matrix((data, (row, col)),shape=(4,4)).toarray()

row = np.array([0,1,2,3])
col = np.array([3,2,1,0])
data = np.array([-1,1,1,-1])
gamma2 = sparse.csr_matrix((data, (row, col)),shape=(4,4)).toarray()

row = np.array([0,1,2,3])
col = np.array([2,3,0,1])
data = np.array([-1j,1j,1j,-1j])
gamma3 = sparse.csr_matrix((data, (row, col)),shape=(4,4)).toarray()

row = np.array([0,1,2,3])
col = np.array([2,3,0,1])
data = np.array([-1,-1,-1,-1])
gamma4 = sparse.csr_matrix((data, (row, col)),shape=(4,4)).toarray()

row = np.array([0,1,2,3])
col = np.array([0,1,2,3])
data = np.array([1,1,-1,-1])
gamma5 = sparse.csr_matrix((data, (row, col)),shape=(4,4)).toarray()

gamma51=np.dot(gamma5,gamma1)
gamma52=np.dot(gamma5,gamma2)
gamma53=np.dot(gamma5,gamma3)
gamma54=np.dot(gamma5,gamma4)

gamma5i = np.zeros((4,4,4),dtype="c16")
gammai = np.zeros((4,4,4),dtype="c16")

gamma5i[0]=gamma51
gamma5i[1]=gamma52
gamma5i[2]=gamma53
gamma5i[3]=gamma54

gammai[0]=gamma5
gammai[1]=gamma1
gammai[2]=gamma2
gammai[3]=gamma3
