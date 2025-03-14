import pygame
from Tools.scripts.generate_global_objects import Printer

pygame.init()  # Initialize Pygame modules
print('Setup Start')
screen = pygame.display.set_mode(size=(600, 480))  # Create window
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # Close window
            quit()  # end pygame