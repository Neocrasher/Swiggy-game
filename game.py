import pygame,random,math
pygame.init()
SCREEN_WIDTH = 800

SCREEN_HEIGHT = 500

PLAYER_START_X = 370

PLAYER_START_Y = 280

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

playerImg = pygame.image.load('player.png')

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
running = True
while running:
    screen.fill(pygame.Color("black"))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerX_change = -5
            if event.key == pygame.K_a:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bulet(bulletX,bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_a, pygame.K_d]:
            playerX_change = 0
    playerX = playerX + playerX_change
    playerX = max(0,min(playerX, SCREEN_WIDTH - 64)) 
    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] = enemyX[i] + enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] = enemyX_change[i] * -1
            enemyY[i] = enemyY[i] + enemyY_change[i]
        if collide(enemyX[i], enemyY[i],bulletX,bulletY):
            bulletY = PLAYER_START_Y
            score_value += 1
            bullet_state = "ready"
            enemyX[i] = (random.randint(0, SCREEN_WIDTH - 64))
            enemyY[i] = (random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
        enemy(enemyX[i],enemyY[i], i)
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        bulet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
