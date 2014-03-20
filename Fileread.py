'''
Created on 11-Mar-2014

@author: akm
'''
outfile = open('file.txt','w');
outfile.write('file write example\n');
outfile.write('writing multiple lines\n');
outfile.write('trying to show use of split llines\n');

outfile.close();

infile = open('file.txt','r');
##content = infile.read();
##print content;
for line in infile:
    print 'Line %s' %line;
infile.close();