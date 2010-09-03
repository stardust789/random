import random
import math

def nextUniform():
    #for i in range(100):
        #print random.randint(-1,1),
    return random.uniform(-1,1)

f = open("data.dat", "w")
for i in range(10000):
    x1 = nextUniform()
    x2 = nextUniform()
    nlevel = 0.5 * nextUniform()
    
    y = math.cos(4*math.sqrt(x1*x1+x2*x2))+nlevel
    print x1, x2, nlevel
    p = str(x1)
    q = str(x2)
    n = str(nlevel)
    fn = str(y)

    
    f.write(p+"\t\t")
    f.write(q+"\t\t")
    f.write(n+"\t\t")
    f.write(fn+"\n")
    
    #f.write(x2)

f.close()
        
