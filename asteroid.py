import pygame
from constants import *
from circleshape import CircleShape

class asterioid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        