import pygame
import math
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        num_points: int = 18,
        noise: float = 0.2,
    ) -> None:
        """
        Initialize the asteroid with a given position, radius, and parameters
        to control its irregular shape.

        Args:
            x (float): The x-coordinate of the asteroid's center.
            y (float): The y-coordinate of the asteroid's center.
            radius (float): The base radius of the asteroid.
            num_points (int): The number of vertices for the polygon.
            noise (float): The maximum fractional deviation from the radius (e.g., 0.4 for ±40%).
        """
        super().__init__(x, y, radius)
        self.rotation = 0.0
        self.num_points = num_points
        self.noise = noise
        self.original_vertices = self._generate_vertices()

    def _generate_vertices(self) -> list[tuple[float, float]]:
        """
        Generates the base vertices for the asteroid polygon with noise.
        """
        vertices = []
        for i in range(self.num_points):
            # Calculate the angle for the current vertex.
            angle = (i / self.num_points) * 2 * math.pi
            # Apply a random noise factor to vary the radius.
            offset = random.uniform(1 - self.noise, 1 + self.noise)
            r = self.radius * offset
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            vertices.append((x, y))
        return vertices

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the asteroid on the provided screen by rotating the precomputed vertices
        and then drawing them as a polygon.
        """
        rotated_vertices = []
        # Rotate each vertex according to the current rotation angle.
        for vx, vy in self.original_vertices:
            rotated_x = vx * math.cos(self.rotation) - vy * math.sin(self.rotation)
            rotated_y = vx * math.sin(self.rotation) + vy * math.cos(self.rotation)
            # Translate the vertex to the asteroid's current position.
            rotated_vertices.append(
                (self.position[0] + rotated_x, self.position[1] + rotated_y)
            )

        pygame.draw.polygon(screen, RGB_WHITE, rotated_vertices, width=2)

    def update(self, dt_s: float) -> None:
        self.position += self.velocity * dt_s
        self.rotation += 0.5 * dt_s  # Adjust the rotation speed as needed.
        self.wrap_position()

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
        mirror_split_velocity = original_velocity.rotate(-split_angle)

        split_asteroid = Asteroid(
            original_position.x, original_position.y, split_radius
        )
        split_asteroid.velocity = split_velocity

        mirror_split_asteroid = Asteroid(
            original_position.x, original_position.y, split_radius
        )
        mirror_split_asteroid.velocity = mirror_split_velocity
