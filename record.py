import numpy as np
import os.path

gamma=0.8
decay_length=30
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
    def __init__(self,cycle,ncycle):
        self.cycle=cycle
        self.ncycle=ncycle
        self.nGames=0
        self.allScores=[]
        self.rawScores=[]
        self.currScores=[]
        self.allGameBoards=[]
        self.currGameBoards=[]

    def recordBoard(self,board,score):
        self.currScores.append(evalBoard(np.array(board),score))
        self.currGameBoards.append(np.array(board))

    def recordGame(self,score):
        self.nGames+=1
        self.rawScores.append(score)

        for i,board in enumerate(self.currGameBoards):
            self.allGameBoards.append(board)

            if i==len(self.currGameBoards)-1:
                reward=-5
            else:
                reward=self.currScores[i+1]-self.currScores[i]

            self.allScores.append(reward)
            if reward!=0:
                length = min(decay_length,len(self.allScores))
                for j in range(1,length):
                    self.allScores[-1-j]+=reward*np.power(gamma,j)

        self.currGameBoards=[]
        self.currScores=[]
    def scoreStats(self):
        return np.average(self.rawScores),np.var(self.rawScores),np.average(self.allScores)

    def saveRecord(self):
        npBoards = np.array(self.allGameBoards).reshape((len(self.allGameBoards),1,22,10))
        npScores = np.array(self.allScores)
        nprScores = np.array(self.rawScores)
        n=self.cycle%ncycle
        np.save('data/boards%d.npy' % n,npBoards)
        np.save('data/scores%d.npy' % n,npScores)
        np.save('data/rScores%d.npy' % n,nprScores)
