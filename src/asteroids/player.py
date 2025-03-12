import pygame


from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown = 0

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

    def rotate(self, dt_s: float):
        self.rotation += PLAYER_TURN_SPEED * dt_s

    def move(self, dt_s: float):
        # draw Y unit vector
        y_vec = pygame.Vector2(0, 1)

        # rotate Y unit vector by player rotation to get player direction vector
        dir_vec = y_vec.rotate(self.rotation)

        # scale direction vector by player speed and delta time to get player movement vector
        player_move = dir_vec * PLAYER_XY_SPEED * dt_s

        self.position += player_move

    def shoot(self, dt_s: float):
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity += (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED * dt_s
        )
        self.cooldown += PLAYER_SHOOT_COOLDOWN

    def update(self, dt_s: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt_s)
        if keys[pygame.K_s]:
            self.move(-dt_s)
        if keys[pygame.K_a]:
            self.rotate(-dt_s)
        if keys[pygame.K_d]:
            self.rotate(dt_s)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                self.cooldown -= dt_s
            else:
                self.shoot(dt_s)
