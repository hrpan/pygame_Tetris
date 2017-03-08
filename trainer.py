from keras.models import load_model
import numpy as np

class Trainer:
    def __init__(self,cfg):
        self.ncycle=cfg.ncycle
        self.use_sample_weight=cfg.use_sample_weight
        self.epochs=cfg.epochs
        self.batch_size=cfg.batch_size
        self.lr_td=cfg.lr_td
        self.gamma_td=cfg.gamma_td
    def loadData(self,trainFiles):
        x_array=[]
        y_array=[]
        for x,y in trainFiles:
            x_array.append(np.load(x))
            y_array.append(np.load(y))
        self.x_train=np.concatenate(x_array)
        self.y_train=np.concatenate(y_array)
    def v_iter(self):
        length = len(self.y_train)
        y_pred = self.model.predict(self.x_train,512)
        for i in range(length-1):
            delta=self.y_train[i]+self.gamma_td*y_pred[i+1]-y_pred[i]
            self.y_train[i]=y_pred[i]+self.lr_td*delta 
    def loadModel(self,modelFile):
        self.model=load_model(modelFile)
        self.modelFile=modelFile
    def trainModel(self):
        self.v_iter()
        self.model.fit(self.x_train,self.y_train,self.batch_size,self.epochs)
    def saveModel(self):
        self.model.save(self.modelFile)

