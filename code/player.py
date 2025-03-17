#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.animation_frames = ['run_0', 'run_1', 'run_2', 'run_3', 'run_4', 'run_5']  # add more frames as needed
        self.current_frame = 0
        self.animation_speed = 5  # Adjust for animation speed (lower is faster)
        self.animation_counter = 0
        self.is_jumping = False
        self.jump_count = 10
        self.initial_y = position[1]  # Store initial Y position

    def move(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.update_sprite()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 7.5

        if self.is_jumping:
            if self.jump_count >= -7.5:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 0.5
            else:
                self.is_jumping = False
                self.rect.y = self.initial_y  # Reset to initial Y position

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def update_sprite(self):
        self.surf = pygame.image.load(f'./asset/{self.animation_frames[self.current_frame]}.png').convert_alpha()
        self.rect = self.surf.get_rect(center=self.rect.center)  # keep the player centered.
