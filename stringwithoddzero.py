'''
Created on 14-Mar-2014

@author: akm
'''
import math
def comb(n,r):
    f=math.factorial
    return f(n)/f(r)/f(n-r)

def fun(n,r):
    return comb(n,r)*pow(9,n-r)

#print fun(3,1)
n = 4
def fun1(n):
    res = 0
    for i in range(0,n):
        if(i%2!=0):
            res = res +fun(n,i)
    return res        
        
                
    