import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 720, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake — Phase 1")

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # black background
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
