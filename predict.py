from keras.models import load_model
import numpy as np


model = load_model('model/model.h5')

opers=np.arange(5)

slope=0.01

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Predict:
    def __init__(self,cycle,ncycle):
        self.cycle=cycle
        self.ncycle=ncycle
        """
        if cycle>0:
            n = (cycle-1)%ncycle
            rScores = np.load('data/rScores%d.npy' % n)
            self.var = np.var(rScores) 
        else:
            self.var = 1000
        """
        #self.eps = 1-sigmoid(self.var)
        self.eps = np.exp(-0.05*cycle)

    def predictOper(self,boards):
        boards = np.array(boards).reshape((5,1,22,10))
        predicts = model.predict(boards)
        if np.random.rand()>self.eps:
            roll = np.argmax(predicts)
        else:
            roll = np.random.choice(opers)
        return roll


