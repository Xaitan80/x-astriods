import pygame
from constants import *

def main():
    pygame.init()
    my_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        dt = my_clock.tick(60) / 1000

    
                

if __name__ == "__main__":
    main()
