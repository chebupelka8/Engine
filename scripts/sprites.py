import pygame
from Engine.scripts.image import Image, Animation
from Engine.scripts.math import Vec2
from Engine.scripts.shape import RectangleShape, CollisionRectangle
from Engine.scripts.collision import Collider
from Engine.scripts.group import SpriteGroup


class StaticSprite(CollisionRectangle):
    def __init__(self, position: Vec2, image: Image) -> None:
        super().__init__(position, image.size.x, image.size.y)

        self.__image = image
    
    def draw(self, __display: pygame.Surface) -> None:
        
        self.update()
        __display.blit(self.__image.image, self.rectangle)
        
    def __repr__(self) -> str:
        return f"StaticSprite(position={self.position}, image={self.__image})"

class AnimatedSprite(CollisionRectangle):
    def __init__(self, position: Vec2, animation: Animation) -> None:
        super().__init__(position, animation[0].size.x, animation[0].size.y)

        self.__verify(animation)
        
        self.__animation: Animation = animation
        self.__frame = 0
        self.__is_freezed: bool = False
    
    @staticmethod
    def __verify(__animation) -> None:
        if not isinstance(__animation, Animation): raise TypeError("Argument should be an instanse of the 'Animtion' class")
    
    def draw(self, __display: pygame.Surface) -> None:
        self.size = self.__animation[int(self.__frame)].size
        self.update()

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