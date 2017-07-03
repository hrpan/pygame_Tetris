import matplotlib.pyplot as plt
import numpy as np
import codecs
f = codecs.open('log',encoding='utf-8')
y=[]
y_var=[]
for line in f:
    if '100/100' in line:
        data = line.split()[3].split('/')
        y.append(float(data[0]))
        y_var.append(float(data[1]))

N=len(y)
x=np.linspace(0,N,N)
y=np.array(y)
y_var=np.array(y_var)
y_err=y_var/np.sqrt(N)
plt.errorbar(x,y,y_err,color='b')
plt.show()        
