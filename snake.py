# import libraries 
import pygame
import time
import random

set
# window size
window = 720
window = 480

#defining colors

black = pygame.color(0, 0, 0)
white = pygame.color(255, 255, 255)
red = pygame.color(255, 0, 0)
green = pygame.color(0, 255, 0)
blue = pygame.color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Lightcaster Studios Snakes') 
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position_ = [100, 50]

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body

snake_body = [ [100, 50], [90, 50], [80, 50], [70, 50] ]

    # fruit position
    # fruit= [random.randrange(1, window_x//10]
    # fruit_spawn = True
    
    #setting default snake direction
    # towards right
direction = 'right'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size): 
     # creating font object score_font 
     score_font = pygame.font.sysfont(font, size)

#create the display 
# score surface object
# text surface object

score_rect = score_surface.get_rect()

#displaying text
game_window.blit(score_surface, score_rect)

# game over function
def game_over():

    # creating font object my_font
    my_font = pygame.font.sysfont('time new roman', 50)

    # creating a text surface on which text will be drawn
    game_over_surface = my_font.render('your score is :' + str(score), True, red)

    # create a rectangular object for the surface object
    game_over_recy = game_over_surface.get_rect()

# setting position of the text 
game_over_rect.midtop = (window_x/2, window_y/4)

# blit will draw the text on screen
game_window.bilt(game_over_surface, game_over_rect)
pygame.display.flip()

# after 2 seconds we will quit the program
time.sleep(2)

#ddeactivating pygame library
pygame.quit()

#quit the program,
quit()

# main function
while True:

    #handling key events
    for event in pygame.event.get():
         if even.type == pygame.k_up:
            change_to ='W'
         if event.key == pygame.k_down:
            change_to ='S' 
         if event.key == pygame.k_left:
            change_to ='A' 
         if event.key == pygame.k_right:
            change_to ='D' 

# If two keys pressed simultaneously don't want snake to move into two direction simultaneously

if change_to == 'up' and direction != 'down': 
    direction ='up'      
if change_to =='down' and direction != 'up':
    direction == 'down'           
if change_to == 'left' and direction != 'right':
    direction = 'left'
if change_to == 'right' and direction != 'left':
    direction = 'right'

# moving the snake
if direction == 'up':
    snake_position[1] -= 10
if direction == 'down':
    snake_position[1] += 10
if direction == 'left':
    snake_position[1] -= 10
if direction == 'right':
    snake_position[1] += 10

#snake body growing mechanism
# if fruits and snakes collide then scores will be incremented by 10

snake_body.insert(0, list(snake_position))
if snake[position0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
else: snake_body.pop()
if not fruit_spawn:
    fruit_position = [random.randrange(1, (window_x//10)) * 10, randrom.randrange(1, (window_y//10)) * 10]

fruit_spawn = True
game_window.fill(black)

for pos in snake_body:
     pugame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

# Game Over conditions

if snake_position[0] < 0 or snake_position[0] > window_x-10:
    game_over()
if snake_position[1] < 0 or snake_position[1] > window_y-10:
    game_over()

#touching the snake body
for block in snake_body[1:]:
    if snake_position[0] == block[0] and snake_position[1] == block[1]:
        game_over()

# displaying score continuously
show_score(1,white, 'times new roman', 20)

# Refresh game screen
pygame.display.update()

# Frames per second /refresh rate
fps.tick(snake_speed)

