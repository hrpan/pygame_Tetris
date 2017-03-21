import numpy as np
import os.path
from config import Config

"""
def evalBoard(board,score):
    penalty=0
    for i,j in np.transpose(np.where(board==1)):
        for k in range(i+1,22):
            if board[k][j]==0 or board[k][j]==-1:
                penalty+=1
            else:
                break
    return score-0.2*penalty
"""

def evalBoard(board,score):
    return score

class Record:
    def __init__(self,cycle):
        cfg=Config()
        self.cycle=cycle
        self.ncycle=cfg.ncycle
        self.nGames=0
        self.allScores=[]
        self.rawScores=[]
        self.currScores=[]
        self.allGameBoards=[]
        self.currGameBoards=[]
        self.allActions=[]
        self.currActions=[]
    def recordBoard(self,board,score,action):
        self.currScores.append(evalBoard(np.array(board),score))
        self.currGameBoards.append(np.array(board))
        self.currActions.append(action) 
    def recordGame(self,score):
        self.nGames+=1
        self.rawScores.append(score)

        for i,board in enumerate(self.currGameBoards):
            self.allGameBoards.append(board)
            self.allActions.append(self.currActions[i])
            if i==len(self.currGameBoards)-1:
                reward=-1
            else:
                reward=self.currScores[i+1]-self.currScores[i]

            self.allScores.append(reward)
        self.currGameBoards=[]
        self.currScores=[]
        self.currActions=[]
    def scoreStats(self):
        return np.average(self.rawScores),np.var(self.rawScores),np.average(self.allScores)

    def saveRecord(self):
        npBoards = np.array(self.allGameBoards,dtype='int8').reshape((len(self.allGameBoards),22,10,1))[:,2:22,:,:]
        npScores = np.array(self.allScores,dtype='float32')
        nprScores = np.array(self.rawScores)
        npActions = np.array(self.allActions,dtype='int8')
        n=self.cycle%self.ncycle
        np.save('data/boards%d.npy' % n,npBoards)
        np.save('data/scores%d.npy' % n,npScores)
        np.save('data/rScores%d.npy' % n,nprScores)
        np.save('data/actions%d.npy' % n,npActions)
