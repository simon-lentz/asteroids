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
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
