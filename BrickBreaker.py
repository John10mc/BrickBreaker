import pygame, sys, random, time
from pygame.locals import *

#Function for the direction and ball movement
def ballMovement():
    if(direction == 'topright'):
        ball.left = ball.left +  MOVESPEED
        ball.top = ball.top - MOVESPEED

    elif(direction == 'topleft'):
        ball.left = ball.left -  MOVESPEED
        ball.top = ball.top - MOVESPEED

    elif(direction == 'bottomleft'):
        ball.left = ball.left -  MOVESPEED
        ball.top = ball.top + MOVESPEED

    elif(direction == 'bottomright'):
        ball.left = ball.left +  MOVESPEED
        ball.top = ball.top + MOVESPEED

#Function to end the game
def terminate():
    pygame.quit()
    sys.exit()

#Function to wait for the user to push a button and run terminate
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                return

#Function to give the font its characteristics
def drawText(text, font, surface, x, y):
     textobj = font.render(text, 1, BLACK)
     textrect = textobj.get_rect()
     textrect.topleft = (x, y)
     surface.blit(textobj, textrect)

#Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (242, 15, 15)
MOVESPEED = 3
P_MOVESPEED = 10
direction = 'topright'
score=0

#Starts pygame and creates the windows
pygame.init()
windowSurface = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Brick Breaker")
windowSurface.fill(WHITE)
font = pygame.font.SysFont(None, 48)

#Start screen
drawText('Welcome', font, windowSurface, (370 / 3), (300 / 3))
drawText('Press a key to start.', font, windowSurface, (260 / 3) - 30, (400 / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

#This brings in the sounds for the game
gameOverSound = pygame.mixer.Sound('fail.wav')
cheer = pygame.mixer.Sound('cheer.wav')
scoreSound = pygame.mixer.Sound('score2.wav')
pygame.mixer.music.load('background2.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

#Start player position
plyGameStartx = random.randint (40, 360)
plyGameStarty = random.randint(350, 380)

#Ball start position
aiGameStartx = random.randint (40, 360)
aiGameStarty = random.randint(350, 380)

#Creates the player
player = pygame.Rect(plyGameStartx, plyGameStarty, 60, 10)
pygame.draw.rect(windowSurface, RED, player)

#Creates the ball
ball = pygame.Rect(aiGameStartx, aiGameStarty, 10, 10)
pygame.draw.rect(windowSurface, BLACK, ball)

#Creates the Top,bottom and sides of the game
top = pygame.Rect(0, 0, 400, 10)
pygame.draw.rect(windowSurface, BLACK, top)
lSide = pygame.Rect(0, 0, 10, 400)
pygame.draw.rect(windowSurface, BLACK, lSide)
rSide = pygame.Rect(390, 0, 10, 400)
pygame.draw.rect(windowSurface, BLACK, rSide)
bottom = pygame.Rect(0, 400, 400, 10)
pygame.draw.rect(windowSurface, BLACK, bottom)

#Creates the blocks to be hit
food = []
x = 15
y = 15

for row in range(1, 5):
    for column in range(1,7):
        block = pygame.Rect(x, y, 50, 20)
        food.append(block)
        x = x + 60

    if (row % 2 == 0):
        x = x - 370
    else:
        x = 25
    y = y + 25

#This part is for the movement of the player
moveRight = False
moveLeft  = False
moveDown  = False
moveUp    = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_UP:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
            if event.key == K_m:
                if pygame.mixer.music.play():
                    pygame.mixer.music.pause()
                elif pygame.mixer.music.pause():
                    pygame.mixer.music.play()


        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False


    if (moveRight):
        if (player.right <= 390):
            player.right = player.right + P_MOVESPEED
    elif (moveLeft):
        if (player.left >= 10):
            player.left = player.left - P_MOVESPEED
    elif (moveUp):
        if (player.top >= 360):
            player.top = player.top - P_MOVESPEED
    elif (moveDown):
        if (player.bottom <= 380):
            player.bottom = player.bottom + P_MOVESPEED


    windowSurface.fill(WHITE)

#This draws all the components of the game
    for block in food:
        pygame.draw.rect(windowSurface, GREEN, block)

    pygame.draw.rect(windowSurface, BLACK, ball)
    pygame.draw.rect(windowSurface, RED, player)
    pygame.draw.rect(windowSurface, BLACK, top)
    pygame.draw.rect(windowSurface, BLACK, lSide)
    pygame.draw.rect(windowSurface, BLACK, rSide)

    drawText('Score: %s' % (score), font, windowSurface, 50, 230)

#This code if for when the player hits the bottom and looses
    if  ball.colliderect(bottom) :
        drawText('Game Over', font, windowSurface, (160 / 3), (400 / 3))
        drawText('Press a key to end.', font, windowSurface, (400 / 3) - 80, (400 / 3) + 50)
        pygame.display.update()
        pygame.mixer.music.stop()
        gameOverSound.play()
        waitForPlayerToPressKey()
        terminate()

#this is for when the player hits all the blocks
    if score == 24:
        drawText('Perfect Score', font, windowSurface, (160 / 3), (400 / 3))
        drawText('Press a key to end.', font, windowSurface, (400 / 3) - 80, (400 / 3) + 50)
        pygame.display.update()
        pygame.mixer.music.stop()
        cheer.play()
        waitForPlayerToPressKey()
        terminate()

    ballMovement()


    if ball.colliderect(rSide):
        if direction == 'topright':
            direction = 'topleft'
        if direction == 'bottomright':
            direction = 'bottomleft'

    elif ball.colliderect(lSide):
        if direction == 'bottomleft':
            direction = 'bottomright'
        if direction == 'topleft':
            direction = 'topright'

    elif ball.colliderect(top):
        if direction == 'topright':
            direction = 'bottomright'
        if direction == 'topleft':
            direction = 'bottomleft'

    if player.colliderect(ball):
        if direction == 'bottomleft':
            direction = 'topleft'
        if direction == 'bottomright':
            direction = 'topright'


    for block in food:
        if ball.colliderect(block):
            if(direction == 'topright'):
                direction = 'bottomright'
                food.remove(block)
            elif(direction == 'topleft'):
                direction = 'bottomleft'
                food.remove(block)
            elif(direction == 'bottomleft'):
                direction = 'bottomright'
                food.remove(block)
            elif(direction == 'bottomright'):
                direction = 'bottomleft'
                food.remove(block)
            score = score + 1
            MOVESPEED = MOVESPEED + 0.2
            scoreSound.play()


    pygame.display.update()
    time.sleep(0.02)

