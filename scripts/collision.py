import pygame


class Collider:
    
    @classmethod
    def group_collider(cls, __sprite, *__groups) -> list:
        collisions = list()

        for sprites in __groups:
            for sprite in sprites:
                if cls.collide_rect(__sprite.rectangle, sprite.rectangle):
                    collisions.append(sprite)
        
        return collisions
    
    @classmethod
    def collide_rect(cls, __rect_0, __rect_1) -> bool:
        return __rect_0.colliderect(__rect_1)