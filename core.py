# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 17:03:24 2017

@author: Rick
"""

from random import choice
from block import Block
import numpy as np
block_chars=['I','L','J','O','S','T','Z']

origin=[1,5]

board_h = 22
board_w = 10

dir_U = [-1,0]
dir_D = [1,0]
dir_L = [0,-1]
dir_R = [0,1]

class Tetris:
    def __init__(self):
        self.score=0
        self.board=[[0]*board_w for i in range(board_h)]
        self.curr_block=-1
        
    def reset(self):
        self.score=0
        self.board=[[0]*board_w for i in range(board_h)]
        self.curr_block=-1
        
    def start(self):
        self.over=False
        self.spawnBlock()
        
    def spawnBlock(self):
        self.curr_block=Block(choice(block_chars),origin)
        if self.checkViolation()==True:
            self.end()
            
    def end(self):
        self.over=True
        self.curr_block=-1

    def detachBlock(self):
        for pt in self.curr_block.getPTS():
            self.board[pt[0]][pt[1]]=1
        self.clearLines()
        self.spawnBlock()

    def nextIter(self):
        self.curr_block.move(dir_D)
        if self.checkViolation():
            self.curr_block.move(dir_U)
            self.detachBlock()
            
    def moveDrop(self):
        while not self.checkViolation():
            self.curr_block.move(dir_D)
        self.curr_block.move(dir_U)
        self.detachBlock()
        
    def moveDown(self):
        self.curr_block.move(dir_D)
        if self.checkViolation():
            self.curr_block.move(dir_U)
            
    def moveLeft(self):
        self.curr_block.move(dir_L)
        if self.checkViolation():
            self.curr_block.move(dir_R)

    def moveRight(self):
        self.curr_block.move(dir_R)
        if self.checkViolation()==True:
            self.curr_block.move(dir_L)
            
    def rotateCW(self):
        self.curr_block.rotateCW()
        if self.checkViolation()==True:
            self.curr_block.rotateCCW()
    
    
    def rotateCCW(self):
        self.curr_block.rotateCCW()
        if self.checkViolation()==True:
            self.curr_block.rotateCW()
                
    def checkViolation(self):
        for pt in self.curr_block.getPTS():
            if pt[0]<0 or pt[0]>=board_h or pt[1]<0 or pt[1]>=board_w:
                return True
            if self.board[pt[0]][pt[1]]==1:
                return True
        return False

    def clearLines(self):
        lineCount=0
        for line in range(board_h):
            if 0 not in self.board[line]:
                lineCount+=1
                for line_tmp in range(line,0,-1):
                    self.board[line_tmp]=self.board[line_tmp-1]
                    self.board[line_tmp-1]=[0]*board_w
        self.score+=lineCount

    def previewBoard(self,oper):
        """
        0:CCW
        1:CW
        2:LEFT
        3:RIGHT
        4:NULL
        """
        if oper==4:
            return self.getState()
        
        if oper==0:
            self.curr_block.rotateCCW()
        elif oper==1:        
            self.curr_block.rotateCW()
        elif oper==2:
            self.curr_block.move(dir_L)
        elif oper==3:
            self.curr_block.move(dir_R)
        
        if self.checkViolation():
            if oper==0:
                self.curr_block.rotateCW()
            elif oper==1:        
                self.curr_block.rotateCCW()
            elif oper==2:
                self.curr_block.move(dir_R)
            elif oper==3:
                self.curr_block.move(dir_L)            
            return self.getState()
        else:
            result = self.getState()
            if oper==0:
                self.curr_block.rotateCW()
            elif oper==1:        
                self.curr_block.rotateCCW()
            elif oper==2:
                self.curr_block.move(dir_R)
            elif oper==3:
                self.curr_block.move(dir_L)              
        return result

    def getState(self):
        if self.curr_block==-1:
            return self.board
        else:
            result=[x[:] for x in self.board]
            for pt in self.curr_block.getPTS():
                result[pt[0]][pt[1]]=1
            return result
