import numpy as np
import os.path
from config import Config

def floodfill(board,row,col,idx):
    shape=board.shape
    if row<0 or row>=shape[0] or col<0 or col>=shape[1]:
        return False
    else:
        if board[row][col]==0:
            board[row][col]=idx
            floodfill(board,row+1,col,idx)
            floodfill(board,row-1,col,idx)
            floodfill(board,row,col+1,idx)
            floodfill(board,row,col-1,idx)
            return True
    return False

def getHeights(board):
    height=np.array([0]*10)
    for i in range(board.shape[1]):
        pos=np.where(board[:,i]==1)[0]
        if len(pos)>0:
            height[i]=20-pos[0]
        else:
            height[i]=0
    return height 

def roughness(board):
    height=getHeights(board)
    #return np.sum(np.ediff1d(height)*np.ediff1d(height))
    return np.sum(np.absolute(np.ediff1d(height)))

def caves(board):
    height=20-getHeights(board)
    cave=0
    for col in range(board.shape[1]):
        for row in range(height[col],board.shape[0]):
            if board[row][col]==0 or board[row][col]==-1:
                cave+=1
    return cave        

def evalBoard(board,score):
    board=board[2:22,:]
    hole_idx=2
    penalty=0
    penalty+=roughness(board)
    #penalty+=0.1*np.average(getHeights(board))
    penalty+=caves(board)
    """
    for idx,x in np.ndenumerate(board):
        if x == 0 or x == -1:
            floodfill(board,idx[0],idx[1],hole_idx)
            #penalty+=np.sum(board==hole_idx)**2
            hole_idx+=1
    hole_idx-=2
    penalty+=0.3*hole_idx
    """
    return 10*score-penalty

"""
def evalBoard(board,score):
    return score
"""

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
