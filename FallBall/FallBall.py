import sys, pygame
pygame.init()

size = width,height = 1024, 600
bgcolor = 150, 0, 150
gravity = 10

screen = pygame.display.set_mode(size)

class Ball():
   
    speed_x = 0
    speed_y = 0
    power = 0.9

    def __init__(self):  
        self.image = pygame.image.load("ball.bmp")
        self.image_location = self.image.get_rect()
    def move(self): 
        self.speed_y = self.speed_y + gravity
        if self.image_location.bottom > height:
            self.speed_y = int(-self.power * (self.speed_y - gravity))
        self.image_location = self.image_location.move((self.speed_x, self.speed_y))

ball_1 = Ball()

while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
     screen.fill(bgcolor)
     ball_1.move()
     screen.blit(ball_1.image, ball_1.image_location)
     pygame.display.flip()
