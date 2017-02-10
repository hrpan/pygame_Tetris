from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, Flatten, MaxPooling2D, Dropout

model = Sequential()
model.add(Convolution2D(24,6,6,input_shape=(1,22,10)))
model.add(Activation('relu'))
model.add(Convolution2D(12,3,3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(9))
model.add(Activation('relu'))
model.add(Dense(9))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(optimizer='sgd',loss='binary_crossentropy')

#model.add(Activation('linear'))
#model.compile(optimizer='sgd',loss='mse')

model.save('model.h5')
