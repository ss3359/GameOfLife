import random 
import math 
import pandas as pd
import numpy as np
import pygame


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
grid=[[False for i in range(25)] for j in range(25)]


#Functions/Classes



def FillInGrid(grid): 
    for i in range(25): 
        for j in range(0,24): 
            I=random.randint(0,24)
            J=random.randint(0,24)
            grid[I][J]=True
def FillInSquares(i,j): 
    W=pygame.Rect(i,j,20,20)
    pygame.draw.rect(WINDOW,WHITE,W,0); 
def DrawEmptySquares(w,h): 
    for i in range(0,w,20): 
        for j in range(0,h,20): 
            R=pygame.Rect(i,j,20,20)
            pygame.draw.rect(WINDOW,WHITE,R)
            pygame.draw.rect(WINDOW,BLACK,R)
            pygame.draw.rect(WINDOW,RED,R,1)
            
def UpdateTheWindow(w,h): 
     DrawEmptySquares(w,h)
     pygame.display.update()

class GameOfLife: 
    def __init__(self,r,c,g):
        self.rows=r
        self.columns=c
        self.generations=g
        grid=[[]]
        FillInGrid(grid)
    def FillGrid(self,grid): 
        for i in range(0,self.rows): 
            for j in range(0,self.columns): 
                grid[i][j]=random.randint(0,1)
        self.grid=grid

    def DoAlgorithm(self,x,y): 
        alive=0
        NewGrid=[[]]
        for dx in range(-1,1): 
            for dy in range(-1,1): 
                if x==0 and y==0: 
                    continue
                nx=x+dx
                ny=y+dy
                if(0<=nx<self.rows and 0<=ny<self.columns): 
                    if(self.grid[nx][ny]==0):
                        alive+=1

        if grid[x][y]==0 and (alive < 2 or alive >3): 
            NewGrid[x][y]=1
        elif grid[x][y]==0 and (alive==2 or alive ==3): 
            NewGrid[x][y]=0
        elif grid[x][y]==1 and alive==3: 
            NewGrid[x][y]=0
        else: 
            NewGrid[x][y]=grid[x][y]
        return NewGrid

    def Generations(self):
        for n in range(self.generations): 
             NewGrid=[[]]
             for x in range(self.rows): 
                 for y in range(self.columns): 
                     NewGrid[x][y]=self.DoAlgorithm(x,y)[x][y]

             self.grid=NewGrid
             
  




#Run The Window
run=True

while(run): 
    CLOCK.tick(60)
    FillInGrid(grid)

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
             run=False
        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_ESCAPE: 
                run=False 
    #Update The Window
    UpdateTheWindow(WINDOWLENGTH,WINDOWHEIGHT)
#Exit Out Window
pygame.quit()
            