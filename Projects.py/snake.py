# importng libraries
import pygame
import time
import random

snake_speed=15

# Window size
window_x=720
window_y=480

# defining colors
black=pygame.color(0,0,5)
white=pygame.color(255,255,255)
red=pygame.color(255,0,0)
green=pygame.color(0,0,255)
blue=pygame.color(0,255,0)

# intialize pygame
pygame.init()

# intialize game window
pygame.display.set.caption('snaKe')
game_window=pygame.display.set_mode(window_x,window_y)

# FPS (frame per second) controller
fps=pygame.time.clock()

# defining snake default position
snake_position=[100,50]

# defining first 4 block of snake body
snake_body=[[100,50],[90,50],[80,50],[70,50]]

# fruit position
fruite_position=[random.randrange(1,(window_x)),random.randrange(1,(window_y))]
fruit_spawn=True

# setting default snake direction
# towards right
direction='RIGHT'
change_to=direction

# intial score
score=0

# displaying score function
def show_score(choice,color,font,size):

    # creating font object score_font
    score_font=pygame.font.SysFont(font,size)

    # create def




