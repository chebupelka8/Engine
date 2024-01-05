import pygame
from .sprites import *
from typing import Any


class SpriteGroup:
    def __init__(self, *__sprites) -> None:
        map(self.__verify, [*__sprites])

        self.__sprites = [*__sprites]
    
    @staticmethod
    def __verify(__sprite) -> None:
        match __sprite:
            case sprite if isinstance(sprite, (StaticSprite, AnimatedSprite)):
                ...
            case _:
                raise TypeError("Argument should be 'StaticSprite' or 'AnimatedSprite'")
    
    def add_sprite(self, __sprite) -> None:
        self.__sprites.append(__sprite)
    
    def delete_sprite(self, __sprite) -> None:
        self.__sprites.remove(__sprite)
    
    def get(self) -> list:
        return self.__sprites
    
    def __getitem__(self, __index: int) -> Any:
        return self.__sprites[__index]

    def __repr__(self) -> str:
        return f"SpriteGroup(sprites={self.__sprites})"