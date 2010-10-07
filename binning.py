from numpy import *
import math
import random
import numpy as np
from decimal import *

boundary = []
def binboundaries(l,h,s):
    #boundary = []
    #print l,h,s
    for i in np.arange(l, h, s):
        boundary.append(i)
        #print boundary
    #return boundary

def discretedata(d, b):
    newval = []
    print "\n Original Data in list for binning....\n";
    print d
    #print b
    #t1 = array(x1)
    #t2 = array(b)
    for i in range(len(d)):
        #print i, x1[i]
        for j in range(len(b)):
            #print x1[i], b[j]
            if(int(d[i] > b[j])):
                j = j+1
                #print "incremented j"
            elif (int(d[i] < b[j])):
                #print "Not greater"
                avg = (b[j]+b[j-1])/2
                #print avg
                newval.append(avg)
                break
    return newval    
                    
def bootstrap(n, newx1, newx2, newy):
    bx1 = []
    bx2 = []
    by = []
    my_data = []
    print "\n***************************************************\n";
    print "Bootstrapped Sample with N = 50"
    for i in range(len(newx1)):
        r = random.randrange(1,50)
        bx1.append(newx1[r])
        bx2.append(newx2[r])
        by.append(newy[r])
    print bx1
    print bx2
    print by
    f = open('sample.txt','w')
    for item in range(len(bx1)):
        f.write("%s " % bx1[item])
        f.write("%s " % bx2[item])
        f.write("%s\n" % by[item])
        my_data.append(bx1[item])
        my_data.append(bx2[item])
    print "File Written successfully"
    print my_data
        
x1 = []
x2 = []
y = []
newx1 = []
newx2 = []
newy = []
#bound = []
for line in file('data.dat','r'):
    data = line.split('\t\t')
    x1.append(eval(data[0]))
    x2.append(eval(data[1]))
    y.append(eval(data[3]))
    #newlist = [[int(x) for x in y] for y in x1]
    #x = [map(int, uniList(l)) for l in x1]
#print x1,x2,y
#print x1

binsize = 0.5
blrange = -1
bhrange = 1
n = 50
binboundaries(blrange, bhrange+0.1, binsize)
newx1 = discretedata(x1, boundary)
newx2 = discretedata(x2, boundary)
newy = discretedata(y, boundary)
print "\nData after binning........................................\n";
print newx1
print newx2
print newy
bootstrap(n, newx1, newx2, newy)
   

#for i in range(len(x1)):
#    print x1[i]
    


