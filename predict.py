from keras.models import load_model
import numpy as np
from config import Config

slope=0.01

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Predict:
    def __init__(self,cycle):
        cfg=Config()
        self.model=load_model('model/model.h5')
        self.cycle=cycle
        self.ncycle=cfg.ncycle
        """
        if cycle>0:
            n = (cycle-1)%ncycle
            rScores = np.load('data/rScores%d.npy' % n)
            self.var = np.var(rScores) 
        else:
            self.var = 1000
        """
        #self.eps = 1-sigmoid(self.var)
        self.eps = max(np.exp(-0.05*cycle),cfg.eps_pred)

    def predictOper(self,boards):
        boards = np.array(boards).reshape((5,22,10,1))
        if np.random.rand()>self.eps:
            predicts = self.model.predict(boards)
            roll = np.argmax(predicts)
        else:
            roll = np.random.choice(range(5))
        return roll


