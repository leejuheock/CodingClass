import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [20, 20]
black = 130, 130, 110

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        if event.type == pygame.K_DOWN:
           x_plus = 2 if speed [0] > 0 else -2
           y_plus = 2 if speed[1] > 0 else -2
           if event.key == pygame.K_UP:
              speed = [speed[0] + x_plus, speed[1] + y_plus]
           if event.key == pygame.K_DOWN:
              speed = [speed[0] - x_plus, speed[1]- y_plus]
            
           
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
