'''
Created on 15-Mar-2014

@author: akm
'''
def lucky_recursive(n):
    if(n==1):
        return 4
    else:
        if(n==2):
            return 7
        else:
            return lucky_recursive(n/2)*10 + lucky_recursive(n%2)
        
def lucky( n):
    if(n==1):
        return 4
    if(n==2):
        return 7
    res = 0
    while(n/2>0):
        if(n%2==0):
            res = res*10+7
        else:
            res = res*10+4
        n=n/2                  
    return reverse(res)
def reverse(num):
  rev = 0
  while(num > 0):
    rev = (10*rev)+num%10
    num //= 10
  return rev        
print lucky(11000000000000000000000000000000000000000000000000000000000000000000000000000)        
    
