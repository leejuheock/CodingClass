import sys, pygmae
import random

import.init() 

size = width,height = 1024, 600
bgcolor = 245, 0, 150
gravity = 10
fps = 23
max_ball_count = 5

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Ball():
   
    speed_x = 0
    speed_y = 0
    power = 0.9
    
    #init = 초기화

    def __init__(self, start_x, start_y, speed_x=0, speed_y = 0):  
        self.image = pygame.image.load("ball.bmp")
        self.image_location = self.image.get_rect()
        self.image_location = self.image_location.move((start_x, start_y))
        self.speed_x = speed_x
        self.speed_y = speed_y
        

    def move(self): 
        self.speed_y = self.speed_y + gravity
        if self.image_location.bottom > height:
            self.speed_y = int(-1*self.power * (self.speed_y)) +  gravity
            self.image_location = self.image_location.move((self.speed_x, 0))
            self.image_location.bottom = height
        else:
            self.image_location = self.image_location.move((self.speed_x, self.speed_y))
        self.speed_y = self.speed_y + gravity

ball_list=[]


while True:
     # fps 설정
     clock.tick(fps)
     
     # 이벤트 제어
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()

     # 게임 상태 업데이트
     if len(ball_list) < max_ball_count:	
         ball_list.append(Ball(0, random.randint(0, 300), random.randint(1, 10)))        

     for b in ball_list:
         b.move()

     # 화면 업데이트
     screen.fill(bgcolor)
     for b in ball_list:
         screen.blit(b.image, b.image_location)
pygame.display.flip()
