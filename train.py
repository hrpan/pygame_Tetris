from keras.models import load_model
import numpy as np
import os.path

x_train = np.load('data/boards0.npy')
scores = np.load('data/scores0.npy')
n=1
while os.path.isfile('data/boards%d.npy' % n):
    x_train = np.concatenate((x_train,np.load('data/boards%d.npy' %n)))
    scores = np.concatenate((scores,np.load('data/scores%d.npy' %n)))
    n+=1
s_avg = np.average(scores)
print s_avg
def procScore(score):
	if score>s_avg:
		return 1
	else:
		return 0

#y_train = (scores-np.amin(scores))/(np.amax(scores)-np.amin(scores))
y_train = np.array([procScore(x) for x in scores])
weight = np.exp(scores)

model = load_model('model/model.h5')
model.fit(x_train,y_train,nb_epoch=1,sample_weight=weight)
model.save('model/model.h5')
