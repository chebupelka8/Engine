"""Engine is a engine for python games made with pygame"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# import pygame
from pygame.locals import *
import sys
from .scripts.sprites import *
from .scripts.image import *
from .scripts.math import *
from .scripts.loop import *
from .scripts.event import *
from .scripts.group import *
from .scripts.collision import Collider

print("Welcome! (Engine: alpha 0.1)")