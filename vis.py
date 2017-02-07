# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 04:15:44 2017

@author: Rick
"""

import pygame

pygame.init()

font = pygame.font.SysFont("monospace",16)
size = width, height = 400,500

o = 20,30

cell = 10,22
vis_cell = 10,20
cell_w = 20

tbox = cell[0]*cell_w, cell[1]*cell_w
v_tbox = [o[0]-1,o[1]-1,vis_cell[0]*cell_w+2,vis_cell[1]*cell_w+2]


"""
COLOR
"""
white=255,255,255
black=0,0,0


"""
DRAW FUNCS
"""
def visInit():
    screen = pygame.display.set_mode(size)
    screen.fill(black)
    label_Score = font.render("SCORE:",1,white)
    screen.blit(label_Score,(300,200)) 
    pygame.draw.rect(screen,white,v_tbox,1)
    return screen

def boxPTS(i,j):
    if i<2:
        return (0,0,0,0)
    else:
        return [o[0]+j*cell_w,
                o[1]+(i-2)*cell_w,
                cell_w,
                cell_w]


def drawScore(game,screen,font):    
    text_Score = font.render('%5d' % game.score,1,white,black)    
    screen.blit(text_Score,(300,240))    
    
def drawBoard(game,screen):
    board = game.board
    block = game.curr_block
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==1:
                pygame.draw.rect(screen,white,boxPTS(i,j),0)
            else:
                pygame.draw.rect(screen,black,boxPTS(i,j),0)
    if block!=-1:
        for box in block.getPTS():
            pygame.draw.rect(screen,white,boxPTS(box[0],box[1]),0)
                