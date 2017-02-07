# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 04:50:24 2017

@author: Rick
"""


"""
BLOCKS


block = {
'I': [[0,0],[0,1],[4,1],[4,0]],
'J': [[0,1],[0,2],[3,2],[3,0],[2,0],[2,1]],
'L': [[0,0],[0,2],[3,2],[3,1],[1,1],[1,0]],
'O': [[0,0],[0,2],[2,2],[2,0]],
'S': [[0,0],[0,1],[1,1],[1,2],[3,2],[3,1],[2,1],[2,0]],
'T': [[0,1],[0,2],[3,2],[3,1],[2,1],[2,0],[1,0],[1,1]],           
'Z': [[0,1],[0,2],[2,2],[2,1],[3,1],[3,0],[1,0],[1,1]]}
"""
block = {
 'I': [[0,0],[0,1],[0,2],[0,3]],
 'J': [[0,0],[0,1],[0,2],[1,2]],
 'L': [[1,0],[0,0],[0,1],[0,2]],
 'O': [[0,0],[0,1],[1,1],[1,0]],
 'S': [[1,0],[1,1],[0,1],[0,2]],
 'T': [[0,0],[0,1],[1,1],[0,2]],
 'Z': [[0,0],[0,1],[1,1],[1,2]]
         }
def ptSum(p1,p2):
    return [p1[0]+p2[0],p1[1]+p2[1]]

def ptSub(p1,p2):
    return [p1[0]-p2[0],p1[1]-p2[1]]

def r_CW(p,a):
    tmp = ptSub(p,a)
    return ptSum(a,[-tmp[1],tmp[0]])


def r_CCW(p,a):
    tmp = ptSub(p,a)
    return ptSum(a,[tmp[1],-tmp[0]])
      
class Block:
    def __init__(self,c,pos):
        self.shape=c
        self.pos = pos
        self.pts = [x for x in block[c]]
        
    def getCenter(self):
        """
        c=[0.0,0.0]
        for pt in self.pts:
            c=ptSum(c,pt)
        c[0]=int(c[0]/len(self.pts))
        c[1]=int(c[1]/len(self.pts))
        return c
        """
        return self.pts[1]
    def getPTS(self):
        center = self.getCenter()
        return [ptSum(self.pos,ptSub(pt,center)) for pt in self.pts]
                
    def move(self,direction):
        self.pos=ptSum(self.pos,direction)
        
    def rotateCW(self):
        center = self.getCenter()
        if self.shape!='O':
            self.pts=[r_CW(pt,center) for pt in self.pts]
                  
    def rotateCCW(self):
        center = self.getCenter()
        if self.shape!='O':
            self.pts=[r_CCW(pt,center) for pt in self.pts]
            