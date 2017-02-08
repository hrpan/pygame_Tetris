import numpy as np

class Record:
    def __init__(self):
	self.nGames=0
	self.scores=[]
	self.allGameBoards=[]
        self.currGameBoards=[]
    def recordBoard(self,board):
	self.currGameBoards.append(board)
    def recordGame(self,score):
	self.nGames+=1
	for board in self.currGameBoards:
	    self.allGameBoards.append(board)
	    self.scores.append(score)	
	self.currGameBoards=[]
    def saveRecord(self):
	npBoards = np.array(self.allGameBoards).reshape((len(self.allGameBoards),1,22,10))
	npScores = np.array(self.scores)
	np.save('data/boards',npBoards)
	np.save('data/scores',npScores)
