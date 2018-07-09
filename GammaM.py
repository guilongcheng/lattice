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

