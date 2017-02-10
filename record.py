import numpy as np
import os.path


class Record:
    def __init__(self):
	self.nGames=0
	self.scores=[]
	self.allGameBoards=[]
        self.currGameBoards=[]
    def recordBoard(self,board):
        self.currGameBoards.append(np.array(board))
    def recordGame(self,score):
	self.nGames+=1
        print score
        for board in self.currGameBoards:
            self.allGameBoards.append(board)
            self.scores.append(score)	
        self.currGameBoards=[]
    def saveRecord(self):
        npBoards = np.array(self.allGameBoards).reshape((len(self.allGameBoards),1,22,10))
        npScores = np.array(self.scores)
        n=0
        while os.path.isfile('data/boards%d.npy' % n):
            n+=1
        np.save('data/boards%d.npy' % n,npBoards)
        np.save('data/scores%d.npy' % n,npScores)
