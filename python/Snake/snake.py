from sys import displayhook
from tarfile import BLOCKSIZE
from tkinter import LEFT, RIGHT
import pygame
import random
from enum import Enum
from collections import namedtuple



pygame.init()
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')
BLOCKSIZE=20
class SnakeGame:

    def __init__(self,w=640, h=480):
        self.w =w
        self.h=h
        #init display
        
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        #init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2 ,self.h/2)
        self.snake= [self.head, Point(self.head.x-BLOCKSIZE, self.head.y),
                    Point(self.head.x-(2*BLOCKSIZE), self.head.y)]
        self.score=0
        self.food=0
        self._place_food()


    def _place_food(self):
        x=random.randint(0, (self.w-BLOCKSIZE)//BLOCKSIZE)*BLOCKSIZE 
        y=random.randint(0, (self.w-BLOCKSIZE)//BLOCKSIZE)*BLOCKSIZE 
        self.food=Point(x,y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        #1. collect user input

        #2. move
        #3. check if game over
        #4. place new food or just move
        #5. update ui and clock

        
        #6. return game over and score
        game_over=False
        return game_over, self.score

    

if __name__=='__main__':
    game = SnakeGame()

    #game loop
    while True:
        game_over, score =game.play_step()
        if game_over==True:
            break
    
    print('Final score', score)

     
     
     
     
     
        #break if game over




    pygame.quit()


