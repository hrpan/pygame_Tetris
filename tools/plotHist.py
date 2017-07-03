import matplotlib.pyplot as plt
import os.path
import numpy as np
from time import sleep

plt.figure()
#plt.show(block=False)
plt.ion()

while True:
    print 'monitoring...'
    i=0
    y=[]
    y_err=[]
    while os.path.isfile('data/boards%i.npy'%i):
        y_data=np.load('data/rScores%i.npy'%i)
        y.append(np.average(y_data))
        y_err.append(np.sqrt(np.var(y_data))/len(y_data))
        i+=1
    x=np.linspace(0,i,i)
    plt.errorbar(x,np.array(y),yerr=np.array(y_err),color='b')
    plt.pause(30)
    plt.clf()
#    sleep(10)
