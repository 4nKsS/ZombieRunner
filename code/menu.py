#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_RED, WIN_WIDTH, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window  # Add menu background image
        self.surf = pygame.image.load('./asset/background.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/menu.ogg')  # Add menu music
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Add text on screen
            self.menu_text(70, 'Zombie', C_RED, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, 'Runner', C_RED, ((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTION)):
                self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 230 + 30 * i))

            pygame.display.flip()
            # Check for all events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()  # Close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
