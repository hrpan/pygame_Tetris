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
        self.model=load_model(cfg.modelfile[0])
        self.cycle=cycle
        self.ncycle=cfg.ncycle

    def predictOper(self,boards):
        boards = np.array(boards).reshape((1,22,10,1))[:,2:22,:,:]
        predicts = self.model.predict(boards)[0]
        roll = np.random.choice(range(5),p=predicts)
        return roll


