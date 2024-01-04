"""Engine is a engine for python games made with pygame"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# import pygame
from pygame.locals import *
import sys
from Engine.scripts.sprites import *
from Engine.scripts.image import *
from Engine.scripts.math import *
from Engine.scripts.loop import *
from Engine.scripts.event import *
from Engine.scripts.group import *
from Engine.scripts.collision import Collider

print("Welcome! (Engine: v0.1)")