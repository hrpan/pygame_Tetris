import sys
import os.path
from config import Config
from trainer import Trainer

def dataPath(prefix,n):
    return (prefix+'boards%d.npy'%n,prefix+'scores%d.npy'%n,prefix+'actions%d.npy'%n)

cycle=int(sys.argv[1])

cfg=Config()

trainer=Trainer(cfg,cycle)

trainer.loadModel(cfg.modelfile)

prefix='data/'
fileArray=[]
for n in range(cfg.ncycle):
    if os.path.isfile(dataPath(prefix,n)[0]):
        fileArray.append(dataPath(prefix,n))
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
