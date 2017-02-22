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
		n = (self.cycle-1)%self.ncycles
		rScores = np.load('data/rScores%d.npy' % n)
		self.var = 	np.var(rScores)	
		self.eps = 1-sigmoid(self.var)

	def predictOper(self,boards):
		self.boards = np.array(boards).reshape((5,1,22,10))
		predicts = model.predict(boards)
		prob = np.ones((5))*(self.eps/4)
		prob[np.argmax(predicts)] = 1-self.eps
		return np.random.choice(opers,p=prob)


