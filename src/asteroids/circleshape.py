from abc import ABC, abstractmethod

import pygame


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
