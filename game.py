import pygame,random,math
pygame.init()
SCREEN_WIDTH = 800

SCREEN_HEIGHT = 500

PLAYER_START_X = 370

PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50

ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 4

ENEMY_SPEED_Y = 40

BULLET_SPEED_Y = 10

COLLISION_DISTANCE = 27

# Initialize Pygame

pygame.init()

# Create the screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background

background = pygame.image.load('bg game.jpg')

# Caption and Icon

pygame.display.set_caption("Space Invader")

# Player

playerImg = pygame.image.load('images-removebg-preview.png')

playerX = PLAYER_START_X

playerY = PLAYER_START_Y

playerX_change = 0

# Enemy

enemyImg = []

enemyX = []

enemyY = []

enemyX_change = []

enemyY_change = []

num_of_enemies = 10

for _i in range(num_of_enemies):

    enemyImg.append(pygame.image.load('enemy.png'))

    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) # 64 is the size of the enemy

    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))

    enemyX_change.append(ENEMY_SPEED_X)

    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet

bulletImg = pygame.image.load('bullet.png')

bulletX = 0

bulletY = PLAYER_START_Y

bulletX_change = 0

bulletY_change = BULLET_SPEED_Y

bullet_state = "ready"

# Score

score_value = 0

font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
textX = 10

textY = 10
def show_score(x,y):
    score = font.render("Score: "+ str(score_value),True,pygame.Color("white"))
    screen.blit(score,(x,y))
def game_over():
    overtext = over_font.render("Game OVER", True,pygame.Color("white"))
    screen.blit(overtext,(400,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def bulet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x+16,y+10))
def collide(eX,ey,bX,bY):
    distance = math.sqrt((eX - bX)**2 + (ey - bY)**2)
    return distance < COLLISION_DISTANCE
