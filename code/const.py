#C
import pygame

C_RED = (205, 92, 92)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'background_0': 0,
    'background_1': 1,
    'background_2': 2,
    'background_3': 3,
    'background_4': 4,
    'background_5': 5,
    'background_6': 6,
    'background_7': 7,
    'run_1' :3,
    'go_1':6
}

ENTITY_HEALTH = {
    'background_0': 999,
    'background_1': 999,
    'background_2': 999,
    'background_3': 999,
    'background_4': 999,
    'background_5': 999,
    'background_6': 999,
    'background_7': 999,
    'run_1': 100,
    'go_1': 1,


}

ENTITY_DAMAGE = {
    'background_0': 0,
    'background_1': 0,
    'background_2': 0,
    'background_3': 0,
    'background_4': 0,
    'background_5': 0,
    'background_6': 0,
    'background_7': 0,
    'run_1': 1,
    'go_1': 25,

}

# M
MENU_OPTION = ('START',
               'SCORE',
               'EXIT')

#S
SPAWN_TIME = 4000
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

