from keras.models import load_model
import theano
import numpy as np

#theano.config.openmp=False

model = load_model('model/model.h5')

opers=np.arange(5)

epsilon=0.1

def predictOper(boards):
    boards = np.array(boards).reshape((5,1,22,10))
    predicts = model.predict(boards)
    #print predicts.shape, predicts
    
    prob=np.ones((5))*(epsilon/4)
    prob[np.argmax(predicts)]=1-epsilon
    roll=np.random.choice(opers,p=prob)
    
    #roll=np.argmax(predicts)
    return roll

