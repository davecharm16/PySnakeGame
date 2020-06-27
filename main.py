import pygame
import time
import random
import math


def distance(x1, x2, y1, y2):
    dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return dist


# initialize pygame
pygame.init()

# SET_WINDOW SIZE
window_size = 632, 632

snake_body = []
snakeBodyX = []
snakeBodyY = []

# block image for snake
snake_image = pygame.image.load('snakebody.png')
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
snake_head = pygame.image.load('snakeHead.png')
# Call screen method
screen = pygame.display.set_mode(window_size)

'''snake movement'''
snake_headX = 448
snake_headY = 416
snake_xChange = 0
snake_yChange = 0

'''snake food'''
_food = pygame.image.load('food.png')
foodX = random.randint(0, 568)
foodY = random.randint(0, 568)

snakeBodyX.append(snake_headX)
snakeBodyY.append(snake_headY)

'''Setting the Background'''
background = pygame.image.load('background1.png').convert()


def snake_headMovement(x, y, ):
    screen.blit(snake_head, (x, y))


def food(x, y):
    screen.blit(_food, (x, y))


def snakebodyMovement(x, y, i):
    screen.blit(snake_body[i], (x, y))


def collide(x1, x2, y1, y2):
    global foodX, foodY
    global score
    if distance(x1, x2, y1, y2) <= 32:
        foodX = random.randint(0, 568)
        foodY = random.randint(0, 568)
        score += 1
        return True


def collision_with_Body(x1, x2, y1, y2):
    if distance(x1, x2, y1, y2) > 0:
        return False
    else:
        return True


''' setting score '''
score = 0


def setScore():
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render("SCORE : " + str(score), 1, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = 124, 32
    screen.blit(text, textRect)


in_game = False
running = True
# Loop the screen

'''Testing the Launcher'''


def launcher():
    not_in_game = True
    global running
    global in_game
    while not_in_game:
        font = pygame.font.Font('TanglewoodTales.ttf', 45)
        text1 = font.render("Press KEY \"N\" to Start the Game", 1, (255, 255, 255), (0,200,0))
        text2 = font.render("Snake", 1, (255, 255, 255), (0,200,0))
        textrect2 = text2.get_rect()
        textrect1 = text1.get_rect()
        textrect1 = 20,300
        textrect2 = 250, 250
        screen.blit(background, (0, 0))
        screen.blit(text1, textrect1)
        screen.blit(text2, textrect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                not_in_game = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    not_in_game = False
                    in_game = True
                    running = True
        pygame.display.update()

def game_Over():
    global snake_headX
    global snake_headY
    font = pygame.font.Font('freesansbold.ttf', 80)
    text2 = font.render("Game Over", 1, (255, 255, 255), (0, 200, 0))
    textrect2 = text2.get_rect()
    textrect2 = 100, 300
    screen.blit(text2, textrect2)
    snake_headY,snake_headX = 2000, 2000




while running:
    '''Set the screen color'''
    screen.fill((0, 192, 0))
    if in_game is False:
        launcher()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake_yChange = -30
                snake_xChange = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake_yChange = 30
                snake_xChange = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake_xChange = -30
                snake_yChange = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake_xChange = 30
                snake_yChange = 0
        if event.type == pygame.KEYUP:
            snake_xChange = snake_xChange
            snake_yChange = snake_yChange

    screen.blit(background, (0, 0))
    setScore()

    snakeBodyX.append(snake_headX)
    snakeBodyY.append(snake_headY)
    snake_headX += snake_xChange
    snake_headY += snake_yChange
    snake_headMovement(snake_headX, snake_headY)

    if collide(snake_headX, foodX, snake_headY, foodY):
        foodX = random.randint(0, 568)
        foodY = random.randint(0, 568)
        snake_body.append(snake_image)
    if snake_headX > 608 or snake_headX < 20 or snake_headY > 608 or snake_headY < 20:
        game_Over()
        # in_game = False

    if len(snake_body) > 0:
        for i in range(len(snake_body)):
            snakebodyMovement(snakeBodyX[len(snakeBodyX) - (i + 1)], snakeBodyY[len(snakeBodyY) - (i + 1)], i)
            if collision_with_Body(snake_headX, snakeBodyX[len(snakeBodyX) - (i + 1)], snake_headY,
                                   snakeBodyY[len(snakeBodyY) - (i + 1)]):
                running = False

    food(foodX, foodY)
    time.sleep(0.2)
    pygame.display.update()
