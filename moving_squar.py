import pygame
import sys

# initailize pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 300, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Square Game")

# Colors
WHITE = (255, 255, 255)
RED = (0, 0, 0)

# Square settings
square_size = 100
x = 100 # X position of the square
y = 100 # y position of the square
speed = 1 # Movement speed

# Main game loop
running = True
while running:
    pygame.time.delay(30) # Delay for smoother movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # Fill background
    screen.fill(WHITE)
    
    # Draw the square
    pygame.draw.rect(screen, RED,(x, y, square_size, square_size))
    
    # Update display
    pygame.display.update()

#Quit
pygame.quit()
sys.exit()
