from keras.models import load_model
import theano
import numpy as np
import os.path

theano.config.openmp=True

x_train = np.load('data/boards0.npy')
scores = np.load('data/scores0.npy')

scale=0.0

n=1
while os.path.isfile('data/boards%d.npy' % n):
    x_train = np.concatenate((x_train,np.load('data/boards%d.npy' %n)))
    scores = np.concatenate((scores,np.load('data/scores%d.npy' %n)))
    n+=1

s_avg = np.average(scores)
#print s_avg

def procScore(score):
    if score>s_avg:
    	return 1
    else:
    	return 0
y_train = scores
#y_train = np.abs(scores)
#y_train = (scores-np.amin(scores))/(np.amax(scores)-np.amin(scores))
#y_train = np.array([procScore(x) for x in scores])
weight = np.exp(scale*scores)

model = load_model('model/model.h5')
#model.fit(x_train,y_train,batch_size=32,nb_epoch=1,sample_weight=weight)
model.fit(x_train,y_train,batch_size=128,nb_epoch=1)
model.save('model/model.h5')
