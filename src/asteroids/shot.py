import pygame

from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,
            color=RGB_WHITE,
            radius=SHOT_RADIUS,
            center=self.position,
            width=2,
        )

    def update(self, dt_s: float):
        self.position += self.velocity * dt_s
