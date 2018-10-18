# _*_  coding : utf-8  _*_

import ctypes
import numpy as np

def call_fortran(n,A, libname):
    f = np.ctypeslib.load_library("./"+libname, ".")
    # .argtypes => karg type
    #f.HELLO_FROM_FORTRAN.argtypes = [
    f.hello_from_fortran_.argtypes = [
        ctypes.POINTER(ctypes.c_int32), 
        np.ctypeslib.ndpointer(dtype=np.float64)
        ]
    #f.HELLO_FROM_FORTRAN.restype = ctypes.c_void_p # return arg type
    f.hello_from_fortran_.restype = ctypes.c_void_p # return arg type

    fn = ctypes.byref(ctypes.c_int32(n))  # sed const as a pointor 

    #f.HELLO_FROM_FORTRAN(fn, A)
    f.hello_from_fortran_(fn, A)

print("     #### calling fortran module from main.py  ####")

libname='libfort.so'
n = 3
A = np.identity(n, dtype=np.float64)

print()
print("     #### Write from Pyton ####")
print(n)
print(A)
print()

print("     #### call_fortran ###")
call_fortran(n,A, libname)
