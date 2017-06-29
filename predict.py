from keras.models import load_model
import numpy as np
from config import Config

slope=0.01

def sigmoid(x):
    return 1/(1+np.exp(-x))

def expected_value(x):
    tmp=0
    for i,prob in enumerate(x):
        tmp+=i*prob
    return tmp

class Predict:
    def __init__(self,cycle):
        cfg=Config()
        self.model=load_model(cfg.modelfile)
        self.cycle=cycle
        self.ncycle=cfg.ncycle
        self.eps = max(1./(1.+cfg.eps_decay_rate*cycle),cfg.eps_pred)
        print 'EPS_greedy:%.3e'% self.eps
    def predictOper(self,boards):
        boards = np.array(boards).reshape((1,22,10,1))[:,2:22,:,:]
        
        if np.random.rand()>self.eps:
            predicts = self.model.predict(boards)
            #expected = np.array([expected_value(x) for x in predicts])
            roll=np.argmax(predicts[0])
        else:
            roll = np.random.choice(range(5))
        return roll
        """
        predicts = self.model.predict(boards)[0]
        prob = np.exp(predicts)/np.sum(np.exp(predicts))
        roll = np.random.choice(range(5),p=prob)
        return roll
        """
