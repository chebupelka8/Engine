import pygame
from Engine.scripts.math import Vec2, Size
from Engine.scripts.collision import Collider


class RectangleShape:
    def __init__(self, position: Vec2, width: int, height: int) -> None:
        self.__rectangle = pygame.Rect(position.x, position.y, width, height)
        self.__size = Size(width, height)
    
    @property
    def size(self) -> Size:
        return self.__size
    
    @size.setter
    def size(self, __size: Size) -> None:
        self.__size = __size
    
    @property
    def rectangle(self) -> pygame.Rect:
        return self.__rectangle
    
    @property
    def position(self) -> Vec2:
        return Vec2(self.__rectangle.x, self.__rectangle.y)