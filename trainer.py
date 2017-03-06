from keras.models import load_model
import numpy as np

def reformat(y):
    scores=np.zeros((len(y),5))
    for i,y in enumerate(y):
        scores[i][min(int(y),4)]=1
    return scores 

class Trainer:
    def __init__(self,cfg):
        self.ncycle=cfg.ncycle
        self.use_sample_weight=cfg.use_sample_weight
        self.epochs=cfg.epochs
        self.batch_size=cfg.batch_size
    def loadData(self,trainFiles):
        x_array=[]
        y_array=[]
        for x,y in trainFiles:
            x_array.append(np.load(x))
            y_array.append(np.load(y))
        self.x_train=np.concatenate(x_array)
        self.y_train=reformat(np.concatenate(y_array))
    def loadModel(self,modelFile):
        self.model=load_model(modelFile)
        self.modelFile=modelFile
    def trainModel(self):
        self.model.fit(self.x_train,self.y_train,self.batch_size,self.epochs)
    def saveModel(self):
        self.model.save(self.modelFile)

