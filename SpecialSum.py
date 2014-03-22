'''
Created on 20-Mar-2014

@author: akm
'''
from fractions import gcd
def foo(n):
    ret = 0
    for i in range(1,n+1):
        if(gcd(n,i)==1):
            ret +=1
    return ret


def SpecialSum(n):
    sum =0
    for i in range(1,n+1):
        if(n%i==0):
            sum += foo(i)
    return sum


##for i in range(1,10):
  ##  print foo(i)
print SpecialSum(7)         