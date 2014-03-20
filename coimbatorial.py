'''
Created on 14-Mar-2014

@author: akm
'''
import math
def comb(n,r):
    f=math.factorial
    return f(n)/f(r)/f(n-r)

str = '3 1'
words = str.split()
r = words.pop()
print r;
n = words.pop()
print n
print comb(int(n), int(r))
for word in words:
    print word
x =5    
while(x>0):
    print x    
    x = x-1
    
    
    
    


