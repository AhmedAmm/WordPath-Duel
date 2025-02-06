from settings import *

import pygame
import sys

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(GRAY)
            pygame.display.flip()

            self.clock.tick(FPS)


if __name__ == "__main__":
    main = Main()
    main.run()
