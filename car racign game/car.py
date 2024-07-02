import pygame
import time
import random

pygame.init()

width = 1200
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Racing Game')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

carImg = pygame.image.load('car.png')
carImg = pygame.transform.scale(carImg, (50, 100))
car_width = 50

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width / 2), (height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def draw_score(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, (10, 10))

def game_loop():
    x = width * 0.45
    y = height * 0.8

    x_change = 0

    thing_startx = random.randrange(0, width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    score = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)

        draw_score(score)

        if x > width - car_width or x < 0:
            crash()

        if thing_starty > height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, width)
            score += 1
            thing_speed += 0.5
            thing_width += (score * 1.2)

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        pygame.display.update()
        pygame.time.Clock().tick(60)

game_loop()
pygame.quit()
quit()
