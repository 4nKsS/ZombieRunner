#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity
import pygame


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.animation_frames = ['go_1', 'go_2', 'go_3', 'go_4', 'go_5', 'go_6', 'go_7','go_8','go_9','go_10' ]  # Adicione os quadros necessários
        self.current_frame = 0
        self.animation_speed = 5
        self.animation_counter = 0

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

        self.update_sprite()

    def update_sprite(self):
        self.animation_counter += 1

        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)

        self.surf = pygame.image.load(f'./asset/{self.animation_frames[self.current_frame]}.png').convert_alpha()
        self.rect = self.surf.get_rect(center=self.rect.center)  # Mantém o centro do retângulo alinhado
