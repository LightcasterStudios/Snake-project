# importin Libraries
import pygame
import time
import random
import sys

# -1. setup-

pygame.init()

# screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Grid settings
CELL_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Create screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lightcaster Studios' Snake")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont(None, 30)

# -2. Helper Functions-

def draw_text(text, x, y, color=WHITE):
    """Draws text to the screen"""
    img = FONT.render(text, True, color)
    screen.blit(img, (x, y))

def random_position():
    """Returns a random grid-aligned position"""
    x = random.randrange(0, GRID_WIDTH) * CELL_SIZE
    Y = random.randrange(0, GRID_WIDTH) * CELL_SIZE
    return x, Y

# -3. Snake Class-

class Snake:
    def __init__(self, color, start_pos):
        self.color = color
        self.body = [start_pos]
        self.direction = (CELL_SIZE, 0) #moving right initially
        self.alive = True
        self.score = 0

    def change_direction(self, new_dir):
        """Prevents reversing direction instantly"""
        opposite = (-self.direction[0], -self.direction[0])
        if new_dir != opposite:
            self.direction = new_dir

    def move(self):
        """Moves snake forward"""
        if not self.alive:
            return

        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        # Adds a segment to the snake
        self.body.append(self.body[-1])
        self.score += 1

    def draw(self):
        """draws the snake"""
        for segment in self.body:
            pygame.draw.rect(
                screen,
                self.color,
                (segment[0],segment[1], CELL_SIZE, CELL_SIZE)
            )
    def check_wall_collision(self):
        """checks if snake hits the wall"""
        head_x, head_y = self.body[0]
        if(
            head_x < 0 or
            head_x >= SCREEN_WIDTH or
            head_y < 0 or
            head_y >= SCREEN_HEIGHT
        ):
            self.alive= False

    def check_self_collision(self):
        # checks if snake hits itself
        if self.body[0] in self.body[1:]:
            self.alive = False

# -4. Ai Logic-
def ai_choose_direction(ai_snake, fruit_pos, obstacles):

    directions = [
        (CELL_SIZE, 0), # right
        (-CELL_SIZE, 0), # left
        (0, CELL_SIZE), # down
        (0, -CELL_SIZE), # up
          ]

    head_x, head_y =ai_snake.body[0]
    fx, fy =fruit_pos

#sorting the directions by distance to fruit
    def distance(dir):
        nx = head_x + dir[0]
        ny = head_y+ dir[1]
        return abs(nx - fx) + abs(ny - fy)

    directions.sort(key=distance)

    # Pick the first safe direction
    for d in directions:
        nx = head_x + d[0]
        ny = head_y + d[1]

        # wall check
        if nx < 0 or nx >= SCREEN_WIDTH or ny < 0 or ny >= SCREEN_HEIGHT:
            continue
    # collision check
        if (nx, ny) in obstacles:
            continue
        return d

# if no safe move, keep going (likely death)
    return ai_snake.direction

# -5. Game modes-

def game_loop_single():
    player = Snake(GREEN, random_position())
    fruit = random_position()

    while True:
        clock.tick(12)
        screen.fill(BLACK)

        # -Input-
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    player.change_direction((0, -CELL_SIZE))
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                     player.change_direction((0, CELL_SIZE))
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    player.change_direction((-CELL_SIZE, 0))
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    player.change_direction((CELL_SIZE, 0))

        # -Logic-
        player.move()
        player.check_wall_collision()
        player.check_self_collision()

        if player.body[0] == fruit:
            player.grow()
            fruit = random_position()

        if not player.alive:
            return

# -Draw-
        player.draw()
        pygame.draw.rect(screen, WHITE, (*fruit, CELL_SIZE, CELL_SIZE))
        draw_text(f"Score: {player.score}", 10, 10)

        pygame.display.flip()

def game_loop_vs_ai():
    player = Snake(BLUE, random_position())
    ai =  Snake(RED, random_position())
    fruit = random_position()

    while True:
        clock.tick(15)
        screen.fill(BLACK)

        # -Input-
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
                player.change_direction((0, -CELL_SIZE))
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                player.change_direction((0, CELL_SIZE))
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.change_direction((-CELL_SIZE, 0))
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.change_direction((CELL_SIZE, 0))

        # -Ai-
        obstacles = set(player.body + ai.body)
        ai.direction = ai_choose_direction(ai, fruit, obstacles)

        # -Logic-
        player.move()
        ai.move()

        for snake in (player, ai):
            snake.check_wall_collision()
            snake.check_self_collision()

        if player.body[0] == fruit:
            player.grow()
            fruit = random_position()

        if ai.body[0] == fruit:
            ai.grow()
            fruit = random_position()

        if not player.alive or not ai.alive:
            return

        # -Draw-
        player.draw()
        ai.draw()
        pygame.draw.rect(screen, WHITE, (*fruit, CELL_SIZE, CELL_SIZE))
        draw_text(f"Player: {player.score}", 10, 10)
        draw_text(f"Evil: {ai.score}", 10, 40)

        pygame.display.flip()

# 6. -Menu-

def menu():
   while True:
     screen.fill(BLACK)
     draw_text("Lightcaster Studio's Snake", 200, 100)
     draw_text("1 - Single Player", 220, 160)
     draw_text("2 - Vs Evil Snake", 220, 200)
     draw_text("ESC - Quit", 220, 240)

     pygame.display.flip()

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game_loop_single()
            elif event.key == pygame.K_2:
                game_loop_vs_ai()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

# -Entry point-
menu()