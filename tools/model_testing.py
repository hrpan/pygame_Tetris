from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, Flatten, MaxPooling2D, Dropout, BatchNormalization
import numpy as np

model = Sequential()
conv=True
"""CONV NET"""
if conv:
    model.add(Convolution2D(64,4,4,activation='relu',input_shape=(1,22,10)))
    model.add(BatchNormalization())
    model.add(Convolution2D(64,4,4,activation='relu'))
    model.add(Convolution2D(64,4,4,activation='relu'))
    model.add(Flatten())
    model.add(Dense(500,activation='relu'))
    model.add(Dense(500,activation='relu'))
else:
    model.add(Flatten(input_shape=(1,22,10)))
    model.add(Dense(1000,activation='relu'))
    model.add(Dense(1000,activation='relu'))


model.add(Dense(1))
model.add(Activation('linear'))
model.compile(optimizer='rmsprop',loss='mse')

print model.summary()

x_train = np.load('data/bkp/boards0.npy')
y_train = np.load('data/bkp/scores0.npy')

b_size=1024
epochs=3
model.fit(x_train,y_train,batch_size=b_size,nb_epoch=epochs)

