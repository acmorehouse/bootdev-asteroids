from circleshape import CircleShape
from logger import log_event

import constants
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x_pos = x
        self.y_pos = y
        self.radius = radius   
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        split_1_velocity = self.velocity.rotate(angle)
        split_2_velocity = self.velocity.rotate(-angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = split_1_velocity * 1.2

        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2.velocity = split_2_velocity * 1.2
