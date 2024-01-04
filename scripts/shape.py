import pygame
from Engine.scripts.math import Vec2, PrivateVec2
from Engine.scripts.collision import Collider
from Engine.scripts.group import SpriteGroup


class RectangleShape:
    def __init__(self, position: Vec2, width: int, height: int) -> None:
        self.__rectangle = pygame.Rect(position.x, position.y, width, height)
        self.__size = Vec2(width, height)
    
    @property
    def size(self) -> Vec2:
        return self.__size
    
    @size.setter
    def size(self, __size: Vec2) -> None:
        self.__size = __size
    
    @property
    def rectangle(self) -> pygame.Rect:
        return self.__rectangle
    
    @property
    def center(self) -> PrivateVec2:
        return PrivateVec2(self.__rectangle.centerx, self.__rectangle.centery)
    
    @property
    def position(self) -> PrivateVec2:
        return PrivateVec2(self.__rectangle.x, self.__rectangle.y)

class CollisionRectangle(RectangleShape):
    def __init__(self, position: Vec2, width: int, height: int) -> None:
        super().__init__(position, width, height)

        self.__movement = Vec2(0, 0)
        self.__collide_groups = None
        self.__collide_side = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False
        }
    
    @property
    def movement(self) -> Vec2:
        return self.__movement

    @movement.setter
    def movement(self, __movement: Vec2) -> None:
        self.__movement = __movement
    
    def set_collision_groups(self, *__groups: SpriteGroup) -> None:
        self.__collide_groups = [*__groups]
    
    def get_collision_side(self, __side: str) -> bool:
        return self.__collide_side.get(__side)
    
    def update(self) -> None:
        # horizontal
        self.rectangle.x += self.movement.x
        
        if self.__collide_groups != None:
            collisions = Collider.group_collider(self, *self.__collide_groups)

            for sprite in collisions:
                if self.movement.x > 0:
                    self.rectangle.right = sprite.rectangle.left
                    self.__collide_side["right"] = True
                if self.movement.x < 0:
                    self.rectangle.left = sprite.rectangle.right
                    self.__collide_side["left"] = True
            
            if len(collisions) == 0:
                self.__collide_side["right"] = self.__collide_side["left"] = False
        
        # vertical
        self.rectangle.y += self.movement.y

        if self.__collide_groups != None:
            collisions = Collider.group_collider(self, *self.__collide_groups)

            for sprite in collisions:
                if self.movement.y > 0:
                    self.rectangle.bottom = sprite.rectangle.top
                    self.__collide_side["bottom"] = True
                if self.movement.y < 0:
                    self.rectangle.top = sprite.rectangle.bottom
                    self.__collide_side["top"] = True

            if len(collisions) == 0:
                self.__collide_side["top"] = self.__collide_side["bottom"] = False