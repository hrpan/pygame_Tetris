import numpy as np
import os.path

gamma=0.95
ncycle=4

def evalBoard(board,score):
    penalty=0
    for i in np.arange(21,1,-1):
        for j in range(10):
            if board[i][j]==0 and board[i-1][j]==1:
                penalty+=1
    return score-0.3*penalty

class Record:
    def __init__(self,cycle):
        self.cycle=cycle
	self.nGames=0
	self.allScores=[]
        self.rawScores=[0]
        self.currScores=[]
	self.allGameBoards=[]
        self.currGameBoards=[]
    def recordBoard(self,board,score):
        self.rawScores[-1]=score
        self.currScores.append(evalBoard(board,score))
        self.currGameBoards.append(np.array(board))
    def recordGame(self):
	self.nGames+=1
        self.rawScores.append(0)
        length=len(self.currGameBoards)
        for i,board in enumerate(self.currGameBoards):
            self.allGameBoards.append(board)
            if i==length-1:
                reward=-1
            else:
                reward=self.currScores[i+1]-self.currScores[i]
            self.allScores.append(reward)
            if reward!=0:
                for j in range(1,len(self.allScores)):
                    self.allScores[-1-j]+=reward*np.power(gamma,j)
        self.currGameBoards=[]
        self.currScores=[]
    def averageScore(self):
        return np.average(self.allScores),np.average(self.rawScores)
    def saveRecord(self):
        npBoards = np.array(self.allGameBoards).reshape((len(self.allGameBoards),1,22,10))
        npScores = np.array(self.allScores)
        n=self.cycle%ncycle
        #while os.path.isfile('data/boards%d.npy' % n):
        #    n+=1
        np.save('data/boards%d.npy' % n,npBoards)
        np.save('data/scores%d.npy' % n,npScores)
