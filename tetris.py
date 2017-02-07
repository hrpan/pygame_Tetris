# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 03:57:47 2017

@author: Rick
"""

import sys, pygame
import vis
import core

game = core.Tetris()

pygame.init()
font = pygame.font.SysFont("monospace",16)

screen = vis.visInit()

game.start()

tick=-1

while 1:
    if game.curr_block==-1:
        break
    if tick==-1:
        tick = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                game.moveLeft()
            if event.key==pygame.K_RIGHT:
                game.moveRight()
            if event.key==pygame.K_DOWN:
                game.moveDown()
            if event.key==pygame.K_z:
                game.rotateCCW()
            if event.key==pygame.K_x:
                game.rotateCW()
            if event.key==pygame.K_SPACE:
                game.moveDrop()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game.moveLeft()
    elif keys[pygame.K_RIGHT]:
        game.moveRight()
    if keys[pygame.K_DOWN]:
        game.moveDown()

    pygame.time.delay(30)
    vis.drawScore(game,screen,font)
    vis.drawBoard(game,screen)
    if (pygame.time.get_ticks()-tick)>1500:
        tick = pygame.time.get_ticks()
        game.nextIter()
    pygame.display.flip()