# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 03:57:47 2017

@author: Rick
"""
import sys, pygame
import vis
import core
import predict
import record


mode='AI'
#mode='PLAY'


pygame.init()
font = pygame.font.SysFont("monospace",16)

screen = vis.visInit()

game = core.Tetris()
opers=[game.rotateCCW,game.rotateCW,game.moveLeft,game.moveRight]
game.start()
tick=-1

if mode=='AI':
    aiGames=10
    cycle=int(sys.argv[1])
    ncycle=6
    pred=predict.Predict(cycle,ncycle)
    rec=record.Record(cycle,ncycle)

while 1:
    if game.over:
        if mode=='AI':
            rec.recordGame(game.score)
            stats=rec.scoreStats()
            sys.stdout.write('\rGame:%4d/%d   R-Score(avg/var): %.3f/%.3f   H-Score(avg): %.3f' % (rec.nGames,aiGames,stats[0],stats[1],stats[2]))
            sys.stdout.flush()
            if rec.nGames==aiGames:
                print ''
                break
            game.reset()
            game.start()
        else:
            break
    if tick==-1:
        tick = pygame.time.get_ticks()

    if mode=='PLAY':        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print ''
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
            pygame.time.delay(50)
        elif keys[pygame.K_RIGHT]:
            game.moveRight()
            pygame.time.delay(50)
        if keys[pygame.K_DOWN]:
            game.moveDown()
            pygame.time.delay(50)
        pygame.time.delay(10)
        if (pygame.time.get_ticks()-tick)>1500:
            tick = pygame.time.get_ticks()
            game.nextIter()
    elif mode=='AI':
        for i in range(3):
            boards=[game.previewBoard(i) for i in range(5)]
            bestOper=pred.predictOper(boards)
            if bestOper==4:
                break
            opers[bestOper]()
            rec.recordBoard(game.getState(),game.score)
        game.nextIter()


    game.clearLines()
    vis.drawScore(game,screen,font)
    vis.drawBoard(game,screen)
    
    pygame.display.flip()

if mode=='AI':
    rec.saveRecord()
