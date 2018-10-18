# FPython
example of fortran module to call within python
 
 even in ifort, dont have to use DLLEXPORT
 but in main.py, should be large letter and attaching _ after module

  e.g. 
    subroutine hello_from_fortran (fortran program)

    ==> f.HELLO_FROM_FORTRAN_(*kargs)

 compile option
 ifort -fPIC -shared -o libfort.so test.f90
