import random 
import math 
import pandas as pd
import numpy as np
import pygame
import time


#Initalize Pygame
pygame.init() 


#Constants
WINDOWLENGTH=500
WINDOWHEIGHT=500

#Colors
RED=(255, 0, 0),  # Red
GREEN=(0, 255, 0),  # Green
BLUE=(0, 0, 255),  # Blue
YELLOW=(255, 255, 0),  # Yellow
CYAN=(0, 255, 255),  # Cyan
MAGENTA=(255, 0, 255),  # Magenta
BLACK=(0, 0, 0),  # Black
WHITE=(255, 255, 255),  # White
GRAY=(128, 128, 128),  # Gray

WINDOW=pygame.display.set_mode((WINDOWLENGTH,WINDOWHEIGHT), 0,32)
pygame.display.set_caption("Game Of Life")
CLOCK=pygame.time.Clock()

#Variables
# grid=[[False for i in range(25)] for j in range(25)]


#Functions/Classes

class GameOfLife: 
    def __init__(self,r,c,g):
        self.rows=r
        self.columns=c
        self.generations=g
        self.grid=[[0 for j in range(self.columns)] for i in range(self.rows)]
    def FillGrid(self): 
        for i in range(0,self.rows): 
            for j in range(0,self.columns): 
                self.grid[i][j]=random.randint(0,1)
        

    def DoAlgorithm(self,x,y): 
        alive=0
        NewGrid=[[0 for j in range(self.columns)] for i in range(self.rows) ]
        for dx in range(-1,2): 
            for dy in range(-1,2): 
                if dx==0 and dy==0: 
                    continue
                nx=x+dx
                ny=y+dy
                if(0<=nx<self.rows and 0<=ny<self.columns): 
                    if(self.grid[nx][ny]==0):
                        alive+=1

        if self.grid[x][y]==1: 
            if(alive<2 or alive>3):
                NewGrid[x][y]=0
            else:
                NewGrid[x][y]=1
        else: 
            if alive==3:
                NewGrid[x][y]=1        
        return NewGrid

    def DrawGrid(self):
        for x in range(self.rows): 
                 for y in range(self.columns): 
                     W=pygame.Rect(x*20,y*20,20,20)
                     if self.grid[x][y]==1:
                         pygame.draw.rect(WINDOW,WHITE,W)
                         pygame.draw.rect(WINDOW,BLACK,W,1)
                        
                     else: 
                       pygame.draw.rect(WINDOW,BLACK,W)
                       pygame.draw.rect(WINDOW,RED,W,1)
        pass
    def Generations(self):
        for n in range(self.generations): 
             NewGrid=[[0 for j in range(self.columns)] for i in range(self.rows)]
             for x in range(self.rows): 
                 for y in range(self.columns): 
                     NewGrid[x][y]=self.DoAlgorithm(x,y)[x][y]
             self.grid=NewGrid
             self.DrawGrid()
             pygame.display.update()
              
def FillInSquares(i,j): 
    W=pygame.Rect(i,j,20,20)
    pygame.draw.rect(WINDOW,WHITE,W,0); 
def DrawEmptySquares(w,h): 
    for i in range(0,w,20): 
        for j in range(0,h,20): 
            R=pygame.Rect(i,j,20,20)
            pygame.draw.rect(WINDOW,BLACK,R)
            pygame.draw.rect(WINDOW,RED,R,1)
            
def UpdateTheWindow(): 
     g.Generations()

#Run The Window
run=True
g=GameOfLife(25,25,500)
g.FillGrid()

while(run): 
    time.sleep(0.1)
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
             run=False
        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_ESCAPE: 
                run=False 
    #Update The Window
    UpdateTheWindow()
#Exit Out Window
pygame.quit()
            