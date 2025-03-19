#C
import pygame

C_RED = (205, 92, 92)
C_WHITE = (255, 255, 255)

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
    'run_1': 300,
    'go_1': 50,


}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
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

