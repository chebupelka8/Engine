import pygame, sys
from pygame.locals import *
from Engine.scripts.math import Vec2
from Engine.scripts.image import Image


class WindowLoop:

    def __init__(self, __size: Vec2, fps: int = 144) -> None:
        pygame.init()

        self.__display = pygame.display.set_mode((__size.x, __size.y))
        pygame.display.set_caption("Engine: v0.1")
        pygame.display.set_icon(Image("Engine/assets/icon.png").image)
        
        self.__clock = pygame.time.Clock()
        self.__fps = fps
    
    def set_window_title(self, __title: str) -> None:
        pygame.display.set_caption(__title)
    
    def set_window_icon(self, __icon: Image) -> None:
        pygame.display.set_icon(__icon.image)
    
    @property
    def display(self) -> pygame.Surface:
        return self.__display
    
    def destroy(self) -> None:
        pygame.quit()
        sys.exit()
    
    def update_events(self, __event: pygame.Event) -> None:
        if __event.type == QUIT:
            self.destroy()
    
    def update_display(self) -> None:
        pygame.display.update()
        self.__display.fill("#1b1b1b")
        self.__clock.tick(self.__fps)

        for event in pygame.event.get():
            self.update_events(event)
        
        # self.__events.clear()
            
