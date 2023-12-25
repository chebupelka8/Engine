class Vec2:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.__verify(x, y)

        self.__x = x
        self.__y = y
    
    @staticmethod
    def __verify(x, y) -> None:
        match x, y:
            case x, y if all(map(lambda a: isinstance(a, (int, float)), [x, y])):
                ...
            case _:
                raise ValueError("Arguments 'x' and 'y' should be 'int' or 'float'")
    
    @property
    def x(self) -> int | float:
        return self.__x
    
    @x.setter
    def x(self, __value: int | float) -> None:
        self.__x = __value
    
    @property
    def y(self) -> int | float:
        return self.__y
    
    @y.setter
    def y(self, __value: int | float) -> None:
        self.__y = __value
    
    @property
    def xy(self) -> list:
        return [self.__x, self.__y]
    
    def __repr__(self) -> str:
        return f"Vec2(x={self.__x}, y={self.__y})"
    
    def __getitem__(self, __index) -> int | float:
        return [self.__x, self.__y][__index]
    
    def __setitem__(self, __index, __value) -> None:
        res = [self.__x, self.__y]
        res[__index] = __value
        self.__verify(*res)

        self.__x, self.__y = res
    
    def __abs__(self):
        return Vec2(abs(self.__x), abs(self.__y))