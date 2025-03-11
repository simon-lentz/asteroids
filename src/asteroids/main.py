# https://www.pygame.org/docs/ref/pygame.html
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player


def main():
    print(
        f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}"
    )

    # initialize pygame
    pygame.init()

    # set screen using constants.py
    pygame.display.set_caption("Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create player-related containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add groups as static field (tuple[Group, Group])before creating any instances
    Player.containers = (updatable, drawable)

    # create a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # create a game clock to decouple game speed (should be linked to FPS) from while loop refresh rate
    clock = pygame.time.Clock()

    # delta time tracking variable in seconds
    dt_s = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill background
        pygame.Surface.fill(screen, RGB_BLACK)

        updatable.update(dt_s)

        for object in drawable:
            object.draw(screen)

        # update screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt_s = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
