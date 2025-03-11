# https://www.pygame.org/docs/ref/pygame.html
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *


def main():
    print(
        f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}"
    )

    # initialize pygame
    pygame.init()

    # set screen using constants.py
    pygame.display.set_caption("Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a game clock to decouple game speed (should be linked to FPS) from while loop refresh rate
    clock = pygame.time.Clock()

    # delta time tracking variable in seconds
    dt_s = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
        dt_ms = clock.tick()
        dt_s = dt_ms / 1000


if __name__ == "__main__":
    main()
