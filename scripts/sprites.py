import pygame
from Engine.scripts.image import Image, Animation
from Engine.scripts.math import Vec2
from Engine.scripts.shape import RectangleShape
from Engine.scripts.collision import Collider
from Engine.scripts.group import SpriteGroup


class StaticSprite(RectangleShape):
    def __init__(self, position: Vec2, image: Image) -> None:
        super().__init__(position, image.size.x, image.size.y)

        self.__image = image
        self.__movement = Vec2(0, 0)
        self.__collide_groups = None
    
    @property
    def movement(self) -> Vec2:
        return self.__movement

    @movement.setter
    def movement(self, __movement: Vec2) -> None:
        self.__movement = __movement
    
    def collide(self, *__groups: SpriteGroup) -> None:
        self.__collide_groups = [*__groups]
    
    def draw(self, __display: pygame.Surface) -> None:
        
        self.__update()
        __display.blit(self.__image.image, self.rectangle)
    
    def __update(self) -> None:
        # horizontal
        self.rectangle.x += self.movement.x
        
        if self.__collide_groups != None:
            for sprite in Collider.group_collider(self, *self.__collide_groups):
                if self.movement.x > 0:
                    self.rectangle.right = sprite.rectangle.left
                if self.movement.x < 0:
                    self.rectangle.left = sprite.rectangle.right
        
        # vertical
        self.rectangle.y += self.movement.y

        if self.__collide_groups != None:
            for sprite in Collider.group_collider(self, *self.__collide_groups):
                if self.movement.y > 0:
                    self.rectangle.bottom = sprite.rectangle.top
                if self.movement.y < 0:
                    self.rectangle.top = sprite.rectangle.bottom
        
    def __repr__(self) -> str:
        return f"StaticSprite(position={self.position}, image={self.__image})"

class AnimatedSprite(RectangleShape):
    def __init__(self, position: Vec2, animation: Animation) -> None:
        super().__init__(position, animation[0].size.x, animation[0].size.y)

        self.__verify(animation)
        
        self.__animation: Animation = animation
        self.__frame = 0
        self.__is_freezed: bool = False
        self.__movement = Vec2(0, 0)
        self.__collide_groups = None
    
    @staticmethod
    def __verify(__animation) -> None:
        if not isinstance(__animation, Animation): raise TypeError("Argument should be an instanse of the 'Animtion' class")
    
    def draw(self, __display: pygame.Surface) -> None:
        self.__update()

        __display.blit(self.__animation[int(self.__frame)].image, self.position.xy)
    
    @property
    def movement(self) -> Vec2:
        return self.__movement

    @movement.setter
    def movement(self, __movement: Vec2) -> None:
        self.__movement = __movement
    
    def collide(self, *__groups: SpriteGroup) -> None:
        self.__collide_groups = [*__groups]
    
    def animating(self, __speed: int | float) -> None:
        if not self.__is_freezed:
            self.__frame += __speed
            if self.__frame >= self.__animation.count(): self.__frame = 0
    
    def freeze(self) -> None:
        self.__is_freezed = True
    
    def unfreeze(self) -> None:
        self.__is_freezed = False
    
    def __update(self) -> None:
        self.size = self.__animation[int(self.__frame)].size

        # horizontal
        self.rectangle.x += self.movement.x
        
        if self.__collide_groups != None:
            for sprite in Collider.group_collider(self, *self.__collide_groups):
                if self.movement.x > 0:
                    self.rectangle.right = sprite.rectangle.left
                if self.movement.x < 0:
                    self.rectangle.left = sprite.rectangle.right
        
        # vertical
        self.rectangle.y += self.movement.y

        if self.__collide_groups != None:
            for sprite in Collider.group_collider(self, *self.__collide_groups):
                if self.movement.y > 0:
                    self.rectangle.bottom = sprite.rectangle.top
                if self.movement.y < 0:
                    self.rectangle.top = sprite.rectangle.bottom
    
    def __repr__(self) -> str:
        return f"AnimatedSprite(position={self.position}, animation={self.__animation}, frame={int(self.__frame)})"