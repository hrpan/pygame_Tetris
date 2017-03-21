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
        self.eps = max(np.exp(-cfg.eps_decay_rate*cycle),cfg.eps_pred)

    def predictOper(self,board):
        board = np.array(board).reshape((1,22,10,1))[:,2:22,:,:]
        probs = self.model.predict(board)
        roll = np.random.choice(range(5),p=probs[0])
        return roll


