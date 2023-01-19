import numpy as np
def Regulafalsi_ali_hyder304(f, xu, xl, es):
    if f(xu)*f(xl) > 0:
        print("Invalid Limit!")
        return None
    print("I am Ali_hyder AP-19304")
    itr = 1
    error = 100
    xr_old = xl
    while error > es:
        xr=xu-(f(xu)*(xu-xl))/(f(xu)-f(xl))
        error=np.abs((xr-xr_old)/xr)*100
        print('itr:%d, a:%0.6f, f(a):%0.6f, b:%0.6f, f(b):%0.6f, c:%0.6f, f(c):%0.6f, error:%0.6f'
        %(itr, xu, f(xu), xl, f(xl), xr, f(xr), error))
        if f(xr)*f(xl) > 0:
            xu = xr
        else:
            xl = xr
        itr = itr + 1
        xr_old = xr
    return(itr-1,xr,error)

"""
f = lambda x: x*3-6*x*2+11*x-6.1
Regulafalsi_ali_hyder304(f,3.5,2.5,0.0001)
I am ali_hyderullah AP-19304
itr:1, a:3.500000, f(a):0.900000, b:2.500000, f(b):-1.100000, c:3.050000, f(c):0.000000, error:18.032787
itr:2, a:3.500000, f(a):0.900000, b:3.050000, f(b):0.000000, c:3.050000, f(c):0.000000, error:0.000000   
"""