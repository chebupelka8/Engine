from .math import Vec2


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