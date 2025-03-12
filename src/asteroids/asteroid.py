import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,
            color=RGB_WHITE,
            radius=self.radius,
            center=self.position,
            width=2,
        )

    def update(self, dt_s: float):
        self.position += self.velocity * dt_s

    def split(self):
        original_position = self.position
        original_velocity = self.velocity
        original_radius = self.radius

        self.kill()

        if original_radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        split_radius = original_radius - ASTEROID_MIN_RADIUS

        original_velocity *= 1.2
        split_velocity = original_velocity.rotate(split_angle)
        print(f"Split Velocity: {split_velocity}")
        mirror_split_velocity = original_velocity.rotate(-split_angle)

        split_asteroid = Asteroid(
            original_position.x, original_position.y, split_radius
        )
        split_asteroid.velocity = split_velocity

        mirror_split_asteroid = Asteroid(
            original_position.x, original_position.y, split_radius
        )
        mirror_split_asteroid.velocity = mirror_split_velocity
