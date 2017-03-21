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
        a_array=[]
        for x,y,a in trainFiles:
            x_array.append(np.load(x))
            y_array.append(np.load(y))
            a_array.append(np.load(a))
        self.x=np.concatenate(x_array)
        self.y=np.concatenate(y_array)
        self.a=np.concatenate(a_array)
    def reformat(self):
        length = len(self.y)
        self.y_train=np.zeros((length,5))
        for i in range(length):
            self.y_train[i][self.a[i]]=1
    def getWeight(self):
        weight=np.array(self.y,dtype='float32')
        for i in reversed(range(len(weight))):
            if weight[i]==-1:
                weight[i]=0
            else:
                weight[i]+=weight[i+1]   
        baseline=-0.5
        weight-=baseline
        return weight
    def loadModel(self,modelFile):
        self.model=load_model(modelFile)
        self.modelFile=modelFile
    def trainModel(self):
        self.reformat()
        weight=self.getWeight()
        self.model.fit(self.x,self.y_train,self.batch_size,self.epochs,sample_weight=weight)
    def saveModel(self):
        self.model.save(self.modelFile)

