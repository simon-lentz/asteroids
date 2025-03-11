import pygame


from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(
            surface=screen,
            color=RGB_WHITE,
            points=self.triangle(),
            width=2,
        )

    def update(self, dt_s: float):
        print(dt_s)
