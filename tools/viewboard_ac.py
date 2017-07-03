import numpy as np
import os
from keras.models import load_model

actor = load_model('model/ac/actor.h5')
critic = load_model('model/ac/critic.h5')

def printBoard(board,score):
    for i in range(20):
        for j in range(10):
            print '%2d'%board[i][j][0],
        print ''
    print 'Score:', score
    print 'Actor:', actor.predict(board.reshape(1,20,10,1))
    print 'Critic:', critic.predict(board.reshape(1,20,10,1))

os.system('clear')
while True:
    cycle=int(raw_input('Cycle:'))
    if cycle<0:
        break
    boards = np.load('data/boards%d.npy' % cycle)
    scores = np.load('data/scores%d.npy' % cycle)
    frame=0
    while True:
        print 'Total length:', len(boards)
        command=raw_input('Command:')
        if command=='g':
            print 'Total length:', len(boards)
            frame=int(raw_input('Frame:'))
            printBoard(boards[frame],scores[frame])
        elif command=='f':
            find=int(raw_input('Find Score:'))
            idx=np.where(scores==find)[0]
            print idx
            for i in idx:
                if scores[i]!=scores[i+1]:
                    print i
        elif command=='n':
            frame+=1
            printBoard(boards[frame],scores[frame])
        elif command=='p':
            frame-=1
            printBoard(boards[frame],scores[frame])
        elif command=='pred':
            start=int(raw_input('Start frame:'))
            end=int(raw_input('End frame:'))
            print model.predict(boards[start:end])            
            
