from keras.models import load_model
import numpy as np

class Trainer:
    def __init__(self,cfg,cycle):
        self.cycle=cycle
        self.ncycle=cfg.ncycle
        self.use_sample_weight=cfg.use_sample_weight
        self.epochs=cfg.epochs
        self.batch_size=cfg.batch_size
        self.lr_td_decay=cfg.lr_td_decay
        self.gamma_td=cfg.gamma_td
        self.nbins=cfg.nbins
    def loadData(self,trainFiles):
        x_array=[]
        y_array=[]
        a_array=[]
        for x,y,a in trainFiles:
            x_array.append(np.load(x))
            y_array.append(np.load(y))
            a_array.append(np.load(a))
        self.x=np.concatenate(x_array)
        self.y=np.concatenate(y_array)
        self.a=np.concatenate(a_array)
    def v_iter(self):
        length = len(self.y)
        y_pred = self.model.predict(self.x,2048,verbose=1)
        print ''
        self.y_train=np.array(y_pred)
        for i in range(length):
            if self.y[i]==-1:
                self.y_train[i]=[0,0,0,0,0]
            else:
                action=self.a[i]
                delta=self.y[i]+self.gamma_td*np.amax(y_pred[i+1])-y_pred[i][action]
                lr_td=1/(1+self.lr_td_decay*self.cycle)
                self.y_train[i][action]=y_pred[i][action]+lr_td*delta
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
        self.v_iter()
        if self.use_sample_weight:
            weight=self.getWeight()
        else:
            weight=None
        self.model.fit(self.x,self.y_train,self.batch_size,self.epochs,sample_weight=weight)
    def saveModel(self):
        self.model.save(self.modelFile)

