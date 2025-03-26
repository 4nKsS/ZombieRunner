#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame

from code.Score import Score
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame modules
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                score.show_score()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass
