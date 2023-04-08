# import the pygame module
import pygame

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *

# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Create the surface, give dimensions and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)

        # Draw the ellipse onto the surface
        pygame.draw.ellipse(self.image, (255, 0, 0), [
                            0, 0, width, height], 100)

    def move(self, x, y):
        gameDisplay.blit(self.image, (x, y))


class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Square, self).__init__()

        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((100, 15))

        # Define the color of the surface using RGB color coding.
        self.surf.fill(color)
        self.rect = self.surf.get_rect()

    def move(self, x, y):
        gameDisplay.blit(self.surf, (x, y))


pygame.init()

w = 800
h = 600

gameDisplay = pygame.display.set_mode((w, h))
# w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption('Bar Game MultiPlayer')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False


bar1_x = (w * 0.45)
bar1_y = (h * 0.8)
bar1_x_change = 0
bar1_y_change = 0
bar2_x = (w * 0.45)
bar2_y = (h * 0.2)
bar2_x_change = 0
bar2_y_change = 0
ball_x_change = 0
ball_y_change = 0
bar1 = Square(BLUE)
bar2 = Square(GREEN)
ball = Ball(15, 15)
ball_x = (w * 0.45+45)
ball_y = (h * 0.8-15)
started = False
font = pygame.font.Font(None, 32)
score1 = 0
score2 = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bar1_x_change = -5
            elif event.key == pygame.K_RIGHT:
                bar1_x_change = 5
            elif event.key == pygame.K_UP:
                bar1_y_change = -5
            elif event.key == pygame.K_DOWN:
                bar1_y_change = 5
            elif event.key == pygame.K_SPACE:
                if ball_y > h//2 and not started:
                    ball_y_change = -3
                    started = True
                elif not started:
                    ball_y_change = 3
                    started = True
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT,  pygame.K_RIGHT]:
                bar1_x_change = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                bar1_y_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bar2_x_change = -5
            elif event.key == pygame.K_d:
                bar2_x_change = 5
            elif event.key == pygame.K_w:
                bar2_y_change = -5
            elif event.key == pygame.K_s:
                bar2_y_change = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a,  pygame.K_d]:
                bar2_x_change = 0
            elif event.key in [pygame.K_w, pygame.K_s]:
                bar2_y_change = 0
    bar1_x += bar1_x_change
    bar1_y += bar1_y_change
    bar2_x += bar2_x_change
    bar2_y += bar2_y_change
    ball_y += ball_y_change
    ball_x += ball_x_change

    if bar1_x > w-bar1.rect.width:
        bar1_x = w-bar1.rect.width
    elif bar1_x < 0:
        bar1_x = 0
    if bar1_y < h//2+1+15:
        bar1_y = h//2+1+15
    elif bar1_y > h-bar1.rect.height:
        bar1_y = h-bar1.rect.height
    if bar2_x > w-bar2.rect.width:
        bar2_x = w-bar2.rect.width
    elif bar2_x < 0:
        bar2_x = 0
    if bar2_y > h//2-1-2*bar1.rect.height:
        bar2_y = h//2-1-2*bar1.rect.height
    elif bar2_y < 0:
        bar2_y = 0
    if not started and ball_y > h//2:
        ball_x = bar1_x+45
        ball_y = bar1_y-15
    elif not started:
        ball_x = bar2_x+45
        ball_y = bar2_y+15
    if started:
        if (ball_x >= (bar1_x) and ball_x <= (bar1_x+bar1.rect.width)) and (ball_y >= bar1_y and ball_y <= (bar1_y+bar1.rect.height)):
            ball_y_change = -3
            if bar1_x_change == 0:
                ball_x_change = 0
            else:
                ball_x_change = (bar1_x_change/abs(bar1_x_change))*2

        if (ball_x >= (bar2_x) and ball_x <= (bar2_x+bar2.rect.width)) and (ball_y >= bar2_y and ball_y <= (bar2_y+bar2.rect.height)):
            ball_y_change = 3
            if bar2_x_change == 0:
                ball_x_change = 0
            else:
                ball_x_change = -(bar2_x_change/abs(bar2_x_change))*2
        ball_y += ball_y_change
        ball_x += ball_x_change
    if ball_x > w or ball_x < 0:
        ball_x_change = -ball_x_change
    if ball_y < 0:

        ball_x = (w * 0.45+45)
        ball_y = (h * 0.8-15)
        bar1_x = (w * 0.45)
        bar1_y = (h * 0.8)
        bar2_x = (w * 0.45)
        bar2_y = (h * 0.2)
        ball_x_change = 0
        ball_y_change = 0
        started = False
        score1 += 1
    elif ball_y > h:
        ball_x = (w * 0.45+45)
        ball_y = (h * 0.2+15)
        bar1_x = (w * 0.45)
        bar1_y = (h * 0.8)
        bar2_x = (w * 0.45)
        bar2_y = (h * 0.2)
        ball_x_change = 0
        ball_y_change = 0
        started = False
        score2 += 1
    gameDisplay.fill(white)
    pygame.draw.line(gameDisplay, BLACK, [0, h//2-1], [w, h//2-1], 2)
    score1_surf = font.render('Player A: '+str(score1), True, BLUE, WHITE)
    score2_surf = font.render('Player B: '+str(score2), True, GREEN, WHITE)
    bar1.move(bar1_x, bar1_y)
    bar2.move(bar2_x, bar2_y)
    ball.move(ball_x, ball_y)
    gameDisplay.blit(score1_surf, (0, h-20))
    gameDisplay.blit(score2_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
