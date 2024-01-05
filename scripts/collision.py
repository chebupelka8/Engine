import pygame
from .group import SpriteGroup


class Collider:
    
    @classmethod
    def group_collider(cls, __sprite, *__groups: SpriteGroup) -> list:
        collisions = []

        for sprites in __groups:
            for sprite in sprites.get():
                if cls.__collide_rect(__sprite.rectangle, sprite.rectangle):
                    collisions.append(sprite)
        
        return collisions
    
    @classmethod
    def __collide_rect(cls, __rect_0: pygame.Rect, __rect_1: pygame.Rect) -> bool:
        return __rect_0.colliderect(__rect_1)