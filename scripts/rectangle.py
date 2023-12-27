import pygame
from Engine.scripts.vec import Vec2


class Rectangle:
    def __init__(self, position: Vec2, width: int, height: int) -> None:
        self.__position = position
        self.__width = width
        self.__height = height

        self.__rect = pygame.Rect(self.__position.x, self.__position.y, self.__width, self.__height)
    
    @property
    def rect(self) -> pygame.Rect:
        return self.__rect
    
    def collide_rect(self, __rect) -> bool:
        return self.__rect.colliderect(__rect.rect)