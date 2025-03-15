#!/usr/bin/python
# -*- coding: utf-8 -*-
from asyncio.staggered import staggered_race

from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'background_':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'background_{i}', (0, 0)))
                    list_bg.append(Background(f'background_{i}', (WIN_WIDTH,0)))
                return list_bg