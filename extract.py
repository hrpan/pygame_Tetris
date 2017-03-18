import numpy as np
import sys
import os.path
from config import Config

cfg=Config()

def getGameFrames(y,game):
    count=0
    start=0
    for i,val in enumerate(y):
        if val==-1:
            count+=1
            if count>game:
                end=i
                break
            elif count==game:
                start=i+1
    return (start,end)

cycle=int(sys.argv[1])

x_array=np.load('data/boards%d.npy'%(cycle%cfg.ncycle))
y_array=np.load('data/scores%d.npy'%(cycle%cfg.ncycle))
r_array=np.load('data/rScores%d.npy'%(cycle%cfg.ncycle))
a_array=np.load('data/actions%d.npy'%(cycle%cfg.ncycle))

if os.path.isfile('data/sample/boards.npy'):
    x_s_array=np.load('data/sample/boards.npy')
    y_s_array=np.load('data/sample/scores.npy')
    r_s_array=np.load('data/sample/rScores.npy')
    a_s_array=np.load('data/sample/actions.npy')
else:
    x_s_array=np.empty((0,20,10,1),dtype='int8')
    y_s_array=np.empty((0,),dtype='float32')
    r_s_array=np.empty((0,))
    a_s_array=np.empty((0,),dtype='int8')

r_avg = np.average(r_array)

games=np.where(r_array>r_avg)[0]
print games
for i in games:
    (start,end)= getGameFrames(y_array,i)
    x_s_array=np.append(x_s_array,x_array[start:end+1],axis=0)
    y_s_array=np.append(y_s_array,y_array[start:end+1],axis=0)
    r_s_array=np.append(r_s_array,r_array[i:i+1],axis=0)
    a_s_array=np.append(a_s_array,a_array[start:end+1],axis=0)

np.save('data/sample/boards.npy',x_s_array)
np.save('data/sample/scores.npy',y_s_array)
np.save('data/sample/rScores.npy',r_s_array)
np.save('data/sample/actions.npy',a_s_array)

