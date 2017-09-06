import sys, pygame
import random
import time

pygame.init()

size = width,height = 1024, 600
bgcolor = 150, 30, 150
gravity = 1
fps = 27
max_ball_count = 6
out_delay = 0.7
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Ball():
   
    speed_x = 0
    speed_y = 0
    power = 0.9
    is_out = False

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
        if self.image_location.left > width or self.image_location.right < 0:
            self.is_out = True

class Person():
  
    def __init__(self):
        self.image = pygame.image.load("person2.png")
        self.image_location = self.image.get_rect()
        start_x = (width - self.image_location.width) / 2
        start_y = height - self.image_location.height
        self.image_location = self.image_location.move((start_x, start_y))

    def move_left(self):
        self.image_location = self.image_location.move((-30,0))
    def move_right(self):
        self.image_location = self.image_location.move((30,0))
    def move_up(self):
        self.image_location == self.image_location.move((0, 30))
ball_list = []
person = Person()
is_dead = False
while True:
     # fps 설정
     clock.tick(fps)
     
     if is_dead:
         time.sleep(out_delay)
         ball_list = []
         person = Person()
         is_dead = False
         continue
     
     # 이벤트 제어
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
              person.move_left()
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
              person.move_right()
         elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
              person.move_up()

     # 게임 상태 업데이트

        #len 리스트나 튜플안에 있는 객체를 세주는것. 
     if len(ball_list) < max_ball_count:
        if random.randint(0,100) < 5:
            ball_list.append(Ball(0, random.randint(0, 300), random.randint(8, 10)))       

     # image_location 사각형.     
      
     # 공을 움직이는 부분
     i = 0    
     for b in ball_list:
         b.move()
         if b.is_out:
             del ball_list[i]
         i = i + 1
     #인플레이트 확장하다.
         
         hitbox = b.image_location.inflate((-30,-30))
         if hitbox.colliderect(person.image_location):
             is_dead = True
     if  is_dead:
         font = pygame.font.Font(None, 36)
         text = font.render("Out!",0,(0, 0, 0))
         textpos = text.get_rect(centerx=width / 2, centery=height / 2)
         screen.blit(text, textpos)
             
      # 화면 업데이트
     screen.fill(bgcolor)
     for b in ball_list:
         screen.blit(b.image, b.image_location)
     if person:
         screen.blit(person.image, person.image_location)
     pygame.display.flip()
