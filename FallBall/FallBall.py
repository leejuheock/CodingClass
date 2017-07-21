import sys, pygame
pygame.init()

size = width,height = 1024, 600
bgcolor = 150, 0, 150
gravity = 10
fps = 23

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Ball():
   
    speed_x = 0
    speed_y = 0
    power = 0.9
    
    #init = CHOGIHWA
    def __init__(self, start_x, start_y):  
        self.image = pygame.image.load("ball.bmp")
        self.image_location = self.image.get_rect()
        self.image_location = self.image_location.move((start_x, start_y))
        

    def move(self): 
        self.speed_y = self.speed_y + gravity
        if self.image_location.bottom > height:
            self.speed_y = int(-self.power * (self.speed_y - gravity))
            self.image_location = self.image_location.move((self.speed_x, 0))
            self.image_location.bottom = height
        else:
            self.image_location = self.image_location.move((self.speed_x, self.speed_y))

ball_list = []
ball_list.append(Ball(200,0))
ball_list.append(Ball(200,0))
ball_list.append(Ball(200,0))
while True:
     # fps setting
     clock.tick(fps)
     
     # event wpdj
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
     # Game staitus  update
     for b in ball_list
         b.move()
     ball_list[0].move()
     # HwaMyun update 
     screen.fill(bgcolor)
     for b in ball_list:
         screen.blit(b.image, b.image_location)
      pygame.display.flip()
