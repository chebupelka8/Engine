import pygame
from Engine.scripts.image import Image, Animation
from Engine.scripts.vec import Vec2


class Coordinated:
    def __init__(self, __position: Vec2) -> None:
        self.__position = __position
        self.__verify(self.__position)
    
    @staticmethod
    def __verify(__pos) -> None:
        match __pos:
            case pos if not isinstance(pos, Vec2):
                raise TypeError("Argument should be a 'Vec2'")
            case _:
                ...
    
    @property
    def position(self) -> Vec2:
        return self.__position
    
    @position.setter
    def position(self, __position: Vec2) -> None:
        self.__position = __position

class StaticSprite(Coordinated):
    def __init__(self, position: Vec2, image: Image) -> None:
        super().__init__(position)

        self.__image = image
    
    def draw(self, __display: pygame.Surface) -> None:
        __display.blit(self.__image.image, self.position.xy)
    
    def __repr__(self) -> str:
        return f"StaticSprite(position={self.position}, image={self.__image})"

class AnimatedSprite(Coordinated):
    def __init__(self, position: Vec2, animation: Animation) -> None:
        super().__init__(position)

        self.__verify(animation)
        
        self.__animation: Animation = animation
        self.__frame = 0
        self.__is_freezed: bool = False
    
    @staticmethod
    def __verify(__animation) -> None:
        if not isinstance(__animation, Animation): raise TypeError("Argument should be an instanse of the 'Animtion' class")
    
    def draw(self, __display: pygame.Surface) -> None:
        __display.blit(self.__animation[int(self.__frame)].image, self.position.xy)

    def animating(self, __speed: int | float) -> None:
        if not self.__is_freezed:
            self.__frame += __speed
            if self.__frame >= self.__animation.count(): self.__frame = 0
    
    def freeze(self) -> None:
        self.__is_freezed = True
    
    def unfreeze(self) -> None:
        self.__is_freezed = False
    
    def __repr__(self) -> str:
        return f"AnimatedSprite(position={self.position}, animation={self.__animation}, frame={int(self.__frame)})"