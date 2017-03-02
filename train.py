from keras.models import load_model
import numpy as np
import os.path
from config import Config

cfg = Config()
        
x_train = np.load('data/boards0.npy')
y_train = np.load('data/scores0.npy')

n=1
while os.path.isfile('data/boards%d.npy' % n):
    x_train = np.concatenate((x_train,np.load('data/boards%d.npy' %n)))
    y_train = np.concatenate((y_train,np.load('data/scores%d.npy' %n)))
    n+=1

#============================================

nbins=10000
eps=1e-5
bins=np.linspace(np.amin(y_train)-eps,np.amax(y_train)+eps,nbins)
hist=np.histogram(y_train,bins=bins,density=True)
idx=np.digitize(y_train,bins)
weights = np.array([1/hist[0][x-1] for x in idx])

#============================================

model = load_model('model/model.h5')
#model.fit(x_train,y_train,batch_size=128,nb_epoch=1,sample_weight=weights)
model.fit(x_train,y_train,batch_size=cfg.batch_size,nb_epoch=cfg.epochs)
model.save('model/model.h5')

#============================================
