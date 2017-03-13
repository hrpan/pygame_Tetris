from keras.models import load_model
import numpy as np

class Trainer:
    def __init__(self,cfg,cycle):
        self.cycle=cycle
        self.ncycle=cfg.ncycle
        self.use_sample_weight=cfg.use_sample_weight
        self.epochs=cfg.epochs
        self.batch_size=cfg.batch_size
        self.lr_td=cfg.lr_td
        self.gamma_td=cfg.gamma_td
        self.nbins=cfg.nbins
    def loadData(self,trainFiles):
        x_array=[]
        y_array=[]
        for x,y in trainFiles:
            x_array.append(np.load(x))
            y_array.append(np.load(y))
        self.x=np.concatenate(x_array)
        self.y=np.concatenate(y_array)
    def v_iter(self):
        length = len(self.y)
        self.y_train=np.empty(length)
        y_pred = self.model.predict(self.x)
        for i in range(length):
            if self.y[i]==-1:
                self.y_train[i]=0
            else:
                delta=self.y[i]+self.gamma_td*y_pred[i+1]-y_pred[i]
                self.y_train[i]=y_pred[i]+self.lr_td*delta
    def getWeight(self):
        eps=1e-7
        binning=np.linspace(np.amin(self.y_train)-eps,np.amax(self.y_train)+eps,self.nbins)
        hist=np.histogram(self.y_train,binning,density=True)
        idx=np.digitize(self.y_train,binning)
        return np.array([1/hist[0][x-1] for x in idx])
    def loadModel(self,modelFile):
        self.model=load_model(modelFile)
        self.modelFile=modelFile
    def trainModel(self):
        for i in range(self.epochs):
            self.v_iter()
            if self.use_sample_weight:
                weight=self.getWeight()
            else:
                weight=None
            self.model.fit(self.x,self.y_train,self.batch_size,1,sample_weight=weight)
    def saveModel(self):
        self.model.save(self.modelFile)

