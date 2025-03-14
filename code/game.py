#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame

from code.const import WIN_WIDTH, WIN_HEIGH
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # Initialize Pygame modules
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGH))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()

            pass

