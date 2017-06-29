import sys
import os.path
import numpy as np
from config import Config
from trainer import Trainer

special_data=('data/sample/boards.npy','data/sample/scores.npy','data/sample/actions.npy')

def dataPath(prefix,n):
    return (prefix+'boards%d.npy'%n,prefix+'scores%d.npy'%n,prefix+'actions%d.npy'%n)

cycle=int(sys.argv[1])

cfg=Config()

trainer=Trainer(cfg,cycle)

trainer.loadModel(cfg.modelfile)

prefix='data/'
fileArray=[]
for n in range(cfg.ncycle):
#print 'Training cycles: ', cycle, ' ',
#fileArray.append(dataPath(prefix,cycle%cfg.ncycle))
#for n in np.random.permutation(cycle)[0:cfg.train_capacity-1]:
#    print n, ' ',
    if os.path.isfile(dataPath(prefix,n)[0]):
        fileArray.append(dataPath(prefix,n))
#print ''
if os.path.isfile(special_data[0]):
    fileArray.append(special_data)
trainer.loadData(fileArray)
trainer.trainModel()
trainer.saveModel()

#============================================
"""if cfg.use_sample_weight:
    nbins=100
    eps=1e-5
    bins=np.linspace(np.amin(y_train)-eps,np.amax(y_train)+eps,nbins)
    hist=np.histogram(y_train,bins=bins,density=True)
    idx=np.digitize(y_train,bins)
    weights = np.array([1/hist[0][x-1] for x in idx])
else:
    weights = np.array([1 for x in y_train])
"""
#============================================
