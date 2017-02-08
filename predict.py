from keras.models import load_model
import numpy as np
model = load_model('model/model.h5')

def predictOper(boards):
	boards = np.array(boards).reshape((5,1,22,10))
	return np.argmax(model.predict(boards))
