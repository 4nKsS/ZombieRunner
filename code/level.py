#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Score import Score
from code.const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, C_GREEN, WIN_WIDTH
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('background_'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000
        self.timer = 0
        self.last_time = pygame.time.get_ticks()

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.ogg')
        pygame.mixer_music.play(1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            #timer

            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.last_time
            if elapsed_time >= 1000:
                self.timer += 1  # Incrementar o temporizador a cada segundo
                self.last_time = current_time

            # 00:000 format
            milliseconds = current_time % 1000
            seconds = self.timer
            timer_text = f'{seconds:02}.{milliseconds:03}'

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if ent.name == 'run_1':
                    self.level_text(30, f'Health: {ent.health:} | {timer_text}', C_WHITE, (WIN_WIDTH/2, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    score_instance = Score(self.window)
                    score_instance.save_score(self.timer)


                    conn = sqlite3.connect('game_scores.db')
                    cursor = conn.cursor()
                    cursor.execute('SELECT * FROM scores ORDER BY id DESC LIMIT 1')
                    last_score = cursor.fetchone()
                    conn.close()


                    self.window.fill((0, 0, 0))
                    font = pygame.font.SysFont('Arial', 40)
                    text = f"Run: {last_score[0]} - Time: {last_score[1]:.2f}s"
                    text_surf = font.render(text, True, (255, 255, 255))

                    # Center the text
                    text_rect = text_surf.get_rect(center=(self.window.get_width() / 2, self.window.get_height() / 2))
                    self.window.blit(text_surf, text_rect)
                    pygame.display.flip()

                    pygame.time.wait(3000)  # Wait for 3 seconds
                    return False

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
