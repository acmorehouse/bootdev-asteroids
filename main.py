import pygame
import circleshape

from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from logger import log_state
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import PLAYER_RADIUS

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# Group creation

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

# Initialize pygame module
    pygame.init()

# Global clock initialize

    global_clock = pygame.time.Clock()
    dt = 0

# Set screen for game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# initialize Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

# initialize AsteroidField
    player = AsteroidField()

# Game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        

        updatable.update(dt)

        for elements in drawable:
            elements.draw(screen)

        pygame.display.flip()

        dt = global_clock.tick(60)/1000
        # print(f"delta time: {dt}")

if __name__ == "__main__":
    main()
