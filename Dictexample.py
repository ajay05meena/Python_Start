'''
Created on 20-Mar-2014

@author: akm
'''
T = 4 ;
A = 'abc'
B = 'def'
C = 'fgh'
D = 'cba'
list = ()

Dict = {}
Dict[A] = A[::-1]

Dict[B] = B[::-1]

Dict[C] = C[::-1]

Dict[D] = D[::-1]

for key in Dict.keys():
    if(Dict.get(key)in Dict):
        print Dict.get(key)[(len(Dict.get(key))/2)+1]
A = 5
B = 7       
print "%s %s" %(A ,B)    
        