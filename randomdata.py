from numpy import *
import random
import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np

x1 = []
def nextUniform():
    #for i in range(100):
        #print random.randint(-1,1),
    return random.uniform(-1,1)

f = open("data.dat", "w")
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
for i in range(1000):
    x1 = r_[nextUniform()]
    x2 = r_[nextUniform()]
    nlevel = 0.5 * np.random.normal(0,1,1)
    y = r_[math.cos(4*math.sqrt(x1*x1+x2*x2))+nlevel]
    #print y, x2, nlevel
    p = str(x1)
    q = str(x2)
    n = str(nlevel)
    #fn = str(y)

    '''
    f.write(p+"\t\t")
    f.write(q+"\t\t")
    f.write(n+"\t\t")
    f.write(fn+"\n")
    
    #f.write(x2)
    '''
    ax.scatter(x1,x2,y)

f.close()
'''
x1 = r_[0:nextUniform():100j]
x2 = r_[0:nextUniform():100j]
nlevel = r_[1:0.5*np.random.normal(0,1,1):100j]
print nlevel
y = math.cos(4*math.sqrt(x1*x1+x2*x2))+nlevel
#print y
'''
plt.show()
