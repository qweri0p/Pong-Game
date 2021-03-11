import pygame, random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velx = 5
        self.vely = random.randrange(5, 9)

class paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.score=""
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pong!")
 
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ball = block(WHITE, 20, 20)

player1 = paddle(WHITE, 25, 100)

player2 = paddle(WHITE, 25, 100)

player1.score = 0
player2.score = 0

block_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

def Paddle1Reset():
    player1.rect.y = 200
    player1.rect.x = 25
    player_list.add(player1)
    all_sprites_list.add(player1)

def Paddle2Reset():
    player2.rect.y = 200
    player2.rect.x = 950
    player_list.add(player2)
    all_sprites_list.add(player2)

def BallReset():
    ball.rect.y = 225
    ball.rect.x = 500
    ball.velx = 5
    ball.vely = random.randrange(5, 9)
    block_list.add(ball)
    all_sprites_list.add(ball)

def MoveDown1():
    player1.rect.y += 10

def MoveUp1():
    player1.rect.y -= 10

def MoveDown2():
    player2.rect.y += 10

def MoveUp2():
    player2.rect.y -= 10

def Reset():
    Paddle1Reset()
    Paddle2Reset()
    BallReset()

def Player1Point():
    Reset()
    player1.score += 1
    ball.velx = ball.velx * -1

def Player2Point():
    Reset()
    player2.score += 1
    ball.velx = ball.velx * -1

Reset()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.key.set_repeat(1, 20)
                MoveUp1()
            if event.key == pygame.K_s:
                pygame.key.set_repeat(1, 20)
                MoveDown1()
            if event.key == pygame.K_DOWN:
                pygame.key.set_repeat(1, 20)
                MoveDown2()
            if event.key== pygame.K_UP:
                pygame.key.set_repeat(1, 20)
                MoveUp2()
                
               
 
    # --- Game logic should go here
    
    if ball.rect.y <= 0 or ball.rect.y >= 475:
        ball.vely = ball.vely * -1

    ball.rect.x += ball.velx
    ball.rect.y += ball.vely

    collide_list1 = pygame.sprite.spritecollide(player1, block_list, False)
    collide_list2 = pygame.sprite.spritecollide(player2, block_list, False)

    for block in collide_list1:
        ball.velx = ball.velx * -1
        ball.velx = ball.velx * 1.1
    
    for block in collide_list2:
        ball.velx = ball.velx * -1
        ball.velx = ball.velx * 1.1

    if ball.rect.x <= 0:
        Player2Point()
    elif ball.rect.x >= 1000:
        Player1Point()

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
