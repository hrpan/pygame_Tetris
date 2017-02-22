import numpy as np
import os.path

gamma=0.75
decay_length=20
ncycle=6

def evalBoard(board,score):
    penalty=0
    for i,j in np.transpose(np.where(board==1)):
        for k in range(i+1,22):
            if board[k][j]==0 or board[k][j]==-1:
                penalty+=1
            else:
                break
    return score-0.2*penalty

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
        self.currScores.append(evalBoard(np.array(board),score))
        self.currGameBoards.append(np.array(board))
    def recordGame(self):
	self.nGames+=1
        self.rawScores.append(0)
        length=len(self.currGameBoards)
        for i,board in enumerate(self.currGameBoards):
            self.allGameBoards.append(board)
            if i==length-1:
                reward=-5
            else:
                reward=self.currScores[i+1]-self.currScores[i]
            self.allScores.append(reward)
            if reward!=0:
                for j in range(1,decay_length):
                    self.allScores[-1-j]+=reward*np.power(gamma,j)
        self.currGameBoards=[]
        self.currScores=[]
    def scoreStats(self):
        return np.average(self.rawScores),np.var(self.rawScores),np.average(self.allScores)
    def saveRecord(self):
        npBoards = np.array(self.allGameBoards).reshape((len(self.allGameBoards),1,22,10))
        npScores = np.array(self.allScores)
        n=self.cycle%ncycle
        #while os.path.isfile('data/boards%d.npy' % n):
        #    n+=1
        np.save('data/boards%d.npy' % n,npBoards)
        np.save('data/scores%d.npy' % n,npScores)
