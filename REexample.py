'''
Created on 12-Mar-2014

@author: akm
'''
import re
str = 'https://www.facebook.com/coca-cola/photos/a.99394368305.88399.40796308305/10153093413773306/?type=1'
match = re.search(r'\/((\d)+)\/',str);
if match:
    print 'found ' ,match.group()
else:
    print 'not found'


  
##pattern = re.compile();