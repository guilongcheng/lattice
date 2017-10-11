#!/bin/env python
#-*- coding: utf-8 -*-
import time
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
from sympy import LeviCivita
import xarray as xr
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
except ImportError:
    print("matplotlib package not find")
    PackageLost=["matplotlib"]
try:
    import gvar as gv
    import corrfitter as cf
    import lsqfit
except ImportError:
    print("lsqfit package not find")
    PackageLost.append("lsqfit")
try:
    import bottleneck
except ImportError:
    print("bottleneck package not find")
    PackageLost.append("bottleneck")

endian = "<"

typename = np.array(["other", "x", "y", "z", "t", "d", "c", "d2",
                "c2", "complex", "mass", "smear", "displacement",
                "s_01", "s_02", "s_03", "s_11", "s_12", "s_13",
                "d_01", "d_02", "d_03", "d_11", "d_12",
                "d_13", "conf", "operator", "momentum", "direction",
                "t2", "mass2", "column", "row",
                "temporary", "temporary2", "temporary3", "temporary4",
                "errorbar", "operator2", "param",
                "fit_left", "fit_right", "jackknife", "jackknife2",
                "jackknife3", "jackknife4", "summary",
                "channel", "channel2", "eigen", "d_row", "d_col",
                "c_row", "c_col", "parity", "noise",
                "evenodd", "disp_x", "disp_y", "disp_z", "disp_t",
                "t3", "t4", "t_source", "t_current", "t_sink",
                "bootstrap", "nothing"])

HeadType = np.dtype(
    [('head',
      [('n_dims', 'i4'), ('one_dim',
                          [('type', 'i4'), ('n_indices', 'i4'), ('indices', 'i4', 1024)
                           ], 16)
       ])
     ]
)


class Time(object):

    """used to calculate codes run time """

    def __init__(self):
        """ """
        self.time={}

    def start(self, arg1="all"):
        """TODO: Docstring for start.

        :arg1: time name
        :returns: current time

        """
        self.time[arg1] = time.time()

    def end(self, arg1="all",iodata=0,Ncal=0):
        """TODO: Docstring for end.

        :arg1: time name
        :returns: this time name all used times.

        """
        self.time[arg1] = time.time() - self.time[arg1]
        print(20*"=","time")
        print("%s time  used is : %fs"%(arg1, self.time[arg1]))
        if Ncal != 0:
            print("%s Gflops is : %f"%(arg1,Ncal/(1024**3)/self.time[arg1]))
        if iodata != 0:
            print("%s io is %f GB/s"%(arg1,iodata/(1024**3)/self.time[arg1]))
        print(20*"=")

class TwoPointF(xr.Dataset):

    def ReadData(self, filename, coords={},format=""):
        """ReadData from files. filename can be a strings or list
        format can be  npy,npz,io_g(io_general),b(binary),chroma ...

        :filename: TODO
        :format: TODO
        :returns: TODO
        """
        if "io_g" in format:
            head_data = np.fromfile(filename, dtype=HeadType, count=1)[0]
            DataType_ = np.dtype([
                ('head_tmp', 'S102400'),
                ('data', endian + 'f8', tuple(head_data['head']['one_dim']['n_indices']\
                                              [0:head_data['head']['n_dims']]))
            ])
            data = np.fromfile(filename, dtype=DataType_)[0]['data']
            head_data = np.fromfile(filename, dtype=HeadType, count=1)[0]
            n_dims_ = head_data['head']['n_dims']
            type_ = head_data['head']['one_dim']['type'][0:n_dims_]
            typename_ = [typename[i] for i in type_]
            n_indices_ = tuple(head_data['head']['one_dim']['n_indices'][0:n_dims_])
            indices_ = head_data['head']['one_dim']['indices'][0:n_dims_]
            coords_ = {}
            for i in range(n_dims_):
                coords_[typename_[i]] = indices_[i][0:n_indices_[i]]
            self["corr2"] = xr.DataArray(data, coords=coords_, dims=tuple(typename_))
        elif "b" in format:
            if  type(filename) is list:
                pass
        else:
            pass
