import pygame

pygame.init() # Initialize Pygame modules
print('Setup Start')
screen = pygame.display.set_mode(size=(600, 480)) # Create window

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit()#end pygame