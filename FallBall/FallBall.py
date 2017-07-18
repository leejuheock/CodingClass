import sys, pygame
pygame.init()

size = width,height = 320, 240
bgcolor = 310, 20, 150
gravity = 10

screen - pygame.display.set_mode(size)

class Ball():
   
    speed_x = 0
    speed_y = 0


    def __init__(self):  
    ball = pygame.image.load("ball.bmp")
    ballrect = ball.get_rect()
 
