import numpy as np

def newtonrphes_masood66(f,x0,es):
    print("I am Masoodullah Roll no: AP-19066")
    xold = x0
    itr = 1
    error = 100
    while error>es:
        dydx = deriv(f,xold)
        xr=xold-(f(xold)/dydx)
        error=np.abs((xr-xold)*100/xr)
        print('itr no:%d, xold:%0.6f, f(xold):%0.6f, xr:%0.6f, f(xr):%0.6f, error:=%0.6f' 
        %(itr,xold,f(xold),xr,f(xr),error))
        xold=xr
        itr=itr+1
    return(itr-1,xr,error)

def deriv(f,x):
    h=0.00001
    df=(f(x+h)-f(x))/h
    return df

"""
OUTPUT OF NEWTON RAPHSON

f= lambda x: x**3-6*x**2+11*x-6.1

I am Masoodullah Roll no: AP-19066
itr no:1, xold:2.500000, f(xold):-0.475000, xr:0.599886, f(xr):-1.444556, error:=316.745854
itr no:2, xold:0.599886, f(xold):-1.444556, xr:0.895846, f(xr):-0.341982, error:=33.036938
itr no:3, xold:0.895846, f(xold):-0.341982, xr:1.024535, f(xr):-0.052721, error:=12.560695
itr no:4, xold:1.024535, f(xold):-0.052721, xr:1.052963, f(xr):-0.002341, error:=2.699803
itr no:5, xold:1.052963, f(xold):-0.002341, xr:1.054348, f(xr):-0.000005, error:=0.131341
itr no:6, xold:1.054348, f(xold):-0.000005, xr:1.054351, f(xr):0.000000, error:=0.000305
(6, 1.0543507261131704, 0.0003047157398743075)
"""