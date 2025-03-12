from abc import ABC, abstractmethod

import pygame

from constants import *


# Base class for game objects
class CircleShape(ABC, pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def update(self, dt_s: float):
        pass

    def wrap_position(self):
        # If object goes off one edge, reappear on the opposite
        if self.position.x < (0 - self.radius):
            self.position.x = SCREEN_WIDTH
        elif self.position.x > (SCREEN_WIDTH + self.radius):
            self.position.x = 0
        if self.position.y < (0 - self.radius):
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > (SCREEN_HEIGHT + self.radius):
            self.position.y = 0

    def collision(self, other: "CircleShape") -> bool:
        dist = self.position.distance_to(other.position)
        if dist <= (self.radius + other.radius):
            return True
        return False
