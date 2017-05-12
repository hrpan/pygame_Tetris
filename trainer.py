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
    def getWeight(self):
        eps=1e-7
        binning=np.linspace(np.amin(self.y)-eps,np.amax(self.y)+eps,self.nbins)
        hist=np.histogram(self.y,binning,density=True)
        idx=np.digitize(self.y,binning)
        return np.array([1/hist[0][x-1] for x in idx])
    def loadModel(self,modelFile):
        self.actor=load_model(modelFile[0])
        self.critic=load_model(modelFile[1])
        self.modelFile=modelFile
    def trainModel(self):
        #y_pred=np.ndarray.flatten(self.critic.predict(self.x))
        y_pred=self.critic.predict(self.x)
        y_critic=np.array(y_pred)
        y_actor=np.zeros((len(self.y),5))
        for i in range(len(y_critic)):
            if self.y[i]==-1:
                y_critic[i]=0
            else:
                y_critic[i][self.a[i]]=self.y[i]+self.gamma_td*np.amax(y_pred[i+1])
        print 'Training actor...'
        self.actor.fit(self.x,y_pred,self.batch_size,self.epochs)
        print 'Training critic...'
        self.critic.fit(self.x,y_critic,self.batch_size,self.epochs)
        #self.critic.fit(self.x,y_critic,self.batch_size,50)
        print ''
    def saveModel(self):
        self.actor.save(self.modelFile[0])
        self.critic.save(self.modelFile[1])

