import numpy as np

def bisection_masood66(f,a,b,es):
    if f(a)*f(b)>0:
        return None
    print("I am Masoodullah Roll no: AP-19066")
    itr = 1
    error = 100
    c_old = b
    while error>es:
        c=(a+b)/2
        error=np.abs((c-c_old)*100/c)
        print('itr no:%d, a:%0.6f, f(a):%0.6f, b:%0.6f, f(b):%0.6f, c:%0.6f, f(c):%0.6f, error:=%0.6f' 
        %(itr,a,f(a),b,f(b),c,f(c),error))
        if f(c)*f(b)<0:
            a=c
        else:
            b=c
        itr=itr+1
        c_old=c
    return(itr-1,c,error)

f=lambda x: np.log(x**4)-0.7
bisection_masood66(f, 0.5, 2, 0.1)

""" OUTPUT OF BISECTION

f=lambda x: np.log(x**4)-0.7

bisection_masood66(f, 0.5, 2, 0.1)
I am Masoodullah Roll no: AP-19066
itr no:1, a:0.500000, f(a):-3.472589, b:2.000000, f(b):2.072589, c:1.250000, f(c):0.192574, error:=60.000000
itr no:2, a:0.500000, f(a):-3.472589, b:1.250000, f(b):0.192574, c:0.875000, f(c):-1.234126, error:=42.857143
itr no:3, a:0.875000, f(a):-1.234126, b:1.250000, f(b):0.192574, c:1.062500, f(c):-0.457502, error:=17.647059
itr no:4, a:1.062500, f(a):-0.457502, b:1.250000, f(b):0.192574, c:1.156250, f(c):-0.119272, error:=8.108108
itr no:5, a:1.156250, f(a):-0.119272, b:1.250000, f(b):0.192574, c:1.203125, f(c):0.039689, error:=3.896104
itr no:6, a:1.156250, f(a):-0.119272, b:1.203125, f(b):0.039689, c:1.179688, f(c):-0.039002, error:=1.986755
itr no:7, a:1.179688, f(a):-0.039002, b:1.203125, f(b):0.039689, c:1.191406, f(c):0.000537, error:=0.983607
itr no:8, a:1.179688, f(a):-0.039002, b:1.191406, f(b):0.000537, c:1.185547, f(c):-0.019183, error:=0.494234
itr no:9, a:1.185547, f(a):-0.019183, b:1.191406, f(b):0.000537, c:1.188477, f(c):-0.009311, error:=0.246508
itr no:10, a:1.188477, f(a):-0.009311, b:1.191406, f(b):0.000537, c:1.189941, f(c):-0.004384, error:=0.123102
itr no:11, a:1.189941, f(a):-0.004384, b:1.191406, f(b):0.000537, c:1.190674, f(c):-0.001922, error:=0.061513
Out  [22]: (11, 1.190673828125, 0.061513225343448844)"""
            
          