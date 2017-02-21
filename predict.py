from keras.models import load_model
import numpy as np


model = load_model('model/model.h5')

opers=np.arange(5)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def predictOper(boards,cycle):
    boards = np.array(boards).reshape((5,1,22,10))
    predicts = model.predict(boards)
    epsilon=1-sigmoid(cycle) 
    prob=np.ones((5))*(epsilon/4)
    prob[np.argmax(predicts)]=1-epsilon
    roll=np.random.choice(opers,p=prob)
    
    #roll=np.argmax(predicts)
    return roll

