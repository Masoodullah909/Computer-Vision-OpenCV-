import numpy as np
def trapule_masood66(f,a,b,n):
    print("I am Masoodullah Roll no: AP-19066")
    h=(b-a)/n
    mid_sum=0
    for i in range(1,n):
        mid_sum=mid_sum+f(a+i*h)
    I_trap=(h/2)*(f(a)+2*mid_sum+f(b))
    print('The integral of given function is: I=%0.6f' %(I_trap))
    return I_trap

""" PROGRAM OUTPUT

f= lambda x: x*np.exp(x)

I am Masoodullah Roll no: AP-19066
The integral of given function is: I=1.014771
1.014771073589269

"""   